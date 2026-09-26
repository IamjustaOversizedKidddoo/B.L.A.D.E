# 🤝 Contributing & Daily Study Protocol

This repository is maintained as an engineering-grade learning journal and technical portfolio covering 40 weeks (200 days) of advanced offensive operations, defensive engineering, security research, and systems programming.

---

## ⚡ Daily Study Workflow

The repository is built around a lean, on-demand workflow. Follow these five steps every learning day:

### 1. Scaffold the Day On-Demand
Day folders are not pre-generated in advance. When you are ready to start a day, run the scaffolding command:

```bash
# Using Python:
python scripts/new-day.py 1
python scripts/new-day.py "START DAY 42"

# Or using Bash / Zsh:
bash scripts/new-day.sh 1
bash scripts/new-day.sh "START DAY 42"
```

The script automatically selects the appropriate template tier from `curriculum.json`:
* 💡 **LIGHT Tier** (Objectives, Topics, Notes, Commands, What I Learned, Checklist) for core theory and reading days.
* 🔬 **FULL Tier** (Adds Lab Walkthrough, Evidence directory, Interview Q&A, Security Takeaways, Deliverable) for hands-on lab and capstone days.

### 2. Study & Document Notes
* Open `days/day-XXX/README.md`.
* Write conceptual insights in paragraphs in `## 📝 Notes & Concepts`.
* Document commands, flags, and syntax in `commands.md`.
* For lab-heavy days, follow `lab.md` to execute the scenario in your isolated environment.

### 3. Save Evidence & Artifacts (Full Tier)
* Save terminal logs in `days/day-XXX/evidence/logs/`.
* Save screen captures in `days/day-XXX/evidence/screenshots/`.
* Save network packet captures in `days/day-XXX/evidence/pcaps/`.

### 4. Mark Day Completed
When you have finished studying, answering interview questions, and completing the checklist:
* Edit the frontmatter in `days/day-XXX/README.md`:
  ```yaml
  status: completed
  completed_date: "YYYY-MM-DD"
  ```
* Or simply run via CLI:
  ```bash
  python scripts/progress/cli.py complete <day_number>
  ```

### 5. Commit and Push
Create a structured git commit adhering to conventional commits:
```bash
git add days/day-001/
git commit -m "docs: complete Day 001 TCP/IP architecture notes and Wireshark capture"
git push
```

---

## 🤖 Automated Progress Bar Recomputation

GitHub Markdown is static and does not run background code. To ensure the progress dashboard remains 100% accurate without manual effort:

### Automated CI/CD Trigger (GitHub Actions)
The repository includes `.github/workflows/update-progress.yml`.
* **When triggered:** On every `git push` to `main` or `master` containing changes to `days/**` or `curriculum.json`.
* **What it does:** Automatically runs `python scripts/progress/update.py`, recomputes completion metrics across all 9 phases, 40 weeks, and 200 days, rewrites the progress bars in `README.md`, `PROGRESS.md`, and Week READMEs in place, and commits the changes using `[skip ci]`.

### Manual Local Trigger
You can also manually recompute progress metrics locally at any time:
```bash
python scripts/progress/update.py
```

---

## 🔗 Related In-Progress Tracks Policy

This repository is the **overarching master umbrella**. Two parallel specialized tracks run concurrently:
1. **VAPT Training Curriculum (Currently Phase 4)**: Web, API, and network penetration testing.
2. **90-Day AWS Cloud Security Roadmap (Targeting SCS-C03)**: AWS cloud security, IAM, KMS, and GuardDuty.

### Cross-Referencing Rules:
* **Never duplicate notes:** If a topic in this journal overlaps with notes already written in your VAPT track or AWS Cloud Security track, **link out** to the other repository instead of rewriting identical material.
* **Maintain single source of truth:** Keep platform-specific lab outputs in their respective specialized tracks and reference their findings here.

---

## 🛡️ Journal Integrity & Ethical Boundary
1. **No Fabricated Progress:** Never mark a day completed if you have not studied the material and validated the concepts.
2. **Authorized Environments Only:** All lab work, packet captures, and exploit reproductions must occur inside private, isolated lab environments (e.g., host-only hypervisors, Docker containers, or authorized CTF ranges).
3. **Commit Cleanly:** Avoid committing binary blobs, credentials, or client data.
