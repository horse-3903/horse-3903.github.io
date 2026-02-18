---
title: Logistic Regression
published: 2026-02-16
description: "A comprehensive guide to Logistic Regression — exploring how it transforms Linear Regression into a powerful tool for binary and multi-class classification."
tags: ["Classical Machine Learning", "Supervised Learning"]
category: IOAI ML Notes
draft: false
access: public
---
# Syllabus Map

* Study map: [Syllabus Study Map](/posts/syllabus/ioai-study-map/)

---
# Overview

* Logistic Regression builds upon the foundation of **Linear Regression**.  

* While Linear Regression models continuous outcomes, Logistic Regression adapts the same linear model to **predict probabilities** for **classification tasks**.

---

# Preface: Relation to Linear Regression

* In Linear Regression, predictions are made using:

$$
\hat{y}_i = w x_i + b
$$

* However, such predictions are unbounded and not suitable for probabilities (which must lie between 0 and 1).
  
* To address this, Logistic Regression introduces **normalisation functions** that map the linear output to a probability space.

---

# Linear Function

* The base linear model used in Logistic Regression is identical to that of Linear Regression:

$$
\hat{y}_i = w x_i + b
$$

* This linear component serves as the **input (logit)** to the normalisation (activation) function.

---

# Normalisation Functions

* Normalisation functions map the unbounded linear output $z = w x + b$ into a constrained probability range.

## 1. Sigmoid Function (Binary Classification)

* For **binary classification**, we use the **Sigmoid** (or Logistic) function:

$$
\sigma(z) = \frac{1}{1 + e^{-z}}
$$

* This function ensures $0 < \sigma(z) < 1$, interpreting the output as the probability that a given input belongs to class $1$:

$$
\hat{y}_i = P(y_i = 1 \mid x_i, \theta) = \sigma(w x_i + b)
$$

## 2. Softmax Function (Multi-class Classification)

8 For **multi-class classification**, the **Softmax** function generalises the sigmoid to multiple outputs:

$$
\sigma(\vec{z})_i = \frac{e^{z_i}}{\sum_{j=1}^{n} e^{z_j}}
$$

* Softmax produces a vector of probabilities across all classes that sum to 1.

---

# Cost Function

* Logistic Regression is trained by **Maximum Likelihood Estimation (MLE)** — finding parameters $\theta = (w, b)$ that maximise the likelihood of the observed data.

## Maximum Likelihood Estimation (MLE)

### 1. Probability for a Single Data Point

* For a binary target $y_i \in \{0, 1\}$:

$$
P(y_i = 1 \mid x_i, \theta) = \sigma(w x_i + b)
$$

$$
P(y_i = 0 \mid x_i, \theta) = 1 - \sigma(w x_i + b)
$$

* We can express both cases compactly as:

$$
P(y_i \mid x_i, \theta) = (\hat{y}_i)^{y_i} (1 - \hat{y}_i)^{1 - y_i}
$$

---

### 2. Likelihood of the Entire Dataset

* Assuming independent samples:

$$
P(y \mid x, \theta) = \prod_{i=1}^{n} P(y_i \mid x_i, \theta)
$$

* We maximise this likelihood with respect to $\theta$:

$$
\hat{\theta} = \arg\max_{\theta} \prod_{i=1}^{n} P(y_i \mid x_i, \theta)
$$

* To simplify computation, we take the log of the likelihood:

$$
\log P(y \mid x, \theta) = \sum_{i=1}^{n} [y_i \log \hat{y}_i + (1 - y_i) \log (1 - \hat{y}_i)]
$$

* Since optimisation algorithms typically **minimise** functions, we take the negative log likelihood to obtain the **cost function**:

$$
C(w, b) = - \sum_{i=1}^{n} [y_i \log \hat{y}_i + (1 - y_i) \log (1 - \hat{y}_i)]
$$

---

## Relationship with Cross-Entropy Loss

* The Logistic Regression cost function is equivalent to **Cross-Entropy Loss**, which measures the dissimilarity between two probability distributions — the true labels $p(x)$ and predicted probabilities $q(x)$:

$$
H(p, q) = - \sum_{i=1}^{n} p(x_i) \log q(x_i)
$$

* In this context, minimising cross-entropy ensures the predicted probabilities closely match the true class labels.

---

# Gradient Descent Optimisation

* We optimise $w$ and $b$ using **Gradient Descent**, updating parameters iteratively to minimise the cost function:

$$
w = w - \alpha \frac{\partial C}{\partial w}
$$

$$
b = b - \alpha \frac{\partial C}{\partial b}
$$

* where $\alpha$ is the learning rate.

---

# Derivation of Gradients

* We start from:

$$
\hat{y}_i = \sigma(w x_i + b)
$$

$$
C(w, b) = - \sum_{i=1}^{n} [y_i \log \hat{y}_i + (1 - y_i) \log (1 - \hat{y}_i)]
$$

### 1. Derivative of Cost with Respect to Predictions

$$
\frac{\partial C}{\partial \hat{y}_i}
= - \left( \frac{y_i}{\hat{y}_i} - \frac{1 - y_i}{1 - \hat{y}_i} \right)
= \frac{\hat{y}_i - y_i}{\hat{y}_i(1 - \hat{y}_i)}
$$

### 2. Derivative of Predictions with Respect to Parameters

Since $\hat{y}_i = \sigma(z_i) = \sigma(w x_i + b)$:

$$
\frac{\partial \hat{y}_i}{\partial z_i} = \hat{y}_i (1 - \hat{y}_i)
$$

$$
\frac{\partial z_i}{\partial w} = x_i, \quad \frac{\partial z_i}{\partial b} = 1
$$

* Combining these equatons, we have:

$$
\frac{\partial \hat{y}_i}{\partial w} = x_i \hat{y}_i (1 - \hat{y}_i)
$$

$$
\frac{\partial \hat{y}_i}{\partial b} = \hat{y}_i (1 - \hat{y}_i)
$$

### 3. Applying the Chain Rule

- Gradient w.r.t. $w$:

$$
\frac{\partial C}{\partial w} = \sum_{i=1}^{n} (\hat{y}_i - y_i) x_i
$$

- Gradient w.r.t. $b$:

$$
\frac{\partial C}{\partial b} = \sum_{i=1}^{n} (\hat{y}_i - y_i)
$$

---

# Final Gradient Update Rules

- **Weight update:**

$$
w = w - \alpha \cdot \frac{1}{m} \sum_{i=1}^{n} (\hat{y}_i - y_i) x_i
$$

- **Bias update:**

$$
b = b - \alpha \cdot \frac{1}{m} \sum_{i=1}^{n} (\hat{y}_i - y_i)
$$

# Logistic Regression In Practice

## When to Use Logistic Regression

* When the decision boundary is roughly linear in feature space.
* When you need well-calibrated class probabilities.
* When interpretability of feature weights is important.
* When you have high-dimensional sparse features (e.g., text).

## When Not to Use Logistic Regression

* When class separation is highly nonlinear without feature engineering.
* When severe class imbalance is not handled by weighting or resampling.
* When label noise is high and margins are weak.
* When you need structured or sequence outputs.

## Practical Notes

### Standardise features and tune regularisation strength.

* In practice, standardise features and tune regularisation strength.
### Use class weights or decision thresholds to control precision and recall.

* In practice, use class weights or decision thresholds to control precision and recall.
### Prefer multinomial loss for multi-class problems when available.

* In practice, prefer multinomial loss for multi-class problems when available.
### Check calibration and use Platt scaling if needed.

* In practice, check calibration and use Platt scaling if needed.





