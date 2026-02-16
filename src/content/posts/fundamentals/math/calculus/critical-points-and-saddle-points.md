---
title: Critical Points and Saddle Points
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

* Critical points satisfy $\nabla f(x)=0$.
* They can be minima, maxima, or saddle points.

## Practical Notes

### Saddle points are common in high dimensions.

* Training can stall even without being at a useful minimum.

### Curvature diagnostics help interpretation.

* Hessian sign patterns indicate local geometry.

## Why This Matters for ML

* Training may stall at flat regions or saddle points even when not near good minima.
* Zero gradient alone is not enough to conclude optimization success.
* Curvature interpretation helps explain why momentum/adaptive methods can escape plateaus.
* This is central to understanding deep-network loss landscapes.