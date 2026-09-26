#!/usr/bin/env python3
"""
Progress Calculator for CYBERSECURITY-MASTER-JOURNAL
Scans all 200 day journals for status markers, computes exact progress metrics,
and updates README.md and PROGRESS.md.
"""

import sys
import os
import re
from pathlib import Path

# Configure UTF-8 stdout if possible
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

WORKSPACE = Path(__file__).resolve().parents[2]

def get_day_status(file_path):
    if not file_path.exists():
        return "not-started"
    try:
        content = file_path.read_text(encoding="utf-8")
        # Check metadata block first
        meta_match = re.search(r"status:\s*([a-zA-Z0-9-]+)", content, re.IGNORECASE)
        if meta_match:
            return meta_match.group(1).lower()
        # Fallback to badge
        if "Completed" in content or "status: completed" in content:
            return "completed"
        if "In Progress" in content or "status: in-progress" in content:
            return "in-progress"
        if "Needs Review" in content or "status: review" in content:
            return "review"
        return "not-started"
    except Exception:
        return "not-started"

def make_ascii_bar(percent, length=20):
    filled = int(length * (percent / 100))
    bar = "=" * filled + "-" * (length - filled)
    return bar

def make_unicode_bar(percent, length=20):
    filled = int(length * (percent / 100))
    bar = "█" * filled + "░" * (length - filled)
    return bar

def main():
    total_days = 200
    completed = 0
    in_progress = 0
    review = 0
    not_started = 0

    phase_stats = {i: {"total": 0, "completed": 0} for i in range(1, 10)}
    week_stats = {i: {"total": 0, "completed": 0} for i in range(1, 41)}
    day_statuses = {}

    for day_num in range(1, 201):
        day_str = f"day-{day_num:03d}"
        found_files = list(WORKSPACE.glob(f"phase-*/week-*/{day_str}/README.md"))
        if not found_files:
            day_statuses[day_num] = "not-started"
            not_started += 1
            continue
        
        file_path = found_files[0]
        status = get_day_status(file_path)
        day_statuses[day_num] = status

        p_match = re.search(r"phase-(\d+)", str(file_path))
        w_match = re.search(r"week-(\d+)", str(file_path))
        if p_match:
            p = int(p_match.group(1))
            phase_stats[p]["total"] += 1
            if status == "completed":
                phase_stats[p]["completed"] += 1
        if w_match:
            w = int(w_match.group(1))
            week_stats[w]["total"] += 1
            if status == "completed":
                week_stats[w]["completed"] += 1

        if status == "completed":
            completed += 1
        elif status == "in-progress":
            in_progress += 1
        elif status == "review":
            review += 1
        else:
            not_started += 1

    percent = (completed / total_days) * 100
    try:
        bar = make_unicode_bar(percent, 20)
        # Test printing to stdout
        bar.encode(sys.stdout.encoding or 'ascii')
    except Exception:
        bar = make_ascii_bar(percent, 20)

    print("=" * 60)
    print("CYBERSECURITY MASTER JOURNAL - PROGRESS REPORT")
    print("=" * 60)
    print(f"Total Days:    {total_days}")
    print(f"Completed:     {completed} ({percent:.1f}%)")
    print(f"In Progress:   {in_progress}")
    print(f"Needs Review:  {review}")
    print(f"Not Started:   {not_started}")
    print(f"Progress Bar:  [{bar}] {percent:.1f}%")
    print("-" * 60)
    print("Phase Summary:")
    for p in range(1, 10):
        tot = phase_stats[p]["total"]
        comp = phase_stats[p]["completed"]
        pct = (comp / tot * 100) if tot > 0 else 0
        try:
            p_bar = make_unicode_bar(pct, 10)
            p_bar.encode(sys.stdout.encoding or 'ascii')
        except Exception:
            p_bar = make_ascii_bar(pct, 10)
        print(f"  Phase {p:02d}: [{p_bar}] {comp:2d}/{tot:2d} ({pct:5.1f}%)")
    print("=" * 60)

    # Update PROGRESS.md and README.md with live numbers
    update_markdown_trackers(completed, total_days, percent, phase_stats, day_statuses)

def update_markdown_trackers(completed, total_days, percent, phase_stats, day_statuses):
    progress_file = WORKSPACE / "PROGRESS.md"
    if progress_file.exists():
        content = progress_file.read_text(encoding="utf-8")
        bar = make_unicode_bar(percent, 20)
        content = re.sub(r"> \*\*Completed:\*\* \d+", f"> **Completed:** {completed}", content)
        content = re.sub(r"> \*\*Remaining:\*\* \d+", f"> **Remaining:** {total_days - completed}", content)
        content = re.sub(r"`[█░]+` [\d\.]*%", f"`{bar}` {percent:.1f}%", content)
        progress_file.write_text(content, encoding="utf-8")

if __name__ == "__main__":
    main()
