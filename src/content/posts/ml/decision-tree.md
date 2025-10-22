---
title: Decision Tree
published: 2025-10-22
description: "A comprehensive guide to Decision Trees — exploring how they recursively split data to model complex decision boundaries for classification and regression tasks."
tags: ["Machine Learning", "<Subtopic>"]
category: Notes
draft: False
---

# Introduction

## Overview

## Overall Goals
* Recursively split dataset until pure leaf node obtained
* Means that there is only one class in each node

---

# Structure of a Decision Tree

## Root Node

* The starting point of the decision tree and represents the entire dataset
* It is the initial node from which the tree branches out, and does not have incoming branches

## Decision Node

* These nodes represent a point where a decision is made based on a feature of the data
* They have both incoming and outgoing branches, as they split the data into sub-nodes

## Leaf Node

* These nodes are the final nodes of the decision tree and represent the ultimate outcome
* Leaf nodes do not have any outgoing branches, as no further splitting occurs at these points
* They contain the final classification or regression value for a given data point

## Parent Node

* This is a relative term, referring to any node that splits into two or more child nodes.

## Child Node

* This is a relative term, referring to any node that originates from a parent node

---

# Training Algorithm

## Step-by-Step Procedure

### 1. Start with the full training dataset at the root node
* All samples and their labels are considered together.

### 2. Check if the node should stop splitting:
* All samples belong to one class, or
* The stopping condition is met.

#### For each feature:
* Evaluate all possible split points.

#### For numeric features:
* Sort unique values.
* Compute midpoints between consecutive values.
* Each midpoint = potential threshold

#### For categorical features:
* Consider subsets of categories or one-hot encodings.

### 3. Compute the impurity or loss for each possible split:

* Use Entropy / Information Gain or Gini Index (for classification).

* Use Mean Squared Error (for regression).

### 4. Select the split with the best score:

* Highest information gain or lowest impurity.

* Record the chosen feature and threshold.

### 5. Partition the dataset into child nodes:

* Left node → samples satisfying the condition

* Right node → samples not satisfying it

### 7. Repeat recursively for each child node:

* Treat each child as a new dataset.

* Apply the same splitting logic.

* Stop when leaf conditions are met.

## Recursive Splitting Logic
* The process is **greedy**: it chooses the best split at each step, not globally optimal.

* The resulting tree can easily overfit, which is why pruning is necessary.

* Real implementations (like CART) use binary splits only.

---

# Splitting Criteria

## Information Gain

* Information Gain is applied to quantify which feature provides maximal information about classification based on **entropy**
* The intention is decreasing the **entropy** initiating from the root node to the leaf nodes.

Given the set of values in a parent node $ S $ which is split into child nodes $ S_L $ and $ S_R  $ :

$$
IG(S, t) = H(S) - \frac{|S_L|}{|S|}H(S_L) - \frac{|S_R|}{|S|}H(S_R)
$$

Where:
* $ H(S) $ = entropy before split
* $ H(S_L), H(S_R) $ = entropy of left/right subsets
* $ |S|, |S_L|, |S_R| $ = number of samples in the parent and child nodes

## Entropy

* The entropy of a random variable quantifies the **average level of uncertainty** with the variable's potential states
* Essentially, it is the **measurement of the impurity or randomness in the data points**

Given a variable $ y $ having the discrete states $ \mathcal{y} \in [0, 1] $ contained in the set $ S $ : 

$$
H(S) = - \sum_{y \space \in \space \mathcal{S}} p(y) \space \log p(y)
$$

## GINI impurity

* Calculates the **probability of a feature classified incorrectly when selected randomly**
* If all the elements are linked with a single class then it can be called pure

Given a variable  $ y $  having the discrete states $ \mathcal{y} \in [0, 1] $  contained in the set $ S $ :

$$
H(S) = 1 - \sum_{y \space \in \space \mathcal{S}} (p(y))^2
$$

## Mean Squared Loss (MSE)

* Regular regression-based MSE over a set $ S $

Given the set of values in a parent node $ S $

$$
\text{MSE}(S) = \frac{1}{|S|} \sum_{(x, y_S) \in S} (y - \bar y_S)^2
$$

Where: 
$$
\text{(average) } \bar y_S = \frac{1}{|S|} \sum_{(x, y_S) \in S} y
$$

---

# Data Splitting (CART)

| **Feature Type** | **Split Condition** | **Split Decision** | **Example Condition** |
| --- | --- | --- | --- |
| **Numeric / Continuous** | x < t  or  x > t  | - Sort all unique values of (x) <br>- Compute midpoints between consecutive values <br>- Each midpoint = possible threshold (t) | `Age < 32.5` |
| **Ordered Categories** | rank(x) < t  | - Map categories to ranks <br>- Treat as numeric thresholds | `EducationLevel ≤ 2` |
| **Binary Categorical** |  x = v  | - Single split into {v} vs. {not v} | `IsStudent = Yes` |
| **Multi-Categorical** | x ∈ S  or  x ∉ S | - Enumerate all possible subsets S of categories <br>- Often one-hot encode and treat as binary features | `Color ∈ {Red, Blue}` |
| **Boolean** | x < 0.5  or  x ≥ 0.5 | - Treated as numeric with only one possible threshold | `IsWeekend < 0.5` |

---

# Stopping Condition

* Stops splitting of nodes when leaf node is reached
* Use a minimum count on the number of training instances assigned to each leaf node
* Basically atomic-class nodes

---

# Pruning Branches

## Goals of Pruning

* Prevent overfitting of model
* Reduce computational loads
* Concurrently maximising accuracy and speed

## Pre-Pruning (Early Stopping)

* **Maximum Depth**: It limits the maximum level of depth in a decision tree
* **Minimum Samples per Leaf**: Set a minimum threshold for the no. of samples in each leaf node
* **Minimum Samples per Split**: Specify the minimal number of samples needed to break up a node
* **Maximum Features:** Restrict the quantity of features considered for splitting

## Post-Pruning (Reducing Nodes)

* **Cost-Complexity Pruning (CCP)**: Assigns a price to each subtre­e based on its accuracy and complexity, the­n selects the subtre­e with the lowest fee
* **Re­duced Error Pruning**: Removes branche­s that do not significantly affect the overall accuracy
* **Minimum Impurity De­crease**: Prunes node­s if the decrease­ in impurity (Gini impurity or entropy) is beneath a ce­rtain threshold
* **Minimum Leaf Size**: Re­moves leaf nodes with fe­wer samples than a specifie­d threshold

---

# Variants of Decision Tree Algorithms

## Iterative Dichotomiser 3 (ID3)
* **Splitting Criterion**: Information Gain / Entropy.
* **Output**: Classification ($ \bar y $).

* **Feature Handling**:
    * Works primarily with categorical features.
    * Does not handle continuous variables directly.

* **Pruning**: None.

* **Limitation**: Biased toward features with many unique values.

## Base Cases
Applicable when deciding whether to stop the algorithm

Given the set of values in a parent node $ S $ and unique class label $ \bar y $ to the node, 
$$
\text{ID3}(S) =
\begin{cases}
    \text{if } \exists\, \bar{y} \text{ s.t. } \forall (x, y) \in S,\, y = \bar{y}
    &\Rightarrow\; \text{return leaf with label } \bar{y}, \\

    \text{else if } \exists\, \bar{x} \text{ s.t. } \forall (x, y) \in S,\, x = \bar{x}
    &\Rightarrow\; \text{return leaf with } 
        \begin{cases}
            \text{mode}(y), \text{ for classification} \\
            \text{mean}(y), \text{ for regression}
        \end{cases} \\

    \text{else} 
    &\Rightarrow\; \text{continue splitting recursively}
\end{cases}
$$


### Case 1: All values of $ y $ in $ S $ is equal to $ \bar y $

* Node should be represented by $ \bar y $

### Case 2: No more attributes $ x $ to split the set $ S $

* Node should be represented by the most common occurence of $ y $, or
* Node should be represented by the mean of $ y $

## Recursive Case
Given feature $ f $ and threshold $ t $,
$$
S_L = \{ (x, y) \in S: x_f \le t \}
$$

$$
S_R = \{ (x, y) \in S: x_f \gt t \}
$$

## Key Limitation
Notice that ID3 picks a feature $ A $ in feature space $ \mathcal F $ which provides the maximum information gain of the set $ S $.

$$
A^* = \underset{A \in \mathcal F}{\arg \max} \space IG(S, A)
$$

However, if a feature has **many distinct values** splitting by that feature will produce **very many small subsets**.

Since information gain is calculated using the reduction in entropy of the set, for a **very small subset** $ S_v $ : 

$$
H(S_v) \approx 0
$$

Since the subset is **very pure**, meaning that the likelihood of predicting the classes is **very high**.

$$
IG(S, A) = H(S) - H(S_v) \approx H(S)
$$

The model sees feature $ A^* $ which is used to split the node is seen as *amazing* since it achieves maximum information gain.

However, the model is actually **overfitting** since it is *memorising* the individual examples in the training dataset.

## C4.5

## CART

---

# Bias-Variance Trade Off

## Effect of Tree Depth

## Overfitting vs. Underfitting

## Role of Pruning

--- 

# Inference and Predictions 

## Classification Trees

## Regression Trees

---

# Summary