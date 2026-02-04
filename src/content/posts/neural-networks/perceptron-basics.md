---
title: "Neural Networks: Perceptron Basics"
published: 2026-02-01
description: "Perceptron foundations with core training concepts and functions."
tags: ["Deep Learning", "Neural Networks"]
category: Notes
draft: false
---

# Syllabus Map

* Study map: [Syllabus Study Map](/posts/syllabus/study-map/)

---
# Overview

* The perceptron is the simplest neural unit for binary classification.
* It motivates gradient-based optimization in larger networks.

---

# Gradient Descent

## Core Idea

* Update parameters to reduce loss.
* Use learning rate to control step size.

## Basic Loop

* Compute predictions.
* Measure loss.
* Update weights in the direction of negative gradient.

---

# Backpropagation

## Core Idea

* Use chain rule to compute gradients.
* Propagate error backward through layers.

## Practical Notes

* Requires differentiable activations.
* Enables efficient learning in deep networks.

---

# Activation Functions

## ReLU

* Simple and fast.
* Risk of dead neurons with large negative inputs.

## Sigmoid

* Outputs in [0, 1].
* Can saturate and slow training.

## Tanh

* Outputs in [-1, 1].
* Often better centered than sigmoid.

---

# Loss Functions

## Regression

* Mean Squared Error (MSE).
* Mean Absolute Error (MAE).

## Classification

* Cross Entropy.
* Binary Cross Entropy.


