---
title: Linear Regression
published: 2025-10-18
description: "Understanding the core mechanics of linear regression — from hypothesis to gradient updates."
tags: ["Machine Learning", "Regression"]
category: Notes
draft: false
---

# 🧠 Overview

Linear Regression is one of the simplest and most fundamental algorithms in Machine Learning.  
It models the relationship between an **input variable** \( x \) and an **output variable** \( y \) by fitting a straight line that best represents the data.

---

# 🔢 Mathematical Formulation

The linear model predicts the target value \( \hat{y} \) as:

$$
\hat{y}_i = w x_i + b
$$

where:
- \( w \): weight (slope)  
- \( b \): bias (intercept)  
- \( \hat{y}_i \): predicted value for input \( x_i \)

---

# 📉 Cost Function

To measure how well our model fits the data, we use the **Mean Squared Error (MSE)** cost function:

$$
C = \frac{1}{2m} \sum_{i=1}^{m} (\hat{y}_i - y_i)^2
$$

Substituting the prediction term:

$$
C = \frac{1}{2m} \sum_{i=1}^{m} (w x_i + b - y_i)^2
$$

---

# 🔁 Gradient Descent Optimisation

We update parameters \( w \) and \( b \) iteratively to minimise the cost function:

$$
w = w - \alpha \frac{\partial C}{\partial w}
$$

$$
b = b - \alpha \frac{\partial C}{\partial b}
$$

where \( \alpha \) is the **learning rate**.

---

# 🧩 Derivation of Gradients

1. **Derivative of cost wrt prediction:**
   $$
   \frac{\partial C}{\partial \hat{y}_i} = \frac{1}{m} (\hat{y}_i - y_i)
   $$

2. **Derivative of prediction wrt parameters:**
   $$
   \frac{\partial \hat{y}_i}{\partial w} = x_i, \quad \frac{\partial \hat{y}_i}{\partial b} = 1
   $$

3. **Applying chain rule:**
   - Gradient wrt \( w \):
     $$
     \frac{\partial C}{\partial w} = \frac{1}{m} \sum_{i=1}^{m} (\hat{y}_i - y_i) x_i
     $$
   - Gradient wrt \( b \):
     $$
     \frac{\partial C}{\partial b} = \frac{1}{m} \sum_{i=1}^{m} (\hat{y}_i - y_i)
     $$

---

# ✅ Final Update Rules

- **Weight update:**
  $$
  w = w - \alpha \cdot \frac{1}{m} \sum_{i=1}^{m} (\hat{y}_i - y_i) x_i
  $$

- **Bias update:**
  $$
  b = b - \alpha \cdot \frac{1}{m} \sum_{i=1}^{m} (\hat{y}_i - y_i)
  $$

---

# 💡 Intuition & Insights

- The model adjusts \( w \) and \( b \) in the **opposite direction** of the gradient to reduce error.  
- Each iteration brings the line closer to the “best fit” that minimises the squared differences between predicted and true values.  
- Over time, the gradient becomes smaller as the model converges to the optimal parameters.

---

# 📈 Visualisation

TBC


# 🧭 Summary

- Linear Regression models data using a linear relationship.  
- The cost function is the **mean squared error**.  
- **Gradient Descent** is used to iteratively minimise the cost function by updating \( w \) and \( b \).  
- The final model approximates the best-fitting line through the data.

