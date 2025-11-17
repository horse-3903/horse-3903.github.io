---
title: L1 and L2 Regularisation
published: 2025-11-15
description: "L1 and L2 Regularisation — all you need to know about programming concepts and packages"
tags: ["Machine Learning", "Supervised Learning"]
category: Notes
draft: false
---

# Introduction

## Limitations of Linear Regression
* The standard implementatioon of linear regression does not guarantee a generalisation of the model
* It is limited to the calculation of the empirical error (MSE) without:
  * Controlling the norm of the weight vector
  * Regularisation of the model
* This leads to poorer performance of the model for limited viable practical applications

## Use of Regularisation
* In order to mitigate these limitations, regularisation can be used to control the model
* Regularisation essentially adds an additional term to the error, which is minimised
* This leads to a new minimisation objective - the Regularised Loss Minimisation (RLM) - which outputs a hypothesis where: 

$$
\argmin_\bold{w}(L(\bold{w}) + R(\bold{w}))
$$

* Where: 
  * $ \bold w $ is the weight matrix,
  * $ L(\bold w) $ is the empirical loss from the weight matrix,
  * $ R(\bold w) $ is the regularised loss from the regularisation function.

# Stability
* A learning algorithm is stable if a small change of the input to the algorithm does not change the output of the algorithm by much.

## Example
* Let $ A $ be a training algorithm, and $ S = {z_1, z_2, z_3, ... z_m} $ be the training set of $ m $ values.

* $ A(S) $ is the output of $ A $ after being trained.

* Given the training set $ S $ and additional datapoint $ z' $, let $ S^(i) $ be the training set after replacing the $ i\text{-th} $ element in $ S $ with  $ z' $.

* Linking to the example above, a "small change of the input" would correspond to using $ S^(i) $ instead of $ S^i $ in training $ A $.

* The effect of the change in one training sample would be comparing the loss of $ A(S) $ and $ A(S^(i)) $



# L1 Regularisation


# L2 Regularisation (Ridge Regression)
## Overview
* Ridge regression makes use of one of the simplest regularisation rules, which is defined as 

$$
R(\bold w) = \lambda ||\bold w||^2
$$

* Where:
  * $ \lambda $ is a scalar where $ \lambda > 0 $,
  * $ ||\bold w|| = \sqrt{\sum_{d}^{i=1} w_i^2}$ is the $ l_2 $ norm.

* Applying the learning rule with linear regression and mean-squared error (MSE) loss:
$$
\argmin_{\bold{w}} \bigg( \lambda||\bold w||^2 \space + \space \frac{1}{m} \sum_{i=1}^{N}\frac{1}{2}(\bold{w}_i x_i - y_i)^2 \bigg)
$$

