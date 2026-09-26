#!/usr/bin/env python3
"""
Day Updater CLI: Quickly change the status and checklists of a specific day journal.
Usage:
  python update_day.py 1 --status completed
  python update_day.py 1 --status in-progress
  python update_day.py 1 --status review
  python update_day.py 1 --status not-started
"""

import sys
import os
import re
from pathlib import Path
from datetime import datetime

# Ensure UTF-8 output
if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

WORKSPACE = Path(__file__).resolve().parents[2]
DAYS_DIR = WORKSPACE / "days"

STATUS_MAP = {
    "completed": ("🟢 **Completed**", "completed"),
    "in-progress": ("🟡 **In Progress**", "in-progress"),
    "review": ("🔴 **Needs Review**", "review"),
    "not-started": ("⚪ **Not Started**", "not-started")
}


def update_day(day_num, new_status):
    day_int = int(day_num)
    day_str = f"day-{day_int:03d}"
    day_dir = DAYS_DIR / day_str
    readme_path = day_dir / "README.md"
    
    # If day folder does not exist, scaffold it first
    if not readme_path.exists():
        print(f"[*] Day {day_num} not yet scaffolded. Scaffolding now...")
        scaffold_script = WORKSPACE / "scripts" / "new-day.py"
        import subprocess
        subprocess.run([sys.executable, str(scaffold_script), str(day_num)], check=True)
        
    if not readme_path.exists():
        print(f"[!] Error: Failed to find or scaffold Day {day_num} at {readme_path}")
        return False

    content = readme_path.read_text(encoding="utf-8")
    badge, status_key = STATUS_MAP.get(new_status.lower(), STATUS_MAP["not-started"])
    today_str = datetime.now().strftime("%Y-%m-%d")

    # Update frontmatter status
    content = re.sub(r"status:\s*[a-zA-Z0-9-]+", f"status: {status_key}", content)
    if status_key == "completed":
        content = re.sub(r'completed_date:\s*".*?"', f'completed_date: "{today_str}"', content)
        content = re.sub(r"completed_date:\s*.*", f'completed_date: "{today_str}"', content)
    else:
        content = re.sub(r'completed_date:\s*".*?"', 'completed_date: ""', content)
        content = re.sub(r"completed_date:\s*.*", 'completed_date: ""', content)

    # Update status section badge
    content = re.sub(
        r"## Status\s*\n[^\n]+\n",
        f"## Status\n{badge}  \n",
        content
    )

    # If completed, check off checklist items
    if status_key == "completed":
        content = re.sub(r"- \[ \] Theory", "- [x] Theory", content)
        content = re.sub(r"- \[ \] Core concepts", "- [x] Core concepts", content)
        content = re.sub(r"- \[ \] Commands", "- [x] Commands", content)
        content = re.sub(r"- \[ \] Conceptual review", "- [x] Conceptual review", content)
        content = re.sub(r"- \[ \] Lab scenario", "- [x] Lab scenario", content)
        content = re.sub(r"- \[ \] Evidence", "- [x] Evidence", content)
        content = re.sub(r"- \[ \] Interview questions", "- [x] Interview questions", content)
        content = re.sub(r"- \[ \] Security takeaway", "- [x] Security takeaway", content)
        content = re.sub(r"- \[ \] Review completed", "- [x] Review completed", content)

    readme_path.write_text(content, encoding="utf-8")
    print(f"[+] Day {day_num:03d} status set to: {status_key.upper()}")
    
    # Trigger progress update script
    update_script = WORKSPACE / "scripts" / "progress" / "update.py"
    if update_script.exists():
        import subprocess
        subprocess.run([sys.executable, str(update_script)], check=False)
        
    return True


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python update_day.py <day_number> --status <completed|in-progress|review|not-started>")
        sys.exit(1)

    d_num = sys.argv[1]
    status = "completed"
    if "--status" in sys.argv:
        idx = sys.argv.index("--status")
        if idx + 1 < len(sys.argv):
            status = sys.argv[idx + 1]

    update_day(d_num, status)
