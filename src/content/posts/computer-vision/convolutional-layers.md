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

### Kernels
![](../assets/convolution/kernel-size.gif)
* A kernel is a small window of learnable weights.
* It slides across the input to detect local patterns.
* Kernel size controls how much context the filter sees.

### Stride
![](../assets/convolution/stride.gif)
* Controls how far the kernel moves each step.
* Larger stride reduces spatial resolution.

### Padding
![](../assets/convolution/padding.gif)
* Adds border pixels to preserve spatial size.
* Helps retain edge information.

### Output size
![](../assets/convolution/output-size.gif)
* Depends on input size, kernel size, stride, and padding.
* Use the formula below to compute $H_{out}$ and $W_{out}$.

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

### Channels and feature maps
![](../assets/convolution/channels.svg)
* Input channels match the input (e.g., 3 for RGB).
* Output channels are different learned filters.
* Each output channel is a feature map highlighting a pattern.

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
![](../assets/convolution/residual-block.svg)
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

## Overview
* Pre-trained vision encoders turn images into **feature vectors** or **feature maps**.
* They provide strong starting weights so you can **fine-tune** with less data and time.
* Typical workflow: load a backbone, replace the classifier head, then train.

## ResNet

* **What makes it unique**: residual skip connections stabilise very deep CNNs.
* **When to use**: a reliable default for classification, detection, and segmentation.
* **PyTorch access**:
```py
from torchvision import models

model = models.resnet50(weights=models.ResNet50_Weights.DEFAULT)
model.fc = nn.Linear(model.fc.in_features, num_classes)
```

## VGG

* **What makes it unique**: simple stacks of $3 \times 3$ convolutions and large fully-connected heads.
* **When to use**: baseline or feature extraction when model simplicity matters.
* **PyTorch access**:
```py
from torchvision import models

model = models.vgg16(weights=models.VGG16_Weights.DEFAULT)
model.classifier[-1] = nn.Linear(model.classifier[-1].in_features, num_classes)
```

## MobileNet
* **What makes it unique**: **depthwise separable convolutions** to cut compute.
* **Compute comparison**:
$$
\\text{standard: } K^2 M N H W
\\qquad
\\text{depthwise + pointwise: } K^2 M H W + M N H W
$$
* **When to use**: mobile and edge devices where latency and size matter.
* **PyTorch access**:
```py
from torchvision import models

model = models.mobilenet_v3_small(weights=models.MobileNet_V3_Small_Weights.DEFAULT)
model.classifier[-1] = nn.Linear(model.classifier[-1].in_features, num_classes)
```

## EfficientNet

* **What makes it unique**: compound scaling of depth, width, and resolution.
* **When to use**: strong accuracy-per-parameter and accuracy-per-FLOP trade-offs.
* **PyTorch access**:
```py
from torchvision import models

model = models.efficientnet_b0(weights=models.EfficientNet_B0_Weights.DEFAULT)
model.classifier[-1] = nn.Linear(model.classifier[-1].in_features, num_classes)
```
### Illustration of EfficientNet performance
![](../assets/convolution/efficientnet-model-size.png)

## ConvNeXt
* **What makes it unique**: modernised ConvNet blocks with **large kernel depthwise conv**, **LayerNorm**, and **GELU**.
* **When to use**: strong ConvNet baselines that compete with transformers.
* **PyTorch access**:
```py
from torchvision import models

model = models.convnext_tiny(weights=models.ConvNeXt_Tiny_Weights.DEFAULT)
model.classifier[-1] = nn.Linear(model.classifier[-1].in_features, num_classes)
```

## Vision Transformer (ViT)
* **What makes it unique**: splits images into **patch tokens** and applies transformer attention.
* **Patch count**:
$$
N = \\frac{H W}{P^2}
$$
* **When to use**: large datasets or strong pretraining where attention can shine.
* **PyTorch access**:
```py
from torchvision import models

model = models.vit_b_16(weights=models.ViT_B_16_Weights.DEFAULT)
model.heads.head = nn.Linear(model.heads.head.in_features, num_classes)
```

## DenseNet

* **What makes it unique**: dense skip connections reuse features across layers.
* **When to use**: parameter-efficient models with strong feature reuse.
* **PyTorch access**:
```py
from torchvision import models

model = models.densenet121(weights=models.DenseNet121_Weights.DEFAULT)
model.classifier = nn.Linear(model.classifier.in_features, num_classes)
```

## Practical Notes

* Use for transfer learning.
* Freeze early layers when data is limited.

---

# PyTorch Implementation

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
