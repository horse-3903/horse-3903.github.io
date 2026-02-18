---
title: Pre-trained Language Models
published: 2026-02-16
description: "Open-source and API-based language model families."
tags: ["Natural Language Processing"]
category: IOAI ML Notes
draft: false
access: public
---
# Syllabus Map

* Study map: [Syllabus Study Map](/posts/syllabus/ioai-study-map/)

---
# Overview

* Pre-trained language models can be open-source or API-based.
* They are trained on large corpora and adapted via prompting, fine-tuning, or retrieval augmentation.

---

# Model Categories

## Base (Pretrained) Models

* Strong token prediction capabilities.
* Usually require task-specific tuning for best performance.

## Instruction-Tuned / Chat Models

* Further tuned on instruction-response data.
* Better at following natural language tasks out of the box.

## Reasoning-Optimized Variants

* Often tuned for multi-step problem solving.
* Trade some latency/cost for stronger complex-task behavior.

---

# Open-Source Families

* LLaMA family.
* Mistral family.
* Qwen family.
* Typical deployment options:
* full precision for maximum quality,
* quantized (for example 4-bit/8-bit) for lower memory and faster local inference.

---

# API-Based Models

* GPT-style APIs.
* Claude-style APIs.
* Managed APIs reduce infra burden and provide rapid model upgrades.
* Tradeoff is less control over model internals and serving environment.

---

# Selection Criteria

## Capability Fit

* Evaluate on your real tasks: summarization, extraction, coding, classification, etc.
* Match model size/context length to task difficulty and document length.

## Cost and Latency

* Measure end-to-end latency at target throughput.
* Include token pricing, retries, and context-window overhead.

## Safety and Governance

* Check prompt injection resistance, refusal behavior, and data handling requirements.
* Add policy layers and output filters for production.

## Deployment Constraints

* API model: fastest integration.
* Open-source model: more control, local/privacy-friendly, but higher ops complexity.

---

# Practical Adaptation Patterns

## Prompting Baseline

* Start with strong prompt templates and few-shot examples.
* Establish baseline before heavier adaptation.

## RAG (Retrieval-Augmented Generation)

* Retrieve relevant documents and append to context.
* Reduces hallucinations in domain-specific QA.

## Fine-Tuning

* Use supervised fine-tuning for style/task alignment.
* Prefer parameter-efficient methods (LoRA/QLoRA) when compute is limited.

---

# Practical Notes

## Choose based on latency, cost, and data constraints.

* In practice, choose based on latency, cost, and data constraints.
## Always evaluate on a held-out task set with failure-case slices.

* In practice, always evaluate on a held-out task set with failure-case slices.
## Track regression across model/version changes.

* In practice, track regression across model/version changes.




