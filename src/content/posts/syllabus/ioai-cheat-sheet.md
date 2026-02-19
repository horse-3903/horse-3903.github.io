---
title: IOAI ML Cheat Sheet
published: 2026-02-19
description: "One-page high-yield summary across classical ML, neural networks, computer vision, NLP, and audio."
tags: ["Syllabus", "Cheat Sheet", "Study Guide"]
category: IOAI ML Notes
draft: false
access: restricted
---
# Syllabus Map

* Study map: [Syllabus Study Map](/posts/syllabus/ioai-study-map/)

---

# Classical Machine Learning

## Supervised Learning

* **Linear Regression**: Predict continuous targets; optimize MSE; watch residual patterns.
* **Logistic Regression**: Predict class probabilities with sigmoid/softmax; optimize cross-entropy.
* **Naive Bayes**: Fast probabilistic classifier with conditional-independence assumption.
* **K-Nearest Neighbours**: Non-parametric local voting/regression; sensitive to scaling and distance metric.
* **Decision Tree**: Recursive feature splits; interpretable but high variance without pruning.
* **Support Vector Machines**: Max-margin classifier; kernels enable nonlinear boundaries.

## Regularisation & Ensembles

* **L1 & L2 Regularisation**: L1 drives sparsity; L2 smooth shrinkage; tune strength with cross-validation.
* **Ensemble Methods**: Bagging reduces variance; boosting reduces bias; diversity improves gains.

## Data Science

* **Data Science Fundamentals**: Define objective, data pipeline, validation protocol, and deployment constraints.
* **Evaluation Metrics**: Match metric to task/cost (accuracy, F1, ROC-AUC, PR-AUC, RMSE, etc.).
* **Validation Strategy**: Prevent leakage; choose holdout/stratified/time-aware splits.
* **Feature Engineering**: Encode domain priors via transformations, interactions, and robust preprocessing.
* **Data Processing**: Clean missing/noisy data, standardize formats, and ensure reproducibility.
* **Bias-Variance Tradeoff**: Underfit = high bias; overfit = high variance; regularization balances both.
* **Cross Validation and K-Fold**: Stable model selection under limited data.

## Dimensionality Reduction

* **PCA**: Orthogonal projection maximizing variance; linear, global, efficient.
* **t-SNE & UMAP**: Nonlinear neighborhood-preserving visualization; avoid over-interpreting global geometry.

## Clustering

* **K-Means**: Minimize WCSS with centroid updates; best for compact, roughly spherical clusters.
* **DBSCAN/Hierarchical/Spectral**:
  * DBSCAN finds density-based clusters + outliers.
  * Hierarchical builds dendrograms without fixed k upfront.
  * Spectral uses graph Laplacian for non-convex structure.

---

# Neural Networks

## Core Architectures

* **Neural Networks**: Layered nonlinear function approximators trained by backpropagation.
* **MLP**: Fully connected feed-forward baseline for tabular and low-structure inputs.
* **RNN/LSTM/GRU**: Sequence models with hidden state; gating stabilizes long-term dependencies.

## Training and Optimization

* **Optimisers/Convergence/Regularisation**:
  * SGD(+momentum): often strong generalization.
  * Adam/AdamW: fast, stable defaults.
  * Convergence depends strongly on LR schedules and gradient health.
* **Pooling/BatchNorm/LayerNorm**:
  * Pooling downsamples representations.
  * BatchNorm stabilizes activations across batch.
  * LayerNorm stabilizes per sample (transformer standard).
* **Weight Initialisation**: Xavier/He keep activation/gradient scales controlled at startup.

## Representation and Adaptation

* **Data Embeddings**: Map inputs to dense vectors where similarity reflects semantics/structure.
* **Autoencoders**: Compress and reconstruct; useful for representation learning and anomaly detection.
* **Fine-tuning**: Adapt pretrained models with low LR, regularization, and forgetting-aware strategy.

---

# Computer Vision

## Core Vision Models

* **Convolutional Layers**: Local receptive fields + weight sharing for translation-aware feature extraction.
* **Pre-trained Vision Encoders**: Transfer visual features from large-scale pretraining.
* **CNN Tasks**:
  * Classification: label per image.
  * Detection: boxes + labels.
  * Segmentation: label per pixel.
* **R-CNN Family**: Two-stage detection; region proposals then classification/regression.
* **Vision Transformers**: Patch tokens + self-attention; strong with enough data/pretraining.

## Training and Representation

* **Image Augmentation**: Label-preserving transforms improve robustness and effective data size.
* **Self-Supervised Vision**: Learn strong visual features without labels (contrastive/masked pretext tasks).
* **Vision-Text Encoders**: Shared embedding spaces for zero-shot classification and retrieval.

## Generation

* **Image Generation**:
  * GANs: adversarial, fast sampling, instability risk (mode collapse).
  * Diffusion: denoise from noise, slower but high quality/diversity.

---

# NLP & Audio

## NLP Foundations and Tasks

* **Attention and Transformers**: Self-attention models token interactions at scale.
* **Text Classification**: Encode text, pool representation, classify with task head.
* **Pre-trained Text Encoders**: Contextual embeddings from MLM/contrastive objectives.

## Machine Translation and Seq2Seq

* **Machine Translation**: Encoder-decoder maps source sequence to target sequence.
* **Masked Language Modeling**: Predict masked tokens; core pretraining for encoder models.
* **Encoder-Decoder Models**: Cross-attention lets decoder read encoded source states.
* **Pre-trained Language Models**: Foundation LMs adapted via prompting/fine-tuning/instruction tuning.

## Audio

* **Pre-trained Audio Encoders**: Self/supervised speech-audio representations for transfer.
* **Audio Models**:
  * ASR (speech to text), classification, audio-language understanding, TTS/generation.

---

# Last-Minute Checklist

* Know task -> objective -> metric alignment.
* Distinguish training loss improvements from generalization improvements.
* Use robust validation design to avoid leakage.
* Start with strong baselines before complex models.
* Track both quality and latency/memory constraints.
