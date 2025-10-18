---
title: <Topic Name>
published: 2025-01-01
description: "<One-line summary of the note>"
tags: ["Machine Learning", "<Subtopic>"]
category: Notes
draft: true
---

# Decision Tree

# Overall Goals

- Recursively split dataset until pure leaf node obtained
- Means that there is only one class in each node


# Types of Nodes

## Root Node

- The starting point of the decision tree and represents the entire dataset
- It is the initial node from which the tree branches out, and does not have incoming branches

## Decision Node

- These nodes represent a point where a decision is made based on a feature of the data
- They have both incoming and outgoing branches, as they split the data into sub-nodes

## Leaf Node

- These nodes are the final nodes of the decision tree and represent the ultimate outcome
- Leaf nodes do not have any outgoing branches, as no further splitting occurs at these points
- They contain the final classification or regression value for a given data point

## Parent Node

- This is a relative term, referring to any node that splits into two or more child nodes.

## Child Node

- This is a relative term, referring to any node that originates from a parent node

---

# Loss Function

## Information Gain

- Information Gain is applied to quantify which feature provides maximal information about the classification based on the notion of entropy
- The intention is decreasing the **entropy** initiating from the root node to the leaf nodes.

## Entropy

![image.png](Decision%20Tree%2025de401a9d0a802c85eaf8421b0288a6/73d97bb4-fbb4-4cb1-bac8-efcb371262c3.png)

- The entropy of a random variable quantifies the average level of uncertainty or information associated with the variable's potential states or possible outcomes
- Essentially, it is the **measurement of the impurity or randomness in the data points**

Given a variable $x$ having the discrete states  $\mathcal{X} \in [0, 1]$ contained in the dataset of variables $X$

$$
H(X) = - \sum_{x \space \in \space \mathcal{X}} p(x) \space \log_{2} p(x)
$$

## GINI Index

- Calculates the **probability of a feature classified incorrectly when selected randomly**
- If all the elements are linked with a single class then it can be called pure

Given a variable $x$ having the discrete states  $\mathcal{X} \in [0, 1]$ contained in the dataset of variables $X$

$$
H(X) = 1 - \sum_{x \space \in \space \mathcal{X}} (p(x))^2
$$

---

# Data Splitting (CART)

| **Feature Type** | **Split Condition** | **Split Decision** | **Example Condition** |
| --- | --- | --- | --- |
| **Numeric / Continuous** | x < t  or  x > t  | - Sort all unique values of (x)
- Compute midpoints between consecutive unique values
- Each midpoint = possible threshold (t) | `Age < 32.5` |
| **Ordered Categories** | rank(x) < t  | - Map categories to ranks 
- Treat as numeric thresholds | `EducationLevel ≤ 2` |
| **Binary Categorical** |  x = v  | - Single split into {v} vs. {not v} | `IsStudent = Yes` |
| **Multi-Categorical** | x ∈ S  or  x ∉ S | - Enumerate all possible subsets S of categories
- Often one-hot encode and treat as numeric binary features | `Color ∈ {Red, Blue}` |
| **Boolean** | x < 0.5  or  x ≥ 0.5 | - Treated as numeric with only one possible threshold | `IsWeekend < 0.5` |

---

# Stopping Condition

- Stops splitting of nodes when leaf node is reached
- Use a minimum count on the number of training instances assigned to each leaf node
- Basically atomic-class nodes

---

# Pruning Branches

## Overall Goals

- Prevent overfitting of model
- Reduce computational loads
- Concurrently maximising accuracy and speed

## Pre-Pruning (Early Stopping)

- **Maximum Depth**: It limits the maximum level of depth in a decision tree
- **Minimum Samples per Leaf**: Set a minimum threshold for the no. of samples in each leaf node
- **Minimum Samples per Split**: Specify the minimal number of samples needed to break up a node
- **Maximum Features:** Restrict the quantity of features considered for splitting

## Post-Pruning (Reducing Nodes)

- **Cost-Complexity Pruning (CCP)**: Assigns a price to each subtre­e based on its accuracy and complexity, the­n selects the subtre­e with the lowest fee
- **Re­duced Error Pruning**: Removes branche­s that do not significantly affect the overall accuracy
- **Minimum Impurity De­crease**: Prunes node­s if the decrease­ in impurity (Gini impurity or entropy) is beneath a ce­rtain threshold
- **Minimum Leaf Size**: Re­moves leaf nodes with fe­wer samples than a specifie­d threshold