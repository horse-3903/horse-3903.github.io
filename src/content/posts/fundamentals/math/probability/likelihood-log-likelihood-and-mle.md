---
title: Likelihood, Log-Likelihood, and MLE
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

* Likelihood treats parameters as unknowns and observed data as fixed.
* MLE picks parameters that maximize observed-data likelihood.

## Key Formula

$$
\hat\theta=\arg\max_\theta \prod_{i=1}^n p(x_i\mid\theta)
$$

Usually optimize:
$$
\hat\theta=\arg\max_\theta \sum_{i=1}^n \log p(x_i\mid\theta)
$$

## Why This Matters for ML

* MLE is the statistical foundation of many classical ML estimators.
* Log-likelihood turns products into sums, enabling stable optimization and gradient methods.
* Logistic regression and many generative models are trained by maximizing likelihood objectives.
* Understanding likelihood is key for comparing models and defining principled losses.