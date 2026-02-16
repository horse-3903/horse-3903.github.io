---
title: Covariance and Quadratic Forms
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

* Covariance captures joint variation between features.
* Quadratic forms encode curvature and energy-like measures.

# Key Formulas

## Covariance Matrix
$$
\Sigma = \frac{1}{m}X^\top X
$$

* Here, $X \in \mathbb{R}^{m \times d}$ (rows are samples, columns are features).
* This form assumes $X$ is already **mean-centered** feature-wise.
* If data is not centered, use $X_c = X - \mathbf{1}\mu^\top$ and compute:
$$
\Sigma = \frac{1}{m}X_c^\top X_c
$$
* Diagonal entries of $\Sigma$ are feature variances
* Off-diagonal entries are pairwise covariances.

## Quadratic Form
$$
q(x)=x^\top A x
$$

* This is a **quadratic form**: it maps vector $x$ to a scalar using matrix $A$.
* It measures magnitude/curvature of $x$ under the geometry induced by $A$.
* If $A$ is positive definite, then $q(x) > 0$ for all $x \ne 0$, which corresponds to convex bowl-shaped geometry.

## Practical Notes

### Standardise features before covariance analysis.

* Otherwise large-scale features dominate covariance structure.

### Positive-definite matrices yield strictly convex quadratic forms.

* This improves optimisation behaviour.

## Why This Matters for ML

* Covariance defines principal directions and explained variance in PCA.
* Mahalanobis distance uses inverse covariance to handle correlated, differently scaled features.
* Quadratic forms appear in curvature approximations and second-order optimisation reasoning.
* L2 regularisation is a quadratic penalty that improves conditioning and generalisation behaviour.
