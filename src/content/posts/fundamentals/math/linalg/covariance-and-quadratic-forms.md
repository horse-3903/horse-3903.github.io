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

## Key Formulas

$$
\Sigma = \frac{1}{m}X^\top X
$$

$$
q(x)=x^\top A x
$$

## Practical Notes

### Standardize features before covariance analysis.

* Otherwise large-scale features dominate covariance structure.

### Positive-definite matrices yield strictly convex quadratic forms.

* This improves optimization behavior.

## Why This Matters for ML

* Used in PCA, Gaussian models, Mahalanobis distance, and second-order optimization.