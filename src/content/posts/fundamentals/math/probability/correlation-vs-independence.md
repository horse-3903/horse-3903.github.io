---
title: Correlation vs Independence
published: 2026-02-16
description: "Math fundamentals note for IOAI ML preparation."
tags: ["Mathematics Fundamentals", "Probability"]
category: IOAI ML Notes
draft: false
access: public
---
# Syllabus Map

* Study map: [Syllabus Study Map](/posts/syllabus/ioai-study-map/)

---

# Core Idea

* Correlation captures linear association.
* Independence means full probabilistic non-influence.

## Key Point

* Independence implies zero correlation (under finite variance), but not the reverse.

## Why This Matters for ML

* Feature engineering and model assumptions often confuse correlation with independence.
* Spurious correlations can mislead interpretation and degrade robustness.
* Independence assumptions appear in simplified models and require careful validation.
* This distinction helps prevent incorrect causal or predictive conclusions.