---
title: Projections and Orthogonality
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

* Orthogonal vectors have zero dot product.
* Projection decomposes a vector into explained and residual components.

## Key Formula

Projection of $x$ onto $u$:
$$
\mathrm{proj}_u(x)=\frac{x^\top u}{u^\top u}u
$$

## Practical Notes

### Residuals are orthogonal to fitted subspace in least squares.

* This gives geometric intuition for regression fit quality.

### Orthonormal bases simplify computations.

* Dot products and decompositions become more stable.

## Why This Matters for ML

* Core to regression geometry, PCA intuition, and subspace methods.