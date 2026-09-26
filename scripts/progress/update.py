#!/usr/bin/env python3
"""
scripts/progress/update.py — Scans all day journals, computes progress across phases,
weeks, and overall 200 days, and updates README.md, PROGRESS.md, and Week READMEs in place.
"""

import os
import sys
import json
import re

# Ensure UTF-8 output on Windows terminals
if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
CURRICULUM_PATH = os.path.join(ROOT_DIR, 'curriculum.json')
DAYS_DIR = os.path.join(ROOT_DIR, 'days')
README_PATH = os.path.join(ROOT_DIR, 'README.md')
PROGRESS_PATH = os.path.join(ROOT_DIR, 'PROGRESS.md')


def make_bar(pct, length=20, fill_char='█', empty_char='░'):
    filled = int(round((pct / 100.0) * length))
    filled = max(0, min(length, filled))
    return (fill_char * filled) + (empty_char * (length - filled))


def load_curriculum():
    with open(CURRICULUM_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_day_status(day_num):
    day_folder = os.path.join(DAYS_DIR, f"day-{day_num:03d}")
    readme_path = os.path.join(day_folder, 'README.md')
    if not os.path.exists(readme_path):
        return 'not-started'
    
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    for line in content.splitlines():
        line = line.strip().lower()
        if line.startswith('status:'):
            val = line.split(':', 1)[1].strip()
            if 'completed' in val:
                return 'completed'
            elif 'in-progress' in val or 'progress' in val:
                return 'in-progress'
            elif 'review' in val:
                return 'review'
            elif 'not-started' in val or 'not started' in val:
                return 'not-started'
    return 'not-started'


def calculate_metrics(curriculum):
    days_data = []
    
    total_completed = 0
    total_in_progress = 0
    total_review = 0
    total_not_started = 0
    
    current_active_day = None
    current_active_phase = None
    current_active_week = None
    
    phase_metrics = []
    week_metrics = []
    
    for phase in curriculum:
        pnum = phase['phase_num']
        ptitle = phase['phase_title']
        pid = phase.get('phase_id', f"phase-{pnum:02d}")
        
        phase_completed = 0
        phase_total = 0
        phase_in_progress = 0
        
        for week in phase.get('weeks', []):
            wnum = week['week_num']
            wtitle = week['week_title']
            wid = week.get('week_id', f"week-{wnum:02d}")
            
            week_completed = 0
            week_total = len(week.get('days', []))
            week_in_progress = 0
            week_review = 0
            
            for day in week.get('days', []):
                dnum = day['day_num']
                dtitle = day['title']
                dtier = day.get('tier', 'light')
                
                status = get_day_status(dnum)
                
                if status == 'completed':
                    total_completed += 1
                    phase_completed += 1
                    week_completed += 1
                elif status == 'in-progress':
                    total_in_progress += 1
                    phase_in_progress += 1
                    week_in_progress += 1
                elif status == 'review':
                    total_review += 1
                    week_review += 1
                else:
                    total_not_started += 1
                    
                phase_total += 1
                
                # Identify first active day
                if current_active_day is None and status in ['in-progress', 'review', 'not-started']:
                    current_active_day = (dnum, dtitle)
                    current_active_phase = (pnum, ptitle)
                    current_active_week = (wnum, wtitle)
                    
                days_data.append({
                    'day_num': dnum,
                    'title': dtitle,
                    'phase_num': pnum,
                    'phase_id': pid,
                    'week_num': wnum,
                    'week_id': wid,
                    'tier': dtier,
                    'status': status
                })
                
            week_pct = (week_completed / week_total * 100.0) if week_total > 0 else 0.0
            if week_completed == week_total and week_total > 0:
                week_status_str = "🟢 Completed"
            elif week_in_progress > 0 or week_completed > 0:
                week_status_str = "🟡 In Progress"
            elif week_review > 0:
                week_status_str = "🔴 Needs Review"
            else:
                week_status_str = "⚪ Not Started"
                
            week_metrics.append({
                'phase_num': pnum,
                'phase_id': pid,
                'week_num': wnum,
                'week_id': wid,
                'week_title': wtitle,
                'completed': week_completed,
                'total': week_total,
                'pct': week_pct,
                'status_str': week_status_str,
                'deliverable': week.get('deliverable', '')
            })
            
        phase_pct = (phase_completed / phase_total * 100.0) if phase_total > 0 else 0.0
        phase_metrics.append({
            'phase_num': pnum,
            'phase_title': ptitle,
            'phase_id': pid,
            'completed': phase_completed,
            'total': phase_total,
            'pct': phase_pct
        })
        
    total_days = len(days_data)
    overall_pct = (total_completed / total_days * 100.0) if total_days > 0 else 0.0
    
    if current_active_day is None and days_data:
        current_active_day = (days_data[-1]['day_num'], days_data[-1]['title'])
        current_active_phase = (phase_metrics[-1]['phase_num'], phase_metrics[-1]['phase_title'])
        current_active_week = (week_metrics[-1]['week_num'], week_metrics[-1]['week_title'])
        
    return {
        'total_days': total_days,
        'total_completed': total_completed,
        'total_in_progress': total_in_progress,
        'total_review': total_review,
        'total_not_started': total_not_started,
        'overall_pct': overall_pct,
        'current_active_day': current_active_day,
        'current_active_phase': current_active_phase,
        'current_active_week': current_active_week,
        'phase_metrics': phase_metrics,
        'week_metrics': week_metrics,
        'days_data': days_data
    }


def update_readme(metrics):
    if not os.path.exists(README_PATH):
        print(f"Warning: {README_PATH} not found.")
        return
        
    with open(README_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
        
    bar = make_bar(metrics['overall_pct'], length=20)
    act_day_num, act_day_title = metrics['current_active_day']
    act_pnum, act_ptitle = metrics['current_active_phase']
    act_wnum, act_wtitle = metrics['current_active_week']
    
    dashboard_block = f"""<!-- PROGRESS-DASHBOARD:START -->
```text
Overall Progress: [{bar}] {metrics['overall_pct']:.1f}%
Completed Days:   {metrics['total_completed']} / {metrics['total_days']}
In Progress:      {metrics['total_in_progress']}
Needs Review:     {metrics['total_review']}
Remaining:        {metrics['total_not_started']} Days
Current Phase:    Phase {act_pnum} — {act_ptitle}
Current Week:     Week {act_wnum:02d} — {act_wtitle}
Current Day:      Day {act_day_num:03d} — {act_day_title}
```
<!-- PROGRESS-DASHBOARD:END -->"""

    phase_lines = ["<!-- PHASE-PROGRESS:START -->"]
    deliverables = [
        "projects/project-01-security-lab-environment/README.md",
        "projects/project-02-web-pentest-report/README.md",
        "projects/project-03-corporate-ad-lab/README.md",
        "projects/project-04-cve-intelligence-pipeline/README.md",
        "projects/project-05-red-team-engagement-report/README.md",
        "projects/project-06-soc-detection-lab/README.md",
        "projects/project-07-malware-triage-forensics/README.md",
        "projects/project-08-personal-security-toolkit/README.md",
        "projects/project-09-purple-team-platform/README.md"
    ]
    
    deliv_titles = [
        "Multi-OS Security Lab Environment",
        "Web Security Lab & Pentest Report",
        "Corporate Active Directory Lab",
        "CVE Research & Intelligence Pipeline",
        "Full Red Team Engagement Report",
        "SOC & Detection Engineering Lab",
        "Malware Triage & Forensics Report",
        "Personal Security Toolkit in Rust",
        "Purple Team Security Operations Platform"
    ]
    
    weeks_ranges = [
        "Weeks 01–06", "Weeks 07–12", "Weeks 13–18", "Weeks 19–21",
        "Weeks 22–27", "Weeks 28–32", "Weeks 33–35", "Weeks 36–38", "Weeks 39–40"
    ]
    
    for i, pm in enumerate(metrics['phase_metrics']):
        p_bar = make_bar(pm['pct'], length=10)
        p_idx = pm['phase_num'] - 1
        d_link = deliverables[p_idx] if p_idx < len(deliverables) else ""
        d_name = deliv_titles[p_idx] if p_idx < len(deliv_titles) else "Capstone Deliverable"
        w_range = weeks_ranges[p_idx] if p_idx < len(weeks_ranges) else ""
        
        line = (f"* **[Phase {pm['phase_num']}: {pm['phase_title']}]({pm['phase_id']}/README.md)**  \n"
                f"  `[{p_bar}]` {pm['pct']:.1f}% ({pm['completed']} / {pm['total']} Days) • {w_range} • Deliverable: [{d_name}]({d_link})")
        phase_lines.append(line)
        
    phase_lines.append("<!-- PHASE-PROGRESS:END -->")
    phase_block = "\n".join(phase_lines)
    
    # Replace dashboard block
    if "<!-- PROGRESS-DASHBOARD:START -->" in content and "<!-- PROGRESS-DASHBOARD:END -->" in content:
        content = re.sub(
            r'<!-- PROGRESS-DASHBOARD:START -->.*?<!-- PROGRESS-DASHBOARD:END -->',
            dashboard_block,
            content,
            flags=re.DOTALL
        )
    else:
        # Fallback regex replace for older README format
        content = re.sub(
            r'```text\s*\nOverall Progress:.*?\n```',
            dashboard_block,
            content,
            flags=re.DOTALL
        )
        
    # Replace phase progress block
    if "<!-- PHASE-PROGRESS:START -->" in content and "<!-- PHASE-PROGRESS:END -->" in content:
        content = re.sub(
            r'<!-- PHASE-PROGRESS:START -->.*?<!-- PHASE-PROGRESS:END -->',
            phase_block,
            content,
            flags=re.DOTALL
        )
    else:
        # Pattern replace
        content = re.sub(
            r'(### 🏆 Phase Progress Breakdown\s*\n\s*)(?:(\* \*\*\[Phase \d+:.*?\n)+)',
            r'\1' + phase_block + '\n\n',
            content
        )
        
    with open(README_PATH, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"[✓] Updated {README_PATH}")


def update_progress_md(metrics):
    bar = make_bar(metrics['overall_pct'], length=20)
    
    # Generate Phase table rows
    phase_rows = []
    for pm in metrics['phase_metrics']:
        pbar = make_bar(pm['pct'], length=10)
        status_badge = "🟢 Completed" if pm['pct'] == 100.0 else ("🟡 In Progress" if pm['completed'] > 0 else "⚪ Not Started")
        row = f"| [Phase {pm['phase_num']:02d}: {pm['phase_title']}]({pm['phase_id']}/README.md) | `{pbar}` {pm['pct']:.1f}% | {pm['completed']} / {pm['total']} | {status_badge} |"
        phase_rows.append(row)
    phase_table_text = "\n".join(phase_rows)
    
    # Generate Days table rows
    day_rows = []
    badge_map = {
        'completed': '🟢 Completed',
        'in-progress': '🟡 In Progress',
        'review': '🔴 Needs Review',
        'not-started': '⚪ Not Started'
    }
    
    for d in metrics['days_data']:
        badge = badge_map.get(d['status'], '⚪ Not Started')
        tier_tag = f"`[{d['tier'].upper()}]`"
        day_str = f"Day {d['day_num']:03d}"
        link = f"[**{day_str}**](days/day-{d['day_num']:03d}/README.md)"
        w_link = f"[W{d['week_num']:02d}]({d['phase_id']}/{d['week_id']}/README.md)"
        p_link = f"[P{d['phase_num']:02d}]({d['phase_id']}/README.md)"
        row = f"| {badge} | {link} | {d['title']} | {tier_tag} | {w_link} | {p_link} |"
        day_rows.append(row)
    day_table_text = "\n".join(day_rows)
    
    progress_content = f"""# 📊 MASTER PROGRESS TRACKER

> **Master Plan:** 40 Weeks • 200 Days • 9 Core Deliverables  
> **Status:** {badge_map.get('completed' if metrics['overall_pct'] == 100.0 else ('in-progress' if metrics['total_completed'] > 0 else 'not-started'))}  
> **Last Synchronized:** Dynamically calculated by `scripts/progress/update.py`

---

## 📈 Executive Summary

```text
╔══════════════════════════════════════════════════════════════════════════════╗
║ TOTAL DAYS: 200      COMPLETED: {metrics['total_completed']:<3}      IN PROGRESS: {metrics['total_in_progress']:<3}     NEEDS REVIEW: {metrics['total_review']:<3}  ║
║ REMAINING: {metrics['total_not_started']:<3}      OVERALL PROGRESS: [{bar}] {metrics['overall_pct']:>5.1f}% ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

---

## 🏆 Phase Progress Breakdown

| Phase | Progress Bar | Days Completed | Status |
| :--- | :--- | :--- | :--- |
{phase_table_text}

---

## 🔗 Related In-Progress Tracks & Unified Architecture

> **Master Umbrella Plan:** This **CYBERSECURITY MASTER LEARNING JOURNAL** (40 Weeks / 200 Days) serves as the primary master curriculum covering foundations, offensive operations, detection engineering, malware forensics, and tool engineering.

To ensure efficient cross-referencing and eliminate duplicate note-taking, two parallel in-progress tracks are maintained and referenced rather than re-copied:

| In-Progress Track | Primary Scope | Current Status | Integration with Master Journal |
| :--- | :--- | :--- | :--- |
| **VAPT Training Curriculum** | Hands-on vulnerability assessment, web exploitation, network pen-testing | 🟡 **Phase 4 in Progress** | Deepens Phase 2 (Web & Recon) and Phase 3 (Internal PrivEsc). Lab notes and PoCs are cross-linked. |
| **90-Day AWS Cloud Security** | AWS Certified Security - Specialty (**SCS-C03**), IAM architecture, GuardDuty, KMS | 🟡 **Active Roadmap** | Expands Phase 2 (Cloud Recon) and Phase 9 (Hybrid Capstone). AWS infrastructure notes are referenced. |

---

## 📅 Master 200-Day Tracking Table

| Status | Day | Day Title | Tier | Week | Phase |
| :---: | :--- | :--- | :---: | :---: | :---: |
{day_table_text}

---

[🔙 Back to Master Dashboard](README.md) | [🗺️ Master Roadmap](ROADMAP.md) | [📚 Sources](SOURCES.md)
"""
    with open(PROGRESS_PATH, 'w', encoding='utf-8') as f:
        f.write(progress_content)
        
    print(f"[✓] Updated {PROGRESS_PATH}")


def update_week_readmes(metrics):
    badge_symbol = {
        'completed': '🟢',
        'in-progress': '🟡',
        'review': '🔴',
        'not-started': '⚪'
    }
    
    for wm in metrics['week_metrics']:
        pid = wm['phase_id']
        wid = wm['week_id']
        week_readme_path = os.path.join(ROOT_DIR, pid, wid, 'README.md')
        
        if not os.path.exists(week_readme_path):
            continue
            
        with open(week_readme_path, 'r', encoding='utf-8') as f:
            w_content = f.read()
            
        bar = make_bar(wm['pct'], length=20)
        
        # Update Status line
        w_content = re.sub(
            r'> \*\*Status:\*\* [^\n]+',
            f"> **Status:** {wm['status_str']}",
            w_content
        )
        # Update Progress line
        w_content = re.sub(
            r'> \*\*Progress:\*\* `[^`]+` \d+\.?\d*%\s*\(\d+\s*/\s*\d+\s*Days Completed\)',
            f"> **Progress:** `{bar}` {wm['pct']:.0f}% ({wm['completed']} / {wm['total']} Days Completed)",
            w_content
        )
        
        # Update checkboxes for days in this week
        for d in metrics['days_data']:
            if d['phase_id'] == pid and d['week_id'] == wid:
                dnum = d['day_num']
                st = d['status']
                check_char = 'x' if st == 'completed' else ' '
                symbol = badge_symbol.get(st, '⚪')
                tier_badge = f"`[{d['tier'].upper()}]`"
                
                # Replace schedule line
                pattern = rf'- \[[ x]\] \[. Day {dnum:03d}: [^\]]+\]\(\.\./\.\./days/day-{dnum:03d}/README\.md\)\s*(?:`\[(LIGHT|FULL)\]`)?'
                replacement = f"- [{check_char}] [{symbol} Day {dnum:03d}: {d['title']}](../../days/day-{dnum:03d}/README.md) {tier_badge}"
                w_content = re.sub(pattern, replacement, w_content)
                
        with open(week_readme_path, 'w', encoding='utf-8') as f:
            f.write(w_content)
            
    print("[✓] Updated all 40 Week READMEs.")


def main():
    curriculum = load_curriculum()
    metrics = calculate_metrics(curriculum)
    
    print("=" * 60)
    print("  CYBERSECURITY MASTER LEARNING JOURNAL — PROGRESS RECOMPUTE")
    print("=" * 60)
    print(f"Total Days:     {metrics['total_days']}")
    print(f"Completed:      {metrics['total_completed']} ({metrics['overall_pct']:.1f}%)")
    print(f"In Progress:    {metrics['total_in_progress']}")
    print(f"Needs Review:   {metrics['total_review']}")
    print(f"Not Started:    {metrics['total_not_started']}")
    print("-" * 60)
    
    update_readme(metrics)
    update_progress_md(metrics)
    update_week_readmes(metrics)
    print("=" * 60)
    print("Progress recalculation completed successfully.")


if __name__ == '__main__':
    main()
