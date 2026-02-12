---
title: Data Embeddings
published: 2026-02-12
description: "Embeddings for text, images, audio and structured data with practical usage notes."
tags: ["Neural Network", "Deep Learning"]
category: IOAI ML Notes
draft: false
pinned: false
access: restricted
---
# Syllabus Map

* Study map: [Syllabus Study Map](/posts/syllabus/ioai-study-map/)

---

# Overview

* Embeddings map discrete or high-dimensional inputs into dense vectors that capture **similarity** and **structure**.
* Good embeddings make **downstream learning easier** by placing related items closer in vectour space.
* This note summarises embeddings for **text, images, audio, and structured data**, plus practical tips.

---

# Core Idea

* An embedding is a learnable function $f(x) \rightarrow \mathbb{R}^d$.
* Similar inputs should have **nearby vectors** (cosine similarity or dot product).
* Embeddings are usually **trained jointly** with a task or via **self-supervision**.

---

# Text Embeddings

## Tokenisation matters
* **Word-level**: simple but large vocab and OOV issues.
* **Subword** (BPE/WordPiece): handles OOV and morphology.
* **Character**: robust but longer sequences.

## Static vs contextual
* **Static** (Word2Vec, GloVe, fastText): one vectour per token.
* **Contextual** (BERT, GPT-style): token vectour depends on surrounding words.

## Training objectives
* **Skip-gram / CBOW**: predict context words.
* **Masked language modelling**: predict masked tokens.
* **Contrastive**: pull positives together, push negatives apart.

## Practical notes
* For similarity, **cosine** is a strong default.
* Normalise embeddings if using dot products across batches.
* Mean-pooling of token vectors is a good baseline for sentence embeddings.

---

# Positional Embeddings

* Models without recurrence need **position information**.
* **Learned positional embeddings**: lookup table indexed by position.
* **Sinusoidal**: fixed, extrapolates to longer sequences.
* **Relative positions**: encode distance between tokens, improves generalisation.

---

# Image Embeddings

## Common approaches
* **CNN features**: global average pooled activations.
* **Vision Transformers**: patch embedding + positional embeddings.
* **CLIP-style**: map images and text into a shared space.

## Practical notes
* Pretrained image encoders often transfer well with **linear probing**.
* For retrieval, **L2-normalise** embeddings.

---

# Audio Embeddings

## Inputs
* Raw waveform, but often use **spectrograms** or **MFCCs**.

## Embedding strategies
* CNN or Transformer over time-frequency bins.
* Contrastive objectives (e.g., predict future segments).

## Practical notes
* Log-mel spectrograms are a robust default.
* Augmentations (time shift, noise) improve invariance.

---

# Structured Data Embeddings

## Categorical features
* Use **embedding tables** instead of one-hot for large vocabularies.
* Rare categories can be bucketed into `UNK`.

## Numerical features
* Standardise inputs before feeding into MLPs.
* Optionally embed via **piecewise linear** or **bucket embeddings**.

## Mixed data
* Concatenate numerical features with categorical embeddings.
* Use **feature crossing** only when necessary to reduce complexity.

---

# Graph Embeddings (Brief)

* Node embeddings via **message passing** (GCN, GAT).
* Graph-level embeddings via **pooling** (mean, sum, attention).
* Contrastive objectives work well for self-supervised graph learning.

---

# How To Choose Embedding Sise

* Too small: underfits, loses nuance.
* Too large: overfits, slower, harder to regularise.
* Rules of thumb:
  * Small vocab (<1k): 16–64 dims.
  * Medium (1k–100k): 64–256 dims.
  * Large (>100k): 256–1024 dims.
* Validate with **downstream performance** and **memory budget**.

---

# Practical Tips

* **Normalise** for retrieval tasks; keep raw for classification unless needed.
* For nearest-neighbour search, use **approximate** indexes (FAISS, HNSW).
* **Freeze vs finetune**: freeze when data is small, finetune when domain shifts.
* Monitour for **embedding collapse** (all vectors become similar).

---

# PyTorch Examples

```py
import torch
import torch.nn as nn

# Token embeddings
tok_emb = nn.Embedding(num_embeddings=30000, embedding_dim=256)

# Positional embeddings (learned)
pos_emb = nn.Embedding(num_embeddings=512, embedding_dim=256)

# Categorical feature embedding
city_emb = nn.Embedding(num_embeddings=1000, embedding_dim=32)

# Simple sentence embedding: mean pooling
tokens = torch.randint(0, 30000, (8, 32))  # batch, seq
emb = tok_emb(tokens)
sent_emb = emb.mean(dim=1)
```



