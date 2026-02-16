---
title: Pooling, Batch Norm, and Layer Norm
published: 2026-02-16
description: "Pooling plus batch and layer normalisation fundamentals."
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

* This note covers **pooling**, **batch normalisation**, and **layer normalisation**.
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
H_{out} = \left\lfloour \frac{H + 2P - K}{S} \right\rfloour + 1,\quad
W_{out} = \left\lfloour \frac{W + 2P - K}{S} \right\rfloour + 1
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
* Pooling can **hurt localisation** tasks (detection/segmentation) due to spatial loss.
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
* **Small batch sises** can make BN unstable.
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

---

# Layer Normalisation

## Core idea
* Layer norm normalises activations **within each sample** across its feature dimensions.
* It does not depend on batch statistics, so it behaves the same in train and eval.

## How it works
* For a sample with $d$ features:
  * Mean: $ \mu = \frac{1}{d}\sum_{j=1}^d x_j $
  * Variance: $ \sigma^2 = \frac{1}{d}\sum_{j=1}^d (x_j - \mu)^2 $
  * Normalise: $ \hat{x}_j = \frac{x_j - \mu}{\sqrt{\sigma^2 + \epsilon}} $
  * Scale/shift: $ y_j = \gamma \hat{x}_j + \beta $
* Stats are computed **per sample**, not across the batch.

## Practical notes
* **Batch-size agnostic**: stable even with very small batches.
* Common in **RNNs** and **Transformers**, where batch stats can be noisy.
* No running averages are needed; train and eval behave identically.
* Placement:
  * Classic: `Linear → LayerNorm → ReLU` or `Linear → LayerNorm`.
  * Transformers: often use **pre-norm** (`LayerNorm → sublayer`) for stability.

## PyTorch examples
```py
import torch.nn as nn

ln = nn.LayerNorm(normalized_shape=512)

block = nn.Sequential(
    nn.Linear(512, 512, bias=False),
    nn.LayerNorm(512),
    nn.ReLU(inplace=True)
)
```

---

# Layer Norm vs Batch Norm

## Key differences
* **Statistics source**:
  * BatchNorm uses batch-level statistics (across samples).
  * LayerNorm uses per-sample statistics (across features).
* **Train vs eval behavior**:
  * BatchNorm behaves differently in train/eval because of running statistics.
  * LayerNorm behaves the same in train/eval.
* **Batch-size sensitivity**:
  * BatchNorm can degrade with very small batches.
  * LayerNorm is batch-size agnostic.
* **Typical use cases**:
  * BatchNorm: CNNs with reasonably large batches.
  * LayerNorm: Transformers/RNNs or small-batch regimes.

## Rule of thumb
* Use **BatchNorm** for vision models with stable batch statistics.
* Use **LayerNorm** when batch statistics are unreliable or sequence modeling dominates.
