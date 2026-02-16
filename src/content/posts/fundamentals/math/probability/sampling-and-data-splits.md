---
title: Sampling and Data Splits
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

* Evaluation requires representative sampling and strict holdout discipline.

## Practical Notes

### Keep test data untouched until final evaluation.

* Using test feedback during tuning causes leakage.

### Stratify when class imbalance is present.

* Preserves class proportions across splits.

## Why This Matters for ML

* Reliable generalization estimates require clean train/validation/test separation.
* Sampling strategy affects class balance, metric stability, and fairness of comparisons.
* Leakage from improper splits can invalidate reported performance.
* Cross-validation and stratification decisions are rooted in these fundamentals.