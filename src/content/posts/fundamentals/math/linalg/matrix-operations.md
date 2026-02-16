---
title: Matrix Operations
published: 2026-02-16
description: "Math fundamentals note for IOAI ML preparation."
tags: ["Mathematics Fundamentals", "Linear Algebra"]
category: IOAI ML Notes
draft: false
access: public
---
# Syllabus Map

* Study map: [Syllabus Study Map](/posts/syllabus/ioai-study-map/)

---

# Core Idea

* Matrices represent linear maps and batched data.
* Core operations are addition, multiplication, and transpose.

## Key Formulas

If $A\in\mathbb{R}^{m\times n}$ and $B\in\mathbb{R}^{n\times p}$, then:
$$
AB\in\mathbb{R}^{m\times p},\quad (AB)_{ij}=\sum_{k=1}^n A_{ik}B_{kj}
$$

$$
(AB)^\top = B^\top A^\top
$$

## Practical Notes

### Check matrix shapes before multiplication.

* Shape mismatch is the most common implementation bug.

### Matrix multiplication is not commutative.

* Usually $AB \ne BA$.

## Why This Matters for ML

* Every linear layer in neural networks is matrix multiplication plus bias.
* Batched prediction, feature transforms, and covariance calculations all rely on matrix operations.
* Understanding shape rules prevents common implementation and debugging errors in ML code.
* Efficient tensor/matrix operations are central to training speed on GPU hardware.