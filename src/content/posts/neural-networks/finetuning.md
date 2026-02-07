---
title: Fine-tuning
published: 2026-02-07
description: "Fine-tuning strategies for adapting pretrained models to specific tasks."
tags: ["Neural Network", "Deep Learning"]
category: Notes
draft: false
pinned: false
---

# Syllabus Map

* Study map: [Syllabus Study Map](/posts/syllabus/ioai-study-map/)

---

# Overview

* Fine‑tuning adapts a **pretrained model** to a new task or dataset.
* It can be **full fine‑tuning** (update all weights) or **parameter‑efficient** (update small adapters).
* The choice depends on data size, compute budget, and how far the task is from pretraining.

---

# Core idea

* Start from a model with useful representations.
* Update a subset (or all) parameters using task‑specific data.
* Benefits:
  * Faster convergence.
  * Better performance with limited data.
* Risks:
  * Overfitting if the dataset is small.
  * Catastrophic forgetting of general features.

---

# Full Fine‑tuning

## What it is
* All model weights are updated.
* Highest capacity to adapt to a new domain.

## When to use
* Large task dataset.
* High domain shift from pretraining data.
* Sufficient compute and memory.

## Tips
* Use smaller learning rates for stability.
* Consider layer‑wise learning rates (lower for early layers).
* Monitor validation to avoid overfitting.

---

# Parameter‑efficient fine‑tuning (PEFT)

## What it is
* Freeze most weights; train small **adapter** components.
* Much cheaper in memory and compute.

## Common methods
* **Adapters**: small bottleneck layers inserted into the network.
* **LoRA**: low‑rank updates to weight matrices.
* **Prefix/Prompt Tuning**: learn task‑specific tokens.

## When to use
* Limited compute or many tasks.
* Need fast iteration and small checkpoints.
* Want to preserve base model behaviour.

---

# Practical workflow

## Step 1: Prepare data
* Clean and align labels.
* Use validation splits to track overfitting.

## Step 2: Choose strategy
* Full fine‑tune for maximum performance.
* PEFT for efficiency and scalability.

## Step 3: Train
* Use warmup and decay schedules.
* Monitor loss curves and early stop if needed.

## Step 4: Evaluate and deploy
* Compare against the base model.
* Save the fine‑tuned weights or adapters.
