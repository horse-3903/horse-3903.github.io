---
title: Autoencoders
published: 2026-02-07
description: "Autoencoder architectures, objectives, and common applications."
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

* Autoencoders learn to compress data into a latent code and reconstruct the original input.
* They are trained without labels, making them useful for representation learning.
* Common uses include dimensionality reduction, denoising, and anomaly detection.
* The bottleneck forces the model to capture the most salient structure in the data.

---

# Core Idea

* Learn an encoder $f_\theta$ that maps input $x$ to a compact latent vector $z$.
* Learn a decoder $g_\phi$ that reconstructs $\hat{x}$ from $z$.
* Train by minimising reconstruction error so $x \approx \hat{x}$.

---

# How It Works

### Step 1: Encode the input
* Start with input vector $x \in \mathbb{R}^d$.
* Compute latent code $z = f_\theta(x)$.
* The bottleneck dimension $k$ is typically smaller than $d$.

### Step 2: Decode the latent code
* Reconstruct $\hat{x} = g_\phi(z)$.
* Decoder mirrors the encoder or uses a task-specific head.
* Output shape matches the input shape.

### Step 3: Measure reconstruction error
* Compare $x$ and $\hat{x}$ with a suitable loss.
* Typical losses: MSE for real-valued data, BCE for binary data.
* The loss defines what details are prioritised in reconstruction.

### Step 4: Update parameters
* Backpropagate the reconstruction loss through decoder and encoder.
* Update $\theta, \phi$ with gradient descent.
* Repeat over mini-batches until convergence.

---

# Objective / Formula

$$
z = f_\theta(x), \quad \hat{x} = g_\phi(z)
$$

$$
\min_{\theta,\phi} \; \mathbb{E}_{x \sim p_{\text{data}}} \left[ \mathcal{L}(x, \hat{x}) \right]
$$

---

# Practical Notes

* **Undercomplete** autoencoders (small $k$) encourage compact, informative codes.
* **Overcomplete** autoencoders need regularisation (e.g. sparsity, dropout) to avoid trivial identity mapping.
* **Denoising** autoencoders reconstruct clean $x$ from corrupted $\tilde{x}$, improving robustness.
* **Variational** autoencoders add a distributional constraint for generative modelling.
* Reconstruction quality can be high even when downstream representations are weak, so validate with task metrics.
* For images, convolutional encoders/decoders usually outperform fully connected ones.

