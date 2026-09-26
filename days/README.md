# 📅 Daily Learning Journals (`days/`)

This directory houses all instantiated daily learning journals for the **CYBERSECURITY MASTER LEARNING JOURNAL** (40 Weeks / 200 Days).

---

## ⚡ On-Demand Scaffolding Architecture

In accordance with our lightweight engineering design:
* Day folders are **not** pre-generated in advance to avoid repository clutter.
* Individual days are scaffolded **on-demand** only when you begin studying that specific day.
* Each day automatically inherits the correct curriculum tier:
  * 💡 **LIGHT Tier** (Objectives, Topics, Notes, Commands, What I Learned, Checklist) for core theory and reading days.
  * 🔬 **FULL Tier** (Adds Lab Walkthrough, Evidence directory, Interview Q&A, Security Takeaways, Deliverable) for hands-on lab and capstone days.

---

## 🚀 How to Scaffold a Day

To scaffold any day (e.g. Day 001 or Day 042):

```bash
# Using Python:
python scripts/new-day.py 1
python scripts/new-day.py "START DAY 42"

# Or using Bash / Zsh:
bash scripts/new-day.sh 1
bash scripts/new-day.sh "START DAY 42"
```

---

## 📂 Instantiated Days
As you start days, they will appear here:
* `day-001/`
* `day-002/`
* ...

[🔙 Back to Master Dashboard](../README.md) | [🗺️ Master Roadmap](../ROADMAP.md) | [📊 Master Progress](../PROGRESS.md)
