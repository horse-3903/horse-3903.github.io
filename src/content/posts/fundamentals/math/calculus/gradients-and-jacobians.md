---
title: Gradients and Jacobians
published: 2026-02-16
description: "Math fundamentals note for IOAI ML preparation."
tags: ["Mathematics Fundamentals", "Calculus"]
category: IOAI ML Notes
draft: false
access: public
---
# Syllabus Map

* Study map: [Syllabus Study Map](/posts/syllabus/ioai-study-map/)

---

# Core Idea

* Gradient is the vector of partial derivatives for scalar output.
* Jacobian generalizes derivatives to vector outputs.

## Key Formulas

$$
\nabla f(x)=\left[\frac{\partial f}{\partial x_1},\ldots,\frac{\partial f}{\partial x_n}\right]^\top
$$

$$
J_{ij}=\frac{\partial f_i}{\partial x_j}
$$

## Practical Notes

### Negative gradient gives steepest local decrease.

* This is the basis of gradient descent updates.

### Jacobians are useful for sensitivity and transformations.

* Especially relevant in sequence and manifold models.

## Why This Matters for ML

* Gradient vectors determine direction and strength of optimization updates.
* Jacobians describe how representations change under transformations, useful in sensitivity checks.
* Many modern objectives (contrastive, sequence, diffusion components) rely on multivariate gradients.
* Understanding gradient geometry helps with clipping, normalization, and optimization stability.