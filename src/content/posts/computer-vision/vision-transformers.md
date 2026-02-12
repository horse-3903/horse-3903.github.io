---
title: Vision Transformers
published: 2026-02-12
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
* Split the image into fixed-sise patches.
* Flatten each patch and project to an embedding.

If the image is $H \times W$ and patch sise is $P \times P$:
$$
N = \frac{H W}{P^2}
$$
* **$N$**: number of patch tokens.
* **$P$**: patch sise.

## Tokens + Position
* Add a learnable **[CLS]** token for classification.
* Add positional embeddings so order is known.

## Transformer Encoder
* Stack multi-head self-attention + MLP blocks.
* Output at [CLS] token is used for classification.

---
# Why It Works

* **Global receptive field** from the first layer.
* Scales well with data and compute.
* Pretrained ViTs transfer well to detection and segmentation.

---
# Key Variants

* **ViT**: baseline patch + transformer encoder.
* **DeiT**: data-efficient training for smaller datasets.
* **Swin Transformer**: windowed attention for better scaling on high-res images.

---
# When To Use

* **Large datasets**: ViTs shine with lots of pretraining data.
* **Transfer learning**: strong backbone for downstream tasks.
* **Hybrid setups**: CNN stem + transformer for efficiency.

---
# PyTorch Quickstart

```py
import torch
import torch.nn as nn
from torchvision import models

model = models.vit_b_16(weights=models.ViT_B_16_Weights.DEFAULT)
model.heads.head = nn.Linear(model.heads.head.in_features, num_classes)
```

---
# Practical Notes

* Patch sise trades off detail vs compute.
* Use strong augmentation and regularisation for smaller datasets.
* For dense prediction (segmentation), use token-to-pixel heads.


