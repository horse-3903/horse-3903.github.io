---
title: CNN Tasks
published: 2026-02-15
description: "Core CNN-based vision tasks and common model families."
tags: ["Computer Vision", "Deep Learning"]
category: IOAI ML Notes
draft: false
access: public
---
# Syllabus Map

* Study map: [Syllabus Study Map](/posts/syllabus/ioai-study-map/)

---
# Overview

* CNNs are used for image-level prediction, region-level localization, and pixel-level labeling.
* The output granularity determines the task:
* **Image classification**: one label per image.
* **Object detection**: boxes + labels per object.
* **Image segmentation**: label per pixel.

---

# Image Classification

## Core Idea

* Input: full image tensor $H \times W \times C$.
* Output: class probability vector of size $K$.
* Train with cross-entropy on labeled images.
* Evaluate with top-1/top-5 accuracy and confusion matrix.

---

# Object Detection

## Core Idea

* Input: image with variable number of objects.
* Output: $(x, y, w, h, \text{class}, \text{confidence})$ per detected object.
* Train with multi-part loss: classification + box regression (+ objectness).
* Evaluate with mAP at different IoU thresholds (for example, mAP@0.5 and mAP@[0.5:0.95]).

## You-Only-Look-Once (YOLO)

![](../../assets/cnn-tasks/yolo.png)

### Step 1: Prepare Labels

* Convert annotations to normalized box format $(c_x, c_y, w, h, \text{class\_id})$.
* Ensure class IDs are contiguous and images/labels are paired correctly.

### Step 2: Train Grid-Based Predictions

* Split image into feature grid cells.
* Predict objectness, class scores, and box offsets per anchor/location.

### Step 3: Optimize Detection Loss

* Compute objectness loss for object/background.
* Compute class loss for positive samples.
* Compute box loss (IoU-based or L1-style, depending on YOLO version).
* A common multi-part objective is:

$$
\mathcal{L}_{\text{YOLO}}=
\lambda_{\text{box}}\mathcal{L}_{\text{box}}+
\lambda_{\text{obj}}\mathcal{L}_{\text{obj}}+
\lambda_{\text{cls}}\mathcal{L}_{\text{cls}}
$$
* $\mathcal{L}_{\text{YOLO}}$ is total YOLO training loss.
* $\mathcal{L}_{\text{box}}$, $\mathcal{L}_{\text{obj}}$, and $\mathcal{L}_{\text{cls}}$ are box, objectness, and class losses.
* $\lambda_{\text{box}}$, $\lambda_{\text{obj}}$, and $\lambda_{\text{cls}}$ weight each loss term.

$$
\mathcal{L}_{\text{box}}=\sum_{i\in \text{Pos}}\left(1-\text{IoU}(b_i,\hat{b}_i)\right)
$$
* $\text{Pos}$ is the set of positive anchors (matched to objects).
* $b_i$ is the predicted box for anchor $i$, and $\hat{b}_i$ is the ground-truth box.
* $\text{IoU}(b_i,\hat{b}_i)$ is overlap quality; higher IoU gives lower loss.

$$
\mathcal{L}_{\text{obj}}=-\sum_i \left[y_i\log p_i+(1-y_i)\log(1-p_i)\right]
$$
* $y_i \in \{0,1\}$ is the objectness label for anchor $i$.
* $p_i$ is the predicted probability that anchor $i$ contains an object.
* The expression is binary cross-entropy over all anchors.

$$
\mathcal{L}_{\text{cls}}=-\sum_{i\in \text{Pos}}\sum_{c=1}^{C} y_{i,c}\log \hat{p}_{i,c}
$$
* $C$ is the number of classes.
* $y_{i,c}$ is the one-hot class label for positive anchor $i$ and class $c$.
* $\hat{p}_{i,c}$ is the predicted class probability for class $c$ at anchor $i$.

### Step 4: Run Post-Processing

* Filter low-confidence predictions.
* Compute overlap with Intersection over Union (IoU):

$$
\text{IoU}(A,B)=\frac{|A\cap B|}{|A\cup B|}
$$
* $A$ is a predicted box and $B$ is a reference box (often ground truth or another prediction).
* $|A\cap B|$ is intersection area; $|A\cup B|$ is union area.
* IoU ranges from $0$ (no overlap) to $1$ (perfect overlap).

* IoU close to $1$ means strong overlap; IoU close to $0$ means little overlap.
* Apply Non-Maximum Suppression (NMS) to remove duplicate detections:
  * Sort boxes by confidence score.
  * Keep the highest-score box and suppress lower-score boxes that overlap it too much.
  * Repeat until no candidate boxes remain.

$$
\text{suppress } b_j \text{ if } \text{IoU}(b_i,b_j)>\tau_{\text{nms}} \text{ and } s_i>s_j
$$
* $b_i$ and $b_j$ are candidate predicted boxes.
* $s_i$ and $s_j$ are their confidence scores.
* $\tau_{\text{nms}}$ is the NMS IoU threshold used to drop duplicate boxes.

### Step 5: Evaluate and Deploy

* Measure mAP and latency.
* Tune confidence/NMS thresholds for task-specific precision-recall tradeoff.

---

## Single Shot MultiBox Detector (SSD)

![](../../assets/cnn-tasks/ssd.png)

### Step 1: Build Multi-Scale Feature Maps

* Extract backbone features at several spatial resolutions.
* Attach detection heads to each scale for small-to-large objects.

### Step 2: Match Ground Truth to Default Boxes

* Predefine default boxes (anchors) with multiple scales/aspect ratios.
* Match anchors to ground-truth boxes using IoU rules.

### Step 3: Train Classification and Localization

* Predict class logits for each anchor.
* Predict box offsets relative to matched default boxes.
* Typical SSD objective:

$$
\mathcal{L}_{\text{SSD}}=\frac{1}{N}\left(\mathcal{L}_{\text{cls}}+\alpha \mathcal{L}_{\text{loc}}\right)
$$
* $\mathcal{L}_{\text{SSD}}$ is total SSD loss.
* $\mathcal{L}_{\text{cls}}$ is classification loss and $\mathcal{L}_{\text{loc}}$ is localization loss.
* $N$ is the number of matched positive anchors for normalization.
* $\alpha$ balances localization against classification.

$$
\mathcal{L}_{\text{loc}}=\sum_{i\in \text{Pos}} \space \sum_{m\in\{c_x,c_y,w,h\}}
\text{SmoothL1}\!\left(t_i^m-\hat{t}_i^m\right)
$$
* $m\in\{c_x,c_y,w,h\}$ iterates over box center and size coordinates.
* $t_i^m$ is predicted offset and $\hat{t}_i^m$ is target offset for anchor $i$.
* $\text{SmoothL1}$ is a robust regression loss less sensitive to outliers than L2.

### Step 4: Apply Hard Negative Mining

* Keep informative negative anchors with highest classification loss.
* Balance positive and negative samples during training.
* Standard ratio target is:

$$
\frac{N_{\text{neg}}}{N_{\text{pos}}}\le 3
$$
* $N_{\text{neg}}$ is the number of selected negative anchors.
* $N_{\text{pos}}$ is the number of positive anchors.
* The inequality enforces at most a 3:1 negative-to-positive ratio.

### Step 5: Decode and Filter Predictions

* Convert offsets back to absolute boxes.
* Apply confidence thresholding and NMS before final outputs.

---

## Detection Transformers (DETR)

### Step 1: Encode Image Features

* Run image through a CNN backbone to get feature maps.
* Flatten features and add positional encodings.

### Step 2: Decode with Object Queries

* Feed learned object queries into a transformer decoder.
* Each query predicts one potential object slot.

### Step 3: Hungarian Matching

* Match predictions to ground-truth objects one-to-one.
* Use matching cost from class and box terms.
* Matching is solved by:

$$
\hat{\sigma}=\arg\min_{\sigma}\sum_i
\left[
-\log \hat{p}_{\sigma(i)}(c_i)+
\lambda_1\|b_i-\hat{b}_{\sigma(i)}\|_1+
\lambda_2\left(1-\text{GIoU}(b_i,\hat{b}_{\sigma(i)})\right)
\right]
$$
* $\sigma$ is a matching between predictions and ground-truth objects.
* $\hat{\sigma}$ is the optimal one-to-one assignment found by Hungarian matching.
* $\hat{p}_{\sigma(i)}(c_i)$ is predicted probability of the true class $c_i$ for matched prediction $\sigma(i)$.
* $\|b_i-\hat{b}_{\sigma(i)}\|_1$ is L1 box distance.
* $\text{GIoU}$ is generalized IoU for box overlap quality.
* $\lambda_1$ and $\lambda_2$ weight localization terms in the matching cost.

### Step 4: Optimize Set Prediction Loss

* Train class predictions including a "no-object" class.
* Train box regression with L1 + generalized IoU loss.
* DETR set loss:

$$
\mathcal{L}_{\text{DETR}}=
\mathcal{L}_{\text{cls}}+
\lambda_1\mathcal{L}_{L1}+
\lambda_2\mathcal{L}_{\text{GIoU}}
$$
* $\mathcal{L}_{\text{DETR}}$ is total DETR training loss.
* $\mathcal{L}_{\text{cls}}$ is classification loss including the no-object class.
* $\mathcal{L}_{L1}$ is coordinate regression loss.
* $\mathcal{L}_{\text{GIoU}}$ is overlap-based regression loss.
* $\lambda_1$ and $\lambda_2$ set the relative weight of box losses.

### Step 5: Inference without NMS

* Keep high-confidence query outputs directly.
* One-to-one matching behavior reduces duplicate detections.

---

# Image Segmentation

## Core Idea

* Input: image and dense pixel mask labels.
* Output: mask $H \times W$ (semantic) or per-instance masks (instance segmentation).
* Train with pixel-wise losses (cross-entropy, Dice, or combined loss).
* Evaluate with IoU (Jaccard), Dice score, and pixel accuracy.

## U-Net

### Step 1: Encode Context

* Downsample with convolution blocks to capture global context.
* Store intermediate feature maps for skip connections.

### Step 2: Decode Spatial Detail

* Upsample progressively back to image resolution.
* Concatenate decoder features with matching encoder skip features.

### Step 3: Predict Pixel Masks

* Use final convolution layer to output per-pixel class logits.
* Convert logits to masks with softmax/sigmoid.

### Step 4: Train with Dense Losses

* Use cross-entropy for multi-class segmentation.
* Add Dice loss when classes are imbalanced or objects are thin/small.
* Common combined objective:

$$
\mathcal{L}_{\text{seg}}=
\lambda_{\text{ce}}\mathcal{L}_{\text{CE}}+
\lambda_{\text{dice}}\mathcal{L}_{\text{Dice}}
$$
* $\mathcal{L}_{\text{seg}}$ is total segmentation loss.
* $\mathcal{L}_{\text{CE}}$ is pixel-wise cross-entropy.
* $\mathcal{L}_{\text{Dice}}$ emphasizes region overlap quality.
* $\lambda_{\text{ce}}$ and $\lambda_{\text{dice}}$ weight the two terms.

$$
\mathcal{L}_{\text{Dice}}=
1-\frac{2\sum_i p_i y_i+\epsilon}{\sum_i p_i+\sum_i y_i+\epsilon}
$$
* $p_i$ is predicted probability (or soft mask value) at pixel $i$.
* $y_i$ is ground-truth mask value at pixel $i$.
* $\epsilon$ is a small constant for numerical stability.
* The fraction is soft Dice overlap; subtracting from $1$ turns it into a minimization loss.

### Step 5: Post-Process Masks

* Apply thresholding for binary masks.
* Use connected components or morphology to clean noisy regions.
