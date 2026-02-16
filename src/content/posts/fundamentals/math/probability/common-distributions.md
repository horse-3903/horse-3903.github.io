---
title: Common Distributions
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

* Bernoulli models binary outcomes.
* Binomial models count of successes.
* Gaussian models continuous noise and aggregate effects.

## Practical Notes

### Match distribution assumptions to data type.

* Wrong assumptions degrade calibration and fit quality.

## Why This Matters for ML

* Data-type-specific modeling assumptions map directly to distribution choices.
* Bernoulli/Binomial link to binary/count tasks; Gaussian assumptions appear in noise models.
* Losses like MSE and logistic loss have probabilistic interpretations via these distributions.
* Calibration and uncertainty interpretation depend on correct distributional modeling.