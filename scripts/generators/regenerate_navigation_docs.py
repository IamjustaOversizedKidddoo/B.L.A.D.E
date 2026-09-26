import json
import os
import sys

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
CURRICULUM_PATH = os.path.join(ROOT_DIR, 'curriculum.json')

with open(CURRICULUM_PATH, 'r', encoding='utf-8') as f:
    phases = json.load(f)

# 1. Regenerate all 40 Week READMEs
print("Regenerating 40 Week READMEs...")
for p in phases:
    pnum = p['phase_num']
    ptitle = p['phase_title']
    pid = p.get('phase_id', f"phase-{pnum:02d}")
    
    for w in p['weeks']:
        wnum = w['week_num']
        wtitle = w['week_title']
        wid = w.get('week_id', f"week-{wnum:02d}")
        
        week_dir = os.path.join(ROOT_DIR, pid, wid)
        os.makedirs(week_dir, exist_ok=True)
        
        light_count = sum(1 for d in w['days'] if d.get('tier') == 'light')
        full_count = sum(1 for d in w['days'] if d.get('tier') == 'full')
        
        day_lines = []
        for d in w['days']:
            dnum = d['day_num']
            dtitle = d['title']
            dtier = d.get('tier', 'light').upper()
            tier_badge = f"`[{dtier}]`"
            day_lines.append(f"- [ ] [⚪ Day {dnum:03d}: {dtitle}](../../days/day-{dnum:03d}/README.md) {tier_badge}")
        
        schedule_text = "\n".join(day_lines)
        tools_text = ", ".join([f"`{t}`" for t in w.get('tools', ['Standard Toolchain'])])
        concepts_text = "\n".join([f"* {c}" for c in w.get('major_concepts', [])])
        
        content = f"""# WEEK {wnum:02d} — {wtitle}

> **Phase:** [Phase {pnum:02d} — {ptitle}](../README.md)  
> **Status:** ⚪ Not Started  
> **Progress:** `░░░░░░░░░░░░░░░░░░░░` 0% (0 / {len(w['days'])} Days Completed)  
> **Curriculum Tiers:** {light_count} Light (Theory & Reading) • {full_count} Full (Hands-on Lab & Deliverable)

---

## 🎯 Weekly Objective
{w.get('objective', '')}

## 📅 Schedule of Days
{schedule_text}

---

## 🧰 Tools & Utilities
{tools_text}

## 🧠 Major Concepts
{concepts_text}

---

## 🔬 Weekly Hands-on Lab
**{w.get('weekly_lab', '')}**

## 📌 Week Deliverable
*{w.get('deliverable', '')}*

---

## 🔍 Weekly Review & Reflection
### Concepts Mastered
* [Notes on mastered concepts]

### Weak Areas & Topics Needing Review
* [List areas requiring additional focus]

---

[🔙 Back to Phase {pnum:02d}](../README.md) | [📊 Master Progress](../../PROGRESS.md) | [🗺️ Master Roadmap](../../ROADMAP.md)
"""
        with open(os.path.join(week_dir, 'README.md'), 'w', encoding='utf-8') as f:
            f.write(content)

print("40 Week READMEs generated successfully.")

# 2. Regenerate 9 Phase READMEs
print("Regenerating 9 Phase READMEs...")
for p in phases:
    pnum = p['phase_num']
    ptitle = p['phase_title']
    pid = p.get('phase_id', f"phase-{pnum:02d}")
    phase_dir = os.path.join(ROOT_DIR, pid)
    os.makedirs(phase_dir, exist_ok=True)
    
    total_days = sum(len(w['days']) for w in p['weeks'])
    total_light = sum(sum(1 for d in w['days'] if d.get('tier') == 'light') for w in p['weeks'])
    total_full = sum(sum(1 for d in w['days'] if d.get('tier') == 'full') for w in p['weeks'])
    
    week_lines = []
    for w in p['weeks']:
        wnum = w['week_num']
        wtitle = w['week_title']
        wid = w.get('week_id', f"week-{wnum:02d}")
        w_days = len(w['days'])
        w_light = sum(1 for d in w['days'] if d.get('tier') == 'light')
        w_full = sum(1 for d in w['days'] if d.get('tier') == 'full')
        week_lines.append(f"- [ ] **[Week {wnum:02d}: {wtitle}]({wid}/README.md)** — {w_days} Days ({w_light} Light, {w_full} Full) • Deliverable: *{w.get('deliverable', '')}*")
        
    weeks_text = "\n".join(week_lines)
    
    content = f"""# PHASE {pnum:02d} — {ptitle}

> **Phase Status:** ⚪ Not Started  
> **Progress:** `░░░░░░░░░░░░░░░░░░░░` 0% (0 / {total_days} Days Completed)  
> **Curriculum Composition:** {total_light} Light Days (Theory) • {total_full} Full Days (Labs/Deliverables)

---

## 🎯 Phase Objective
{p.get('phase_objective', 'Master the domains and competencies assigned to this phase.')}

---

## 📅 Weeks in Phase {pnum:02d}
{weeks_text}

---

## 📌 Major Deliverables in Phase {pnum:02d}
* {p.get('weeks', [{}])[-1].get('deliverable', 'Phase Capstone Deliverable')}

---

## 🧠 Core Competencies & Skills Acquired
* Systematic analysis across offensive and defensive workflows
* Reproducible lab setups and artifact verification
* Professional documentation and incident correlation

---

## 🏆 Phase Completion Criteria
- [ ] All {total_days} daily journals completed
- [ ] All weekly hands-on labs executed and evidence documented in `days/day-XXX/evidence/`
- [ ] Phase deliverable completed in `projects/`
- [ ] Technical review and interview questions completed

---

[🔙 Master Dashboard](../README.md) | [📊 Master Progress](../PROGRESS.md) | [🗺️ Master Roadmap](../ROADMAP.md)
"""
    with open(os.path.join(phase_dir, 'README.md'), 'w', encoding='utf-8') as f:
        f.write(content)

print("9 Phase READMEs generated successfully.")
