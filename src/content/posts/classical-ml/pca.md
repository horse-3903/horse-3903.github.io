---
title: Principal Component Analysis (PCA)
published: 2026-02-07
description: "A comprehensive guide to PCA — reducing dimensionality by projecting data onto directions of maximum variance."
tags: ["Classical Machine Learning", "Unsupervised Learning"]
category: IOAI ML Notes
draft: false
---


# Syllabus Map

* Study map: [Syllabus Study Map](/posts/syllabus/ioai-study-map/)

---
# Overview

* **Principal Component Analysis (PCA)** is an **unsupervised, linear dimensionality reduction** technique.

* It finds new axes (**principal components**) that capture the **maximum variance** in the data while remaining **orthogonal**.

* PCA **rotates the coordinate system** to align with directions where the data varies the most.

* The **first component captures the largest spread**; each subsequent component captures the next-largest spread while staying orthogonal to previous components.

* Keeping only the first few components **preserves most structure** while discarding noise and redundancy.

---

# Why Dimensionality Reduction Matters

* **High-dimensional spaces** make distance metrics less meaningful and models harder to generalise.

* Many features are **redundant or noisy**, so compressing them can **improve efficiency** without losing much signal.

---

# Mathematical Formulation

* Start with a **data matrix** $X \in \mathbb{R}^{m \times n}$ where rows are samples and columns are features.

* **Mean-centre** each feature:
  $$
  X_c = X - \mu
  $$
  where $\mu$ is the feature-wise mean vector.

* **Mean-centring** means subtracting each feature's average from every sample, so **every column has mean 0**.

* Compute the **covariance matrix**:
  $$
  \Sigma = \frac{1}{m} X_c^\top X_c
  $$

* The covariance matrix $\Sigma \in \mathbb{R}^{n \times n}$ contains **pairwise covariances** between features: 
  * **Diagonal entries** are variances (how spread out that feature is around its mean)
  * **Off-diagonals** measure how features vary together (how one feature varies with the variation of another)

---

# Eigen Decomposition

* Solve the **eigenvalue problem**:
  $$
  \Sigma v_i = \lambda_i v_i
  $$

* Each **eigenvector** $v_i$ is a principal component direction.

* Each **eigenvalue** $\lambda_i$ is the variance captured along that direction.

## How Eigenvalues Are Found

* Solve the **characteristic equation**:
  $$
  \det(\Sigma - \lambda I) = 0
  $$

* This yields a polynomial in $\lambda$ whose **roots are the eigenvalues**.

* In practice, **numerical algorithms** (e.g., QR or SVD) are used because direct polynomial solving is unstable for large matrices.

## Intuitive Explanation

* A matrix can be seen as a transformation that **stretches, squashes, or rotates** space.

* Most directions get rotated, but an **eigenvector** is a special direction that does **not** rotate — it only scales.

* The amount of scaling is the **eigenvalue**.

## Why Eigenvectors Matter in PCA

* The **covariance matrix** encodes how the data varies in every direction.

* Its **eigenvectors** are the **orthogonal directions** where this variation acts like pure scaling.

* The **largest eigenvalue** gives the direction of **maximum variance** (the first principal component), the next largest gives the second, and so on.

* This is why PCA uses eigenvectors: they provide **independent axes** that explain the data’s spread without mixing directions.

---

# Principal Components

* **Sort eigenvalues in descending order**: $\lambda_1 \ge \lambda_2 \ge \dots \ge \lambda_n$.

* The top $k$ eigenvectors form the **projection matrix**:
  $$
  W_k = [v_1, v_2, \dots, v_k]
  $$

* Sorting by descending eigenvalues ensures the **first component captures the most variance**, the second captures the next most, and so on.

* These components are **not original features**

* They are **new directions** (linear combinations of features) that maximize variance along each direction.

---

# Projection to Lower Dimensions

* **Project** the centred data into the new feature space:
  $$
  Z = X_c W_k
  $$

* $Z \in \mathbb{R}^{m \times k}$ is the **reduced representation**.

---

# Explained Variance

* The **explained variance ratio** for component $i$ is:
  $$
  r_i = \frac{\lambda_i}{\sum_{j=1}^{n} \lambda_j}
  $$

* **Cumulative variance** for the top $k$ components:
  $$
  R_k = \sum_{i=1}^{k} r_i
  $$

---

# Choosing the Number of Components

* Pick the **smallest $k$** such that $R_k$ exceeds a target threshold (e.g. 0.90 or 0.95).

* Alternatively, use the **elbow method** on the scree plot of eigenvalues.

---

# Reconstruction and Error

* **Approximate reconstruction** back to the original space:
  $$
  \hat{X} = Z W_k^\top + \mu
  $$

* **Reconstruction error decreases** as $k$ increases, but so does compression.

* The **error comes from discarding components**: lower-variance directions still contain information that is lost when projecting to $k$ dimensions.

* **Mean-centring does not create this error**; it only shifts data to zero mean so variance is measured consistently.

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

* **Fit PCA on the training set only**, then transform validation and test sets.
* **Standardise features** before computing components.
* Choose component count via **explained variance** or cross-validation.
* Inspect **loadings** to understand what each component captures.




