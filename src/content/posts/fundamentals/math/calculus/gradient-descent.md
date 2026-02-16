---
title: Gradient Descent
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

* Iterative method that updates parameters in the negative gradient direction.

## Update Rule

$$
\theta_{t+1}=\theta_t-\eta\nabla_\theta L(\theta_t)
$$

## Practical Notes

### Learning rate controls stability-speed tradeoff.

* Too large diverges; too small is slow.

### Mini-batch noise can aid exploration.

* Moderate stochasticity can escape poor regions.

## Why This Matters for ML

* Central optimizer for classical and deep learning models.