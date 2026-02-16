---
title: PyTorch Basics
published: 2026-02-16
description: "Core PyTorch concepts: tensors, autograd, modules, loss functions, and optimisers."
tags: ["Programming Fundamentals"]
category: IOAI ML Notes
draft: false
access: public
---
# Syllabus Map

* Study map: [Syllabus Study Map](/posts/syllabus/ioai-study-map/)
* Programming hub: [Programming Fundamentals](/posts/fundamentals/programming/)

---

# PyTorch Basics

```py
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
```

## Tensors
```py
# Create tensors
x = torch.tensor([1.0, 2.0, 3.0])
X = torch.randn(3, 4)
Z = torch.zeros(2, 2)

# Attributes
X.shape
X.ndim
X.dtype
X.device
```

## Autograd
```py
x = torch.tensor([2.0, 3.0], requires_grad=True)
y = (x ** 2).sum()
y.backward()
x.grad
```

## Modules
```py
class MLP(nn.Module):
    def __init__(self, in_dim, hidden_dim, out_dim):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(in_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, out_dim)
        )

    def forward(self, x):
        return self.net(x)
```

## Loss and Optimiser
```py
model = MLP(10, 32, 2)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=1e-3)
```

