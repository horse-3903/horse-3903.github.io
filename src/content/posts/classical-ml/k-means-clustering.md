---
title: K-Means Clustering
published: 2026-02-07
description: "A concise guide to k-means clustering, its objective, and practical usage."
tags: ["Classical Machine Learning", "Unsupervised Learning"]
category: Notes
draft: false
---

# Syllabus Map

* Study map: [Syllabus Study Map](/posts/syllabus/ioai-study-map/)

---

# Overview

* **K-means** groups data into $k$ clusters by minimising **within-cluster variance**.
* It works best for **compact, roughly spherical** clusters.

---

# K-Means

## Core Idea

* K‑means alternates between **assigning points to the nearest centre** and **recomputing centres** as averages.
* It is a simple, fast way to find **compact, well‑separated** clusters.
* Results depend on initial centres, so multiple runs are common.

## How It Works

### Step 1: Initialise centres
* Choose $k$ initial centres $ \mu_1, \dots, \mu_k $.
* Use **random** initialisation or **k‑means++** for better stability.

#### What is k‑means++?
* A smarter **seeding method** that spreads centres apart.
* It reduces the chance of **poor local minima**.
* Steps:
  * Pick the **first centre** uniformly at random from the data.
  * For each point, compute its **squared distance** to the nearest chosen centre.
  * Sample the **next centre** with probability proportional to that squared distance.
  * Repeat until $k$ centres are chosen.

### Step 2: Assignment step
* Assign each point $ x_i $ to the nearest centre:
$$
c_i = \arg\min_{j \in \{1,\dots,k\}} \|x_i - \mu_j\|^2
$$
* This creates $k$ clusters based on closest centre.

### Step 3: Update step
* Recompute each centre as the mean of its assigned points:
$$
\mu_j = \frac{1}{|C_j|} \sum_{i: c_i = j} x_i
$$
* This moves centres to the **average location** of their clusters.

### Step 4: Check convergence
* Stop if assignments no longer change or centres move less than a tolerance.
* Otherwise, repeat Steps 2–3.

## Objective Function

* Minimise the sum of squared distances:
$$
\min_{\{\mu_1,\dots,\mu_k\}} \sum_{i=1}^{n} \min_{j \in \{1,\dots,k\}} \|x_i - \mu_j\|^2
$$

## Practical Notes

* Sensitive to **initialisation**; use **k-means++** for stability.
* Requires choosing $k$ (use **elbow** or **silhouette** methods).
* Struggles with **non-spherical** or **unequal density** clusters.
* Scale features before clustering to avoid dominance by large‑scale dimensions.
