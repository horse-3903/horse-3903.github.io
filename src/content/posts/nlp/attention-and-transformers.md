---
title: Attention and Transformers
published: 2026-02-16
description: "Attention mechanisms and transformer architectures for sequence modelling."
tags: ["Neural Network", "Deep Learning"]
category: IOAI ML Notes
draft: false
pinned: false
access: public
---
# Syllabus Map

* Study map: [Syllabus Study Map](/posts/syllabus/ioai-study-map/)

---

# Overview

* Attention lets each token directly read relevant tokens, instead of compressing everything into one fixed vector.
* Transformers stack attention and feed-forward blocks for scalable sequence modelling.
* Core advantages over RNNs: parallel training and better long-range dependency handling.

---

# Scaled Dot-Product Attention

* Each token is projected into query ($Q$), key ($K$), and value ($V$) vectors.
* Attention weights are similarity scores between queries and keys.

$$
\text{Attention}(Q,K,V)=\text{softmax}\!\left(\frac{QK^\top}{\sqrt{d_k}}\right)V
$$

* $d_k$ is key dimension; scaling by $\sqrt{d_k}$ stabilizes logits.
* Softmax rows sum to 1, so each token computes a weighted sum of value vectors.

---

# Multi-Head Attention

* Instead of one attention map, use multiple heads to capture different relations.

$$
\text{head}_i=\text{Attention}(QW_i^Q,KW_i^K,VW_i^V)
$$

$$
\text{MHA}(Q,K,V)=\text{Concat}(\text{head}_1,\dots,\text{head}_h)W^O
$$

* $h$ is number of heads.
* Different heads often specialize (syntax, positional patterns, long dependencies).

---

# Transformer Block

* Standard block has:
* multi-head attention,
* position-wise feed-forward network (FFN),
* residual connections and layer normalization.

$$
X' = X + \text{MHA}(\text{LN}(X))
$$

$$
Y = X' + \text{FFN}(\text{LN}(X'))
$$

* FFN is typically two linear layers with nonlinearity (GELU/ReLU).

---

# Positional Information

* Attention alone is permutation-invariant; position encoding is required.
* Common choices:
* learned absolute positional embeddings,
* sinusoidal embeddings,
* relative/RoPE-style methods in modern LLMs.

---

# Encoder vs Decoder Attention

## Encoder Self-Attention

* Bidirectional: token can attend to all tokens in the sequence.
* Used in BERT-like encoders.

## Decoder Self-Attention (Causal)

* Masked: token at position $t$ can only attend to positions $\le t$.
* Used in GPT-style autoregressive models.

## Cross-Attention

* Decoder queries attend to encoder keys/values.
* Used in seq2seq tasks (translation, summarization).

---

# Complexity and Scaling

* Full self-attention cost is quadratic in sequence length:

$$
\mathcal{O}(n^2 d)
$$

* $n$ is sequence length and $d$ is hidden size.
* Long-context variants (sparse/windowed attention) reduce memory/compute.

---

# Practical Training Pipeline

## Step 1: Tokenize and batch

* Convert text to token IDs.
* Pad/truncate to max sequence length.

## Step 2: Build masks

* Padding mask for variable lengths.
* Causal mask for autoregressive decoding.

## Step 3: Forward pass

* Embed tokens + positions.
* Run through stacked transformer blocks.

## Step 4: Compute objective

* Next-token cross-entropy (decoder LMs),
* masked token loss (encoder models),
* or task-specific supervised loss.

## Step 5: Optimize

* AdamW + learning-rate warmup/decay is common.
* Use gradient clipping and mixed precision for stability/throughput.

---

# Practical Notes

## Attention heads and depth matter more than single-layer width for many tasks.

* Attention heads and depth matter more than single-layer width for many tasks.
## Longer context improves tasks with long dependencies but raises cost.

* Longer context improves tasks with long dependencies but raises cost.
## Prompt/instruction format strongly affects decoder-model behavior at inference.

* Prompt/instruction format strongly affects decoder-model behavior at inference.

