---
title: Image Generation
published: 2026-02-18
description: "GANs and diffusion models for generating images."
tags: ["Computer Vision", "Deep Learning"]
category: IOAI ML Notes
draft: false
access: restricted
---
# Syllabus Map

* Study map: [Syllabus Study Map](/posts/syllabus/ioai-study-map/)

---
# Overview

* Generative models synthesise realistic images.
* Two major families are GANs and diffusion models.
* GANs are usually faster at sampling; diffusion models are usually more stable and higher quality.

---

# GAN (Generative Adversial Network)

![](../assets/image-generation/gan-overview-diagram.png)

## Core Idea

* **Generator** $G$ maps latent noise $z$ to an image $\hat{x}=G(z)$.
* **Discriminator** $D$ predicts whether an image is real ($x$) or generated ($G(z)$).
* Training is adversarial:

$$
\min_G \max_D \;
\mathbb{E}_{x\sim p_{\text{data}}}[\log D(x)] +
\mathbb{E}_{z\sim p(z)}[\log(1-D(G(z)))]
$$

* $p_{\text{data}}$ is the real image distribution.
* $p(z)$ is latent prior (typically Gaussian).

## Step-by-Step GAN Training

### Step 1: Sample data and latent vectors
* Draw real images $x$ from the dataset.
* Draw noise vectors $z\sim \mathcal{N}(0,I)$.

### Step 2: Update discriminator
* Train $D$ to assign high score to real images and low score to generated images.
* This improves real/fake separation.

### Step 3: Update generator
* Train $G$ to produce images that fool $D$.
* Generator gradients flow through discriminator feedback.

### Step 4: Alternate updates
* Repeat discriminator and generator updates.
* Keep training balanced to avoid one network overpowering the other.

## Important GAN Variants

* **DCGAN**: convolutional baseline for stable image generation.
* **WGAN / WGAN-GP**: Wasserstein objective + gradient penalty for improved stability.
* **StyleGAN2/3**: style-based generator with strong photorealism and controllability.

## Practical Notes

* Training can be unstable.
* Requires careful balance of $G$ and $D$.
* Common failure mode: mode collapse (limited diversity).
* Common quality metrics: FID and IS.

---

# Diffusion Models

## Core Idea

* Learn to denoise from random noise to a data sample.
* Forward process gradually adds Gaussian noise to images.
* Reverse process learns to remove noise step-by-step.

$$
q(x_t \mid x_{t-1}) = \mathcal{N}\!\left(\sqrt{1-\beta_t}\,x_{t-1}, \beta_t I\right)
$$

* $\beta_t$ controls noise level at timestep $t$.

## Step-by-Step Diffusion Training

### Step 1: Sample image and timestep
* Draw clean image $x_0$ and random timestep $t$.

### Step 2: Add noise
* Sample $\epsilon \sim \mathcal{N}(0,I)$ and form noisy sample:

$$
x_t = \sqrt{\bar{\alpha}_t}x_0 + \sqrt{1-\bar{\alpha}_t}\,\epsilon
$$

* $\bar{\alpha}_t = \prod_{s=1}^{t}(1-\beta_s)$.

### Step 3: Predict noise
* Train denoiser $\epsilon_\theta(x_t,t,c)$ to estimate the injected noise.
* $c$ is optional conditioning input (for example text prompt).

### Step 4: Optimize denoising loss

$$
\mathcal{L}_{\text{simple}}=
\mathbb{E}_{x_0,\epsilon,t}\left[
\|\epsilon-\epsilon_\theta(x_t,t,c)\|_2^2
\right]
$$

### Step 5: Sample images
* Start from $x_T\sim \mathcal{N}(0,I)$.
* Iteratively denoise from timestep $T$ down to $0$.

## Guidance and Samplers

* **Classifier-free guidance (CFG)** improves condition alignment:

$$
\hat{\epsilon}=
\epsilon_\theta(x_t,t,\varnothing)+
w\left(\epsilon_\theta(x_t,t,c)-\epsilon_\theta(x_t,t,\varnothing)\right)
$$

* $w$ is guidance scale; larger values strengthen condition fidelity but can reduce diversity.
* Common samplers: DDPM, DDIM, and DPM-Solver variants.

## Practical Notes

* Produces high-quality results.
* Often slower at inference.
* Latent diffusion reduces cost by denoising in compressed latent space.
* Key quality controls: noise schedule, number of denoising steps, guidance scale, and sampler.

---

# GANs vs Diffusion (Quick Comparison)

* **Training stability**: diffusion usually easier to optimize.
* **Sampling speed**: GANs are usually faster (single pass).
* **Quality/diversity**: modern diffusion is usually stronger.
* **Conditioning**: diffusion integrates text/image guidance naturally.





