---
title: Bias-Variance Decomposition
published: 2026-02-06
updated: 2026-02-06
description: "Notes on bias-variance decomposition for regression and classification based on mlxtend."
tags: ["Classical Machine Learning"]
category: Notes
draft: false
---

# Syllabus Map

* Study map: [Syllabus Study Map](/posts/syllabus/ioai-study-map/)

---

# Overview

* Bias and variance are commonly used to describe underfitting and overfitting behavior.
* Decomposing loss into bias and variance helps interpret model performance.

---

# Definitions (Expectation Over Training Sets)

* Let the true target be $y = f(x)$ and the prediction be $\hat{y} = h(x)$.
* Bias is the difference between the expected prediction and the true target.
* Variance measures how predictions vary around their expectation.
* Unless stated otherwise, the expectation is taken over different training sets.

---

# Squared Loss Decomposition (Regression)

* Squared loss: $S = (y - \hat{y})^2$.
* The expected squared loss decomposes into bias, variance, and a noise term (often called irreducible error). 

$$
E[(y - \hat{y})^2] = \big(y - E[\hat{y}]\big)^2 + E\big[(\hat{y} - E[\hat{y}])^2\big]
$$

---

# Total Error and Irreducible Error

* **Total error** (expected loss) can be viewed as:
  * **Bias** (systematic error from wrong assumptions),
  * **Variance** (error from sensitivity to training data),
  * **Irreducible error** (noise in the data that no model can remove). 
* In the squared-loss decomposition, the irreducible error is the noise term that is often omitted for simplicity. 

## Why Total Error = Bias^2 + Variance + Irreducible Error

Notation:
* $x$: input features
* $y$: true target
* $\hat{y}$: model prediction from a training set
* $f(x)$: true underlying function
* $\varepsilon$: noise term (unobserved randomness)
* $E[\cdot]$: expectation over different training sets

Assume the data-generating process:
$$
y = f(x) + \varepsilon, \quad E[\varepsilon] = 0, \quad Var(\varepsilon) = \sigma^2
$$

Then:
$$
E[(y - \hat{y})^2] = E[(f(x) + \varepsilon - \hat{y})^2]
$$

Expand the expectation:
$$
E[(y - \hat{y})^2] = E[(f(x) - \hat{y})^2] + E[\varepsilon^2]
$$

And decompose the first term:
$$
E[(f(x) - \hat{y})^2]
= (f(x) - E[\hat{y}])^2 + E[(\hat{y} - E[\hat{y}])^2]
$$

So:
* **Bias^2**: $(f(x) - E[\hat{y}])^2$
* **Variance**: $E[(\hat{y} - E[\hat{y}])^2]$
* **Irreducible error**: $E[\varepsilon^2] = \sigma^2$

Therefore:
$$
E[(y - \hat{y})^2] = \text{Bias}^2 + \text{Variance} + \text{Irreducible Error}
$$

---

# 0-1 Loss Decomposition (Classification)

* 0-1 loss uses the **mode** prediction as the “main prediction,” not the mean.
* Bias is $L(y, E[\hat{y}])$ and variance is $E[L(\hat{y}, E[\hat{y}])]$.
* Decomposing 0-1 loss is less straightforward and has multiple formulations.

---

# Practical Notes

* Bagging typically reduces variance compared to a single decision tree in the provided examples.
* For 0-1 loss, if bias is 1, increasing variance can reduce loss (a counterintuitive edge case).

