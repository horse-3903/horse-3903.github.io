---
title: Image Augmentation
published: 2026-02-15
description: "Simple augmentation techniques to improve generalisation."
tags: ["Computer Vision"]
category: IOAI ML Notes
draft: false
access: restricted
---
# Syllabus Map

* Study map: [Syllabus Study Map](/posts/syllabus/ioai-study-map/)

---
# Overview

* Augmentation increases data diversity without new labels.
* Goal: improve generalisation by making the model invariant to nuisance changes (position, lighting, style).
* Must preserve the label semantics for the target task.

---

# Common Techniques

## Geometric

* Horizontal flip (for natural images where left-right symmetry is valid).
* Random resized crop to change scale and viewpoint.
* Rotation and translation for small pose shifts.
* Affine/perspective transforms for camera distortions.

## Photometric

* Brightness, contrast, saturation, hue jitter.
* Gaussian noise and blur for sensor/noise robustness.
* JPEG compression artifacts for real-world deployment robustness.

## Occlusion and Mixing

* Random erasing / Cutout: mask random image regions.
* CutMix: paste region from image B into image A and mix labels.
* Mixup: convex combination of two images and labels.

$$
\tilde{x} = \lambda x_i + (1-\lambda)x_j,\quad
\tilde{y} = \lambda y_i + (1-\lambda)y_j
$$
* $\lambda \in [0,1]$ controls mixing strength.

---

# Task-Specific Augmentation Rules

## Classification

* Strong photometric + moderate geometric transforms usually help.
* Typical pipeline: random crop, flip, color jitter, normalization.

## Object Detection

* Must transform boxes together with image.
* Use multi-scale resize, random crop with box-validity checks, horizontal flip.
* Avoid aggressive crops that remove all objects.

## Segmentation

* Must transform masks with the same geometry as images.
* Use nearest-neighbor interpolation for mask resizing to avoid class bleeding.
* Photometric transforms apply only to image, not mask labels.

---

# Policy-Based Augmentation

* **AutoAugment**: searches augmentation policies on a validation set.
* **RandAugment**: applies $N$ random transforms with global magnitude $M$.
* **TrivialAugment**: one random transform with random magnitude; simple and strong baseline.

---

# Practical Pipeline Design

## Step 1: Define label-safe transforms

* Keep only transformations that preserve task labels.
* Example: vertical flip is invalid for digit recognition but often valid for aerial imagery.

## Step 2: Set magnitude ranges

* Start with conservative ranges and increase gradually.
* Too-strong augmentations can cause underfitting.

## Step 3: Order transforms

* Typical order: geometric -> photometric -> normalization.
* Put stochastic regularizers (Cutout/Mixup/CutMix) near the end of pipeline.

## Step 4: Validate with ablations

* Add one augmentation family at a time.
* Track validation accuracy/mAP/IoU to isolate impact.

## Step 5: Match training and deployment

* Include corruptions expected at inference (blur, compression, low light).
* Do not train with unrealistic transforms that never appear in production.

---

# Practical Notes

* Keep augmentations label-preserving.
* Tune intensity based on task sensitivity.
* Augmentation and regularization interact: stronger augmentation often allows larger models or fewer explicit regularizers.
* For small datasets, augmentation can matter as much as architecture choice.






