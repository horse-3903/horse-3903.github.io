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

* SVD powers low-rank compression, denoising, and latent-structure extraction.
* PCA is a standard preprocessing step for high-dimensional tabular and vision features.
* Principal components can reduce overfitting and improve downstream training efficiency.
* Spectral views connect directly to embedding quality and variance-preserving representations.