---
title: Audio Models
published: 2026-02-16
description: "Task-specific audio model families for recognition, understanding, and generation."
tags: ["Audio Processing", "Natural Language Processing", "Deep Learning"]
category: IOAI ML Notes
draft: false
access: restricted
---
# Syllabus Map

* Study map: [Syllabus Study Map](/posts/syllabus/ioai-study-map/)

---
# Overview

* Audio models handle speech recognition, audio understanding, and speech/audio generation.
* Choice of model depends on output type:
* text output (ASR),
* class/embedding output (classification, retrieval),
* waveform output (TTS, vocoders, generative audio).

---

# Automatic Speech Recognition (ASR)

## Main Approaches

* **CTC-based models**: predict frame-level token probabilities with monotonic alignment.
* **Encoder-decoder seq2seq**: decoder generates transcript autoregressively.
* **Transducer (RNN-T)**: streaming-friendly compromise between CTC and seq2seq.

## CTC Objective

$$
\mathcal{L}_{\text{CTC}}=-\log P(y\mid x)
$$

* $x$ is acoustic input and $y$ is transcript.
* CTC sums over valid alignments between frames and tokens.

## Typical ASR Pipeline

### Step 1: Audio preprocessing
* Resample, normalize, and chunk long recordings.

### Step 2: Feature/encoder forward
* Extract log-mel features or use raw-waveform frontend.
* Run encoder to produce frame representations.

### Step 3: Decode text
* Greedy/beam search for CTC.
* Beam search with language model fusion when needed.

### Step 4: Evaluate
* Report WER and CER.

---

# Audio Classification and Event Detection

## Tasks

* Speech emotion recognition.
* Speaker identification/verification.
* Acoustic scene and event classification.

## Model Families

* CNN/CRNN on log-mel spectrograms.
* Transformer encoders on spectrogram patches.
* Pretrained audio encoders + linear head.

## Typical Objective

$$
\mathcal{L}_{\text{CE}}=-\sum_{i=1}^{N}\sum_{c=1}^{C} y_{i,c}\log \hat{p}_{i,c}
$$

## Practical Notes

### Use class-balanced sampling for rare events.

* Use class-balanced sampling for rare events.
### Strong augmentations: SpecAugment, time masking, noise, reverb.

* Strong augmentations: SpecAugment, time masking, noise, reverb.

---

# Audio-Language Models

## Core Idea

* Combine an audio encoder with a language model decoder or projector.
* Support instruction following over audio, speech QA, and multimodal chat.

## Typical Architecture

* Audio encoder produces token/segment embeddings.
* Projection layer maps audio embeddings into LLM embedding space.
* LLM decodes text conditioned on audio context.

## Applications

* Speech understanding with long-form reasoning.
* Audio captioning.
* Cross-modal retrieval and question answering.

---

# Speech and Audio Generation

## Text-to-Speech (TTS)

* Input text -> acoustic model -> vocoder waveform.
* Modern systems use diffusion/flow/neural codec decoders for quality.

## Voice Conversion

* Preserve linguistic content while changing speaker identity/style.
* Often uses disentangled speaker/content embeddings.

## Music/Sound Generation

* Autoregressive token models or diffusion over audio latents.
* Conditioning can include text, melody, or style prompts.

---

# Example Models

* **Whisper**: robust multilingual ASR encoder-decoder.
* **wav2vec 2.0 / HuBERT-based ASR stacks**: strong speech encoder backbones.
* **Conformer ASR models**: strong local+global sequence modeling for speech.
* **Qwen-Audio-style models**: audio-language instruction systems.

---

# Model Selection Checklist

* **Need streaming?** choose transducer/streaming conformer.
* **Need best offline transcription quality?** encoder-decoder ASR with beam search.
* **Need low-label setup?** pretrained encoder + lightweight task head.
* **Need multimodal interaction?** audio-language model with instruction tuning.

---

# Practical Notes

## Match sample rate and frontend to pretrained checkpoint assumptions.

* Match sample rate and frontend to pretrained checkpoint assumptions.
## Domain mismatch (accent, channel, background noise) can dominate errors.

* Domain mismatch (accent, channel, background noise) can dominate errors.
## Evaluate by domain slice, not only aggregate metrics.

* Evaluate by domain slice, not only aggregate metrics.