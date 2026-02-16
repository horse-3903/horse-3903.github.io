---
title: Matrix Fundamentals
published: 2026-02-16
description: "A practical guide to matrix basics for machine learning: shapes, multiplication, geometry, determinants, rank, and invertibility."
tags: ["Mathematics Fundamentals"]
category: IOAI ML Notes
draft: false
access: public
---
# Syllabus Map

* Study map: [Syllabus Study Map](/posts/syllabus/ioai-study-map/)

---


# What Is a Matrix?

* A matrix is a rectangular array of numbers.
* Shape is written as $m \times n$ (rows by columns).
* A vector is a special case:
  * Column vector: $n \times 1$
  * Row vector: $1 \times n$

---

# Matrix Operations

## Addition and Scalar Multiplication

* You can add matrices only if shapes match.
* Scalar multiplication scales every entry:
$$
\alpha A = [\alpha a_{ij}]
$$

## Matrix Multiplication

* If $A \in \mathbb{R}^{m \times n}$ and $B \in \mathbb{R}^{n \times p}$, then:
$$
AB \in \mathbb{R}^{m \times p}
$$
* Entry form:
$$
(AB)_{ij} = \sum_{k=1}^{n} A_{ik}B_{kj}
$$
* Matrix multiplication is generally not commutative:
$$
AB \ne BA
$$

## Transpose

* Transpose flips rows and columns:
$$
A^\top_{ij} = A_{ji}
$$
* Useful identities:
$$
(AB)^\top = B^\top A^\top
$$

---

# Geometry of Matrices

## Matrix as a Linear Transformation

* A matrix $A$ maps vectors: $x \mapsto Ax$.
* Geometrically, this can rotate, scale, shear, reflect, or project space.

## Column-Space View

* $Ax$ is a linear combination of columns of $A$.
* The set of all outputs is the column space of $A$.

## Dot Product and Orthogonality

* Dot product:
$$
x^\top y = \sum_i x_i y_i
$$
* Orthogonal vectors satisfy $x^\top y = 0$.

---

# Determinant

## Meaning

* For square $A \in \mathbb{R}^{n \times n}$, $\det(A)$ measures signed volume scaling.
* In 2D, absolute determinant is area scale factor.
* In 3D, absolute determinant is volume scale factor.

## Key Facts

* $\det(A)=0$ means dimensions collapse (matrix is singular).
* $\det(AB)=\det(A)\det(B)$
* $\det(A^\top)=\det(A)$

For a $2 \times 2$ matrix:
$$
A=\begin{bmatrix}a & b \\ c & d\end{bmatrix},\quad \det(A)=ad-bc
$$

---

# Invertibility

## Inverse Matrix

* $A^{-1}$ satisfies:
$$
A^{-1}A = AA^{-1} = I
$$
* Only square matrices can be invertible.

## Equivalent Conditions

For square $A$, these are equivalent:

* $A$ is invertible
* $\det(A)\ne 0$
* $\text{rank}(A)=n$
* Columns of $A$ are linearly independent
* $Ax=b$ has a unique solution for every $b$

---

# Rank and Linear Independence

* Rank = number of linearly independent columns (or rows).
* Full column rank means no redundant features among columns.
* In ML, low-rank structure is common and exploited by PCA, SVD, and embeddings.

---

# Systems of Linear Equations

* A linear system can be written as:
$$
Ax=b
$$
* Cases:
  * Unique solution: full rank square system
  * Infinite solutions: underdetermined / dependent equations
  * No solution: inconsistent system

---

# Matrices in Machine Learning

* Dataset: $X \in \mathbb{R}^{m \times d}$ (samples by features)
* Linear model:
$$
\hat y = Xw + b
$$
* Normal equation (least squares):
$$
w = (X^\top X)^{-1}X^\top y
$$
* Covariance matrix:
$$
\Sigma = \frac{1}{m}X^\top X
$$

---

# Practical Notes

## Check shapes before multiplying.

* Most bugs in linear algebra code are shape mismatches.

## Avoid explicit matrix inverse when solving systems.

* Prefer linear solvers (`solve`) for numerical stability and speed.

## Standardise features for distance-based and regularised methods.

* Unscaled features can dominate matrix operations and degrade conditioning.

