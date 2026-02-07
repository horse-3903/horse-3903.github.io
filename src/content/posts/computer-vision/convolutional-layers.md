---
title: Convolutional Layers
published: 2026-02-01
description: "Convolution basics and pretrained vision encoders."
tags: ["Computer Vision", "Deep Learning"]
category: Notes
draft: false
---

# Syllabus Map

* Study map: [Syllabus Study Map](/posts/syllabus/ioai-study-map/)

---
# Overview

* Convolutions extract local spatial patterns.
* Stacking layers builds hierarchical visual features.
* Residual connections help train deeper CNNs by improving gradient flow.

---

# Convolution Basics

## Core Idea

![Kernel sliding over an image](../assets/convolution/2d-convolution.gif)

* Apply a learnable filter across the image.
* Capture edges, textures, and shapes.
* Weight sharing reduces parameters and improves translation robustness.

## Key Concepts

* Kernels and stride.
* Padding and output size.
* Channels and feature maps.

### Intuition: kernels, channels, and size
* A **kernel** is a small window that slides over the image to detect a pattern.
* **Kernel size** controls the receptive field: larger kernels see more context but add parameters.
* **Stride** controls how far the kernel moves each step: larger stride means more downsampling.
* **Padding** preserves spatial size and keeps edge information.
* **Channels** let the model learn multiple filters in parallel:
  * Input channels match the input (e.g., 3 for RGB).
  * Output channels represent different learned features (edges, textures, parts).
* Each output channel is a **feature map** showing where that pattern appears.

### Output size formula
* For input size $ H \times W $:
$$
H_{out} = \left\lfloor \frac{H + 2P - K}{S} \right\rfloor + 1
$$
$$
W_{out} = \left\lfloor \frac{W + 2P - K}{S} \right\rfloor + 1
$$
* **$H, W$**: input height and width.
* **$K$**: kernel size (assume square kernel for simplicity).
* **$P$**: padding size on each side.
* **$S$**: stride.
* **$H_{out}, W_{out}$**: output height and width.

### Convolution operation
* For input $ x $ and kernel $ w $:
$$
y_{i,j} = \sum_{u,v} w_{u,v}\,x_{i+u,\;j+v}
$$
* **$y_{i,j}$**: output value at spatial location $(i,j)$.
* **$w_{u,v}$**: kernel weight at offset $(u,v)$.
* **$x_{i+u, j+v}$**: input value under the kernel at position $(i,j)$.
* The sum is over the kernel window offsets $u,v$.

---

# Residual Connections

## Core idea
* Residual blocks add the input back to the output:
$$
y = F(x) + x
$$
* This helps gradients flow and enables **very deep** networks.

## Practical notes
* Used heavily in **ResNet** family models.
* Improves training stability without adding many parameters.

---

# Pre-trained Vision Encoders

## Examples

* ResNet.
* Other CNN backbones (VGG, EfficientNet).

## Practical Notes

* Use for transfer learning.
* Freeze early layers when data is limited.

---

# Implementation (PyTorch)

## Core building blocks
```py
import torch
import torch.nn as nn

conv = nn.Conv2d(in_channels=3, out_channels=32, kernel_size=3, stride=1, padding=1)
bn = nn.BatchNorm2d(32)
relu = nn.ReLU()
pool = nn.MaxPool2d(kernel_size=2, stride=2)
```

## A simple CNN block
```py
class ConvBlock(nn.Module):
    def __init__(self, in_ch, out_ch):
        super().__init__()
        self.net = nn.Sequential(
            nn.Conv2d(in_ch, out_ch, 3, padding=1),
            nn.BatchNorm2d(out_ch),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )

    def forward(self, x):
        return self.net(x)
```

## Residual block (basic)
```py
class ResidualBlock(nn.Module):
    def __init__(self, channels):
        super().__init__()
        self.conv1 = nn.Conv2d(channels, channels, 3, padding=1)
        self.bn1 = nn.BatchNorm2d(channels)
        self.conv2 = nn.Conv2d(channels, channels, 3, padding=1)
        self.bn2 = nn.BatchNorm2d(channels)
        self.relu = nn.ReLU()

    def forward(self, x):
        out = self.relu(self.bn1(self.conv1(x)))
        out = self.bn2(self.conv2(out))
        return self.relu(out + x)
```

---

# Dataset processing (PyTorch)

## Basic image dataset
```py
from torchvision import datasets, transforms

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225])
])

train_ds = datasets.ImageFolder("data/train", transform=transform)
val_ds = datasets.ImageFolder("data/val", transform=transform)
```

## DataLoader
```py
from torch.utils.data import DataLoader

train_loader = DataLoader(train_ds, batch_size=32, shuffle=True, num_workers=2)
val_loader = DataLoader(val_ds, batch_size=32, shuffle=False, num_workers=2)
```


