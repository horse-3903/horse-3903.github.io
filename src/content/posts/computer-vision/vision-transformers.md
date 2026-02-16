---
title: Vision Transformers
published: 2026-02-16
description: "How vision transformers model images as token sequences."
tags: ["Computer Vision", "Deep Learning"]
category: IOAI ML Notes
draft: false
access: restricted
---
# Syllabus Map

* Study map: [Syllabus Study Map](/posts/syllabus/ioai-study-map/)

---
# Overview

* Vision Transformers (ViT) treat an image as a **sequence of patch tokens**.
* Self-attention models **global context** from the start.
* Strong performance with large-scale pretraining.

---
# Core Idea

## Patchify
* Split the image into fixed-size patches.
* Flatten each patch and project to an embedding.

If the image is $H \times W$ and patch size is $P \times P$:
$$
N = \frac{H W}{P^2}
$$
* **$N$**: number of patch tokens.
* **$P$**: patch size.
* Each patch has raw dimension $P^2 C$ (with $C$ input channels).
* Linear projection maps each patch to model dimension $D$.

$$
x_p \in \mathbb{R}^{N \times (P^2 C)}, \quad z_0 = x_p E \in \mathbb{R}^{N \times D}
$$
* **$E$** is the learnable patch embedding matrix.

## Tokens + Position
* Add a learnable **[CLS]** token for classification.
* Add positional embeddings so order is known.
* Final encoder input is:

$$
z_0 = [x_{\text{cls}}; x_p E] + E_{\text{pos}}
$$
* **$x_{\text{cls}}$** is the class token and **$E_{\text{pos}}$** is learnable positional embedding.

## Transformer Encoder
* Stack multi-head self-attention + MLP blocks.
* Output at [CLS] token is used for classification.
* Layer structure (pre-norm style):

$$
z_l' = z_{l-1} + \text{MSA}(\text{LN}(z_{l-1}))
$$

$$
z_l = z_l' + \text{MLP}(\text{LN}(z_l'))
$$

* Classification head:

$$
\hat{y} = \text{softmax}(W z_L^{\text{cls}})
$$

## Attention Computation
* Queries, keys, values are linear projections of tokens.
* Attention weights are scaled dot products.

$$
\text{Attention}(Q,K,V)=\text{softmax}\!\left(\frac{QK^\top}{\sqrt{d_k}}\right)V
$$

* Full self-attention cost grows quadratically with token count:

$$
\mathcal{O}(N^2 D)
$$
* Smaller patch size increases $N$, which increases compute and memory.

---
# Why It Works

* **Global receptive field** from the first layer.
* Scales well with data and compute.
* Pretrained ViTs transfer well to detection and segmentation.
* Patch tokens learn semantically rich features when pretrained at scale (for example, ImageNet-21k / JFT-style corpora).

---
# Key Variants

* **ViT**: baseline patch + global attention.
* **DeiT**: strong augmentation + distillation token to train with less data.
* **Swin Transformer**: shifted local windows for near-linear scaling with image size.
* **Hybrid ViT**: CNN stem before transformer to improve local inductive bias.

---
# When To Use

* **Large datasets**: ViTs shine with lots of pretraining data.
* **Transfer learning**: strong backbone for downstream tasks.
* **Hybrid setups**: CNN stem + transformer for efficiency.
* **High-resolution tasks**: use hierarchical/windowed variants (for example, Swin) to reduce quadratic attention cost.

---
# Practical Notes

## Patch size trades off detail vs compute:

* Patch size trades off detail vs compute:
## Smaller $P$ gives finer detail but larger $N$ and higher memory.

* Smaller $P$ gives finer detail but larger $N$ and higher memory.
## Typical settings: $P=16$ for classification baselines, smaller patches for dense tasks.

* Typical settings: $P=16$ for classification baselines, smaller patches for dense tasks.
## Training recipe matters for data-limited settings:

* Training recipe matters for data-limited settings:
## Use RandAugment/Mixup/CutMix, label smoothing, stochastic depth, and AdamW.

* Use RandAugment/Mixup/CutMix, label smoothing, stochastic depth, and AdamW.
## Positional embedding interpolation is needed when fine-tuning at different image resolutions.

* Positional embedding interpolation is needed when fine-tuning at different image resolutions.
## For dense prediction (segmentation/detection), attach FPN/UPerNet-style heads instead of only using [CLS].

* For dense prediction (segmentation/detection), attach FPN/UPerNet-style heads instead of only using [CLS].

## Typical Model Scales

* Typical Model Scales
## **ViT-Tiny/Small**: faster experimentation, lower memory.

* **ViT-Tiny/Small**: faster experimentation, lower memory.
## **ViT-Base**: common transfer-learning default.

* **ViT-Base**: common transfer-learning default.
## **ViT-Large/Huge**: best quality with large-scale pretraining and strong compute budget.

* **ViT-Large/Huge**: best quality with large-scale pretraining and strong compute budget.


