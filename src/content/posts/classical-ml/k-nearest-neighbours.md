---
title: K-Nearest Neighbours
published: 2026-02-19
description: "A comprehensive guide to K-Nearest Neighbours — exploring how local similarity drives instance-based learning."
tags: ["Classical Machine Learning", "Supervised Learning"]
category: IOAI ML Notes
draft: false
access: public
---
# Syllabus Map

* Study map: [Syllabus Study Map](/posts/syllabus/ioai-study-map/)

---
# k-Nearest Neighbours

# Definition

* The **k-nearest neighbours (KNN)** algorithm is a **non-parametric, supervised** learning classifier.
* It uses **proximity** to make classifications or predictions about the grouping of an individual data point.

# Distance Metrics

## Euclidean Distance

* Calculates the **straight-line distance** of a point $p$ from another point $q$, where $i$ is the $i$-th dimension :

$$
d(p, q) = \sqrt{\sum_{i = 1}^{m} (p_i - q_i)^2 }
$$

## Manhattan Distance

* Calculates the **absolute distance** of a point $p$ from another point $q$, where $i$ is the $i$-th dimension :

$$
d(p, q) = \sum_{i = 1}^{m} \bigg| p_i - q_i \bigg|
$$

## Minkowski Distance

$$
d(p, q) = (\sum_{i = 1}^{m} \bigg| p_i - q_i \bigg|)^{\frac{1}{t}}
$$

# Inference

* k-Nearest Neighbours is a **lazy learner**, meaning there is no process of discrete training and saving of weights. 
* This makes **inference simpler** at the cost of performance.

* Consider the dataset $\mathcal{D}$ :

$$
\mathcal{D} = \{ (x_i, y_i) \}_{i=1}^{m}, \space x_i \in \mathbb{R}, \space y_i \in \{0 , 1\}
$$

* For the subset of points with class $c$

$$
\mathcal{X}_c = \{x_i \in \mathbb{R}^m \mid y_i=c \}, \space c \in \{0, 1\}
$$

---

# K-Nearest Neighbours In Practice

## When to Use K-Nearest Neighbours

* When the training data changes often and **retraining cost** should be minimal.
* When **example-based explanations** are useful for stakeholders.
* When **local neighbourhoods** reflect meaningful similarity.
* When you can trade **slower inference** for simple modelling.

## When Not to Use K-Nearest Neighbours

* When features have **incompatible scales** that cannot be normalised.
* When **class imbalance** makes local voting unreliable.
* When **memory constraints** prevent storing the full dataset.
* When **privacy constraints** disallow retaining raw examples.

## Practical Notes

### Use **KD-tree** or **ball-tree** search for speed in low dimensions.

* In practice, use KD-tree or ball-tree search for speed in low dimensions.
### **Weight neighbours** by distance to reduce boundary noise.

* In practice, weight neighbours by distance to reduce boundary noise.
### **Tune $k$ and the metric** with cross-validation.

* In practice, tune $k$ and the metric with cross-validation.
### Consider **dimensionality reduction** before KNN in high dimensions.

* In practice, consider dimensionality reduction before KNN in high dimensions.




