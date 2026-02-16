---
title: Eigenvalues and Eigenvectors
published: 2026-02-16
description: "A practical guide to eigenvalues and eigenvectors: intuition, computation, diagonalisation, and why they matter in ML."
tags: ["Mathematics Fundamentals"]
category: IOAI ML Notes
draft: false
access: public
---
# Syllabus Map

* Study map: [Syllabus Study Map](/posts/syllabus/ioai-study-map/)

---


# Core Definition

For square matrix $A$, an eigenvector $v \ne 0$ and eigenvalue $\lambda$ satisfy:
$$
Av = \lambda v
$$

* $A$ acts on $v$ by scaling (and possibly sign flip), not changing its direction.

---

# How to Compute Eigenvalues

## Step 1: Characteristic Equation

Solve:
$$
\det(A-\lambda I)=0
$$
This polynomial is the characteristic polynomial.

## Step 2: Find Eigenvectors

For each eigenvalue $\lambda$, solve:
$$
(A-\lambda I)v=0
$$
to get non-zero vectors in that null space.

---

# 2x2 Example

Let
$$
A=\begin{bmatrix}2 & 1\\1 & 2\end{bmatrix}
$$

Characteristic equation:
$$
\det\!\left(\begin{bmatrix}2-\lambda & 1\\1 & 2-\lambda\end{bmatrix}\right)
=(2-\lambda)^2-1=0
$$

So eigenvalues are $\lambda_1=3$, $\lambda_2=1$.

Corresponding eigenvectors (up to scaling):

* For $\lambda=3$: $v_1=\begin{bmatrix}1\\1\end{bmatrix}$
* For $\lambda=1$: $v_2=\begin{bmatrix}1\\-1\end{bmatrix}$

---

# Geometric Intuition

* Most vectors are rotated/sheared/scaled by $A$.
* Eigenvectors are special directions that remain on the same line.
* Eigenvalues tell how much stretching/compression occurs along those directions.

---

# Diagonalisation

If $A$ has enough independent eigenvectors, then:
$$
A=PDP^{-1}
$$
where:

* Columns of $P$ are eigenvectors
* $D$ is diagonal with eigenvalues

Then powers are easy:
$$
A^k = PD^kP^{-1}
$$

---

# Symmetric Matrices (Very Important)

If $A=A^\top$:

* All eigenvalues are real
* Eigenvectors for distinct eigenvalues are orthogonal
* Decomposition becomes:
$$
A = Q\Lambda Q^\top
$$
with orthonormal $Q$.

This is the basis of PCA and many optimisation results.

---

# Connection to SVD

For any matrix $X$:
$$
X = U\Sigma V^\top
$$

* Columns of $V$ are eigenvectors of $X^\top X$
* Columns of $U$ are eigenvectors of $XX^\top$
* Singular values satisfy:
$$
\sigma_i^2 = \lambda_i(X^\top X)
$$

---

# Why This Matters in ML

## PCA

* PCA finds principal directions as eigenvectors of covariance matrix.
* Largest eigenvalues correspond to directions of highest variance.

## Dynamical Systems / Iterative Methods

* Eigenvalues control growth/decay rates and convergence behavior.

## Graph Methods

* Spectral clustering uses eigenvectors of graph Laplacians.

---

# Practical Notes

## Normalise eigenvectors when comparing directions.

* Scaling does not change eigenvector direction, so unit vectors are easier to interpret.

## Use symmetric solvers when matrices are symmetric.

* They are more stable and efficient than generic eigensolvers.

## Watch conditioning when eigenvalues are very close.

* Near-degenerate eigenvalues can make eigenvectors numerically unstable.

