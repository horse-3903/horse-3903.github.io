---
title: Principal Component Analysis (PCA)
published: 2026-02-01
description: "A comprehensive guide to PCA — reducing dimensionality by projecting data onto directions of maximum variance."
tags: ["Classical Machine Learning", "Unsupervised Learning"]
category: Notes
draft: false
---


# Syllabus Map

* Study map: [Syllabus Study Map](/posts/syllabus/ioai-study-map/)

---
# Overview

* Principal Component Analysis (PCA) is an unsupervised, linear dimensionality reduction technique.

* It finds new axes (principal components) that capture the maximum variance in the data while remaining orthogonal.

---

# Why Dimensionality Reduction Matters

* High-dimensional spaces make distance metrics less meaningful and models harder to generalise.

* Many features are redundant or noisy, so compressing them can improve efficiency without losing much signal.

---

# Mathematical Formulation

* Start with a data matrix $X \in \mathbb{R}^{m \times n}$ where rows are samples and columns are features.

* Mean-center each feature:
  $$
  X_c = X - \mu
  $$
  where $\mu$ is the feature-wise mean vector.

* Compute the covariance matrix:
  $$
  \Sigma = \frac{1}{m} X_c^\top X_c
  $$

---

# Eigen Decomposition

* Solve the eigenvalue problem:
  $$
  \Sigma v_i = \lambda_i v_i
  $$

* Each eigenvector $v_i$ is a principal component direction.

* Each eigenvalue $\lambda_i$ is the variance captured along that direction.

---

# Principal Components

* Sort eigenvalues in descending order: $\lambda_1 \ge \lambda_2 \ge \dots \ge \lambda_n$.

* The top $k$ eigenvectors form the projection matrix:
  $$
  W_k = [v_1, v_2, \dots, v_k]
  $$

---

# Projection to Lower Dimensions

* Project the centered data into the new feature space:
  $$
  Z = X_c W_k
  $$

* $Z \in \mathbb{R}^{m \times k}$ is the reduced representation.

---

# Explained Variance

* The explained variance ratio for component $i$ is:
  $$
  r_i = \frac{\lambda_i}{\sum_{j=1}^{n} \lambda_j}
  $$

* Cumulative variance for the top $k$ components:
  $$
  R_k = \sum_{i=1}^{k} r_i
  $$

---

# Choosing the Number of Components

* Pick the smallest $k$ such that $R_k$ exceeds a target threshold (e.g. 0.90 or 0.95).

* Alternatively, use the elbow method on the scree plot of eigenvalues.

---

# Reconstruction and Error

* Approximate reconstruction back to the original space:
  $$
  \hat{X} = Z W_k^\top + \mu
  $$

* Reconstruction error decreases as $k$ increases, but so does compression.

---

# PCA via SVD (Practical Computation)

* Instead of eigendecomposition, compute:
  $$
  X_c = U S V^\top
  $$

* The principal components are the columns of $V$, and variances are proportional to $S^2$.

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


