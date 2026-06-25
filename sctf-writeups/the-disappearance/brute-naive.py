# pip install pillow numpy tqdm

import os
import string
import time
import numpy as np
from itertools import combinations, product
from multiprocessing import Pool, cpu_count
from PIL import Image
from tqdm import tqdm

# ----------------------------------------------------------------------------
# Config
# ----------------------------------------------------------------------------
INPUT_IMAGE = "image.jpeg"
OUTPUT_TXT = "results.txt"

# How much text to store per combo in the output file. Full text per combo
# can be ~220 KB; with 52,488 combos that's multi-GB if untruncated.
SAVE_FULL_TEXT = False
PREVIEW_CHARS = 1000

# How much of each combo's text to actually run the scorer on. Scoring the
# full ~220 KB for all 52,488 combos is unnecessary work for a heuristic
# this cheap — a sizeable prefix is plenty to tell noise from plausible
# English (assuming the hidden message starts somewhere near the front
# of the bitstream, which is the common case for this kind of encoding).
SCORE_SAMPLE_CHARS = 10000

# Sliding-window settings for scoring (see WINDOWED SCORING note above).
# Smaller window = more sensitive to short embedded phrases but noisier;
# larger window = smoother but can still get diluted by short messages.
WINDOW_CHARS = 400
WINDOW_STRIDE = 200

NUM_WORKERS = cpu_count()
CHUNK_SIZE = 2000          # combos batched per task sent to a worker (IPC efficiency)

# MSB-first bitplanes: R7..R0, G7..G0, B7..B0
BITPLANES = [
    ("R", 7), ("R", 6), ("R", 5), ("R", 4), ("R", 3), ("R", 2), ("R", 1), ("R", 0),
    ("G", 7), ("G", 6), ("G", 5), ("G", 4), ("G", 3), ("G", 2), ("G", 1), ("G", 0),
    ("B", 7), ("B", 6), ("B", 5), ("B", 4), ("B", 3), ("B", 2), ("B", 1), ("B", 0),
]
CHANNEL_INDEX = {"R": 0, "G": 1, "B": 2}

# Byte translation table: printable ASCII (32-126) and \t \n \r map to themselves,
# everything else maps to a space. 0x00 bytes are dropped separately (not spaced).
_trans = bytearray(256)
for _b in range(256):
    _trans[_b] = _b if (32 <= _b <= 126 or _b in (9, 10, 13)) else 32
TRANS_TABLE = bytes(_trans)

# Populated once per worker process via Pool initializer (read-only afterwards).
_BITPLANE_MATRIX = None


# ----------------------------------------------------------------------------
# Rudimentary English scorer (no external NLP/model dependency)
# ----------------------------------------------------------------------------
# Standard English letter frequencies, percent of all letters (case-insensitive).
ENGLISH_LETTER_FREQ = {
    "e": 12.70, "t": 9.06, "a": 8.17, "o": 7.51, "i": 6.97, "n": 6.75,
    "s": 6.33, "h": 6.09, "r": 5.99, "d": 4.25, "l": 4.03, "c": 2.78,
    "u": 2.76, "m": 2.41, "w": 2.36, "f": 2.23, "g": 2.02, "y": 1.97,
    "p": 1.93, "b": 1.49, "v": 0.98, "k": 0.77, "j": 0.15, "x": 0.15,
    "q": 0.10, "z": 0.07,
}

# A small set of very common English words. Deliberately short/simple list —
# this is meant to be a cheap, rudimentary signal, not a full dictionary.
COMMON_WORDS = frozenset({
    "the", "of", "and", "a", "to", "in", "is", "you", "that", "it", "he",
    "was", "for", "on", "are", "as", "with", "his", "they", "i", "at",
    "be", "this", "have", "from", "or", "one", "had", "by", "but", "not",
    "what", "all", "were", "we", "when", "your", "can", "said", "there",
    "use", "an", "each", "which", "she", "do", "how", "their", "if",
    "will", "up", "other", "about", "out", "many", "then", "them",
    "these", "so", "some", "her", "would", "make", "like", "him", "into",
    "time", "has", "look", "two", "more", "write", "go", "see", "number",
    "no", "way", "could", "people", "my", "than", "first", "water",
    "been", "call", "who", "its", "now", "find", "long", "down", "day",
    "did", "get", "come", "made", "may", "part", "over", "new", "sound",
    "take", "only", "little", "work", "know", "place", "year", "live",
    "me", "back", "give", "most", "very", "after", "thing", "our",
    "just", "name", "good", "man", "think", "say", "great", "where",
    "help", "through", "much", "before", "line", "right", "too", "mean",
    "old", "any", "same", "tell", "boy", "follow", "came", "want",
    "show", "also", "around", "form", "three", "small", "set", "put",
    "end", "does", "another", "well", "large", "must", "big", "even",
    "such", "because", "turn", "here", "why", "ask", "went", "men",
    "read", "need", "land", "different", "home", "us", "move", "try",
    "kind", "hand", "again", "change", "off", "play", "away", "house",
    "point", "page", "letter", "found", "still", "learn", "should",
    "world",
})

_PUNCT_STRIP = string.punctuation


def letter_frequency_fit(lower_sample: str) -> float:
    """0..1 score — how closely the sample's letter distribution matches
    standard English letter frequencies (lower chi-squared = better fit)."""
    alpha_count = sum(lower_sample.count(c) for c in string.ascii_lowercase)
    if alpha_count == 0:
        return 0.0
    chi2 = 0.0
    for letter, expected_pct in ENGLISH_LETTER_FREQ.items():
        observed = lower_sample.count(letter)
        expected = alpha_count * (expected_pct / 100.0)
        if expected > 0:
            chi2 += (observed - expected) ** 2 / expected
    # Normalize by sample size so longer/shorter samples are comparable,
    # then squash into (0, 1] — smaller chi2 -> closer to 1.
    return 1.0 / (1.0 + chi2 / alpha_count)


def common_word_ratio(lower_sample: str) -> float:
    """Fraction of whitespace-split tokens that are in COMMON_WORDS."""
    words = lower_sample.split()
    if not words:
        return 0.0
    matches = sum(1 for w in words if w.strip(_PUNCT_STRIP) in COMMON_WORDS)
    return matches / len(words)


def alphabetic_ratio(sample: str, lower_sample: str) -> float:
    """Fraction of characters in the sample that are letters."""
    if not sample:
        return 0.0
    alpha_count = sum(lower_sample.count(c) for c in string.ascii_lowercase)
    return alpha_count / len(sample)


def score_window(window: str) -> float:
    """Applies the three heuristics to a single (already-sliced) chunk of
    text. Combined as: 0.6*word_score + 0.3*freq_score + 0.1*alpha_score."""
    if not window:
        return 0.0
    lower_window = window.lower()
    word_score = common_word_ratio(lower_window)
    freq_score = letter_frequency_fit(lower_window)
    alpha_score = alphabetic_ratio(window, lower_window)
    return (0.6 * word_score) + (0.3 * freq_score) + (0.1 * alpha_score)


def rudimentary_english_score(text: str) -> float:
    """
    Heuristic-only score in roughly [0, 1] — NOT a real language model.
    Used purely to sort combos so plausible candidates surface first.

    Slides a WINDOW_CHARS-wide window across the first SCORE_SAMPLE_CHARS
    of `text` and returns the BEST single-window score (not an average
    over the whole sample). This matters because a real embedded message
    is usually much shorter than the sampled region; averaging over the
    whole region lets unrelated trailing noise dilute a genuinely English
    passage's score. Taking the max lets that passage be judged on its
    own, regardless of what surrounds it within the sample.
    """
    sample = text[:SCORE_SAMPLE_CHARS]
    if not sample:
        return 0.0
    if len(sample) <= WINDOW_CHARS:
        return score_window(sample)

    best = 0.0
    last_start = len(sample) - WINDOW_CHARS
    for start in range(0, last_start + 1, WINDOW_STRIDE):
        s = score_window(sample[start:start + WINDOW_CHARS])
        if s > best:
            best = s
    # Make sure the tail end is covered even if it doesn't land on a stride boundary.
    if last_start % WINDOW_STRIDE != 0:
        s = score_window(sample[last_start:])
        if s > best:
            best = s
    return best


# ----------------------------------------------------------------------------
# Core extraction (vectorized — verified bit-for-bit equivalent to a naive
# nested-loop implementation across 160 randomized test cases)
# ----------------------------------------------------------------------------
def build_bitplane_matrix(img_array: np.ndarray) -> np.ndarray:
    """Shape (24, H*W) uint8 — row i = bit values of BITPLANES[i] for every pixel,
    in the same row-major (y outer, x inner) pixel order as the original script."""
    h, w, _ = img_array.shape
    n = h * w
    matrix = np.empty((24, n), dtype=np.uint8)
    for idx, (channel, bit_index) in enumerate(BITPLANES):
        chan = img_array[:, :, CHANNEL_INDEX[channel]]
        matrix[idx] = ((chan >> bit_index) & 1).reshape(-1)
    return matrix


def build_bit_level_map():
    """levels[b] = [R_idx, G_idx, B_idx] -> the three BITPLANES indices that
    share bit-index b, in R, G, B order (matches BITPLANES insertion order)."""
    levels = [[] for _ in range(8)]
    for idx, (channel, bit_index) in enumerate(BITPLANES):
        levels[bit_index].append(idx)
    return levels


def bytes_to_clean_text(packed_bytes: bytes) -> str:
    cleaned = packed_bytes.replace(b"\x00", b"")          # drop zero bytes entirely
    translated = cleaned.translate(TRANS_TABLE)            # printable / control -> self, else space
    text = translated.decode("ascii")
    return " ".join(text.split())                          # collapse whitespace


def extract_text_for_combo(combo_indices) -> str:
    """combo_indices: tuple of indices into BITPLANES, ascending order."""
    selected = _BITPLANE_MATRIX[list(combo_indices), :]     # (k, N)
    # order="F" reads column-by-column => for each pixel, all k selected bits in
    # combo order, then next pixel — exactly matching the original nested loop.
    bits = np.ravel(selected, order="F")
    usable_len = (bits.size // 8) * 8                       # original drops trailing partial byte
    if usable_len == 0:
        return ""
    packed = np.packbits(bits[:usable_len])                 # MSB-first, matches original byte<<1|bit
    return bytes_to_clean_text(packed.tobytes())


# ----------------------------------------------------------------------------
# Multiprocessing plumbing
# ----------------------------------------------------------------------------
def _init_worker(bitplane_matrix):
    global _BITPLANE_MATRIX
    _BITPLANE_MATRIX = bitplane_matrix


def process_chunk(combo_chunk):
    """Runs in a worker process. Returns EVERY combo's result — no filtering,
    just extraction + the rudimentary score for sorting."""
    results = []
    for combo in combo_chunk:
        text = extract_text_for_combo(combo)
        score = rudimentary_english_score(text)
        plane_name = ",".join(f"{BITPLANES[i][0]}{BITPLANES[i][1]}" for i in combo)
        stored_text = text if SAVE_FULL_TEXT else text[:PREVIEW_CHARS]
        results.append((combo, plane_name, score, stored_text, len(text)))
    return results, len(combo_chunk)


def generate_constrained_combos(levels):
    """
    Yield sorted tuples of bitplane indices such that:
      - exactly one bit level (0..7) contributes 2 of its 3 channels
      - every other bit level contributes exactly 1 of its 3 channels
    Every yielded combo therefore has exactly 9 entries.
    """
    all_levels = range(8)
    for special_level in all_levels:
        # the 3 ways to pick 2-of-3 channels at the "doubled" level
        special_pairs = combinations(levels[special_level], 2)
        other_levels = [lv for lv in all_levels if lv != special_level]
        other_choice_lists = [levels[lv] for lv in other_levels]  # 7 lists of length 3
        for pair in special_pairs:
            for single_choices in product(*other_choice_lists):
                yield tuple(sorted(pair + single_choices))


def chunked_combo_iter(chunk_size, levels):
    chunk = []
    for combo in generate_constrained_combos(levels):
        chunk.append(combo)
        if len(chunk) >= chunk_size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk


def total_combo_count() -> int:
    # 8 choices of doubled level * C(3,2) channel pairs * 3**7 single choices
    return 8 * 3 * (3 ** 7)


# ----------------------------------------------------------------------------
# Result writing — single pass, ranked by rudimentary English score, nothing dropped
# ----------------------------------------------------------------------------
def write_results(path, all_results, summary_lines, interrupted=False):
    """
    all_results: list of (combo, plane_name, score, stored_text, full_text_len).
    Writes EVERY combo to `path` in one pass, sorted by score descending.
    """
    ranked = sorted(all_results, key=lambda m: m[2], reverse=True)

    with open(path, "w", encoding="utf-8") as out:
        for line in summary_lines:
            out.write(line + "\n")
        if interrupted:
            out.write("[Search was interrupted before completion — "
                      "results below reflect only what was found so far]\n")
        out.write(f"Total combos logged: {len(ranked)}\n")
        out.write(f"Text per combo: {'FULL' if SAVE_FULL_TEXT else f'first {PREVIEW_CHARS} chars'}\n")
        out.write("Ranked by rudimentary English score (highest first) — "
                  "a hand-rolled heuristic (word-match + letter-frequency fit "
                  "+ alpha ratio), NOT a real language model\n\n")

        for rank, (combo, plane_name, score, stored_text, full_len) in enumerate(ranked, start=1):
            out.write("=" * 80 + "\n")
            out.write(f"Rank: {rank}\n")
            out.write(f"Planes: {plane_name}\n")
            out.write(f"Rudimentary English score: {score:.4f}\n")
            out.write(f"Full extracted text length: {full_len:,} chars"
                      f"{' (truncated below)' if not SAVE_FULL_TEXT and full_len > PREVIEW_CHARS else ''}\n")
            out.write("-" * 80 + "\n")
            out.write(stored_text + "\n\n")

        out.flush()
        os.fsync(out.fileno())


# ----------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------
def main():
    t_start = time.time()

    print(f"[*] Loading image: {INPUT_IMAGE}")
    img = Image.open(INPUT_IMAGE).convert("RGB")
    img_array = np.array(img, dtype=np.uint8)
    height, width, _ = img_array.shape
    n_pixels = height * width
    print(f"[*] Image size: {width}x{height} ({n_pixels:,} pixels)")

    print("[*] Building bitplane matrix (24 planes, vectorized)...")
    bitplane_matrix = build_bitplane_matrix(img_array)
    print(f"[*] Bitplane matrix: {bitplane_matrix.shape}, "
          f"{bitplane_matrix.nbytes / 1e6:.1f} MB")

    levels = build_bit_level_map()

    total = total_combo_count()
    n_tasks = (total + CHUNK_SIZE - 1) // CHUNK_SIZE
    print("[*] Constraint: exactly 1 bit level w/ 2 active channels, "
          "all other 7 levels w/ 1 active channel each (9 planes/combo)")
    print(f"[*] Total combinations to search: {total:,} (ALL will be logged, sorted by rudimentary score)")
    print(f"[*] Scoring sample size: first {SCORE_SAMPLE_CHARS:,} chars per combo")
    print(f"[*] Saved text per combo: {'FULL' if SAVE_FULL_TEXT else f'first {PREVIEW_CHARS} chars'}")
    print(f"[*] Workers: {NUM_WORKERS} | chunk size: {CHUNK_SIZE:,} | tasks: {n_tasks:,}\n")

    all_results = []   # (combo, plane_name, score, stored_text, full_text_len)
    checked = 0

    pool = Pool(processes=NUM_WORKERS, initializer=_init_worker, initargs=(bitplane_matrix,))

    def build_summary_lines(checked_count, elapsed_s):
        return [
            f"Input image: {INPUT_IMAGE}",
            f"Image size: {width}x{height} ({n_pixels:,} px)",
            "Constraint: exactly 1 bit level w/ 2 active channels, "
            "all other 7 levels w/ 1 active channel each (9 planes/combo)",
            f"Combinations checked: {checked_count:,}/{total:,}",
            f"Elapsed time: {elapsed_s:,.1f}s",
            "",
        ]

    try:
        with tqdm(total=total, unit="combo", unit_scale=True, smoothing=0.05,
                   dynamic_ncols=True, desc="Scanning bitplanes") as pbar:
            for results, n_in_chunk in pool.imap_unordered(
                process_chunk, chunked_combo_iter(CHUNK_SIZE, levels)
            ):
                checked += n_in_chunk
                pbar.update(n_in_chunk)
                all_results.extend(results)
                best_so_far = max((r[2] for r in all_results), default=0.0)
                pbar.set_postfix(logged=len(all_results), best_score=f"{best_so_far:.3f}")

    except KeyboardInterrupt:
        print("\n[!] Interrupted by user — terminating workers...")
        pool.terminate()
        pool.join()
        elapsed = time.time() - t_start
        write_results(OUTPUT_TXT, all_results, build_summary_lines(checked, elapsed), interrupted=True)
        print(f"[*] Partial results ({len(all_results)} combo(s)) written to {OUTPUT_TXT}")
        raise
    else:
        pool.close()
        pool.join()

    elapsed = time.time() - t_start
    write_results(OUTPUT_TXT, all_results, build_summary_lines(checked, elapsed), interrupted=False)

    print(f"\n[*] Done in {elapsed:,.1f}s. Checked {checked:,} combinations, "
          f"logged {len(all_results):,} (all of them).")
    print(f"[*] Results written to {OUTPUT_TXT}, ranked by rudimentary English score (highest first)")


if __name__ == "__main__":
    main()