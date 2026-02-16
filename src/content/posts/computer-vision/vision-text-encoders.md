---
title: Vision-Text Encoders
published: 2026-02-16
description: "Joint vision-language embedding models."
tags: ["Computer Vision", "Natural Language Processing"]
category: IOAI ML Notes
draft: false
access: restricted
---
# Syllabus Map

* Study map: [Syllabus Study Map](/posts/syllabus/ioai-study-map/)

---
# Overview

* Vision-text encoders map images and text into a shared space.
* Goal: make semantically matching image-text pairs close, and mismatched pairs far apart.
* Main use cases: zero-shot classification, cross-modal retrieval, and multimodal search.

---

# Core Idea

* Train with paired image-text data.
* Use contrastive objectives to align modalities.
* Typical architecture is a **dual encoder**:
* Image encoder $f_\theta(\cdot)$ maps image $I$ to vector $v$.
* Text encoder $g_\phi(\cdot)$ maps caption/prompt $T$ to vector $t$.
* Embeddings are L2-normalized before similarity scoring.

$$
v = \frac{f_\theta(I)}{\|f_\theta(I)\|_2}, \quad
t = \frac{g_\phi(T)}{\|g_\phi(T)\|_2}
$$

* Similarity is scaled cosine similarity:

$$
s_{ij} = \tau \, v_i^\top t_j
$$

* $s_{ij}$ is similarity between image $i$ and text $j$, and $\tau$ is a learnable temperature scale.

---

# Contrastive Training Objective

* For a batch of $N$ paired examples, compute the similarity matrix $S \in \mathbb{R}^{N\times N}$.
* Use symmetric InfoNCE loss: image-to-text and text-to-image.

$$
\mathcal{L}_{i\rightarrow t}
= -\frac{1}{N}\sum_{i=1}^N
\log
\frac{\exp(s_{ii})}{\sum_{j=1}^N \exp(s_{ij})}
$$

$$
\mathcal{L}_{t\rightarrow i}
= -\frac{1}{N}\sum_{i=1}^N
\log
\frac{\exp(s_{ii})}{\sum_{j=1}^N \exp(s_{ji})}
$$

$$
\mathcal{L} = \frac{1}{2}\left(\mathcal{L}_{i\rightarrow t}+\mathcal{L}_{t\rightarrow i}\right)
$$

* The diagonal terms $s_{ii}$ are matched pairs; off-diagonals are in-batch negatives.

---

# Example Models

* **CLIP**: ViT/ResNet image encoder + Transformer text encoder; trained on large noisy web image-text pairs.
* **OpenCLIP**: open-source CLIP reproductions trained on LAION-scale datasets.
* **ALIGN**: large-scale weakly supervised contrastive image-text pretraining.

---

# CLIP Step-by-Step

## Training

### Step 1: Build paired mini-batch
* Sample a batch of $N$ image-caption pairs $(I_i, T_i)$.
* Each pair is treated as a positive match.

### Step 2: Encode image and text
* Compute image embeddings with vision encoder.
* Compute text embeddings with text encoder.
* L2-normalize both embeddings.

### Step 3: Compute similarity matrix
* Compute all pairwise similarities between image and text embeddings in the batch.

$$
S_{ij} = \tau \, v_i^\top t_j
$$

### Step 4: Compute symmetric contrastive loss
* Optimize image-to-text and text-to-image objectives jointly.
* Positive pairs are diagonal entries $S_{ii}$; others are negatives.

### Step 5: Update both encoders
* Backpropagate total contrastive loss.
* Update vision encoder, text encoder, and temperature parameter.

## Inference

### Step 1: Prepare class prompts or queries
* For zero-shot classification, create a text prompt per class.
* For retrieval, use arbitrary text/image queries.

### Step 2: Encode once, compare many
* Encode query image/text.
* Encode candidate texts/images and cache embeddings.

### Step 3: Rank by cosine similarity
* Compute similarity and rank candidates.
* Pick top class (classification) or top-$k$ results (retrieval).

$$
\hat{y}=\arg\max_c \; v^\top t_c
$$

### Step 4: Optional prompt ensembling
* Use multiple templates per class and average embeddings.
* Improves robustness to wording choices.

---

# Inference Patterns

## Zero-Shot Classification

* Create text prompts per class (for example, "a photo of a {class}").
* Encode image once and all prompts once.
* Choose class with highest image-text similarity.

$$
\hat{y} = \arg\max_{c} \; v^\top t_c
$$

## Image-to-Text Retrieval

* Encode all candidate captions/documents.
* Retrieve top-$k$ texts by similarity to image embedding.

## Text-to-Image Retrieval

* Encode all candidate images.
* Retrieve top-$k$ images by similarity to text embedding.

---

# Practical Notes

## Enables zero-shot classification.

* Enables zero-shot classification.
## Useful for retrieval and captioning pipelines.

* Useful for retrieval and captioning pipelines.
## Prompt engineering matters: template choice can change zero-shot accuracy.

* Prompt engineering matters: template choice can change zero-shot accuracy.
## Multiple prompt ensembling (average class prompt embeddings) often improves results.

* Multiple prompt ensembling (average class prompt embeddings) often improves results.
## For retrieval at scale, index normalized embeddings with ANN search (for example, FAISS/HNSW).

* For retrieval at scale, index normalized embeddings with ANN search (for example, FAISS/HNSW).
## Common metrics:

* Common metrics:
## Zero-shot classification: top-1/top-5 accuracy.

* Zero-shot classification: top-1/top-5 accuracy.
## Retrieval: Recall@K and mean reciprocal rank.

* Retrieval: Recall@K and mean reciprocal rank.
## Known limitations:

* Known limitations:
## Sensitive to web-data bias and prompt wording.

* Sensitive to web-data bias and prompt wording.
## Struggles with fine-grained counting or OCR-heavy scenes without task adaptation.

* Struggles with fine-grained counting or OCR-heavy scenes without task adaptation.




