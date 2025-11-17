---
title: Programming Fundamentals
published: 2025-11-14
description: "Fundamentals to Programming with Machine Learning — all you need to know about programming concepts and packages"
tags: ["Machine Learning", "Fundamentals"]
category: Notes
draft: false
---

# NumPy and Pandas for Data Handling

## Numpy
```py
import numpy as np
```

### Basic Arrays
```py
# Creating arrays
np.array([1, 2, 3])
np.array([[1, 2], [3, 4]])

# Array attributes
arr.shape
arr.ndim
arr.size
arr.dtype
```

### Shorthand Arrays
```py
# Zero/One Arrays
np.zeros((3 ,4))
np.ones((5,))

# Identity Matrix
np.eye(4)

# Range Array
np.arange(0, 10, 2)

# Random Array
np.random.seed(42)

np.random.rand(3, 4)     # uniform [0, 1)
np.random.randn(3, 4)    # normal (0, 1)
np.random.randint(0, 10, (3, 3))
```

### Selection and Indexing
```py
# Basic slicing
arr = np.arange(10)
arr[2:6]
arr[:5]
arr[::2]

# 2D slicing
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
A[0]
A[:,1]
A[1:, :2]

# Filtering
A[A > 5]
A[(A > 2) & (A < 8)]
```

### Vectorised Operations
```py
# Elementwise Operations
x + y
x - y
x * y
x / y
x ** 2
np.sqrt(x)

# Matrix Multiplication
x @ y
np.dot(x, y)
np.cross(x, y)

# Broadcasting
X + 3
X + np.array([1, 2, 3])  
```

### Statistics
```py
np.mean(X)
np.median(X)
np.std(X)
np.var(X)
np.min(X)
np.max(X)
np.percentile(X, 95)
```

### Linear Algebra
```py
np.linalg.norm(x)
np.linalg.dot(a,b)
np.linalg.inv(A)
np.linalg.det(A)
np.linalg.eig(A)
np.linalg.svd(A)
```

### Manipulating Arrays
```py
# Reshape
X.reshape(100, 3)

# Flatten
X.flatten()
X.ravel()

# Transpose
X.T

# Expand and Squeeze
np.expand_dims(X, axis=0)
np.squeeze(X)
```

### Stacking and Concatenation
```py
# Stacking
np.hstack([a, b])
np.vstack([a, b])

# Concatenation
np.concatenate([a, b], axis=1)
```

### ML-Specific
```py
# Standardisation
X_std = (X - X.mean(axis=0)) / X.std(axis=0)

# Min-max scaling
X_norm = (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0))

# One-hot encoding
np.eye(num_classes)[labels]
```

$$
\sigma(z) = \frac{1}{1 + e^{-z}}
$$

```py
# Sigmoid
res = 1 / (1 + np.exp(-z))
```

$$
\text{softmax}(z) = \frac{e^{z_i}}{\sum_{j}^{N} e^{z_j}}
$$

```py
# Softmax
exp = np.exp(z - np.max(z))
res = exp / exp.sum(axis=1, keepdims=True)
```

## Pandas

```py
import pandas as pd
```

### Reading Files
```py
# Read a .csv file
df = pd.read_csv("data.csv")

# Read a .xlsx file
df = pd.read_excel("data.xlsx", sheet_name="Sheet1")

# Read a .json file
df = pd.read_json("data.json")

# Read a .jsonl file
df = pd.read_json("data.jsonl", lines=True)

# Read a .parquet file
df = pd.read_parquet("file.parquet")
```

### Inspecting Data
```py
# Output top few rows
df.head()

# Output bottom few rows
df.tail()

# Output information about dataframe
df.info()
df.describe()
df.shape
df.columns
df.index

# Checking for null values
df.isna().sum()

# Checking for duplicates
df.duplicated().sum()

# Checking for unique values
df.nunique()
```

### Selecting Data
```py
# Selecting columns
df["col1"]
df[["col1", "col3"]]

# Selecting rows
df.iloc[2] # By index
df.loc[5] # By label

# Filtering rows
df[df['age'] > 30]
df[(df['age'] > 30) & (df['gender'] == 'M')]
df[df['col'].isin(['A', 'B'])]

# Query rows
df.query("age > 30 and gender == 'M'")
```

### Cleaning Data
```py
# Renaming columns
df.rename(columns={'old':'new'}, inplace=True)

# Dropping columns
df.drop(columns=['col1', 'col2'], inplace=True)

# Dropping rows 
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

# Filling with mean/median
df['age'] = df['age'].fillna(df['age'].mean())
df['age'] = df['age'].fillna(df['age'].median())

# Filling with mode
df['gender'] = df['gender'].fillna(df['gender'].mode()[0])

# Filling with forward or backward values
df.fillna(method='ffill')
df.fillna(method='bfill')
```

--- 

# Matplotlib and Seaborn for Visualisation

```py
import matplotlib.pyplot as plt
import seaborn as sns
```

## Matplotlib

### Figures
```py
# Create figure
plt.figure(figsize=(8, 5))
plt.plot(x, y, label="training loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Training Curve")
plt.legend()
plt.show()

# Create subplots
fig, ax = plt.subplots(2, 2, figsize=(10,8))
ax[0,0].plot(x1, y1)
ax[0,1].hist(x2, y2)
ax[1,0].hist(x3, y3)
ax[1,1].hist(x4, y4)

# Save figure
plt.savefig("chart.png", dpi=300)
```

### Plots
```py
# Line Plot
plt.plot(x, y, label="training loss")

# Scatter Plot
plt.scatter(df['age'], df['income'])

# Bar Chart
plt.bar(categories, values)

# Histogram
plt.hist(df['age'], bins=30)
```

## Seaborn
### Stylising
```python
# Changing palettes
sns.set_palette("viridis")

# Changing size
plt.figure(figsize=(10,4))

# Adding titles and axes
plt.title("Feature Distribution", fontsize=16)
plt.xlabel("Age", fontsize=12)
plt.ylabel("Density", fontsize=12)

# Adding grid
plt.grid(True)
```

### Single Variable Plots
```py
# Histogram
sns.histplot(df['age'], bins=30)

# KDE
sns.kdeplot(df['age'], shade=True)

# Count Plot
sns.countplot(data=df, x='gender')
```

### Two Variable Plots
```py
# Scatter Plot
sns.scatterplot(data=df, x='age', y='income')

# Regression Plot
sns.regplot(data=df, x='age', y='income')

# Joint Plot
sns.jointplot(data=df, x='age', y='income', kind='scatter')

# Hexbin Plot
sns.jointplot(data=df, x='age', y='income', kind='hex')
```

### Multi-Variable Plots
```py
# Pairplot (All pairwise plots)
sns.pairplot(df[['age','income','score']], hue='gender')

# Heatmap
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")

# Boxplot
sns.boxplot(data=df, x='gender', y='income')

# Violin Plot
sns.violinplot(data=df, x='gender', y='income')

# Swarmplot
sns.swarmplot(data=df, x='gender', y='income')
```
---

# Scikit-Learn for ML
```py
import sklearn
import sklearn.model_selection # Splitting, CV, Hyperparameter tuning
import sklearn.preprocessing   # Scaling, Encoding
import sklearn.impute          # Handle missing values
import sklearn.metrics         # Evaluation metrics
import sklearn.linear_model    # Linear models
import sklearn.tree            # Decision trees
import sklearn.ensemble        # Ensemble methods
import sklearn.svm             # SVM
import sklearn.neighbors       # K-NN
import sklearn.cluster         # KMeans
import sklearn.pipeline        # Chaining models and processing
import sklearn.compose         # Column Transformers
```

## Utility
```py
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

## Scaling
```py
# Standard scaler
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled  = scaler.transform(X_test)

# Minmax Scaler
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled  = scaler.transform(X_test)
```

---

# Pytorch Basics

---

# Tensor Manipulation

---

# Training Models on CPU and GPU

