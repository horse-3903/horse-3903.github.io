---
title: Taylor Approximation
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

* Taylor expansion approximates functions locally using derivatives.

## Key Formula

First-order approximation near $x_0$:
$$
f(x) \approx f(x_0) + \nabla f(x_0)^\top (x-x_0)
$$

## Practical Notes

### Optimization steps are locally valid, not globally.

* A good local approximation can still fail far from the expansion point.

### Second-order terms capture curvature.

* Useful for understanding Newton-style methods.

## Why This Matters for ML

* Provides intuition for gradient methods and curvature-aware optimization.