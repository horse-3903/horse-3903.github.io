---
title: Weight Initialisation
published: 2026-02-07
description: "Weight initialisation schemes and practical guidelines for stable training."
tags: ["Neural Network", "Deep Learning"]
category: IOAI ML Notes
draft: false
pinned: false
access: restricted
---

# Syllabus Map

* Study map: [Syllabus Study Map](/posts/syllabus/ioai-study-map/)

---

# Overview

* This note covers **weight initialisation** methods and why they matter.
* Good initialisation prevents **vanishing** or **exploding** activations.

---

# Distributions (Normal vs Uniform)

## Normal distribution
* Bell‑shaped curve centred at zero.
* Higher probability near the mean, fewer extreme values.
![](../assets/weight-initialisation/normal-distribution.svg)

## Uniform distribution
* Flat distribution where all values in a range are equally likely.
* Produces **bounded** weights with no heavy tails.
![](../assets/weight-initialisation/uniform-distribution.svg)

---

# Notation / Terminology

* $ W $: weight matrix for a layer.
* $ b $: bias vector.
* $ n_{in} $: number of input units (fan‑in).
* $ n_{out} $: number of output units (fan‑out).
* $ \mathrm{Var}(W) $: variance of the weight distribution.
* **Symmetry breaking**: ensuring neurons start with different weights.

---

# Core idea

* Initialisation sets the starting scale of weights.
* The goal is to keep activations and gradients in a **stable range**.

# Common schemes

## Random initialisation
* Initialise weights with small random values (uniform or normal).
* Helps **break symmetry** so neurons learn different features.
* Too large can cause exploding activations; too small can cause vanishing.

## Constant initialisation
* Sets all weights to the same value.
* Useful for **bias terms** or controlled experiments.
* Bad for hidden weights because it **does not break symmetry**.

## Xavier / Glorot
* Best for **tanh/sigmoid** activations.
* Variance: $ \mathrm{Var}(W) = \frac{2}{n_{in}+n_{out}} $

### Uniform form
$$
W \sim \mathcal{U}\left(-\sqrt{\frac{6}{n_{in}+n_{out}}},\ \sqrt{\frac{6}{n_{in}+n_{out}}}\right)
$$
* This keeps the initial activations from exploding or shrinking by matching variance across layers.

### Normal form
$$
W \sim \mathcal{N}\left(0,\ \frac{2}{n_{in}+n_{out}}\right)
$$
* Equivalent variance to the uniform version, but with a Gaussian distribution.

## He / Kaiming
* Best for **ReLU‑like** activations.
* Variance: $ \mathrm{Var}(W) = \frac{2}{n_{in}} $

### Uniform form
$$
W \sim \mathcal{U}\left(-\sqrt{\frac{6}{n_{in}}},\ \sqrt{\frac{6}{n_{in}}}\right)
$$
* Keeps activation variance stable for ReLU‑like layers.

### Normal form
$$
W \sim \mathcal{N}\left(0,\ \frac{2}{n_{in}}\right)
$$
* Standard Kaiming normal initialisation for ReLU‑like activations.

# Practical notes

* Match initialisation to activation function.
* Biases are often initialised to zero.
