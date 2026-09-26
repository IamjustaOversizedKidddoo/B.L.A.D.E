"""
Assemble curriculum from parts 1, 2, 3, and 4 into curriculum.json.
"""

import json
from pathlib import Path

# Part 1 and 2
p1_scope = {}
with open(r"d:\RED TEAMING\generate_curriculum_part1.py", "r", encoding="utf-8") as f:
    exec(f.read(), {}, p1_scope)
phases_1_2 = p1_scope["phases"]

# Part 2 (Phase 3)
p2_scope = {"phases": list(phases_1_2)}
with open(r"d:\RED TEAMING\generate_curriculum_part2.py", "r", encoding="utf-8") as f:
    exec(f.read(), {}, p2_scope)
phases_1_3 = p2_scope["phases"]

# Part 3 (Phases 4 and 5)
p3_scope = {}
with open(r"d:\RED TEAMING\generate_curriculum_part3.py", "r", encoding="utf-8") as f:
    exec(f.read(), {}, p3_scope)
phases_4_5 = p3_scope["phases_4_5"]

# Part 4 (Phases 6, 7, 8, 9)
p4_scope = {}
with open(r"d:\RED TEAMING\generate_curriculum_part4.py", "r", encoding="utf-8") as f:
    exec(f.read(), {}, p4_scope)
phases_6_9 = p4_scope["phases_6_9"]

all_phases = phases_1_3 + phases_4_5 + phases_6_9

print(f"[+] Total Phases: {len(all_phases)} (Expected: 9)")
total_weeks = sum(len(p["weeks"]) for p in all_phases)
print(f"[+] Total Weeks: {total_weeks} (Expected: 40)")
total_days = sum(len(w["days"]) for p in all_phases for w in p["weeks"])
print(f"[+] Total Days: {total_days} (Expected: 200)")

# Save to curriculum.json
output_file = Path(r"d:\RED TEAMING\curriculum.json")
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(all_phases, f, indent=2)

print(f"[SUCCESS] Complete curriculum JSON saved to {output_file}")
