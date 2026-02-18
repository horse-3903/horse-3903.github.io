---
title: Data Processing
published: 2026-02-19
description: "Handling missing values, scaling, and augmentation in leakage-safe ML pipelines."
tags: ["Classical Machine Learning", "Data Science", "Data Processing"]
category: IOAI ML Notes
draft: false
access: public
---
# Syllabus Map

* Study map: [Syllabus Study Map](/posts/syllabus/ioai-study-map/)

---
# Overview

* Data processing prepares raw inputs into model-ready form.
* Correct processing improves stability, convergence, and fairness of evaluation.
* All transforms should be fit on training data only.

---

# Missing Values

## Imputation

* Use mean/median/mode or model-based imputers depending on data type.
* Compare strategies with validation rather than assuming one is best.
* Fit imputers only on training partitions.

## Missingness Indicators

* Add binary flags showing whether a value was missing.
* Can help when missingness itself carries signal.

---

# Scaling and Normalization

## Standardization

* Transform to zero mean and unit variance.
* Useful for distance-based and gradient-based models.

## Min-Max Normalization

* Scales values into a fixed range, often $[0,1]$.
* Can be sensitive to outliers and distribution shift.

## Leakage Rule

* Fit scaler parameters on training data only.
* Reuse fitted parameters for validation/test and production inference.

---

# Data Augmentation

## Vision and Tabular

* Common transforms: flip, crop, jitter, noise injection.
* Improve robustness when applied with realistic perturbations.

## NLP

* Typical methods include back-translation and synonym substitution.
* Use cautiously to avoid semantic drift and label corruption.

---

# Practical Notes

## Build a reproducible preprocessing pipeline

* Use a single pipeline object for fit/transform consistency.
* Version preprocessing with model artifacts.

## Validate preprocessing impact

* Measure whether each transform improves validation quality.
* Remove steps that add complexity without measurable gain.

## Align offline and online data paths

* Feature definitions must match between training and serving.
* Mismatched preprocessing is a common production failure mode.

