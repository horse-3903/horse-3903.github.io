---
title: R-CNN, Fast R-CNN, and Faster R-CNN
published: 2026-02-09
description: "Region-based CNN detectors and how they evolved from R-CNN to Faster R-CNN."
tags: ["Computer Vision", "Deep Learning"]
category: IOAI ML Notes
draft: false
access: restricted
---

# Syllabus Map

* Study map: [Syllabus Study Map](/posts/syllabus/ioai-study-map/)

---
# Overview

* The R-CNN family introduced **region-based** object detection.
* Each step improved speed and end-to-end training.
* The main evolution is: **R-CNN → Fast R-CNN → Faster R-CNN**.

---
# R-CNN

## Core idea
* Generate region proposals, then run a CNN on each proposal.
* Classify each region and refine its box.

## Pipeline
* **Selective Search** proposes ~2k regions per image.
* **Warp + CNN** extracts features for each region separately.
* **SVMs** classify region features.
* **Box regressor** refines bounding boxes.

## Key traits
* **Accurate**, but extremely **slow** at inference.
* Multi-stage training (CNN, SVMs, box regressor).

---
# Fast R-CNN

## Core idea
* Run the CNN **once per image**, then classify regions using pooled features.

## Pipeline
* **Backbone CNN** produces a shared feature map.
* **RoI Pooling** crops region features from the shared map.
* **Single head** outputs class + box for each RoI.

## Key traits
* Much faster than R-CNN.
* End-to-end training for classification + box regression.
* Still depends on **external proposals** (Selective Search).

---
# Faster R-CNN

## Core idea
* Replace external proposal generation with a **Region Proposal Network (RPN)**.

## Pipeline
* **Backbone CNN** shared by RPN and detection head.
* **RPN** predicts objectness + anchor box offsets.
* **RoI Pooling / RoI Align** extracts proposal features.
* **Detection head** predicts class + refined box.

## Key traits
* Fully end-to-end and much faster than Fast R-CNN.
* Strong accuracy-speed tradeoff for general detection.

---
# How They Differ

* **R-CNN**: per-region CNN, SVMs, slow.
* **Fast R-CNN**: shared CNN, RoI Pooling, still external proposals.
* **Faster R-CNN**: shared CNN + built-in RPN proposals.

---
# Training Objectives (High Level)

* **Classification loss**: object class per RoI.
* **Box regression loss**: refine bounding box coordinates.
* **RPN loss** (Faster R-CNN only): objectness + anchor box offsets.

---
# When To Use

* **R-CNN**: historical baseline, rarely used now.
* **Fast R-CNN**: useful for understanding the progression.
* **Faster R-CNN**: strong default for accurate detection.

---
# PyTorch Quickstart (Faster R-CNN)

```py
import torch
from torchvision.models.detection import fasterrcnn_resnet50_fpn
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor

# Load a pre-trained model
model = fasterrcnn_resnet50_fpn(weights="DEFAULT")

# Replace the classifier for a custom number of classes
num_classes = 5  # includes background
in_features = model.roi_heads.box_predictor.cls_score.in_features
model.roi_heads.box_predictor = FastRCNNPredictor(in_features, num_classes)

model.train()
```



