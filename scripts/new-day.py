#!/usr/bin/env python3
"""
scripts/new-day.py — Scaffolds a single day folder on demand for CYBERSECURITY-MASTER-JOURNAL.

Usage:
    python scripts/new-day.py 42
    python scripts/new-day.py "START DAY 42"
    python scripts/new-day.py START DAY 42
    python scripts/new-day.py day-042
"""

import sys
import os
import re
import json

# Ensure UTF-8 output on Windows terminals
if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
CURRICULUM_PATH = os.path.join(ROOT_DIR, 'curriculum.json')
DAYS_DIR = os.path.join(ROOT_DIR, 'days')


def load_curriculum():
    if not os.path.exists(CURRICULUM_PATH):
        print(f"Error: Curriculum file not found at {CURRICULUM_PATH}")
        sys.exit(1)
    with open(CURRICULUM_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)


def parse_day_number(args):
    joined = " ".join(args).strip()
    match = re.search(r'\b(?:day[-_\s]*)?(\d{1,3})\b', joined, re.IGNORECASE)
    if match:
        day_num = int(match.group(1))
        if 1 <= day_num <= 200:
            return day_num
    print("Error: Could not extract a valid day number (1-200) from arguments:")
    print(f"       Arguments received: {args}")
    print("Usage examples:")
    print("  python scripts/new-day.py 42")
    print("  python scripts/new-day.py 'START DAY 42'")
    print("  python scripts/new-day.py day-042")
    sys.exit(1)


def find_day_data(curriculum, day_num):
    for phase in curriculum:
        for week in phase.get('weeks', []):
            for day in week.get('days', []):
                if day.get('day_num') == day_num:
                    return phase, week, day
    return None, None, None


def generate_light_template(phase, week, day):
    dnum = day['day_num']
    pnum = phase['phase_num']
    wnum = week['week_num']
    title = day['title']
    topics_list = "\n".join([f"* {t}" for t in day.get('topics', [])])
    
    phase_id = phase.get('phase_id', f"phase-{pnum:02d}")
    week_id = week.get('week_id', f"week-{wnum:02d}")
    
    return f"""---
day: {dnum}
phase: {pnum}
week: {wnum}
title: "{title}"
tier: light
status: not-started
completed_date: ""
---

# DAY {dnum:03d} — {title}

## Status
⚪ Not Started

> **Phase {pnum:02d}:** [{phase['phase_title']}](../../{phase_id}/README.md)  
> **Week {wnum:02d}:** [{week['week_title']}](../../{phase_id}/{week_id}/README.md)  
> **Tier:** 💡 **LIGHT (Core Foundations & Theory)**

---

## 🎯 Learning Objectives
{day.get('objectives', 'Master the foundational principles of this domain.')}

---

## 📚 Topics
{topics_list}

---

## 📝 Notes & Concepts
### Core Concepts
<!-- Write detailed technical notes explaining what you learned in paragraphs -->

### Concepts Understood
- 

### Concepts Needing Review
- 

---

## 💻 Commands & Code Reference
```bash
# Document key commands, syntax, and one-liners studied today
```

---

## 💡 What I Learned
<!-- Concise written summary of key insights and architectural understanding -->

---

## 🏁 Completion Checklist
- [ ] Theory & assigned readings completed
- [ ] Core concepts understood & documented
- [ ] Commands and syntax documented
- [ ] Conceptual review completed

---

[🔙 Back to Week {wnum:02d}](../../{phase_id}/{week_id}/README.md) | [📊 Master Progress](../../PROGRESS.md) | [🗺️ Master Roadmap](../../ROADMAP.md)
"""


def generate_full_template(phase, week, day):
    dnum = day['day_num']
    pnum = phase['phase_num']
    wnum = week['week_num']
    title = day['title']
    topics_list = "\n".join([f"* {t}" for t in day.get('topics', [])])
    tools_str = ", ".join([f"`{t}`" for t in week.get('tools', ['Standard Security Toolchain'])])
    
    phase_id = phase.get('phase_id', f"phase-{pnum:02d}")
    week_id = week.get('week_id', f"week-{wnum:02d}")
    
    return f"""---
day: {dnum}
phase: {pnum}
week: {wnum}
title: "{title}"
tier: full
status: not-started
completed_date: ""
---

# DAY {dnum:03d} — {title}

## Status
⚪ Not Started

> **Phase {pnum:02d}:** [{phase['phase_title']}](../../{phase_id}/README.md)  
> **Week {wnum:02d}:** [{week['week_title']}](../../{phase_id}/{week_id}/README.md)  
> **Tier:** 🔬 **FULL (Hands-on Lab & Deliverable Focus)**

---

## 🎯 Learning Objectives
{day.get('objectives', 'Execute hands-on exercises and analyze offensive/defensive tradecraft.')}

---

## 📚 Topics
{topics_list}

---

## 📝 Notes & Concepts
### Core Concepts
<!-- Write deep-dive architectural and theoretical notes -->

### Concepts Understood
- 

### Concepts Needing Review
- 

---

## 💻 Commands & Code Reference
```bash
# Document exact commands, scripts, parameters, and flags executed
```

---

## 🔬 Lab Walkthrough
### Objective & Scenario
{day.get('lab', 'Execute controlled security lab exercise and validate findings.')}

### Environment & Prerequisites
- Target / Environment:
- Tools Required: {tools_str}

### Execution Steps
1. 
2. 
3. 

### Expected Result vs. Actual Result
| Phase | Expected Output | Actual Output | Status |
| :--- | :--- | :--- | :--- |
| Execution | | | Pending |

### Security Observations & Defensive Telemetry
- **Events Generated:** 
- **Logs Inspected:** 

---

## 📁 Evidence & Artifacts
- [Screenshots](evidence/screenshots/)
- [Log Files](evidence/logs/)
- [Network Captures](evidence/pcaps/)

---

## ❓ Interview Questions & Answers
### Question 1: {day.get('interview_q', 'Explain the technical mechanics and detection vector for this topic.')}
**My Answer:**
<!-- Your detailed technical answer -->

---

## 🛠️ Mistakes & Troubleshooting
<!-- Document obstacles, syntax errors, or unexpected results encountered and how you solved them -->

---

## 🛡️ Security Takeaway (Attack vs. Defense)
- **Offensive Utility:** 
- **Defensive Detection & Mitigation:** 

---

## 📌 GitHub Deliverable
<!-- Description of the artifact, script, report, or configuration to commit -->

---

## 💡 What I Learned
<!-- Concise written summary of the day's practical outcomes -->

---

## 🏁 Completion Checklist
- [ ] Theory & concepts studied
- [ ] Lab scenario executed in authorized environment
- [ ] Evidence (screenshots/logs/pcaps) collected & linked
- [ ] Interview questions answered in depth
- [ ] Security takeaway (attack vs defense) documented
- [ ] Review completed

---

[🔙 Back to Week {wnum:02d}](../../{phase_id}/{week_id}/README.md) | [📊 Master Progress](../../PROGRESS.md) | [🗺️ Master Roadmap](../../ROADMAP.md)
"""


def scaffold_day(day_num):
    curriculum = load_curriculum()
    phase, week, day = find_day_data(curriculum, day_num)
    
    if not day:
        print(f"Error: Day {day_num} not found in curriculum database.")
        sys.exit(1)
        
    day_dir = os.path.join(DAYS_DIR, f"day-{day_num:03d}")
    tier = day.get('tier', 'light')
    
    if os.path.exists(day_dir):
        readme_path = os.path.join(day_dir, 'README.md')
        print(f"[!] Day folder already exists: {day_dir}")
        if os.path.exists(readme_path):
            with open(readme_path, 'r', encoding='utf-8') as f:
                content = f.read()
            # check status
            status = 'unknown'
            for line in content.splitlines():
                if line.startswith('status:'):
                    status = line.split(':', 1)[1].strip()
            print(f"    Current status: {status}")
            print(f"    Preserving existing files without modification.")
        return day_dir
        
    os.makedirs(day_dir, exist_ok=True)
    
    if tier == 'light':
        readme_content = generate_light_template(phase, week, day)
        with open(os.path.join(day_dir, 'README.md'), 'w', encoding='utf-8') as f:
            f.write(readme_content)
            
        with open(os.path.join(day_dir, 'notes.md'), 'w', encoding='utf-8') as f:
            f.write(f"# Day {day_num:03d} Notes: {day['title']}\n\n<!-- Document deep-dive theoretical notes here -->\n")
            
        with open(os.path.join(day_dir, 'commands.md'), 'w', encoding='utf-8') as f:
            f.write(f"# Day {day_num:03d} Commands: {day['title']}\n\n```bash\n# Key commands and syntax\n```\n")
            
    else:  # full tier
        readme_content = generate_full_template(phase, week, day)
        with open(os.path.join(day_dir, 'README.md'), 'w', encoding='utf-8') as f:
            f.write(readme_content)
            
        with open(os.path.join(day_dir, 'notes.md'), 'w', encoding='utf-8') as f:
            f.write(f"# Day {day_num:03d} Notes: {day['title']}\n\n<!-- Document deep-dive technical notes here -->\n")
            
        with open(os.path.join(day_dir, 'commands.md'), 'w', encoding='utf-8') as f:
            f.write(f"# Day {day_num:03d} Commands: {day['title']}\n\n```bash\n# Lab commands and syntax\n```\n")
            
        with open(os.path.join(day_dir, 'lab.md'), 'w', encoding='utf-8') as f:
            f.write(f"# Day {day_num:03d} Lab Walkthrough: {day['title']}\n\n## Scenario\n{day.get('lab', '')}\n\n## Step-by-Step Execution Guide\n1. \n2. \n")
            
        evidence_dir = os.path.join(day_dir, 'evidence')
        for sub in ['screenshots', 'logs', 'pcaps']:
            sdir = os.path.join(evidence_dir, sub)
            os.makedirs(sdir, exist_ok=True)
            with open(os.path.join(sdir, '.gitkeep'), 'w', encoding='utf-8') as f:
                pass

    print(f"[+] Successfully scaffolded Day {day_num:03d}: {day['title']}")
    print(f"    Tier:      {tier.upper()} ({'Theory & Concepts' if tier == 'light' else 'Hands-on Lab & Deliverable'})")
    print(f"    Phase:     Phase {phase['phase_num']:02d} ({phase['phase_title']})")
    print(f"    Week:      Week {week['week_num']:02d} ({week['week_title']})")
    print(f"    Location:  days/day-{day_num:03d}/")
    print(f"    Status:    ⚪ Not Started (status: not-started)")
    return day_dir


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python scripts/new-day.py <day_number>")
        print("       python scripts/new-day.py 'START DAY 42'")
        sys.exit(1)
        
    day_num = parse_day_number(sys.argv[1:])
    scaffold_day(day_num)
