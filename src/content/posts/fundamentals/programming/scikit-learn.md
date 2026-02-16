---
title: Scikit-Learn for ML
published: 2026-02-16
description: "Common scikit-learn imports and basic preprocessing/splitting workflows."
tags: ["Programming Fundamentals"]
category: IOAI ML Notes
draft: false
access: public
---
# Syllabus Map

* Study map: [Syllabus Study Map](/posts/syllabus/ioai-study-map/)
* Programming hub: [Programming Fundamentals](/posts/fundamentals/programming/)

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

