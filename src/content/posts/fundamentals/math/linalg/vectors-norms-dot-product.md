---
title: Vectors, Norms, and Dot Product
published: 2026-02-16
description: "Math fundamentals note for IOAI ML preparation."
tags: ["Mathematics Fundamentals", "Linear Algebra"]
category: IOAI ML Notes
draft: false
access: public
---
# Syllabus Map

* Study map: [Syllabus Study Map](/posts/syllabus/ioai-study-map/)

---

# Core Idea

* Vectors represent points, directions, and parameter sets.
* Norms measure vector magnitude.
* Dot product measures alignment and similarity.

## Key Formulas

$$
\|x\|_1 = \sum_i |x_i|, \quad \|x\|_2 = \sqrt{\sum_i x_i^2}
$$

$$
x^\top y = \sum_i x_i y_i
$$

$$
\cos(\theta) = \frac{x^\top y}{\|x\|_2\|y\|_2}
$$

## Practical Notes

### Feature scaling affects all norm-based comparisons.

* Unscaled features distort distance and similarity calculations.

### L1 and L2 norms serve different modeling goals.

* L1 encourages sparsity; L2 gives smooth shrinkage.

## Why This Matters for ML

* Core to KNN distance, cosine similarity, regularisation, margin methods, and embedding search.