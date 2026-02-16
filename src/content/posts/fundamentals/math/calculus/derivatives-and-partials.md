---
title: Derivatives and Partial Derivatives
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

* Derivative measures rate of change.
* Partial derivative changes one variable at a time in multivariate functions.

## Key Formulas

$$
\frac{d}{dx}x^n = nx^{n-1}
$$

$$
\frac{\partial f}{\partial x_i}
$$

## Practical Notes

### Derivative sign indicates direction of change.

* Positive increases, negative decreases locally.

### Magnitude indicates sensitivity.

* Larger absolute values mean stronger local effect.

## Why This Matters for ML

* Parameter updates depend on partial derivatives of loss with respect to each weight.
* Sensitivity analysis of features and parameters uses derivative magnitude and sign.
* Regularizers and constraints are optimized through derivative-based updates.
* Understanding local rate of change is necessary for debugging training dynamics.