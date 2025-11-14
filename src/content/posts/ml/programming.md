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

```

--- 

# Matplotlib and Seaborn for Visualisation

---

# Scikit-Learn for ML

---

# Pytorch Basics

---

# Tensor Manipulation

---

# Training Models on CPU and GPU

