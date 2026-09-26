"""
Complete Curriculum Data & Repository Generator for CYBERSECURITY-MASTER-JOURNAL
Defines all 9 Phases, 40 Weeks, and 200 Days with precise curriculum topics,
lab scenarios, interview questions, and tools mapped to authoritative sources:
- PayloadsAllTheThings
- RedTeam-Tools
- BlueTeam-Tools
- Red-Team-Playbooks
- trickest/cve
- HackTricks
- Black Hat Rust
- Sliver
"""

import os
import sys
import json
from pathlib import Path

WORKSPACE_ROOT = Path(r"d:\RED TEAMING")

# Load curriculum definition generator
print("[*] Initializing full curriculum architecture...")
