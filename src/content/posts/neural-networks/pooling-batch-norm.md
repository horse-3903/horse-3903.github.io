---
title: Pooling and Batch Normalisation
published: 2026-02-07
description: "Pooling layers and batch normalisation fundamentals."
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

* This note covers **pooling** and **batch normalisation**.
* These techniques improve **stability**, **generalisation**, and **training speed** in deep networks.

---

# Pooling

## Core idea
* Pooling downsamples spatial dimensions to reduce compute and increase receptive field.
* It introduces **local translation tolerance** but **loses spatial precision**.

## Common types
* **Max pooling**: keeps the largest activation in a window.
* **Average pooling**: averages activations in a window.
* **Global pooling**: reduces each feature map to a single value.

## How it works (2D)
* Input feature map: $H \times W$, window $K \times K$, stride $S$, padding $P$.
* Output size:
$$
H_{out} = \left\lfloor \frac{H + 2P - K}{S} \right\rfloor + 1,\quad
W_{out} = \left\lfloor \frac{W + 2P - K}{S} \right\rfloor + 1
$$
* For a window $W$ of activations:
  * Max pooling: $ y = \max_{x \in W} x $
  * Average pooling: $ y = \frac{1}{|W|}\sum_{x \in W} x $

## Gradient flow
* **Max pooling**: gradient flows only to the argmax element in each window.
* **Average pooling**: gradient is evenly distributed across all elements in the window.

## Design knobs
* **Window size**: larger windows discard more spatial detail.
* **Stride**: larger stride downsamples faster.
* **Padding**: used to preserve size when needed ("same" style pooling).

## Practical notes
* Pooling can **hurt localization** tasks (detection/segmentation) due to spatial loss.
* Many modern CNNs replace pooling with **strided convolutions** for learnable downsampling.
* **Global average pooling** is a strong default before a classifier head.
* For small objects, avoid aggressive early pooling.

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
* Batch norm normalises activations **per feature/channel** using batch statistics.
* It stabilises training, enables higher learning rates, and adds mild regularisation.

## How it works
* For a batch $B$ with $m$ examples:
  * Mean: $ \mu_B = \frac{1}{m}\sum_{i=1}^m x_i $
  * Variance: $ \sigma_B^2 = \frac{1}{m}\sum_{i=1}^m (x_i - \mu_B)^2 $
  * Normalise: $ \hat{x}_i = \frac{x_i - \mu_B}{\sqrt{\sigma_B^2 + \epsilon}} $
  * Scale/shift: $ y_i = \gamma \hat{x}_i + \beta $
* **Conv layers**: stats are computed per channel over **N, H, W**.
* **Affine params**: $\gamma$ and $\beta$ are learned per channel/feature.
* **Running stats**: moving averages of mean/variance are stored for inference.

## Practical notes
* **Train vs eval**:
  * `model.train()` uses batch stats and updates running averages.
  * `model.eval()` uses running averages only.
* **Small batch sizes** can make BN unstable.
  * Options: **SyncBatchNorm**, **GroupNorm**, or **LayerNorm**.
* **Placement**:
  * Common: `Conv → BatchNorm → ReLU`.
  * Avoid bias in conv layers when followed by BN (BN has $\beta$).
* **Momentum** controls how fast running stats update (PyTorch default is `0.1`).
* **Inference**: mismatched train/eval modes cause large accuracy drops.

## PyTorch examples
```py
import torch.nn as nn

bn1 = nn.BatchNorm1d(num_features=128)
bn2 = nn.BatchNorm2d(num_features=64)
bn3 = nn.BatchNorm3d(num_features=32)

# Typical conv block
block = nn.Sequential(
    nn.Conv2d(64, 64, kernel_size=3, padding=1, bias=False),
    nn.BatchNorm2d(64),
    nn.ReLU(inplace=True)
)
```


