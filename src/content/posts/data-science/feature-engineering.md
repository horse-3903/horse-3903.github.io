---
title: Feature Engineering
published: 2026-02-19
description: "Practical feature encoding and feature construction for robust classical ML pipelines."
tags: ["Classical Machine Learning", "Data Science", "Feature Engineering"]
category: IOAI ML Notes
draft: false
access: public
---
# Syllabus Map

* Study map: [Syllabus Study Map](/posts/syllabus/ioai-study-map/)

---
# Overview

* Feature engineering transforms raw data into useful model inputs.
* Strong features often improve performance more than small model changes.
* All feature logic must be leakage-safe with respect to data splits.

---

# Categorical Encoding

## One-Hot Encoding

* Expands each category into a binary indicator vector.
* Works well for low-cardinality unordered categories.
* Can create very high-dimensional sparse inputs.

## Target / Frequency Encoding

* Replaces categories with target statistics or frequency counts.
* Useful for high-cardinality categorical features.
* Must be computed inside folds to avoid target leakage.

## Ordinal Encoding

* Maps ordered categories to integer levels.
* Preserves known rank relationships.
* Avoid for unordered categories.

---

# Statistical Features

## Summary Statistics

* Build mean, variance, quantiles over entities or windows.
* Useful for user/item/session-level signals.
* Keep aggregation windows consistent with training-time availability.

## Rolling Window Features

* Compute moving-window statistics over time.
* Captures local trends and short-term dynamics.
* Must avoid using future timestamps.

## Lag Features

* Include past values such as $x_{t-1}, x_{t-2}, \dots$.
* Helps with autoregressive structure.
* Select lag depth based on domain periodicity and sampling cadence.

## Seasonality Indicators

* Encode hour/day/week/month effects.
* Sine-cosine transforms can represent cyclic continuity.
* Helps separate periodic effects from trend.

---

# Embeddings

## Learned Embeddings

* Dense vectors learned during model training.
* Capture semantic similarity in a compact representation.
* Common for large sparse categorical spaces and text.

## Pretrained Embeddings

* Start from transferred representations from large corpora.
* Often reduce labeled-data requirements.
* Fine-tuning aligns embeddings to target task.

---

# Practical Notes

## Start simple, then increase complexity

* Baseline one-hot and simple aggregates before advanced encoders.
* Complex features are harder to debug and maintain.

## Track feature provenance

* Document exact source, transformation, and time availability.
* This helps prevent leakage and production mismatches.

## Recompute features exactly in production

* Training and serving logic must match.
* Inconsistent pipelines are a common source of performance drops.

