---
title: Naive Bayes
published: 2026-02-18
description: "A comprehensive guide to Naive Bayes - exploring probabilistic classification with Bayes' theorem under conditional independence assumptions."
tags: ["Classical Machine Learning", "Supervised Learning"]
category: IOAI ML Notes
draft: false
access: public
---
# Syllabus Map

* Study map: [Syllabus Study Map](/posts/syllabus/ioai-study-map/)

---
# Overview

* Naive Bayes is a probabilistic classifier built from Bayes' theorem.
* It assumes features are conditionally independent given the class.
* Despite this strong assumption, it is a strong baseline for many classification tasks.

---

# Core Idea

* Bayes' theorem updates a prior belief using observed evidence:

$$
P(A \mid B) = \frac{P(B \mid A)\,P(A)}{P(B)}
$$

* For feature vector $x=(x_1,\dots,x_n)$ and class $y$:

$$
P(y \mid x_1,\dots,x_n) = \frac{P(y)\,P(x_1,\dots,x_n \mid y)}{P(x_1,\dots,x_n)}
$$

* Naive Bayes uses the conditional independence assumption:

$$
P(x_1,\dots,x_n \mid y) = \prod_{i=1}^{n} P(x_i \mid y)
$$

* So classification uses:

$$
P(y \mid x_1,\dots,x_n) \propto P(y)\prod_{i=1}^{n} P(x_i \mid y)
$$

* Predict the class with maximum posterior probability:

$$
\hat{y} = \arg\max_y P(y)\prod_{i=1}^{n}P(x_i \mid y)
$$

---

# Step-by-Step Training and Inference

### Step 1: Estimate class priors
* Compute $P(y=c)$ from class frequencies in the training set.

### Step 2: Estimate feature likelihoods
* Estimate $P(x_i \mid y=c)$ for each class and feature.
* The exact form depends on feature type and Naive Bayes variant.

### Step 3: Apply smoothing
* Use Laplace (additive) smoothing to avoid zero probabilities:

$$
P(x_i=v \mid y=c) = \frac{N_{icv} + \alpha}{N_{ic} + \alpha K}
$$

* $N_{icv}$ is count of feature value $v$ in class $c$, $K$ is number of possible values, and $\alpha>0$ is smoothing strength.

### Step 4: Score new samples
* For each class, compute posterior score and choose the largest.
* Use log-space for numerical stability:

$$
\log P(y \mid x) \propto \log P(y) + \sum_{i=1}^{n}\log P(x_i \mid y)
$$

---

# Common Variants

## Gaussian Naive Bayes
* For continuous features, assume:

$$
x_i \mid y=c \sim \mathcal{N}(\mu_{ic}, \sigma_{ic}^2)
$$

* Estimate mean and variance per class-feature pair.

## Multinomial Naive Bayes
* Best for count features (for example bag-of-words).
* Uses term frequencies and class-conditional token probabilities.

## Bernoulli Naive Bayes
* Best for binary features (feature present/absent).
* Models each feature as Bernoulli conditioned on class.

---

# Naive Bayes In Practice

## When to Use Naive Bayes

* When you need a simple, fast baseline classifier.
* When features are high-dimensional and sparse (for example text).
* When training data is limited.
* When interpretability of probabilistic reasoning is useful.

## When Not to Use Naive Bayes

* When feature dependencies are strong and central to the task.
* When probability calibration is critical without post-calibration.
* When nonlinear interactions dominate predictive signal.
* When richer models clearly outperform and latency budget allows them.

## Practical Notes

### Efficient for baseline deployment

* Naive Bayes trains and serves quickly with low memory overhead.

### Assumption mismatch can hurt performance

* If likelihood assumptions differ from data reality, calibration and accuracy may degrade.

### Tune smoothing strength

* The Laplace parameter $\alpha$ can significantly change rare-feature behavior.

### Compute in log space

* Log-probability arithmetic helps avoid numerical underflow in long feature vectors.
