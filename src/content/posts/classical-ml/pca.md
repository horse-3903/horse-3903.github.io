---
title: Principal Component Analysis
published: 2026-01-21
description: "A comprehensive guide to principal component analysis — exploring how dimension reducibility allows for feature enginneering."
tags: ["Machine Learning", "Unsupervised Learning"]
category: Notes
draft: false
--- 

---
title: Principal Component Analysis (PCA)
published: 2026-01-21
description: "A concise guide to principal component analysis — understanding dimensionality reduction through variance maximisation and orthogonal projections."
tags: ["Machine Learning", "Unsupervised Learning"]
category: Notes
draft: false
---  

# The Problem of Dimensionality

## Curse of Dimensionality

## Redundancy in Features

## Noise Accumulation

---

# Motivation for Dimensionality Reduction

## Why Fewer Dimensions Help

## Information vs Compression

---

# What Is PCA?

## Core Idea

## Unsupervised Nature

## Linear Transformation

---

# Intuition Behind PCA

## Directions of Maximum Variance

## Orthogonal Axes

## Rotating the Coordinate System

---

# Geometric Interpretation

## Projection onto a Subspace

## Best Low-Dimensional Approximation

---

# Mathematical Formulation

## Mean Centering

## Covariance Matrix

## Why Covariance Matters

---

# Eigen Decomposition

## Eigenvectors as Directions

## Eigenvalues as Variance

## Ranking Principal Components

---

# Principal Components

## Definition

## Orthogonality

## Ordering by Importance

---

# Explained Variance

## Variance Ratio

## Cumulative Explained Variance

---

# Choosing the Number of Components

## Variance Threshold

## Elbow Method

---

# Dimensionality Reduction via PCA

## Projection

## New Feature Space

---

# Reconstruction and Information Loss

## Approximate Reconstruction

## Reconstruction Error

---

# Principal Component Analysis (PCA) In Practice

## When to Use PCA

* When you need to compress correlated features into fewer dimensions.
* When you want faster downstream training with minimal accuracy loss.
* When noise is roughly isotropic and variance captures signal.
* When visualising high-dimensional data in 2D or 3D.

## When Not to Use PCA

* When interpretability of original features is required.
* When the target signal is not aligned with top variance directions.
* When data lies on a nonlinear manifold.
* When feature scales cannot be standardised.

## Practical Notes

* Fit PCA on the training set only, then transform validation and test sets.
* Standardise features before computing components.
* Choose component count via explained variance or cross-validation.
* Inspect loadings to understand what each component captures.
