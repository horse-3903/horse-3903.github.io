---
title: Determinant and Invertibility
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

* Determinant describes signed area/volume scaling of a linear map.
* Invertibility means a unique reverse mapping exists.

## Key Formulas

For $2\times2$ matrix:
$$
A=\begin{bmatrix}a & b\\ c & d\end{bmatrix},\quad \det(A)=ad-bc
$$

$$
A^{-1}A = I, \quad \det(A)\ne 0 \Leftrightarrow A \text{ invertible}
$$

## Practical Notes

### Determinant near zero implies numerical instability.

* Systems become ill-conditioned even before exact singularity.

### Avoid explicit inverse when solving systems.

* Prefer stable solvers (`solve`, factorization methods).

## Why This Matters for ML

* Appears in linear regression stability, Gaussian models, and optimization conditioning.