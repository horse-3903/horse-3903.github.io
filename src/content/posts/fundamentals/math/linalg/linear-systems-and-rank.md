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

* Essential for least-squares solutions, feature redundancy analysis, and stability checks.