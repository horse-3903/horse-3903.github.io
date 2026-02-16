---
title: SVD and PCA Intuition
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

* SVD factorizes any matrix into orthogonal directions and singular values.
* PCA uses top-variance directions for dimensionality reduction.

## Key Formulas

$$
X = U\Sigma V^\top
$$

$$
\sigma_i^2 = \lambda_i(X^\top X)
$$

## Practical Notes

### Keep components by explained variance.

* Avoid over-compression that removes predictive information.

### PCA assumes linear structure.

* Nonlinear manifolds may need methods like UMAP/t-SNE.

## Why This Matters for ML

* Core for denoising, compression, visualization baselines, and feature preprocessing.