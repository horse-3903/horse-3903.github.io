# SMU H3 Map

* Content map: [SMU H3 Game Theory Map](/posts/game-theory/smu-h3/)

---

﻿---
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

# t-SNE

## Core Idea

* Converts pairwise distances into probabilities.
* Minimizes divergence between high- and low-dimensional distributions.

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


