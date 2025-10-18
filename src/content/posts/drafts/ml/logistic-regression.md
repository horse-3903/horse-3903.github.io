---
title: <Topic Name>
published: 2025-01-01
description: "<One-line summary of the note>"
tags: ["Machine Learning", "<Subtopic>"]
category: Notes
draft: true
---

# Logistic Regression

# Linear Function

Remember the function for linear regression:

Suppose you have a function $y = wx + b$, where $w$ is the gradient (slope) and $b$ is the $y$-intercept.

The model will also predict the given value $x$ with:

$$

\hat{y}_i = w x_i + b

$$

This regression model can be used for classification tasks when wrapped with normalisation functions — the Sigmoid function and Softmax function.

---

# Normalisation Functions

For **binary classification models**, a linear graph can be normalised using the **Sigmoid function**:

$$

\sigma(z) = \frac{1}{1 + e^{-z}}

$$

For **multi-class classification models**, multiple linear graphs can be normalised using **Softmax**:

$$
\sigma(\vec{z})_i = \frac{e^{z_i}}{\sum_{j=1}^{n} e^{z_j}}

$$

---

# Loss / Cost Function

In probability, in order to find the **maximum likelihood estimation** (MLE) of an event $y$ occurring given $x$, we compute the parameters $\theta = (w, b)$ 

For this first part, $\hat{y}_{\theta, i} = w x_i + b$  for the sake of conceptual understanding

## Single Data Point $x_i$

Probabilities of observing $y$ to be either $0$ or $1$ is given by :

$$

P(y_i = 1 \mid x_i, \theta) = \sigma(\hat{y}_{\theta, i}) = \sigma(w x_i + b)

$$

$$
P(y_i = 0 \mid x_i, \theta) = 1 - P(y_i = 0 \mid x_i, \theta)

$$

Combining these two probabilities, we observe that $y \in \{0, 1\}$ for all values of $x$, meaning that

$$
P(y_i \mid x_i, \theta) = (\sigma(\hat{y}_{\theta, i})^ {y_i}) (\sigma(1 - \hat{y}_{\theta, i}) ^ {(1 - y_i)})
$$

If $y_i = 0$, the term $\sigma(\hat{y}_{\theta, i})^{y_i}$ becomes 1, meaning that $P(y_i = 0 \mid x_i, \theta) = \sigma(1 - \hat{y}_{\theta, i}) ^ {(1 - y_i)}$

If $y_i = 1$, the term $\sigma(1 - \hat{y}_{\theta, i}) ^ {(1 - y_i)}$ becomes 1, meaning that $P(y_i = 1 \mid x_i, \theta) = \sigma( \hat{y}_{\theta, i}) ^ {y_i}$

## Entire Dataset $x$

For the entire dataset, the probability or “confidence”) of observing $y$ to be $0$ or $1$ is :

$$

P(y \mid x, \theta) = \prod_{i=1}^{n} P(y_i \mid x_i, \theta)

$$

In order to have the normalised value $\hat{y}$ to be as close to $y$ as possible, we have to maximise $\theta$ :

$$

\hat{\theta} = \arg\max_{\theta} \prod_{i=1}^{n} P(y_i \mid x_i, \theta)

$$

This can be simplified to a log summation by the product into a sum of log :

$$
\log P(y \mid x, \theta) = \log \left ( \prod_{i=1}^{n} P(y_i \mid x_i, \theta) \right ) = \sum_{i=1}^{n} \log P(y_i \mid x_i, \theta)
$$

$$

\hat{\theta} = \arg\max_{\theta} \sum_{i=1}^{n} \log P(y_i \mid x_i, \theta)

$$

$$
\log P(y \mid x, \theta) = \sum_{i=1}^{n} \bigg[ y_i \log \hat{y}_{\theta, i} +(1 - y_i) \log (1-\hat{y}_{\theta, i}) \bigg]
$$

Since loss/cost functions are usually minimised, we can rewrite the cost function $C(w, b)$ as :

$$
C(w, b) = - \log P(y \mid x, \theta) = - \sum_{i=1}^{n} \bigg[ y_i \log \hat{y}_{\theta, i} + (1 - y_i) \log {(1-\hat{y}_{\theta, i})} \bigg]
$$

## Relation to Cross Entropy Loss

For cross entropy loss, entropy from information theory measures the "uncertainty" of a distribution. 

Suppose you have two distributions, $p(x)$ being the true distribution of data points and $q(x)$ being the predicted distribution.

It tells us the average number of bits needed to encode samples from $p$ if we use a code optimised for $q$, essentially being how “far” the predicted distribution is from the true one :

$$
H(p, q) = - \sum_{i=1}^{n} p(x) \log q(x)
$$

---

# Gradient Update

Since we are training our model using the weights $w$ and $b$, we want to update as training goes on.

This is done using the **partial derivatives** of the cost function with respect to $w$ and $b$:

$$

w = w - \alpha \frac{\partial C}{\partial w}

$$

$$

b = b - \alpha \frac{\partial C}{\partial b}

$$

where $\alpha$ is the learning rate.

# Derivation of Gradient

For the gradient descent section, the following declarations hold for the cost and predicted value :

$$

\hat{y}_i = \sigma(w x_i + b)

$$

$$
C(w, b) = - \sum_{i=1}^{n} \left [ y_i \log \hat{y}_i + (1 - y_i) \log {(1-\hat{y}_i)} \right ]
$$

**1. Derivative of cost with respect to prediction $\hat{y}_i$ :**

$$
\frac{\partial C}{\partial \hat{y}_i}
= - \sum_{i=1}^{n} \left [ \frac{y_i}{\hat{y}_i} + (1 - y_i) \cdot \frac{-1}{1 - \hat{y}_i} \right ] = - \sum_{i=1}^{n} \left ( \frac{y_i}{\hat{y}_i} - \frac{1 - y_i}{1 - \hat{y}_i} \right )
$$

$$
\frac{\partial C}{\partial \hat{y}_i}
= - \sum_{i=1}^{n}  \frac{\hat{y}_i - y_i}{\hat{y}_i (1 - \hat{y}_i)}
$$

---

**2. Derivative of prediction with respect to sigmoid:**

$$
\hat{y}_i = \sigma(z) = \sigma(w x_i + b)
$$

$$

\frac{\partial \hat{y}_i}{\partial z} = \sigma(z) \space \cdot \space (1 - \sigma(z)) = \hat{y}_i \space \cdot \space (1 - \hat{y}_i)

$$

- For $w$ :
    
    $$
    
    \frac{\partial z}{\partial w} = x_i
    
    $$
    
    $$
    
    \frac{\partial \hat{y}_i}{\partial w} = \frac{\partial \hat{y}_i}{\partial z} \space \cdot \space \frac{\partial z}{\partial w} = x_i \hat{y}_i(1 - \hat{y}_i)
    $$
    
- For $b$:
    
    $$
    
    \frac{\partial z}{\partial b} = 1
    
    $$
    
    $$
    
    \frac{\partial \hat{y}_i}{\partial b} = \frac{\partial \hat{y}_i}{\partial z} \space \cdot \space \frac{\partial z}{\partial b} = \hat{y}_i(1 - \hat{y}_i)
    $$
    

---

**3. Chain rule application:**

- Gradient w.r.t. $w$:

$$

\frac{\partial C}{\partial w} = - \sum_{i=1}^{n} x_i \hat{y}_i(1 - \hat{y}_i) \frac{\hat{y}_i - y_i}{\hat{y}_i (1 - \hat{y}_i)}
$$

$$

\frac{\partial C}{\partial w} = - \sum_{i=1}^{n} x_i (\hat{y}_i - y_i)
$$

- Gradient w.r.t. $b$:

$$

\frac{\partial C}{\partial w} = - \sum_{i=1}^{n} \hat{y}_i(1 - \hat{y}_i) \frac{\hat{y}_i - y_i}{\hat{y}_i (1 - \hat{y}_i)}
$$

$$

\frac{\partial C}{\partial b} = - \sum_{i=1}^{n} (\hat{y}_i - y_i)
$$

---

# Final Gradient Update Rules

- Weight update:

$$

w = w + \alpha \cdot \sum_{i=1}^{n} x_i (\hat{y}_i - y_i)
$$

- Bias update:

$$

b = b + \alpha \cdot \sum_{i=1}^{n} (\hat{y}_i - y_i)

$$

## Actual Implementation

In actual implementation, we add the term $\frac{1}{m}$ for scaling, thus the negative log likelihood is :

$$
C(w, b) = - \frac{1}{m} \sum_{i=1}^{n} \left [ y_i \log \hat{y}_i + (1 - y_i) \log {(1-\hat{y}_i)} \right ]
$$