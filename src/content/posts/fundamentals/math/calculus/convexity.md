---
title: Convexity
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

* Convex objectives have no spurious local minima.

## Key Condition

$$
f(\theta x + (1-\theta)y) \le \theta f(x)+(1-\theta)f(y),\;\theta\in[0,1]
$$

## Practical Notes

### Convex models are easier to optimize reliably.

* Logistic regression has convex loss; deep nets generally do not.

### Regularization can improve effective optimization landscape.

* Often helps numerical stability and generalization.

## Why This Matters for ML

* Explains when optimization guarantees are available.