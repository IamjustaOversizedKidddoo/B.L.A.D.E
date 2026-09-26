import json

with open('curriculum.json', 'r', encoding='utf-8') as f:
    phases = json.load(f)

for p in phases:
    pnum = p['phase_num']
    ptitle = p['phase_title']
    print(f"\n=== Phase {pnum}: {ptitle} ===")
    for w in p['weeks']:
        wnum = w['week_num']
        wtitle = w['week_title']
        print(f"  Week {wnum:02d}: {wtitle}")
        for d in w['days']:
            dnum = d['day_num']
            dtitle = d['title']
            print(f"    Day {dnum:03d}: {dtitle}")
