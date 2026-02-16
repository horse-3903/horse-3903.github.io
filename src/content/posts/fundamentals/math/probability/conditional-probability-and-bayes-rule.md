---
title: Conditional Probability and Bayes Rule
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

* Conditional probability updates beliefs given evidence.

## Key Formula

$$
P(A\mid B)=\frac{P(B\mid A)P(A)}{P(B)}
$$

## Practical Notes

### Priors matter when data is limited.

* Posterior estimates can be prior-dominated in low-data settings.

## Why This Matters for ML

* Classification and inference often require conditioning on observed evidence.
* Bayes reasoning appears in posterior prediction and probabilistic model updates.
* It clarifies prior-vs-data influence, especially in small-data settings.
* Many decision rules can be interpreted as choosing outcomes with highest posterior probability.