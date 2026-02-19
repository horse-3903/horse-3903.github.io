---
title: Autoencoders
published: 2026-02-19
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

### Bottleneck Size
* Undercomplete autoencoders (small $k$) encourage compact, informative codes.
* Overcomplete autoencoders usually need regularization (for example sparsity or dropout) to avoid identity mapping.

### Evaluation
* Strong reconstruction does not always imply useful representations for downstream tasks.
* Validate latent quality with task-relevant metrics, not only reconstruction loss.

### Architecture Choice
* For image data, convolutional encoders/decoders usually outperform fully connected architectures.
* Match the architecture to data structure (spatial, sequential, tabular) for better representations.

---

# Types of Autoencoders

## Undercomplete
### Core Mechanism
* Bottleneck $k \ll d$ forces compression.
* Encoder must discard redundant features and keep only information needed for reconstruction.

### Strengths
* Good for dimensionality reduction and compact representations.
* Often learns a useful low-dimensional manifold with simple MLP/CNN blocks.

### Limitations
* Strong compression can remove fine details.
* May underfit if the bottleneck is too narrow.

## Overcomplete
### Core Mechanism
* Bottleneck $k \ge d$ gives high latent capacity.
* Without constraints, the encoder-decoder pair can approximate identity mapping.

### Strengths
* Can preserve more detail than strict bottlenecks.
* Useful when paired with strong regularization.

### Limitations
* Needs regularization (sparsity, noise, weight decay, dropout) to avoid trivial copying.
* Representation quality can look good by reconstruction but be weak for downstream tasks.

## Sparse
### Core Mechanism
* Add sparsity penalty (for example $\ell_1$ on $z$ or KL sparsity constraints).
* Encourages only a few active latent units per sample.

### Strengths
* More interpretable latent codes.
* Better robustness to irrelevant features.

### Limitations
* Overly strong sparsity can hurt reconstruction quality.
* Requires tuning sparsity weight carefully.

## Denoising
### Core Mechanism
* Corrupt input $\tilde{x}$ and reconstruct clean $x$.
* Common corruption: Gaussian noise, masking, salt-and-pepper noise.

### Strengths
* Learns features stable under perturbations.
* Improves robustness to noisy or partially missing inputs.

### Limitations
* Performance depends on corruption type and strength.
* Mismatch between training corruption and real noise hurts transfer.

## Contractive
### Core Mechanism
* Penalize encoder sensitivity using a Jacobian norm term.
* Pushes nearby inputs to map to nearby latent codes.

### Strengths
* Learns locally invariant, smooth features.
* Can improve robustness around the data manifold.

### Limitations
* Jacobian penalties add compute cost.
* Too much contraction can collapse useful variation.

## Variational (VAE)
### Core Mechanism
* Learn a latent distribution $q_\theta(z \mid x)$ with KL regularization toward a prior $p(z)$.
* Encoder outputs $\mu(x)$ and $\sigma(x)$; sample with reparameterization.

### Reparameterization Trick
* In a VAE, direct sampling blocks standard backpropagation through stochastic nodes.
* Rewrite sampling as:

$$
z = \mu(x) + \sigma(x) \odot \epsilon, \quad \epsilon \sim \mathcal{N}(0, I)
$$

* Randomness is isolated in $\epsilon$, while $\mu(x)$ and $\sigma(x)$ stay differentiable.
* In practice, the encoder outputs $\mu(x)$ and $\log \sigma^2(x)$, with $\sigma(x)=\exp\!\left(\frac{1}{2}\log \sigma^2(x)\right)$.
* This enables low-variance gradient estimates and practical VAE training.

$$
\mathcal{L}_{\text{VAE}} =
\mathbb{E}_{q_\theta(z \mid x)}\!\left[\log p_\phi(x \mid z)\right]
- D_{\mathrm{KL}}\!\left(q_\theta(z \mid x)\,\|\,p(z)\right)
$$

### Strengths
* Enables sampling and generation.
* Latent space is smoother and more structured than deterministic AEs.

### Limitations
* Reconstructions can be blurrier than deterministic models.
* KL-reconstruction balance can be hard to tune (posterior collapse risk).

## Convolutional
### Core Mechanism
* Use convolutional encoders/decoders for spatial data.
* Downsample with strided convolutions or pooling, then decode back.

### Strengths
* Preserves locality and scales well to images.
* Learns hierarchical features (edges, textures, objects).

### Limitations
* Can lose global context without attention or large receptive fields.
* Deconvolution artifacts can affect output quality.

## Sequence
### Core Mechanism
* Use RNN or Transformer encoder-decoder for sequential inputs.
* Encode variable-length sequences into latent states or token embeddings.

### Strengths
* Works well for text, speech, and time series.
* Attention-based variants preserve long-range dependencies better than plain RNNs.

### Limitations
* Sequence compression can discard fine temporal/token details.
* Training can be memory-heavy for long contexts.

## Adversarial (AAE)
### Core Mechanism
* Match latent distribution to a target prior with a discriminator.
* Replace explicit KL with adversarial latent regularization.

### Strengths
* Flexible prior matching and often sharper samples.
* Combines reconstruction quality with generative latent structure.

### Limitations
* Inherits adversarial training instability.
* Requires balancing reconstruction and discriminator objectives.
