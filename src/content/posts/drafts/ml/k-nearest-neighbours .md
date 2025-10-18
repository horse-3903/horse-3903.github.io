---
title: <Topic Name>
published: 2025-01-01
description: "<One-line summary of the note>"
tags: ["Machine Learning", "<Subtopic>"]
category: Notes
draft: true
---

# k-Nearest Neighbours

# Definition

The k-nearest neighbors (KNN) algorithm is a non-parametric, supervised learning classifier, which uses proximity to make classifications or predictions about the grouping of an individual data point.

![image.png](k-Nearest%20Neighbours%20256e401a9d0a80dead9ed51e5b9ff35f/image.png)

# Distance Metrics

## Euclidean Distance

Calculates the straight line distance of a point $p$ from another point $q$, where $i$ is the $i$-th dimension :

$$
d(p, q) = \sqrt{\sum_{i = 1}^{m} (p_i - q_i)^2 }
$$

## Manhattan Distance

Calculates the absolute distance of a point $p$ from another point $q$, where $i$ is the $i$-th dimension :

$$
d(p, q) = \sum_{i = 1}^{m} \bigg| p_i - q_i \bigg|
$$

## Minkowski Distance

$$
d(p, q) = (\sum_{i = 1}^{m} \bigg| p_i - q_i \bigg|)^{\frac{1}{t}}
$$

# Inference

k-Nearest Neighbours is a “lazy learner”, meaning there isn’t a process of discrete training and saving of weights. This makes it simpler for the inference process at the cost of performance.

Consider the dataset $\mathcal{D}$ :

$$
\mathcal{D} = \{ (x_i, y_i) \}_{i=1}^{m}, \space x_i \in \mathbb{R}, \space y_i \in \{0 , 1\}
$$

For the subset of points with class $c$

$$
\mathcal{X}_c = \{x_i \in \mathbb{R}^m \mid y_i=c \}, \space c \in \{0, 1\}
$$