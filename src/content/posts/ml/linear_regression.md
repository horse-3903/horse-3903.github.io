---
title: Linear Regression
published: 2025-10-18
description: "The inner workings of linear regression. "
tags: ["Machine Learning"]
category: Notes
draft: false
---

# Linear Regression

## Linear Function

Suppose you have a function $y = wx + b$, where $w$ is the gradient (slope) and $b$ is the $y$-intercept.

The model will predict the given value $\hat{y}$ with:

$$
\hat{y}_i = w x_i + b
$$

---

## Loss / Cost Function

The cost function for calculating the squared error between the predicted value $\hat{y}$ and true value $y$ is:

$$

C = \frac{1}{2m} \sum_{i=1}^{m} (\hat{y}_i - y_i)^2

$$

Expanded form:

$$

C = \frac{1}{2m} \sum_{i=1}^{m} (w x_i + b - y_i)^2

$$

---

## Gradient Update

Since we are training our model using the weights $w$ and $b$, we want to update as training goes on.

This is done using the **partial derivatives** of the cost function with respect to $w$ and $b$:

$$

w = w - \alpha \frac{\partial C}{\partial w}

$$

$$

b = b - \alpha \frac{\partial C}{\partial b}

$$

where $\alpha$ is the learning rate.

---

### Derivation of Gradients

**1. Derivative of cost with respect to prediction $\hat{y}_i$ :**

$$
\frac{\partial C}{\partial \hat{y}_i}
= \frac{\partial}{\partial \hat{y}_i} \Bigg[ \frac{1}{2m} \sum_{i=1}^{m} (\hat{y}_i - y_i)^2 \Bigg]
= \frac{1}{m} (\hat{y}_i - y_i)

$$

---

**2. Derivative of prediction with respect to weights:**

- For $w$ :
    
    $$
    
    \frac{\partial \hat{y}_i}{\partial w} = x_i
    
    $$
    
- For $b$:
    
    $$
    
    \frac{\partial \hat{y}_i}{\partial b} = 1
    
    $$
    

---

**3. Chain rule application:**

- Gradient w.r.t. $w$:

$$

\frac{\partial C}{\partial w} = \frac{1}{m} \sum_{i=1}^{m} (\hat{y}_i - y_i) x_i

$$

- Gradient w.r.t. $b$:

$$

\frac{\partial C}{\partial b} = \frac{1}{m} \sum_{i=1}^{m} (\hat{y}_i - y_i)

$$

---

### Final Gradient Update Rules

- Weight update:

$$

w = w - \alpha \cdot \frac{1}{m} \sum_{i=1}^{m} (\hat{y}_i - y_i) x_i

$$

- Bias update:

$$

b = b - \alpha \cdot \frac{1}{m} \sum_{i=1}^{m} (\hat{y}_i - y_i)

$$