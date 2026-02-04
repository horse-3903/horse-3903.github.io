---
title: t-SNE & UMAP
published: 2026-02-01
description: "A concise guide to t-SNE and UMAP for nonlinear dimensionality reduction."
tags: ["Machine Learning", "Unsupervised Learning"]
category: Notes
draft: false
---

# Syllabus Map

* Study map: [Syllabus Study Map](/posts/syllabus/study-map/)

---
# Overview

* t-SNE and UMAP are nonlinear techniques for visualizing high-dimensional data.
* Both focus on preserving local structure in low-dimensional projections.

---

# t-SNE (T-distributed Stochastic Neighbor Embedding)

## Core Idea

* Given a set of high-dimensional objects, t-SNE computes the probabilities which is proportional to the similarity of the two objects
* This is the conditional probability that $ x_i $ would pick $ x_j $ as its neighbour if neighbors were picked in proportion to their probability density under a Gaussian centered at $ x_i $
* Essentially, it converts pairwise distances into probabilities
* This minimises divergence between high- and low-dimensional distributions.

## How It Works (High Level)

* Compute pairwise similarities in the original space.
* Map points into 2D or 3D.
* Optimize positions to preserve neighborhood structure.

## Practical Notes

* Sensitive to perplexity and learning rate.
* Typically used for visualization, not downstream modeling.

---

# UMAP

## Core Idea

* Builds a graph of local neighborhoods.
* Optimizes a low-dimensional embedding that preserves graph structure.

## How It Works (High Level)

* Construct a k-nearest-neighbor graph.
* Use a fuzzy topological representation.
* Optimize embeddings with a cross-entropy objective.

## Practical Notes

* Faster than t-SNE for larger datasets.
* Often preserves more global structure.


