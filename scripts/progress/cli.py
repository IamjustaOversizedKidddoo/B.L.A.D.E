#!/usr/bin/env python3
"""
Interactive & Command CLI for CYBERSECURITY-MASTER-JOURNAL
Usage:
  python cli.py status
  python cli.py complete <day_number>
  python cli.py start <day_number>
  python cli.py review <day_number>
  python cli.py reset <day_number>
  python cli.py open <day_number>
"""

import sys
import subprocess
from pathlib import Path

# Ensure UTF-8 output
if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

WORKSPACE = Path(__file__).resolve().parents[2]


def main():
    if len(sys.argv) < 2:
        print("CYBERSECURITY MASTER JOURNAL CLI")
        print("Commands:")
        print("  status                  - Show overall curriculum progress and update READMEs")
        print("  start <day>             - Scaffold (if needed) and mark day in-progress")
        print("  complete <day>          - Mark a day completed and update progress")
        print("  review <day>            - Mark a day needs-review")
        print("  reset <day>             - Reset a day to not-started")
        print("  open <day>              - Print file path of day README")
        sys.exit(0)

    cmd = sys.argv[1].lower()

    if cmd == "status":
        update_script = WORKSPACE / "scripts" / "progress" / "update.py"
        subprocess.run([sys.executable, str(update_script)])

    elif cmd in ["complete", "start", "review", "reset"]:
        if len(sys.argv) < 3:
            print(f"Usage: python cli.py {cmd} <day_number>")
            sys.exit(1)
        day_num = sys.argv[2]
        status_map = {
            "complete": "completed",
            "start": "in-progress",
            "review": "review",
            "reset": "not-started"
        }
        update_day_script = WORKSPACE / "scripts" / "progress" / "update_day.py"
        subprocess.run([sys.executable, str(update_day_script), str(day_num), "--status", status_map[cmd]])

    elif cmd == "open":
        if len(sys.argv) < 3:
            print("Usage: python cli.py open <day_number>")
            sys.exit(1)
        day_num = int(sys.argv[2])
        day_path = WORKSPACE / "days" / f"day-{day_num:03d}" / "README.md"
        if day_path.exists():
            print(f"[FOUND] {day_path}")
        else:
            print(f"[!] Day {day_num} not yet scaffolded. Run: python scripts/new-day.py {day_num}")

    else:
        print(f"Unknown command: {cmd}")


if __name__ == "__main__":
    main()
