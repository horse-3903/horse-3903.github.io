---
title: DBSCAN, Hierarchical & Spectral Clustering
published: 2026-02-01
description: "A concise guide to density-based, hierarchical, and spectral clustering."
tags: ["Machine Learning", "Unsupervised Learning"]
category: Notes
draft: false
---

---


# Syllabus Map

* Study map: [Syllabus Study Map](/posts/syllabus/study-map/)

---
# Overview

* Clustering groups data by similarity without labels.
* Different methods make different assumptions about cluster shape.

---

# DBSCAN

## Core Idea

* Groups points by density rather than distance alone.
* Finds clusters of arbitrary shape.

## How It Works (High Level)

* Define neighborhood radius (eps) and minimum points.
* Expand clusters from dense regions.
* Mark isolated points as noise.

## Practical Notes

* Handles outliers well.
* Struggles with varying densities.

---

# Hierarchical Clustering

## Core Idea

* Builds a tree of clusters (dendrogram).
* Can be agglomerative (bottom-up) or divisive (top-down).

## How It Works (High Level)

* Compute pairwise distances.
* Merge or split clusters iteratively.
* Cut the dendrogram at a chosen level.

## Practical Notes

* No need to pre-specify number of clusters.
* Can be expensive for large datasets.

---

# Spectral Clustering

## Core Idea

* Uses eigenvectors of a graph Laplacian.
* Finds clusters in a transformed space.

## How It Works (High Level)

* Build a similarity graph.
* Compute Laplacian eigenvectors.
* Run k-means on the eigenvector representation.

## Practical Notes

* Good for non-convex clusters.
* Requires choosing number of clusters.


