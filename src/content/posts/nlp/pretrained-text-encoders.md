---
title: Pre-trained Text Encoders
published: 2026-02-19
description: "Transformer-based text encoders and their use cases."
tags: ["Natural Language Processing"]
category: IOAI ML Notes
draft: false
access: public
---
# Syllabus Map

* Study map: [Syllabus Study Map](/posts/syllabus/ioai-study-map/)

---
# Overview

* Pre-trained encoders provide rich text representations.
* They map tokens (or full sentences) into contextual vectors that transfer across tasks.
* Most are trained with self-supervised objectives before task-specific fine-tuning.

---

# Core Objectives

## Masked Language Modeling (MLM)

* Mask a subset of tokens and predict the originals using both left and right context.

$$
\mathcal{L}_{\text{MLM}}=-\sum_{i\in \mathcal{M}}\log p_\theta(x_i \mid x_{\backslash \mathcal{M}})
$$

* $\mathcal{M}$ is the set of masked positions.

## Contrastive Sentence Objectives

* Pull semantically related sentence embeddings together and push unrelated ones apart.
* Common in sentence-transformer style encoders.

---

# Example Models

* **BERT**: bidirectional encoder with MLM (+ NSP in original version).
* **RoBERTa**: optimized BERT training recipe (no NSP, larger data/batches).
* **DistilBERT**: compressed BERT via distillation for lower latency.
* **MPNet / DeBERTa**: stronger encoder variants for many downstream benchmarks.

---

# Common Uses

## Feature Extraction

* Freeze encoder and train a small head.
* Use pooled embedding for classification or retrieval features.

## Fine-Tuning

* Update all weights for task-specific performance.
* Add task head (classification/token tagging) and train end-to-end.

---

# Pooling Strategies

* **[CLS] pooling**: use first token representation.
* **Mean pooling**: average token embeddings over non-padding tokens.
* **Max pooling**: take per-dimension max over tokens.
* For semantic retrieval, mean pooling often outperforms raw [CLS] on many datasets.

---

# Step-by-Step Usage

## Step 1: Choose encoder size

* Base model for balanced quality/latency.
* Distilled/smaller model for stricter latency or memory constraints.

## Step 2: Tokenize and truncate

* Use model-matched tokenizer.
* Set max sequence length based on domain document size.

## Step 3: Start with linear probe

* Freeze encoder and train lightweight head.
* Use this to estimate transfer quality quickly.

## Step 4: Fine-tune if needed

* Unfreeze all layers.
* Use smaller learning rate for encoder than task head.

## Step 5: Evaluate robustness

* Check domain shift, long texts, misspellings, and rare terminology.

---

# Practical Notes

## Use domain-adaptive pretraining when domain mismatch is large

* Continue MLM training on in-domain unlabeled text before downstream fine-tuning.
* This often improves specialized terminology handling and contextual representations.
* Monitor for overfitting to narrow corpus style if domain data is limited.

## Normalize embeddings for retrieval with cosine similarity

* L2-normalize sentence embeddings before indexing and search.
* Cosine similarity then reflects angular similarity rather than vector magnitude.
* Keep pooling and normalization consistent between indexing and query pipelines.

## Reduce serving cost with quantization and distillation

* Use quantization to lower memory footprint and improve inference throughput.
* Distill larger encoders into smaller students to retain most performance at lower latency.
* Benchmark quality/latency tradeoffs on real production-like workloads before rollout.




