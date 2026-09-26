"""
Validation and Consistency Checker for CYBERSECURITY-MASTER-JOURNAL
Verifies all 200 days, 40 weeks, 9 phases, links, and integrity.
"""

import sys
import os
import re
from pathlib import Path

# Configure UTF-8 output if possible
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

WORKSPACE = Path(r"d:\RED TEAMING")

errors = []
warnings = []

print("=" * 60)
print("RUNNING REPOSITORY VALIDATION & CONSISTENCY CHECK")
print("=" * 60)

# 1. Check Phases
phases = list(WORKSPACE.glob("phase-*"))
if len(phases) != 9:
    errors.append(f"Expected 9 phase directories, found {len(phases)}")
else:
    print(f"[PASS] Phase Count: 9/9 phases verified.")

# 2. Check Weeks
weeks = list(WORKSPACE.glob("phase-*/week-*"))
if len(weeks) != 40:
    errors.append(f"Expected 40 week directories, found {len(weeks)}")
else:
    print(f"[PASS] Week Count: 40/40 weeks verified.")

# 3. Check Days
days = sorted(list(WORKSPACE.glob("phase-*/week-*/day-*")), key=lambda p: str(p))
if len(days) != 200:
    errors.append(f"Expected 200 day directories, found {len(days)}")
else:
    print(f"[PASS] Day Count: 200/200 days verified.")

# Check day numbering 1 to 200 with no missing/duplicate days
day_nums = []
for d in days:
    match = re.search(r"day-(\d+)", d.name)
    if match:
        day_nums.append(int(match.group(1)))

day_nums_set = set(day_nums)
if len(day_nums_set) != 200:
    errors.append(f"Unique day numbers count: {len(day_nums_set)} / 200. Duplicates or gaps exist!")

missing_days = [n for n in range(1, 201) if n not in day_nums_set]
if missing_days:
    errors.append(f"Missing days: {missing_days}")
else:
    print(f"[PASS] Day Numbering: Sequence 1 to 200 is 100% complete and sequential.")

# Check day files
missing_files = []
for d in days:
    for expected in ["README.md", "notes.md", "commands.md", "lab.md"]:
        if not (d / expected).exists():
            missing_files.append(str(d / expected))
    if not (d / "evidence").is_dir():
        missing_files.append(str(d / "evidence"))

if missing_files:
    errors.append(f"Found {len(missing_files)} missing daily files (e.g. {missing_files[:5]})")
else:
    print(f"[PASS] Daily Files: All 200 days have README.md, notes.md, commands.md, lab.md, and evidence/.")

# 4. Check Projects
projects = list((WORKSPACE / "projects").glob("project-*"))
if len(projects) != 9:
    errors.append(f"Expected 9 projects, found {len(projects)}")
else:
    print(f"[PASS] Projects Count: 9/9 deliverables verified.")

# 5. Check Cheatsheets
cheatsheets = list((WORKSPACE / "cheatsheets").glob("*.md"))
if len(cheatsheets) != 12:
    errors.append(f"Expected 12 cheatsheets, found {len(cheatsheets)}")
else:
    print(f"[PASS] Cheatsheets Count: 12/12 reference guides verified.")

# 6. Check Core Files
core_files = ["README.md", "ROADMAP.md", "PROGRESS.md", "SOURCES.md", "CONTRIBUTING.md", "LICENSE", ".gitignore", "curriculum.json"]
for cf in core_files:
    if not (WORKSPACE / cf).exists():
        errors.append(f"Core file missing: {cf}")
    else:
        print(f"[PASS] Core File Present: {cf}")

# 7. Check Relative Links in Master Files
def check_links_in_file(file_path):
    content = file_path.read_text(encoding="utf-8")
    links = re.findall(r"\[.*?\]\((.*?)\)", content)
    broken = []
    for link in links:
        if link.startswith("http") or link.startswith("#") or link.startswith("mailto"):
            continue
        clean_link = link.split("#")[0]
        if not clean_link:
            continue
        target = (file_path.parent / clean_link).resolve()
        if not target.exists():
            broken.append((link, str(target)))
    return broken

broken_readme = check_links_in_file(WORKSPACE / "README.md")
if broken_readme:
    errors.append(f"Broken links in README.md: {broken_readme}")
else:
    print(f"[PASS] README.md Relative Links: 100% valid.")

broken_progress = check_links_in_file(WORKSPACE / "PROGRESS.md")
if broken_progress:
    errors.append(f"Broken links in PROGRESS.md: {broken_progress[:5]}")
else:
    print(f"[PASS] PROGRESS.md Relative Links: 100% valid.")

print("=" * 60)
if errors:
    print(f"[FAILED] Found {len(errors)} validation errors:")
    for err in errors:
        print(f"  [ERROR] {err}")
    sys.exit(1)
else:
    print("ALL VALIDATION CHECKS PASSED! 100% REPOSITORY INTEGRITY.")
    print("=" * 60)
