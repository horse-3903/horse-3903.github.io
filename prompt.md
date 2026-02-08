# ML Guide Template

Use this as the standard structure for ML‑related guides. Keep it consistent across documents.

## Frontmatter
- Include a complete frontmatter block.
- Use the site’s conventions for `title`, `published`, `description`, `tags`, `category`, and `draft`.
- Use today’s date for new posts.

## Required Sections (Order Matters)
1. **Syllabus Map**
   - Add the study‑map link:
     - `* Study map: [Syllabus Study Map](/posts/syllabus/ioai-study-map/)`
2. **Overview**
   - 2–4 bullets summarising what the topic is and why it matters.
3. **Core Idea**
   - High‑level summary only (no step‑by‑step details).
   - 2–4 bullets.
4. **How It Works**
   - Step‑by‑step breakdown.
   - Each step is a **Heading 3** (`### Step N: ...`).
   - Each step includes:
     - 2–5 bullet points.
     - Clear math where helpful (LaTeX).
   - Explain notation inline or add a brief **Notation** list if needed.
5. **Objective / Formula (if applicable)**
   - Include the main objective function or key equations.
6. **Practical Notes**
   - Pros/cons, limitations, and when to use.
   - Prefer bullets.

## Writing Style
- British English.
- Concise, technical, and structured.
- Use bold sparingly for key terms.
- Keep math readable; prefer short equations over long derivations.

## Formatting Rules
- Use Markdown headings.
- Do not add nested bullet lists.
- Keep bullets single‑level.
- Keep blank lines between sections.

## Example Skeleton
```md
---
title: Title
published: YYYY-MM-DD
description: "Short description."
tags: ["Tag1", "Tag2"]
category: Notes
draft: false
---

# Syllabus Map

* Study map: [Syllabus Study Map](/posts/syllabus/ioai-study-map/)

---

# Overview

* ...

---

# Core Idea

* ...

---

# How It Works

### Step 1: ...
* ...

### Step 2: ...
* ...

---

# Objective / Formula

$$
...
$$

---

# Practical Notes

* ...
```
