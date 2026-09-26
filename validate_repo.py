"""
Validation and Consistency Checker for CYBERSECURITY-MASTER-JOURNAL
Verifies all 9 phases, 40 weeks, 200 curriculum days, tier allocations,
flat on-demand days structure, scripts, workflows, and link integrity.
"""

import sys
import os
import re
import json
from pathlib import Path

# Configure UTF-8 output
if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

WORKSPACE = Path(__file__).resolve().parent

errors = []
warnings = []

print("=" * 60)
print("RUNNING REPOSITORY VALIDATION & CONSISTENCY CHECK")
print("=" * 60)

# 1. Check Phases
phases = sorted(list(WORKSPACE.glob("phase-*")))
if len(phases) != 9:
    errors.append(f"Expected 9 phase directories, found {len(phases)}")
else:
    print(f"[PASS] Phase Count: 9/9 phases verified.")
for p in phases:
    if not (p / "README.md").exists():
        errors.append(f"Missing README.md in {p.name}")

# 2. Check Weeks
weeks = sorted(list(WORKSPACE.glob("phase-*/week-*")))
if len(weeks) != 40:
    errors.append(f"Expected 40 week directories, found {len(weeks)}")
else:
    print(f"[PASS] Week Count: 40/40 weeks verified.")
for w in weeks:
    if not (w / "README.md").exists():
        errors.append(f"Missing README.md in {w.name}")

# 3. Check Curriculum JSON
curr_file = WORKSPACE / "curriculum.json"
if not curr_file.exists():
    errors.append("curriculum.json not found!")
else:
    with open(curr_file, 'r', encoding='utf-8') as f:
        curr = json.load(f)
    total_days = 0
    light_days = 0
    full_days = 0
    seen_days = set()
    for p in curr:
        for w in p['weeks']:
            for d in w['days']:
                dnum = d['day_num']
                total_days += 1
                seen_days.add(dnum)
                tier = d.get('tier')
                if tier == 'light':
                    light_days += 1
                elif tier == 'full':
                    full_days += 1
                else:
                    errors.append(f"Day {dnum} has invalid or missing tier: {tier}")
                    
    if total_days != 200 or len(seen_days) != 200:
        errors.append(f"Expected 200 unique curriculum days, found {total_days} total, {len(seen_days)} unique")
    else:
        print(f"[PASS] Curriculum Database: 200/200 days verified ({light_days} Light, {full_days} Full).")

# 4. Check Flat Days Architecture & On-Demand Engine
days_dir = WORKSPACE / "days"
if not days_dir.exists():
    errors.append("days/ directory missing!")
elif not (days_dir / "README.md").exists():
    errors.append("days/README.md missing!")
else:
    print(f"[PASS] Flat Days Directory: verified.")

# Check Scaffolding & Progress Scripts
new_day_py = WORKSPACE / "scripts" / "new-day.py"
new_day_sh = WORKSPACE / "scripts" / "new-day.sh"
update_py = WORKSPACE / "scripts" / "progress" / "update.py"
cli_py = WORKSPACE / "scripts" / "progress" / "cli.py"

for s, desc in [(new_day_py, "scripts/new-day.py"),
                (new_day_sh, "scripts/new-day.sh"),
                (update_py, "scripts/progress/update.py"),
                (cli_py, "scripts/progress/cli.py")]:
    if not s.exists():
        errors.append(f"Missing script: {desc}")
    else:
        print(f"[PASS] Script: {desc} verified.")

# 5. Check GitHub Action Workflow
workflow_file = WORKSPACE / ".github" / "workflows" / "update-progress.yml"
if not workflow_file.exists():
    errors.append("Missing .github/workflows/update-progress.yml")
else:
    print(f"[PASS] GitHub Action Workflow: update-progress.yml verified.")

# 6. Check Project Deliverables
projects = list((WORKSPACE / "projects").glob("project-*"))
if len(projects) != 9:
    errors.append(f"Expected 9 project folders, found {len(projects)}")
else:
    print(f"[PASS] Deliverable Projects: 9/9 verified.")

# 7. Check Cheatsheets
cheatsheets = list((WORKSPACE / "cheatsheets").glob("*.md"))
if len(cheatsheets) < 12:
    errors.append(f"Expected 12 cheatsheets, found {len(cheatsheets)}")
else:
    print(f"[PASS] Reference Cheatsheets: {len(cheatsheets)} verified.")

# 8. Check Root Documents
for doc in ["README.md", "ROADMAP.md", "PROGRESS.md", "SOURCES.md", "CONTRIBUTING.md", "LICENSE"]:
    p = WORKSPACE / doc
    if not p.exists():
        errors.append(f"Missing root document: {doc}")
    else:
        print(f"[PASS] Root Document: {doc} verified.")

# 9. Verify Related Tracks Section in README.md and PROGRESS.md
for doc in ["README.md", "PROGRESS.md"]:
    txt = (WORKSPACE / doc).read_text(encoding='utf-8')
    if "Related In-Progress Tracks" not in txt or "VAPT Training Curriculum" not in txt or "AWS Cloud Security" not in txt:
        errors.append(f"Missing 'Related Tracks' section in {doc}")
    else:
        print(f"[PASS] Related Tracks Cross-Reference: verified in {doc}.")

# 10. Check Link Patterns in Week READMEs
link_errors = 0
for w in weeks:
    txt = (w / "README.md").read_text(encoding='utf-8')
    # Check that day links point to flat ../../days/day-XXX/README.md
    matches = re.findall(r'\(([^)]+day-\d+[^)]*)\)', txt)
    for m in matches:
        if not m.startswith("../../days/day-"):
            link_errors += 1
            errors.append(f"In {w.name}, link does not match flat days pattern: {m}")
if link_errors == 0:
    print(f"[PASS] Link Integrity: All week day links verified to flat days/ structure.")

print("=" * 60)
if errors:
    print(f"VALIDATION FAILED with {len(errors)} errors:")
    for e in errors:
        print(f"  [X] {e}")
    sys.exit(1)
else:
    print("ALL VALIDATION CHECKS PASSED PERFECTLY!")
    print("=" * 60)
