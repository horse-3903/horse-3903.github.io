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

* Cross-entropy is the default objective for modern classification.
* KL divergence measures distribution mismatch in variational, distillation, and representation settings.
* Entropy regularization appears in uncertainty-aware and exploration-driven methods.
* These information measures connect probabilistic predictions to optimization objectives.