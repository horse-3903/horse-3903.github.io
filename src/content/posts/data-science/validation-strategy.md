---
title: Validation Strategy
published: 2026-02-19
description: "Train/validation/test protocols and cross-validation strategy for reliable model assessment."
tags: ["Classical Machine Learning", "Data Science", "Model Evaluation"]
category: IOAI ML Notes
draft: false
access: public
---
# Syllabus Map

* Study map: [Syllabus Study Map](/posts/syllabus/ioai-study-map/)

---
# Overview

* Validation strategy determines how reliably model performance is estimated.
* Poor split design can create leakage and optimistic scores.
* A good protocol matches the data-generating process and deployment setting.

---

# Train / Validation / Test Split

## Core Rules

* Keep train, validation, and test roles separate.
* Use validation data for model and hyperparameter decisions.
* Reserve the test set for one final unbiased report.

## Time-Aware Data

* For time series, split by time, not random shuffle.
* Ensure training data is strictly earlier than validation/test data.
* This avoids future-to-past leakage.

---

# Cross-Validation

## Why Use It

* Gives a more stable estimate than one single split.
* Useful when dataset size is limited.
* Helps compare models under lower split variance.

## Variants

* K-fold for general tabular settings.
* Stratified k-fold for imbalanced classification.
* Group k-fold when related samples must stay together.
* Time-series split for temporal datasets.

## Detailed Guide

* Full walkthrough: [Cross Validation and K-Fold Cross Validation](/posts/data-science/cross-validation-k-fold/)

---

# Practical Notes

## Prevent leakage in preprocessing

* Fit imputation, scaling, and encoding using training partition only.
* Apply fitted transforms to validation/test without refitting.
* Use pipelines to enforce this consistently.

## Use nested CV when tuning heavily

* Inner loop tunes hyperparameters.
* Outer loop estimates performance of the full tuning procedure.
* Reduces optimistic bias compared with non-nested evaluation.

## Keep protocol fixed during comparisons

* Changing splits across experiments makes comparisons noisy.
* Fix random seeds and split logic before model benchmarking.

