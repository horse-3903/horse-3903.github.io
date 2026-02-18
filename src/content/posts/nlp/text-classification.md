---
title: Text Classification
published: 2026-02-19
description: "Common workflows for assigning labels to text."
tags: ["Natural Language Processing", "Supervised Learning"]
category: IOAI ML Notes
draft: false
access: restricted
---
# Syllabus Map

* Study map: [Syllabus Study Map](/posts/syllabus/ioai-study-map/)

---
# Overview

* Text classification assigns labels to documents or sentences.
* Typical tasks: sentiment analysis, topic labeling, spam/toxicity detection, intent classification.
* Labels can be single-label, multi-class, or multi-label.

---

# Typical Pipeline

## Representation

* Bag-of-words or TF-IDF.
* Embeddings or transformer encoders.

## Classifier

* Logistic regression or linear SVM.
* Fine-tuned transformer.

## Objective

* Single-label multi-class usually uses cross-entropy:

$$
\mathcal{L}_{\text{CE}}=-\sum_{i=1}^{N}\sum_{c=1}^{C} y_{i,c}\log \hat{p}_{i,c}
$$

* Multi-label usually uses binary cross-entropy per class.

---

# Step-by-Step Workflow

## Step 1: Define label space

* Ensure class definitions are mutually exclusive (if single-label).
* Write annotation guidelines to reduce label noise.

## Step 2: Split data correctly

* Use train/validation/test split before model tuning.
* Keep label distribution similar across splits.

## Step 3: Build baseline

* Start with TF-IDF + linear classifier.
* This baseline is fast, interpretable, and often strong on small datasets.

## Step 4: Fine-tune transformer

* Tokenize inputs with pretrained tokenizer.
* Add classification head on top of [CLS] (or pooled) embedding.
* Train end-to-end with cross-entropy.

## Step 5: Evaluate and calibrate

* Evaluate on validation/test data using task-appropriate criteria.
* Tune decision thresholds for imbalanced or multi-label tasks.

---

# Practical Notes

## Handle class imbalance carefully

* Check class frequencies before training to identify majority/minority skew.
* Track per-class validation behavior, not only aggregate performance.
* Prioritize minority-class recall when those errors are costly.

## Use proper train/validation splits

* Split data before tuning to avoid optimistic validation results.
* Preserve label distribution across splits when possible.
* Prevent near-duplicate texts from leaking across train and validation/test sets.

## Use imbalance mitigation methods

* Apply class-weighted loss to penalize minority-class errors more.
* Consider focal loss when many easy examples dominate training.
* Use minority oversampling carefully to improve recall without overfitting.

## Run targeted error analysis

* Inspect the confusion matrix to find systematic class confusions.
* Review false positives and false negatives by class to identify failure modes.
* Check tokenization and domain vocabulary coverage for missing signal.




