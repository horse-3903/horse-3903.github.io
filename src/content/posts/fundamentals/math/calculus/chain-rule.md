---
title: Chain Rule
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

* Derivative of composed functions multiplies local derivatives.

## Key Formula

$$
\frac{d}{dx}f(g(x)) = f'(g(x))g'(x)
$$

## Practical Notes

### Cache intermediate activations in deep models.

* Backprop uses repeated chain-rule application through layers.

### Local gradients can vanish or explode.

* Product of many derivatives can become unstable.

## Why This Matters for ML

* Backpropagation is the chain rule applied over computation graphs.