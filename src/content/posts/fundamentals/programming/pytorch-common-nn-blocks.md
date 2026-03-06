---
title: Common PyTorch nn Blocks
published: 2026-03-01
description: "Common PyTorch nn building blocks: linear layers, activations, convolutions, pooling, normalisation, dropout, embeddings, and recurrent layers."
tags: ["Programming Fundamentals"]
category: IOAI ML Notes
draft: false
access: public
---
# Syllabus Map

* Study map: [Syllabus Study Map](/posts/syllabus/ioai-study-map/)
* Programming hub: [Programming Fundamentals](/posts/fundamentals/programming/)

---

# Common PyTorch `nn` Blocks

```py
import torch
import torch.nn as nn
```

* Most layers below assume the first dimension is the batch dimension.

## Linear layers and activations
```py
mlp = nn.Sequential(
    nn.Linear(128, 64),
    nn.ReLU(),
    nn.Linear(64, 32),
    nn.GELU(),
    nn.Linear(32, 10)
)

x = torch.randn(32, 128)
logits = mlp(x)  # (32, 10)
```

## Convolution and pooling
```py
cnn = nn.Sequential(
    nn.Conv2d(3, 16, kernel_size=3, padding=1),
    nn.ReLU(),
    nn.MaxPool2d(kernel_size=2),
    nn.Conv2d(16, 32, kernel_size=3, padding=1),
    nn.ReLU(),
    nn.AdaptiveAvgPool2d((1, 1)),
    nn.Flatten(),
    nn.Linear(32, 10)
)

images = torch.randn(8, 3, 64, 64)
logits = cnn(images)  # (8, 10)
```

## Normalisation and dropout
```py
block = nn.Sequential(
    nn.Linear(256, 128),
    nn.BatchNorm1d(128),
    nn.ReLU(),
    nn.Dropout(p=0.2),
    nn.LayerNorm(128)
)

x = torch.randn(16, 256)
y = block(x)  # (16, 128)
```

## Embeddings
```py
embed = nn.Embedding(num_embeddings=5000, embedding_dim=128)

tokens = torch.tensor([
    [1, 4, 9, 2],
    [3, 8, 0, 0]
])

x = embed(tokens)  # (2, 4, 128)
```

## Recurrent blocks
```py
lstm = nn.LSTM(input_size=128, hidden_size=256, num_layers=2, batch_first=True)
gru = nn.GRU(input_size=128, hidden_size=256, batch_first=True)

seq = torch.randn(16, 20, 128)

lstm_out, (h_n, c_n) = lstm(seq)
gru_out, h_n = gru(seq)

lstm_out.shape  # (16, 20, 256)
h_n.shape       # (1, 16, 256) for the GRU above
```

## Useful utility blocks
```py
head = nn.Sequential(
    nn.Flatten(),
    nn.Linear(28 * 28, 128),
    nn.ReLU(),
    nn.Dropout(0.1),
    nn.Linear(128, 10)
)

classifier = nn.Identity()  # placeholder block that returns inputs unchanged
```

## Common output layers
```py
binary_head = nn.Sequential(
    nn.Linear(64, 1),
    nn.Sigmoid()
)

multiclass_head = nn.Linear(64, 5)  # raw logits
```

* For multi-class classification, pass raw logits directly into `nn.CrossEntropyLoss()`.
