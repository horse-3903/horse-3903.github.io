---
title: Learning Rate and Convergence
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

* Convergence depends on step size, curvature, and gradient noise.

## Practical Notes

### Use schedules when training plateaus.

* Decay or cosine schedules improve late-stage convergence.

### Monitor both loss and validation metrics.

* Convergence in training loss does not guarantee generalization.

## Why This Matters for ML

* Learning rate is one of the highest-impact hyperparameters in training.
* Convergence diagnostics (oscillation, divergence, stagnation) guide schedule decisions.
* Warmup/decay policies often determine whether large models train stably.
* Generalization quality can depend strongly on the optimization path set by step-size policy.