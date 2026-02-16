---
title: Text Classification
published: 2026-02-16
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

* Report appropriate metrics (macro/micro F1, precision, recall, accuracy).
* Tune decision thresholds for imbalanced or multi-label tasks.

---

# Metrics

## Precision / Recall / F1

$$
\text{Precision}=\frac{TP}{TP+FP},\quad
\text{Recall}=\frac{TP}{TP+FN}
$$

$$
F_1=2\cdot\frac{\text{Precision}\cdot\text{Recall}}{\text{Precision}+\text{Recall}}
$$

## Macro vs Micro

* **Macro-F1**: equal weight per class (good for imbalance).
* **Micro-F1**: aggregates global TP/FP/FN (dominated by frequent classes).

---

# Practical Notes

## Handle class imbalance carefully.

* Handle class imbalance carefully.
## Use proper train/validation splits.

* Use proper train/validation splits.
## Imbalance fixes: class-weighted loss, focal loss, oversampling minority classes.

* Imbalance fixes: class-weighted loss, focal loss, oversampling minority classes.
## Error analysis matters:

* Error analysis matters:
## inspect confusion matrix,

* inspect confusion matrix,
## inspect false positives/negatives by class,

* inspect false positives/negatives by class,
## inspect tokenization issues and domain-specific vocabulary gaps.

* inspect tokenization issues and domain-specific vocabulary gaps.




