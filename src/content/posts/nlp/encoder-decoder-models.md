---
title: Encoder-Decoder Models
published: 2026-02-16
description: "Sequence-to-sequence models for translation and multimodal tasks."
tags: ["Natural Language Processing"]
category: IOAI ML Notes
draft: false
access: restricted
---
# Syllabus Map

* Study map: [Syllabus Study Map](/posts/syllabus/ioai-study-map/)

---
# Overview

* Encoder-decoder models map input sequences to output sequences.
* They are the standard seq2seq architecture for translation, summarization, and speech transcription.

---

# Core Idea

* Encoder builds a latent representation.
* Decoder generates the target sequence.
* Decoder uses both:
* causal self-attention over previous target tokens,
* cross-attention over encoder outputs.

$$
P(y_{1:T}\mid x)=\prod_{t=1}^{T}P(y_t\mid y_{<t},x)
$$

---

# Transformer Encoder-Decoder Mechanics

## Encoder

* Input tokens are embedded + positional encoding.
* Stack self-attention + FFN blocks to produce contextual memory $H$.

## Decoder

* Uses masked self-attention over generated prefix.
* Uses cross-attention where decoder queries attend to encoder memory:

$$
\text{CrossAttn}(Q,K,V)=\text{softmax}\!\left(\frac{QK^\top}{\sqrt{d_k}}\right)V
$$

* Here, $Q$ comes from decoder states, and $K,V$ come from encoder outputs.

---

# Training Objective

* Teacher forcing feeds ground-truth previous token during training.
* Loss is token-level cross-entropy:

$$
\mathcal{L}=-\sum_{t=1}^{T}\log P_\theta(y_t^\star\mid y_{<t}^\star,x)
$$

* Label smoothing is commonly used for better generalization.

---

# Inference Workflow

## Step 1: Encode source sequence

* Run input sequence once through encoder.
* Cache encoder outputs for all decoding steps.

## Step 2: Start decoding

* Initialize with start token.
* Predict next-token distribution.

## Step 3: Search strategy

* Greedy decoding: fastest, less diverse.
* Beam search: better sequence quality.
* Sampling (top-k/top-p): more diverse generation.

## Step 4: Stop condition

* Stop at end-of-sequence token or maximum length.

---

# Use Cases

* Machine translation.
* Summarisation.
* Vision-language modelling.
* Speech recognition (audio encoder + text decoder).

---

# Practical Notes

## Beam size improves quality but increases latency.

* In practice, beam size improves quality but increases latency.
## Exposure bias can appear because training uses teacher forcing but inference uses model outputs.

* In practice, exposure bias can appear because training uses teacher forcing but inference uses model outputs.
## For long inputs, memory can be a bottleneck due to attention complexity.

* In practice, for long inputs, memory can be a bottleneck due to attention complexity.




