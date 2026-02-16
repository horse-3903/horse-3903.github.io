---
title: Training Models on CPU and GPU
published: 2026-02-16
description: "Practical PyTorch workflow for device selection, training loops, and checkpointing."
tags: ["Programming Fundamentals"]
category: IOAI ML Notes
draft: false
access: public
---
# Syllabus Map

* Study map: [Syllabus Study Map](/posts/syllabus/ioai-study-map/)
* Programming hub: [Programming Fundamentals](/posts/fundamentals/programming/)

---

# Training Models on CPU and GPU

```py
import torch
```

* Assumes `model`, `criterion`, `optimizer`, and data loaders are already defined.

## Device selection
```py
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)
```

## Training loop
```py
for epoch in range(10):
    model.train()
    for X_batch, y_batch in train_loader:
        X_batch = X_batch.to(device)
        y_batch = y_batch.to(device)

        optimizer.zero_grad()
        logits = model(X_batch)
        loss = criterion(logits, y_batch)
        loss.backward()
        optimizer.step()

    model.eval()
    with torch.no_grad():
        for X_batch, y_batch in val_loader:
            X_batch = X_batch.to(device)
            y_batch = y_batch.to(device)
            logits = model(X_batch)
```

## Saving and loading
```py
torch.save(model.state_dict(), "model.pt")
model.load_state_dict(torch.load("model.pt", map_location=device))
model.eval()
```
