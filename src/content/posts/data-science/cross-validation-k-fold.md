---
title: Cross Validation and K-Fold Cross Validation
published: 2026-02-19
description: "How cross validation estimates generalization performance, with focus on k-fold cross validation."
tags: ["Classical Machine Learning", "Model Evaluation"]
category: IOAI ML Notes
draft: false
access: public
---
# Syllabus Map

* Study map: [Syllabus Study Map](/posts/syllabus/ioai-study-map/)

---
# Overview

* Cross validation is a resampling strategy used to estimate how well a model generalizes to unseen data.
* It repeatedly trains and evaluates on different train/validation splits.
* This gives a more stable estimate than relying on one single split.

---

# What Is Cross Validation

## Core Idea

* Split available data into two parts many times:
* one part to train,
* one part to validate.
* Average validation performance across runs to estimate expected out-of-sample performance.

## Why It Matters

* Reduces sensitivity to one lucky or unlucky split.
* Uses limited data more efficiently than a single holdout.
* Supports fairer model and hyperparameter comparison.

---

# K-Fold Cross Validation

## Definition

* Partition dataset into $k$ disjoint folds of similar size.
* For fold $j \in \{1,\dots,k\}$:
* use fold $j$ as validation,
* use remaining $k-1$ folds for training.
* Compute score $s_j$ for each fold, then aggregate:

$$
\bar{s}=\frac{1}{k}\sum_{j=1}^{k}s_j
$$

* A common variability summary is:

$$
\sigma_s=\sqrt{\frac{1}{k}\sum_{j=1}^{k}(s_j-\bar{s})^2}
$$

## Typical Choices

* $k=5$ or $k=10$ are common in practice.
* Larger $k$ gives more training data per fold, but higher compute cost.
* Smaller $k$ is faster but may give higher variance estimates.

---

# Common Variants

## Stratified K-Fold

* Preserves class proportions in each fold.
* Recommended for imbalanced classification.

## Group K-Fold

* Keeps all samples from the same group in the same fold.
* Useful when samples are correlated (for example: user ID, patient ID, document source).

## Time-Series Split

* Respects temporal order by training on past and validating on future.
* Avoids leakage from future information.

---

# Step-by-Step Workflow

## Step 1: Set evaluation protocol

* Choose metric and CV variant (standard, stratified, group, or time-aware).
* Fix random seed and preprocessing rules.

## Step 2: Run cross validation

* For each split: fit preprocessing and model on training fold only.
* Evaluate on validation fold and record metrics.

## Step 3: Aggregate and inspect stability

* Report mean and spread across folds.
* Investigate large fold-to-fold variation.

## Step 4: Final training

* After selecting model/hyperparameters, retrain on full training data.
* Keep a separate untouched test set for final reporting.

---

# Practical Notes

## Avoid data leakage

* Fit scalers, imputers, feature selectors, and target encoders inside each training fold only.
* Leakage during preprocessing can inflate validation scores.
* Pipelines help enforce correct fold-local fitting.

## Use nested CV for unbiased model selection estimates

* Inner loop tunes hyperparameters.
* Outer loop estimates generalization of the tuned process.
* This is slower but less optimistic than tuning and reporting on the same folds.

## Keep a final test set

* Cross validation is for model selection and estimation.
* Final test performance should be measured once at the end.
* Repeatedly checking test results turns test data into validation data.

