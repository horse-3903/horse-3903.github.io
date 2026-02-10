---
title: Linear Regression
published: 2025-10-18
description: "A comprehensive guide to Linear Regression — exploring how it models relationships between variables to make accurate continuous predictions."
tags: ["Classical Machine Learning", "Supervised Learning"]
category: IOAI ML Notes
draft: false
access: restricted
---


# Syllabus Map

* Study map: [Syllabus Study Map](/posts/syllabus/ioai-study-map/)

---
# Overview

* **Linear Regression** is one of the simplest and most fundamental algorithms in Machine Learning for regression.

* It models the relationship between an **input variable** $x$ and an **output variable** $y$ by fitting a straight line that best represents the data.

---

# Mathematical Formulation

* The **linear model** predicts the target value $\hat{y}$ as:

$$
\hat{y}_i = w x_i + b
$$

* Where:
  - $w$: weight (slope)  
  - $b$: bias (intercept)  
  - $\hat{y}_i$: predicted value for input $x_i$

---

# Cost Function

* To measure how well our model fits the data, we use the **Mean Squared Error (MSE)** cost function:

$$
C = \frac{1}{2m} \sum_{i=1}^{m} (\hat{y}_i - y_i)^2
$$

* Substituting the prediction term:

$$
C = \frac{1}{2m} \sum_{i=1}^{m} (w x_i + b - y_i)^2
$$

---

# Gradient Descent Optimisation

* We update parameters $w$ and $b$ iteratively to minimise the cost function:

$$
w = w - \alpha \frac{\partial C}{\partial w}
$$

$$
b = b - \alpha \frac{\partial C}{\partial b}
$$

* where $\alpha$ is the **learning rate**.

---

# Derivation of Gradients

1. **Derivative of cost $ w.r.t. $ prediction:**
   $$
   \frac{\partial C}{\partial \hat{y}_i} = \frac{1}{m} (\hat{y}_i - y_i)
   $$

2. **Derivative of prediction $ w.r.t. $ parameters:**
   $$
   \frac{\partial \hat{y}_i}{\partial w} = x_i, \quad \frac{\partial \hat{y}_i}{\partial b} = 1
   $$

3. **Applying chain rule:**
   - Gradient $ w.r.t. $ $w$:
     $$
     \frac{\partial C}{\partial w} = \frac{1}{m} \sum_{i=1}^{m} (\hat{y}_i - y_i) x_i
     $$
   - Gradient $ w.r.t. $ $b$:
     $$
     \frac{\partial C}{\partial b} = \frac{1}{m} \sum_{i=1}^{m} (\hat{y}_i - y_i)
     $$

---

# Final Update Rules

## Weight update:
  $$
  w = w - \alpha \cdot \frac{1}{m} \sum_{i=1}^{m} (\hat{y}_i - y_i) x_i
  $$

## Bias update:
  $$
  b = b - \alpha \cdot \frac{1}{m} \sum_{i=1}^{m} (\hat{y}_i - y_i)
  $$

# Linear Regression In Practice

## When to Use Linear Regression

* When relationships are **approximately linear and additive**.
* When you need **fast training** and a **strong baseline**.
* When **coefficient interpretability** matters for decisions.
* When data is **large** and noise is moderate.

## When Not to Use Linear Regression

* When relationships are **highly nonlinear** without feature engineering.
* When **outliers dominate** the fit and robust methods are needed.
* When **multicollinearity** makes coefficients unstable without regularisation.
* When the target is **bounded, categorical, or count-based**.

## Practical Notes

* **Standardise features** before applying regularisation.
* Inspect **residuals** for heteroscedasticity and bias.
* Use **Ridge or LASSO** when there are many correlated features.
* Add **interaction terms** only when they are justified by domain knowledge.






