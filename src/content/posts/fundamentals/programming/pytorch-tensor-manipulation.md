---
title: PyTorch Tensor Manipulation
published: 2026-02-16
description: "Common tensor shape, indexing, broadcasting, and device/type operations in PyTorch."
tags: ["Programming Fundamentals"]
category: IOAI ML Notes
draft: false
access: public
---
# Syllabus Map

* Study map: [Syllabus Study Map](/posts/syllabus/ioai-study-map/)
* Programming hub: [Programming Fundamentals](/posts/fundamentals/programming/)

---

# Tensor Manipulation

```py
import torch
```

```py
# Reshape / view
X = torch.randn(8, 4)
X.view(4, 8)
X.reshape(2, 16)

# Transpose and permute
X.T
X.permute(1, 0)

# Concatenate / stack
torch.cat([X, X], dim=0)
torch.stack([X, X], dim=0)

# Slicing
X[:2]
X[:, 1:3]

# Broadcasting
X + 3
X + torch.randn(1, 4)

# Type and device
X.float()
X.long()
X.to("cpu")
```
