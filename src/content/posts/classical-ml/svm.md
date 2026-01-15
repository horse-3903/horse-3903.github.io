---
title: Support Vector Machines
published: 2025-11-25
description: "A comprehensive guide to support vector machines — exploring how margin maximisation and regularisation create powerful and flexible classifiers."
tags: ["Machine Learning", "Supervised Learning"]
category: Notes
draft: false
---

# Overview
* Support Vector Machines (SVMs) are effective out-of-the-box classifiers.

* SVM is also a generalisation of the simple yet elegant algorithm called the maximal margin classifier.

* Assuming we have a dataset with two classes, we want to find the optimal hyperplane which can separate the two classes.

* The margin refers to the minimum distance between two data points of two different classes perpendicular to the direction of the hyperplane.

# What is a Hyperplane?
* For a hyperplane in $ p $ dimensions, it is defined as a flat affine subspace with $ p - 1 $ dimensions.

* In other words, a hyperplane can be thought of as a decision boundary. 

# Defining the separating hyperplane
* Assume we have a dataset in a two-dimensional space which can be linearly separated, the hyperplane dividing the data points according to their classes is a line.

* The hyperplane $ H_0 $ can be defined as the set of points $ x $ which satisfy the equation: 

$$
wx + b = 0
$$

* If we select two hyperplanes $ H_1 $ and $ H_2 $ with the same distance from $ H_0 $, and ensuring that each data point lies on the correct side with no data in between, they can be defined as:

$$
(H_1) \space w x_i + b \ge 1 \space \text{ if } y_i = 1
$$

$$
(H_2) \space w x_i + b \le 1 \space \text{ if } y_i = -1
$$

* Where:
  * $ x_i \in \mathbb{R} $
  * $ y_i \in \{-1, 1\} $


# Finding the optimal separating hyperplane
* Since our dataset can be perfectly separated using a hyperplane and any hyperplane can be shifted and rotated, there are an infinite number of possible solutions in choosing a hyperplane.

* The **optimal separating hyperplane** is the solution that is farthest away from the closest data point, or maximises the margin

## Defining the margin
* In order to maximize the distance between the two hyperplanes, we need to find a way to calculate the margin.

* The margin can also be interpreted as a vector that is perpendicular to any hyperplane with a magnitude that is equal to the margin.

1. For any point $ x $, the distance to the hyperplane $ w^\top x + b = 0 $ is:

$$
d = \frac{| w^\top x + b |}{|| w ||}
$$

2. The distance between two margin hyperplanes would be