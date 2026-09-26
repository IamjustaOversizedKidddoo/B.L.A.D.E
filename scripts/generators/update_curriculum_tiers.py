import json
import sys

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

# Define day tier mappings
# Default pattern: In a 5-day week, Days 1-3 are LIGHT (theory/concepts), Days 4-5 are FULL (labs/tools).
# For specific lab-heavy or exercise weeks, more days are FULL.
# Deliverables / Capstones are always FULL.

full_days = {
    # Phase 1
    5, 9, 10, 14, 15, 19, 20, 24, 25, 27, 28, 29, 30,
    # Phase 2
    34, 35, 37, 38, 40, 42, 43, 44, 45, 47, 48, 50, 51, 53, 54, 55, 59, 60,
    # Phase 3
    62, 63, 64, 65, 67, 68, 69, 70, 74, 75, 76, 77, 79, 80, 82, 83, 84, 85, 87, 88, 89, 90,
    # Phase 4
    95, 98, 99, 100, 103, 104, 105,
    # Phase 5
    111, 113, 114, 115, 117, 118, 119, 120, 121, 122, 123, 124, 127, 128, 129, 130, 131, 132, 133, 135,
    # Phase 6
    137, 138, 139, 142, 144, 145, 147, 148, 149, 150, 152, 153, 154, 155, 157, 158, 160,
    # Phase 7
    165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175,
    # Phase 8
    180, 182, 183, 184, 185, 187, 188, 189, 190,
    # Phase 9
    193, 194, 195, 197, 198, 199, 200
}

with open('curriculum.json', 'r', encoding='utf-8') as f:
    phases = json.load(f)

light_count = 0
full_count = 0

for p in phases:
    for w in p['weeks']:
        for d in w['days']:
            dnum = d['day_num']
            tier = 'full' if dnum in full_days else 'light'
            d['tier'] = tier
            if tier == 'full':
                full_count += 1
            else:
                light_count += 1

with open('curriculum.json', 'w', encoding='utf-8') as f:
    json.dump(phases, f, indent=2, ensure_ascii=False)

print(f"Curriculum updated with tiers. Total days: {light_count + full_count}")
print(f"Light days (Theory/Concepts): {light_count}")
print(f"Full days (Hands-on Lab/Deliverable): {full_count}")
