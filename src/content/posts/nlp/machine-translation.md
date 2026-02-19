---
title: Machine Translation
published: 2026-02-19
description: "Machine translation with encoder-decoder models, training, decoding, and evaluation."
tags: ["Natural Language Processing"]
category: IOAI ML Notes
draft: false
access: restricted
---
# Syllabus Map

* Study map: [Syllabus Study Map](/posts/syllabus/ioai-study-map/)

---
# Overview

* Machine translation (MT) is a core NLP task: convert a source-language sentence into a target-language sentence.
* Modern MT is usually built with encoder-decoder transformers trained on parallel corpora (bitext).
* MT is challenging because languages diverge in word order, lexical meaning, morphology, and referential style.
* Encoder-decoder models with cross-attention are the standard backbone for high-quality neural MT systems.

$$
P(y_{1:T'} \mid x_{1:T})=\prod_{t=1}^{T'}P(y_t\mid y_{<t},x_{1:T})
$$

---

# Encoder-Decoder MT

## Core Idea

* The encoder reads the source sentence and outputs contextual representations.
* The decoder generates the target sentence autoregressively.
* Cross-attention lets each decoder step attend to all encoder states.
* Training uses teacher forcing: feed the gold previous target token during learning.

$$
\mathcal{L}_{\text{MT}}=-\sum_{t=1}^{T'}\log P_\theta(y_t\mid y_{<t},x)
$$

## Practical Notes

### Requires parallel data

* MT models are supervised on source-target sentence pairs from bitext.

### Uses shared subword vocabularies

* BPE, unigram, or WordPiece tokenization helps handle rare words and morphology.

### Sentence alignment quality matters

* Poor document/sentence alignment in training data directly hurts translation quality.

---

# Linguistic Divergences

## Core Idea

* Languages differ structurally and lexically, so translation is not token-by-token substitution.
* Typology studies systematic cross-linguistic variation that affects MT design.
* Common divergences include word order, lexical gaps, morphology, and referential density.

## Practical Notes

### Word-order typology

* SVO languages include English, French, Mandarin; SOV includes Hindi and Japanese; VSO includes Irish and Arabic.
* OV languages tend to use postpositions; VO languages tend to use prepositions.

### Lexical divergence and WSD

* A source word may map to multiple target words based on context (word sense disambiguation).
* Some meanings have lexical gaps: no short exact equivalent in another language.

### Morphology and reference

* Languages vary from isolating to polysynthetic and from agglutinative to fusional.
* Pronoun use also varies (pro-drop vs non-pro-drop), affecting adequacy and fluency choices.

---

# Evaluation Metrics

## Adequacy and Fluency

* Adequacy: how well the translation preserves source meaning.
* Fluency: how natural and grammatical the target output is.
* Human evaluation is the gold standard for both.

## Automatic Metrics

* **chrF**: character n-gram precision/recall style metric; robust across morphology-heavy languages.
* **BLEU**: n-gram overlap metric; widely used but less sensitive to semantics.
* **Embedding-based metrics** (for example BERTScore): compare semantic similarity in contextual embedding space.

---

# Decoding Strategies (MT)

## Greedy Decoding

* Picks the best next token at each step.
* Fast but often suboptimal for full-sentence translation quality.

## Beam Search

* Keeps top $k$ partial hypotheses (beam width) at each timestep.
* Approximates search for the sequence with highest model probability.
* Usually combined with length normalization to reduce short-sentence bias.

## Minimum Bayes Risk (MBR)

* Chooses the candidate with minimum expected error under a utility metric (for example chrF or BERTScore).
* Often improves final quality compared with pure likelihood-based beam selection.

---

# Training Pipeline (Practical)

## Step 1: Build and align bitext

* Collect parallel corpus and clean noisy pairs.
* Run document/sentence alignment using similarity scoring and dynamic programming.

## Step 2: Tokenize and batch

* Build subword vocabulary over source and target data.
* Create encoder-decoder training pairs with attention masks.

## Step 3: Train encoder-decoder

* Train with teacher forcing on negative log-likelihood.
* Monitor validation translation metrics, not only token loss.

## Step 4: Expand data coverage

* Use backtranslation: translate target-side monolingual data backward to create synthetic source sentences.
* Add synthetic bitext and retrain forward model for stronger low-resource performance.
* Optionally train multilingual MT with language tags to share signal across related languages.

---

# Practical Notes

### Data quality dominates

* Cleaning, alignment, and domain matching often matter more than small architecture tweaks.

### Low-resource gains come from augmentation

* Backtranslation and multilingual transfer are strong baselines when parallel data is scarce.

### Evaluate with multiple lenses

* Use automatic metrics (chrF/BLEU/BERTScore) plus targeted human checks for adequacy and fluency.

### CAT workflows remain important

* In localization, MT is often used for draft generation and then post-edited by human translators.




