import os
import shutil
import glob
import sys

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

# 1. Audit check: Ensure no non-template evidence or custom notes exist
nested_day_dirs = glob.glob(os.path.join(ROOT_DIR, 'phase-*', 'week-*', 'day-*'))
print(f"Found {len(nested_day_dirs)} nested day folders under phase-*/week-*/")

deleted_count = 0
for day_dir in nested_day_dirs:
    # Double check for custom evidence files
    for root, dirs, files in os.walk(day_dir):
        for f in files:
            if f not in ['.gitkeep', 'README.md', 'notes.md', 'commands.md', 'lab.md']:
                print(f"ERROR: Found unexpected user file: {os.path.join(root, f)}. Aborting!")
                sys.exit(1)
    # Safe to delete untouched template folder
    shutil.rmtree(day_dir)
    deleted_count += 1

print(f"Successfully deleted {deleted_count} untouched nested day template folders.")

# 2. Ensure days/ directory exists with master README.md
days_dir = os.path.join(ROOT_DIR, 'days')
os.makedirs(days_dir, exist_ok=True)

days_readme_path = os.path.join(days_dir, 'README.md')
with open(days_readme_path, 'w', encoding='utf-8') as f:
    f.write("""# 📅 Daily Learning Journals (`days/`)

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
""")

print(f"Created {days_readme_path}")
