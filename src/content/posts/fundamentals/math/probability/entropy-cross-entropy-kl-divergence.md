---
title: Entropy, Cross-Entropy, and KL Divergence
published: 2026-02-16
description: "Math fundamentals note for IOAI ML preparation."
tags: ["Mathematics Fundamentals", "Probability"]
category: IOAI ML Notes
draft: false
access: public
---
# Syllabus Map

* Study map: [Syllabus Study Map](/posts/syllabus/ioai-study-map/)

---

# Core Idea

* Entropy measures uncertainty in a distribution.
* Cross-entropy evaluates predictive coding loss.
* KL divergence measures mismatch between distributions.

## Key Formulas

$$
H(P)=-\sum_x P(x)\log P(x)
$$

$$
D_{KL}(P\|Q)=\sum_x P(x)\log\frac{P(x)}{Q(x)}
$$

## Why This Matters for ML

* Core to classification loss functions, variational objectives, and distribution matching.