---
title: Masked Language Modeling
published: 2026-02-19
description: "How MLM trains encoder models by predicting masked tokens from bidirectional context."
tags: ["Natural Language Processing", "Self-Supervised Learning"]
category: IOAI ML Notes
draft: false
access: public
---
# Syllabus Map

* Study map: [Syllabus Study Map](/posts/syllabus/ioai-study-map/)

---
# Overview

* Masked Language Modeling (MLM) is a self-supervised objective for learning contextual token representations.
* A subset of tokens is masked, and the model predicts original tokens using both left and right context.
* MLM is widely used to pretrain encoder models such as BERT-style architectures.

---

# Core Objective

## Definition

* Let $\mathcal{M}$ be masked token positions in sequence $x_{1:T}$.
* A "mask" means we hide the original token at position $i \in \mathcal{M}$ from the model input and ask the model to recover it.
* In practice, selected tokens are usually replaced by `[MASK]`, but the prediction target remains the original token.
* $x_{\backslash \mathcal{M}}$ means the visible context after masking positions in $\mathcal{M}$.
* The model minimizes negative log-likelihood over masked positions:

$$
\mathcal{L}_{\text{MLM}}=-\sum_{i\in\mathcal{M}}\log P_\theta(x_i\mid x_{\backslash \mathcal{M}})
$$

* Only masked positions contribute to loss, while unmasked tokens provide context.

## Why It Works

* Bidirectional context helps capture syntax and semantics more effectively than one-directional prediction.
* The encoder learns reusable representations for classification, tagging, and retrieval.

---

# Masking Strategy

## Standard BERT-Style Corruption

* Sample a small fraction of input tokens for corruption (commonly 15%).
* For selected positions, typical replacement split is:
  * replace with `[MASK]` most of the time,
  * replace with random token sometimes,
  * keep original token sometimes.

## Purpose of Mixed Corruption

* Reduces mismatch between pretraining and downstream text without `[MASK]`.
* Encourages robust contextual reasoning instead of shortcut reliance on a single mask token.

---

# Step-by-Step Workflow

## Step 1: Prepare corpus

* Collect and clean large unlabeled text.
* Tokenize with the target model tokenizer.

## Step 2: Build MLM training examples

* Sample mask positions per sequence.
* Construct labels only at masked positions.

## Step 3: Pretrain encoder

* Optimize MLM loss with mini-batch training.
* Track masked-token prediction quality on validation data.

## Step 4: Adapt to downstream task

* Fine-tune with task-specific objective (classification, token labeling, retrieval).
* Optionally run domain-adaptive MLM before final fine-tuning.

---

# Practical Notes

## Choose masking policy carefully

* Overly predictable masking can reduce representation quality.
* Dynamic masking across epochs typically improves data efficiency.
* Domain-specific tokenization can significantly affect MLM learning quality.

## Use domain-adaptive pretraining when needed

* Continuing MLM on in-domain text often improves specialized vocabulary handling.
* Gains are strongest when downstream data distribution differs from general web text.
* Stop early if validation indicates over-specialization.

## Remember MLM limitations

* Standard MLM encoders are not direct left-to-right generators.
* For generation-heavy tasks, autoregressive models are usually more suitable.
* For understanding tasks, MLM-pretrained encoders are often strong baselines.
