---
title: Language Modelling
published: 2026-02-19
description: "Modelling token sequences for generation and prediction."
tags: ["Natural Language Processing"]
category: IOAI ML Notes
draft: false
access: restricted
---
# Syllabus Map

* Study map: [Syllabus Study Map](/posts/syllabus/ioai-study-map/)

---
# Overview

* Language models learn to predict the next token in a sequence.
* They estimate sequence probability and support generation, scoring, and completion.

$$
P(x_{1:T})=\prod_{t=1}^{T}P(x_t\mid x_{<t})
$$

---

# Autoregressive Modelling

## Core Idea

* Predict token $x_t$ from previous tokens $x_{<t}$ with causal masking.

$$
\mathcal{L}_{\text{AR}}=-\sum_{t=1}^{T}\log P_\theta(x_t\mid x_{<t})
$$

## Practical Notes

### Enables text generation

* Autoregressive decoding produces coherent next-token continuations.

### Benefits from large pretraining corpora

* Larger and cleaner corpora usually improve fluency and coverage.

### Supports prompting and instruction tuning

* Few-shot prompts and instruction tuning can adapt behavior without architecture changes.

---

# Masked Modelling

## Core Idea

* Predict masked tokens using full context.

$$
\mathcal{L}_{\text{MLM}}=-\sum_{i\in \mathcal{M}}\log P_\theta(x_i\mid x_{\backslash\mathcal{M}})
$$

## Practical Notes

### Used by encoder models

* MLM is the core objective behind BERT-style bidirectional encoders.

### Strong for understanding tasks

* MLM representations are typically strong for classification, retrieval, and tagging.

### Not direct left-to-right generation

* Standard MLM encoders do not naturally decode tokens autoregressively.

---

# Evaluation Metrics

## Perplexity

$$
\text{PPL}=\exp\left(
-\frac{1}{T}\sum_{t=1}^{T}\log P_\theta(x_t\mid x_{<t})
\right)
$$

* Lower perplexity means better next-token prediction.
* Compare only with same tokenizer and data domain.

---

# Decoding Strategies (Autoregressive)

## Greedy Decoding

* Select highest-probability token each step.
* Fast but can be repetitive.

## Temperature Sampling

$$
p_i'=\frac{\exp(\log p_i / \tau)}{\sum_j \exp(\log p_j / \tau)}
$$

* $\tau<1$ makes output more deterministic.
* $\tau>1$ increases diversity.

## Top-k and Top-p (Nucleus)

* **Top-k**: sample only from top $k$ tokens.
* **Top-p**: sample smallest token set with cumulative probability $\ge p$.
* Usually combine with repetition penalties for longer outputs.

---

# Training Pipeline (Practical)

## Step 1: Prepare corpus

* Deduplicate and clean text.
* Build tokenizer aligned with domain vocabulary.

## Step 2: Create training sequences

* Chunk documents into fixed context windows.
* Build labels by shifting tokens one position for AR training.

## Step 3: Optimize model

* Use AdamW, LR warmup/decay, mixed precision.
* Monitor training/validation perplexity and divergence.

## Step 4: Adapt model

* Continue pretraining on domain text.
* Apply supervised fine-tuning or instruction tuning for specific behavior.

---

# Practical Notes

## Data quality often matters more than modest architecture changes.

* In practice, data quality often matters more than modest architecture changes.
## Context length improves long-dependency tasks but increases cost.

* In practice, context length improves long-dependency tasks but increases cost.
## Safety/alignment layers are needed for production deployment.

* In practice, safety/alignment layers are needed for production deployment.




