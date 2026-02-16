---
title: Random Variables, Expectation, and Variance
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

* Random variables map outcomes to values.
* Expectation is the average outcome; variance measures spread.

## Key Formulas

$$
\mathbb{E}[X]=\sum_x xP(X=x)\;\text{or}\;\int xp(x)dx
$$

$$
\mathrm{Var}(X)=\mathbb{E}[(X-\mathbb{E}[X])^2]
$$

## Why This Matters for ML

* Loss minimization is usually expectation minimization under unknown data distributions.
* Variance quantifies uncertainty and instability in model predictions and estimates.
* Evaluation metrics across folds/runs are interpreted through expectation/variance behavior.
* These concepts underpin risk, uncertainty, and robust model comparison.