---
title: Data Science Fundamentals
published: 2026-02-19
description: "Overview of reliable evaluation, validation, feature workflows, and data processing."
tags: ["Classical Machine Learning", "Data Science"]
category: IOAI ML Notes
draft: false
access: public
---
# Syllabus Map

* Study map: [Syllabus Study Map](/posts/syllabus/ioai-study-map/)

---
# Overview

* Data science fundamentals cover evaluation, validation, feature workflows, and clean data pipelines.
* Good practice separates data understanding, modelling, and monitoring into repeatable steps.
* Common failure modes come from leakage, biased data collection, or misaligned metrics.

---

# Core Areas

## Evaluation Metrics

* Choose metrics that match the business and error-cost objective.
* Use both aggregate metrics and diagnostic views (for example confusion matrix).
* Detailed note: [Evaluation Metrics](/posts/classical-ml/data-science/evaluation-metrics/)

## Validation Strategy

* Keep train/validation/test logic strict to avoid leakage.
* Use cross-validation when data is limited or split variance is high.
* Detailed note: [Validation Strategy](/posts/classical-ml/data-science/validation-strategy/)

## Feature Engineering

* Encode categorical variables safely and select features that reflect signal.
* Build statistical and temporal features carefully to avoid leakage.
* Detailed note: [Feature Engineering](/posts/classical-ml/data-science/feature-engineering/)

## Data Processing

* Handle missing values, scaling, and augmentation with training-only fitting.
* Pipeline discipline is key for reproducibility and honest validation.
* Detailed note: [Data Processing](/posts/classical-ml/data-science/data-processing/)

---

# Related Notes

* [Cross Validation and K-Fold Cross Validation](/posts/classical-ml/data-science/cross-validation-k-fold/)
* [Bias-Variance Tradeoff](/posts/classical-ml/bias-variance/)

