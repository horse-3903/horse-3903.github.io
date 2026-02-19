---
title: Pre-trained Audio Encoders
published: 2026-02-19
description: "Self-supervised and supervised audio encoders for speech and general audio tasks."
tags: ["Audio Processing", "Deep Learning"]
category: IOAI ML Notes
draft: false
access: restricted
---
# Syllabus Map

* Study map: [Syllabus Study Map](/posts/syllabus/ioai-study-map/)

---
# Overview

* Pre-trained audio encoders map waveforms/spectrograms into transferable representations.
* They are often trained self-supervised on unlabeled audio, then fine-tuned for downstream tasks.

---

# Pre-trained Audio Encoders

## Common Input Representations
![](../../assets/pretrained-audio/image.png)
* Raw waveform (1D signal).
* Log-mel spectrogram (time-frequency 2D representation).
* Patchified spectrogram tokens (for transformer encoders).

## Example Model Families

### wav2vec 2.0

* **Pretraining signal**: masked prediction with contrastive learning on raw waveform latents.
* **Strengths**: strong speech representations with relatively simple downstream fine-tuning.
* **Best for**: ASR and speech tasks when unlabeled speech is available.
* **Tradeoff**: can be less robust than newer variants under heavy noise/channel shift.

### HuBERT

* **Pretraining signal**: predicts pseudo-label clusters on masked frames (iterative target refinement).
* **Strengths**: stable training and strong phonetic/linguistic structure in embeddings.
* **Best for**: robust ASR transfer and speech representation learning.
* **Tradeoff**: quality depends on clustering/pseudo-label pipeline.

### WavLM

* **Pretraining signal**: masked speech modeling plus denoising and speaker-aware objectives.
* **Strengths**: better robustness to noise and stronger speaker/discriminative cues.
* **Best for**: mixed speech tasks (ASR + speaker/event-style tasks).
* **Tradeoff**: more complex objective and training recipe.

### Whisper Encoder

* **Pretraining signal**: supervised multilingual ASR/translation training inside encoder-decoder setup.
* **Strengths**: strong multilingual robustness and excellent real-world transcription behavior.
* **Best for**: end-to-end ASR pipelines and speech translation-style tasks.
* **Tradeoff**: less "pure SSL encoder" style; often heavier and tied to seq2seq decoding stack.

---

# Self-Supervised Pretraining Idea

* Learn robust audio representations without manual labels.
* Mask portions of audio features and predict hidden targets.

$$
\mathcal{L}_{\text{SSL}}=
\mathcal{L}_{\text{contrastive or classification}}+
\lambda\mathcal{L}_{\text{diversity/regularization}}
$$

* Objective details vary by model family.

---

# Step-by-Step Usage

## Step 1: Choose encoder by task

* Speech recognition: wav2vec 2.0 / HuBERT / Whisper-style encoders.
* Audio event classification: spectrogram transformer or CNN encoders.

## Step 2: Prepare features

* Resample audio consistently (for example 16 kHz for speech).
* Normalize loudness and remove invalid/silent segments.

## Step 3: Extract embeddings

* Run encoder to get frame-level or clip-level embeddings.
* Pool over time for utterance-level tasks.

## Step 4: Train downstream head

* Classification head for event/intent.
* CTC or seq2seq decoder for transcription tasks.

## Step 5: Fine-tune selectively

* Start with frozen encoder.
* Unfreeze upper layers if domain mismatch is large.

---

# Evaluation

* **ASR**: WER/CER.
* **Classification**: accuracy, macro-F1.
* **Retrieval/speaker**: Recall@K, EER, minDCF.

---

# Practical Notes

## Pretraining data diversity strongly affects robustness (accents, noise, microphones).

* In practice, pretraining data diversity strongly affects robustness (accents, noise, microphones).
## Domain adaptation with continued pretraining can improve noisy or specialized audio.

* In practice, domain adaptation with continued pretraining can improve noisy or specialized audio.
## For long audio, chunking + overlap or streaming encoders are important for latency.

* In practice, for long audio, chunking + overlap or streaming encoders are important for latency.




