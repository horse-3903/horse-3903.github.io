---
title: Autoencoders
published: 2026-02-16
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
* Train by minimising reconstruction Error so $x \approx \hat{x}$.

---

# How It Works

### Step 1: Encode the input
* Start with input vector $x \in \mathbb{R}^d$.
* Compute latent code $z = f_\theta(x) \text{ s.t. } z \in \mathbb{R}^k$.
* The bottleneck dimension $k$ is typically smaller than $d$.

### Step 2: Decode the latent code
* Reconstruct $\hat{x} = g_\phi(z)$.
* Decoder mirrors the encoder or uses a task-specific head.
* Output shape matches the input shape.

### Step 3: Measure reconstruction Error
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

## **Undercomplete** autoencoders (small $k$) encourage compact, informative codes.

* In practice, undercomplete autoencoders (small $k$) encourage compact, informative codes.
## **Overcomplete** autoencoders need regularisation (e.g. sparsity, dropout) to avoid trivial identity mapping.

* In practice, overcomplete autoencoders need regularisation (e.g. sparsity, dropout) to avoid trivial identity mapping.
## Reconstruction quality can be high even when downstream representations are weak, so validate with task metrics.

* In practice, reconstruction quality can be high even when downstream representations are weak, so validate with task metrics.
## For images, convolutional encoders/decoders usually outperform fully connected ones.

* In practice, for images, convolutional encoders/decoders usually outperform fully connected ones.

---

# Types of Autoencoders

### Undercomplete
* Bottleneck $k \ll d$ forces compression.
* Good for dimensionality reduction and compact representations.
* Encoder must discard redundant features and keep only information needed for reconstruction.
* Typically uses a stack of linear layers with non-linearities to learn a low-dimensional manifold.

### Overcomplete
* Bottleneck $k \ge d$ can copy inputs.
* Needs regularisation to avoid identity mapping.
* Encoder can learn a high-capacity representation, so constraints (sparsity, noise, weight decay) are required.
* Without constraints, the encoder-decoder pair can approximate an identity function.

### Sparse
* Add sparsity penalty (e.g. $\ell_1$ on $z$, KL constraint).
* Encourages only a few active units per example.
* Encoder learns a distributed code where most latent units are near zero for any given input.
* Sparsity makes the representation more interpretable and robust to irrelevant features.

### Denoising
* Corrupt input $\tilde{x}$ and reconstruct clean $x$.
* Improves robustness to noise and missing values.
* Encoder learns features that are stable under input perturbations.
* Corruption can be Gaussian noise, masking, or salt-and-pepper noise.

### Contractive
* Penalise encoder sensitivity (Jacobian norm).
* Learns locally invariant features.
* Encoder is pushed to map nearby inputs to similar latents.
* Works like a smoothness constraint on $f_\theta$.

### Variational (VAE)
* Learn a distribution over $z$ with KL regularisation.
* Enables sampling and generation.
* Encoder outputs $\mu(x)$ and $\sigma(x)$ for a Gaussian $q_\theta(z \mid x)$.
* Sample $z = \mu + \sigma \odot \epsilon$ using the reparameterization trick.
* KL term shapes the latent space toward a known prior (e.g. $\mathcal{N}(0, I)$).

### Convolutional
* Use conv layers for spatial data.
* Preserves locality and scales to images.
* Encoder uses strided convolutions or pooling to reduce spatial resolution.
* Latent code captures hierarchical spatial features (edges, textures, objects).

### Sequence
* Use RNN/Transformer encoder-decoder.
* Works for text and time series.
* Encoder compresses a variable-length sequence into a fixed-size state or a set of token embeddings.
* Attention-based encoders preserve long-range dependencies better than plain RNNs.

### Adversarial (AAE)
* Match latent distribution with a discriminator.
* KL replaced by adversarial training.
* Encoder is trained to fool the discriminator so $z$ matches a target prior.
* Reconstruction loss and adversarial loss jointly shape the encoder output.
