---
title: Pooling and Batch Normalisation
published: 2026-02-07
description: "Pooling layers and batch normalisation fundamentals."
tags: ["Neural Network", "Deep Learning"]
category: Notes
draft: false
pinned: false
---

# Syllabus Map

* Study map: [Syllabus Study Map](/posts/syllabus/ioai-study-map/)

---

# Overview

* This note covers **pooling** and **batch normalisation**.
* These techniques improve **stability**, **generalisation**, and **training speed** in deep networks.

---

# Pooling

## Core idea
* Pooling reduces spatial resolution while keeping salient information.
* It makes models **translation‑tolerant** and lowers computation.

## Common types
* **Max pooling**: keeps the largest activation in a window.
* **Average pooling**: averages activations in a window.
* **Global pooling**: reduces each feature map to a single value.

## How it works
* For a window $ W $ of activations:
  * Max pooling: $ y = \max_{x \in W} x $
  * Average pooling: $ y = \frac{1}{|W|}\sum_{x \in W} x $
* Stride controls downsampling:
  * Larger stride reduces resolution faster
  * Smaller stride retains more information 

## Practical notes
* Use pooling sparingly in modern CNNs; strided convolutions often suffice.
* Global average pooling can replace fully connected heads.

## PyTorch examples
```py
import torch.nn as nn

max_pool = nn.MaxPool2d(kernel_size=2, stride=2)
avg_pool = nn.AvgPool2d(kernel_size=2, stride=2)
global_avg = nn.AdaptiveAvgPool2d((1, 1))
```

---

# Batch Normalisation

## Core idea
* Batch norm normalises activations to stabilise training.
* It reduces internal covariate shift and allows higher learning rates.

## How it works
* For a batch $ B $:
  * Mean: $ \mu_B = \frac{1}{m}\sum_{i=1}^m x_i $
  * Variance: $ \sigma_B^2 = \frac{1}{m}\sum_{i=1}^m (x_i - \mu_B)^2 $
  * Normalise: $ \hat{x}_i = \frac{x_i - \mu_B}{\sqrt{\sigma_B^2 + \epsilon}} $
  * Scale/shift: $ y_i = \gamma \hat{x}_i + \beta $

## Practical notes
* Use **train** mode for batch statistics; **eval** mode uses running averages.
* Batch size affects stability; very small batches can be noisy.
* For transformers, consider **LayerNorm** instead of BatchNorm.

## PyTorch examples
```py
import torch.nn as nn

bn1 = nn.BatchNorm1d(num_features=128)
bn2 = nn.BatchNorm2d(num_features=64)
```
