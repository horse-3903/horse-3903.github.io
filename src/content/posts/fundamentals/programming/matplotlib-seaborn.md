---
title: Matplotlib and Seaborn for Visualisation
published: 2026-02-16
description: "Core plotting workflows in Matplotlib and Seaborn for ML analysis."
tags: ["Programming Fundamentals"]
category: IOAI ML Notes
draft: false
access: public
---
# Syllabus Map

* Study map: [Syllabus Study Map](/posts/syllabus/ioai-study-map/)
* Programming hub: [Programming Fundamentals](/posts/fundamentals/programming/)

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

