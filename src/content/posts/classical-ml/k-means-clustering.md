---
title: K-Means Clustering
published: 2026-02-19
description: "A concise guide to k-means clustering, its objective, and practical usage."
tags: ["Classical Machine Learning", "Unsupervised Learning"]
category: IOAI ML Notes
draft: false
access: public
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

* Minimise the sum of squared distances (also called **WCSS**, within-cluster sum of squares):
$$
\min_{\{\mu_1,\dots,\mu_k\}} \sum_{i=1}^{n} \min_{j \in \{1,\dots,k\}} \|x_i - \mu_j\|^2
$$
* Caveat: WCSS always decreases as $k$ increases, so lower WCSS alone does **not** mean a better or more meaningful clustering.

## Elbow Method

* Fit k-means for a range of $k$ values (for example $k=1$ to $k=10$).
* Compute WCSS for each $k$.
* Plot WCSS vs $k$ and choose the "elbow": the point where adding more clusters yields diminishing improvement.
* Use this as a heuristic, then validate with task context or other metrics (for example silhouette score).

## Practical Notes

### Initialization
* K-means is sensitive to starting centers; prefer k-means++ and multiple restarts.

### Choosing $k$
* Use elbow and/or silhouette methods instead of fixing $k$ arbitrarily.

### Cluster Shape Assumptions
* K-means works best for compact, roughly spherical, similar-density clusters.
* It can fail on elongated, overlapping, or highly imbalanced clusters.

### Feature Scaling
* Scale features before clustering so high-variance dimensions do not dominate Euclidean distance.

### Outliers
* Means are sensitive to outliers; extreme points can pull cluster centers.


