---
title: Linear Systems and Rank
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

* A linear system is written as $Ax=b$.
* Rank tells how many independent constraints/features exist.

## Key Facts

* Unique solution: full rank square system.
* Infinite solutions: at least one free variable.
* No solution: inconsistent equations.

$$
\text{rank}(A)=\text{number of pivots in REF/RREF}
$$

## Practical Notes

### Rank deficiency implies redundant information.

* Correlated features can reduce effective dimensionality.

### REF/RREF provide structural diagnostics.

* Use pivots to identify dependencies and solvability.

## Why This Matters for ML

* Least-squares fitting and many closed-form estimators reduce to solving linear systems.
* Rank reveals multicollinearity and redundant features, which affect model identifiability.
* Underdetermined systems motivate regularisation and minimum-norm solutions.
* Pivot structure from REF/RREF gives a practical diagnostic for solvability and feature dependence.