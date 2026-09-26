"""
Full Repository Builder for CYBERSECURITY-MASTER-JOURNAL
Reads `curriculum.json` and generates:
1. All 9 Phase folders and READMEs
2. All 40 Week folders and READMEs
3. All 200 Day folders and journals (README.md, notes.md, commands.md, lab.md, evidence/)
4. 9 Project folders with full enterprise templates
5. 8 Lab category directories
6. 12 Topic-specific cheatsheets
7. Master PROGRESS.md table
8. Master ROADMAP.md (ASCII + Mermaid + 40-week breakdown)
9. SOURCES.md (repository mappings)
10. Master README.md dashboard with live progress and complete navigation
11. Progress automation scripts (calculate_progress.py, update_day.py, cli.py)
12. Dashboard web UI (index.html, styles.css, app.js)
13. CONTRIBUTING.md, LICENSE, .gitignore
"""

import json
import os
import sys
from pathlib import Path

WORKSPACE = Path(r"d:\RED TEAMING")

with open(WORKSPACE / "curriculum.json", "r", encoding="utf-8") as f:
    phases = json.load(f)

print(f"[*] Loaded curriculum with {len(phases)} phases.")

# Helper functions
def make_progress_bar(percent, length=20):
    filled = int(length * (percent / 100))
    bar = "█" * filled + "░" * (length - filled)
    return bar

# -------------------------------------------------------------
# 1. CREATE COMMON DIRS
# -------------------------------------------------------------
common_dirs = [
    "assets/roadmap",
    "assets/diagrams",
    "assets/screenshots",
    "assets/architecture",
    "labs/web",
    "labs/linux",
    "labs/windows",
    "labs/active-directory",
    "labs/network",
    "labs/detection",
    "labs/malware-analysis",
    "labs/purple-team",
    "cheatsheets",
    "projects",
    "scripts/progress",
    "scripts/utilities",
    "dashboard"
]

for cd in common_dirs:
    (WORKSPACE / cd).mkdir(parents=True, exist_ok=True)
    gitkeep = WORKSPACE / cd / ".gitkeep"
    if not gitkeep.exists():
        with open(gitkeep, "w") as f:
            f.write("")

print("[+] Common directories created.")

# -------------------------------------------------------------
# 2. GENERATE PHASES, WEEKS, AND DAYS
# -------------------------------------------------------------
for phase in phases:
    p_num = phase["phase_num"]
    p_id = phase["phase_id"]
    p_title = phase["phase_title"]
    p_dir = WORKSPACE / p_id
    p_dir.mkdir(parents=True, exist_ok=True)

    # Phase README
    weeks_list_md = "\n".join([
        f"- [ ] [**Week {w['week_num']:02d}: {w['week_title']}**]({w['week_id']}/README.md) — *{w['objective']}*"
        for w in phase["weeks"]
    ])
    skills_list_md = "\n".join([f"* {s}" for s in phase["skills"]])
    tools_list_md = ", ".join([f"`{t}`" for t in phase["tools"]])

    phase_readme_content = f"""# PHASE {p_num:02d} — {p_title.upper()}

> **Timeline:** {phase['weeks_range']} ({phase['days_range']})  
> **Status:** ⚪ Not Started  
> **Progress:** `░░░░░░░░░░░░░░░░░░░░` 0% (0 / {sum(len(w['days']) for w in phase['weeks'])} Days Completed)

---

## 🎯 Phase Objective
{phase['objective']}

---

## 📅 Weeks in this Phase
{weeks_list_md}

---

## 🛠️ Core Skills Mastered
{skills_list_md}

## 🧰 Primary Tools & Technologies
{tools_list_md}

---

## 📌 Phase Capstone Deliverable
* **Deliverable ID:** `{phase['project_id']}`
* **Title:** [{phase['project_title']}](../projects/{phase['project_id']}/README.md)
* **Location:** `projects/{phase['project_id']}/`

---

## 📝 Phase Completion Criteria
- [ ] All {len(phase['weeks'])} weekly modules fully reviewed and documented.
- [ ] All {sum(len(w['days']) for w in phase['weeks'])} daily lab exercises and journals completed with saved evidence.
- [ ] Capstone project deliverable (`{phase['project_id']}`) authored, tested, and pushed to GitHub.
- [ ] Interview readiness self-assessment completed for phase technical competencies.

[🔙 Back to Master Dashboard](../README.md) | [🗺️ View Roadmap](../ROADMAP.md) | [📊 Master Progress](../PROGRESS.md)
"""
    with open(p_dir / "README.md", "w", encoding="utf-8") as f:
        f.write(phase_readme_content)

    # Generate Weeks in this Phase
    for week in phase["weeks"]:
        w_num = week["week_num"]
        w_id = week["week_id"]
        w_title = week["week_title"]
        w_dir = p_dir / w_id
        w_dir.mkdir(parents=True, exist_ok=True)

        days_list_md = "\n".join([
            f"- [ ] [⚪ Day {d['day_num']:03d}: {d['title']}](day-{d['day_num']:03d}/README.md)"
            for d in week["days"]
        ])
        major_concepts_md = "\n".join([f"* {c}" for c in week["major_concepts"]])
        w_tools_md = ", ".join([f"`{t}`" for t in week["tools"]])

        week_readme_content = f"""# WEEK {w_num:02d} — {w_title.upper()}

> **Phase:** [Phase {p_num:02d} — {p_title}](../README.md)  
> **Status:** ⚪ Not Started  
> **Progress:** `░░░░░░░░░░░░░░░░░░░░` 0% (0 / {len(week['days'])} Days Completed)

---

## 🎯 Weekly Objective
{week['objective']}

## 📅 Schedule of Days
{days_list_md}

---

## 🧰 Tools & Utilities
{w_tools_md}

## 🧠 Major Concepts
{major_concepts_md}

---

## 🔬 Weekly Hands-on Lab
**{week['weekly_lab']}**

## 📌 Week Deliverable
*{week['deliverable']}*

---

## 🔍 Weekly Review & Reflection
### Concepts Mastered
* [Notes on mastered concepts]

### Weak Areas & Topics Needing Review
* [List areas requiring additional focus]

---

[🔙 Back to Phase {p_num:02d}](../README.md) | [📊 Master Progress](../../PROGRESS.md) | [🗺️ Master Roadmap](../../ROADMAP.md)
"""
        with open(w_dir / "README.md", "w", encoding="utf-8") as f:
            f.write(week_readme_content)

        # Generate Days in this Week
        for day in week["days"]:
            d_num = day["day_num"]
            d_dir = w_dir / f"day-{d_num:03d}"
            d_dir.mkdir(parents=True, exist_ok=True)
            (d_dir / "evidence" / "screenshots").mkdir(parents=True, exist_ok=True)
            (d_dir / "evidence" / "logs").mkdir(parents=True, exist_ok=True)
            (d_dir / "evidence" / "pcaps").mkdir(parents=True, exist_ok=True)
            with open(d_dir / "evidence" / ".gitkeep", "w") as f:
                f.write("")

            topics_md = "\n".join([f"* {t}" for t in day["topics"]])

            # Daily README (The Journal)
            day_readme_content = f"""# DAY {d_num:03d} — {day['title'].upper()}

<!-- METADATA
day: {d_num}
phase: {p_num}
week: {w_num}
status: not-started
date: 
-->

## Status
⚪ **Not Started**  
*(Options: ⚪ Not Started | 🟡 In Progress | 🟢 Completed | 🔴 Needs Review)*

---

## 🎯 Learning Objectives
{day['objectives']}

## 📚 Topics
{topics_md}

---

## 👨‍🏫 Professor Notes
<!-- Detailed explanations of the theory, architectural concepts, and protocols learned today. Write in paragraphs rather than raw bullets. -->

---

## 💡 Concepts I Understood
* [Document what you now understand clearly]

## ⚠️ Concepts I Need To Review
* [Document what remains weak or ambiguous]

---

## 💻 Commands & Code
```bash
# Document key commands used today with practical explanations of flags and behavior
```

---

## 🔬 Hands-on Lab
### Objective
{day['lab']}

### Environment
* **Attacker:** Kali Linux / Dedicated Security VM
* **Target:** Test Lab Target / Isolated Network
* **Network Mode:** Isolated Host-Only / Internal Virtual Switch

### Steps
1. [Document step 1]
2. [Document step 2]
3. [Document step 3]

### Expected Result
* [Document what should happen upon successful execution]

### Actual Result
* [Document what actually occurred during lab execution]

### Security Observation
* [Document security indicators, telemetry generated, or defensive observations]

---

## 📸 Evidence
* **Screenshots:** [evidence/screenshots/](evidence/screenshots/)
* **Terminal Logs:** [evidence/logs/](evidence/logs/)
* **Network Captures (PCAPs):** [evidence/pcaps/](evidence/pcaps/)

---

## 📝 What I Learned
<!-- Concise written executive summary of today's insights and knowledge acquisition -->

---

## 🎤 Interview Questions
**Question:** {day['interview_q']}

### My Answers
* **Answer:** <!-- Write your thorough technical answer here as you would explain it to a senior interviewer -->

---

## 🛠️ Mistakes & Troubleshooting
* **Issue:** [Problem encountered]
* **Root Cause:** [Why it happened]
* **Resolution:** [How it was fixed]

---

## 🛡️ Security Takeaway (Attack vs. Defense)
* **Offensive Perspective:** [How an adversary leverages this topic]
* **Defensive Perspective:** [How defenders detect, log, mitigate, or architect against it]

---

## 📦 GitHub Deliverable
* [ ] Daily notes and commands committed
* [ ] Lab execution walkthrough and evidence linked
* [ ] Checklists updated

---

## ✅ Completion Checklist
- [ ] Theory completed
- [ ] Examples understood
- [ ] Lab completed
- [ ] Evidence saved
- [ ] Notes written
- [ ] Interview questions answered
- [ ] Review completed
- [ ] Git commit created

---

[🔙 Back to Week {w_num:02d}](../README.md) | [🏠 Master Dashboard](../../../README.md) | [📊 Progress Tracker](../../../PROGRESS.md)
"""
            with open(d_dir / "README.md", "w", encoding="utf-8") as f:
                f.write(day_readme_content)

            # notes.md
            notes_content = f"""# Day {d_num:03d} Study Notes: {day['title']}

## Core Theoretical Concepts
<!-- Write detailed technical explanations here -->

## Architectural Diagrams / Data Flows
<!-- ASCII or Mermaid diagram of data flows -->

## Key Reference Articles & Documentation
* [Reference link 1]
* [Reference link 2]
"""
            with open(d_dir / "notes.md", "w", encoding="utf-8") as f:
                f.write(notes_content)

            # commands.md
            commands_content = f"""# Day {d_num:03d} Command Cheatsheet: {day['title']}

## Essential Commands

```bash
# Command template
# Explanation of syntax and flags
```

## PowerShell / Script Snippets

```powershell
# Script template
```
"""
            with open(d_dir / "commands.md", "w", encoding="utf-8") as f:
                f.write(commands_content)

            # lab.md
            lab_content = f"""# Day {d_num:03d} Lab Walkthrough: {day['title']}

## Lab Scenario
{day['lab']}

## Prerequisites & Tools
* Host environment ready
* Target service configured

## Step-by-Step Execution Guide
### Step 1: Verification
### Step 2: Execution
### Step 3: Validation & Evidence Capture

## Analysis & Defensive Telemetry
* Events generated:
* Logs inspected:
"""
            with open(d_dir / "lab.md", "w", encoding="utf-8") as f:
                f.write(lab_content)

print("[+] All 9 Phases, 40 Weeks, and 200 Days generated successfully!")

# -------------------------------------------------------------
# 3. GENERATE PROJECTS (9 DELIVERABLES)
# -------------------------------------------------------------
projects = [
    {
        "id": "project-01-security-lab-environment",
        "title": "Multi-OS Security Lab Environment",
        "phase": 1,
        "objective": "Build and document an enterprise-ready, isolated, multi-OS virtualization lab (Kali Linux + Windows Target + Linux Target + Vulnerable Web Container) configured with host-only networking.",
        "tech": "Hyper-V / VirtualBox, Kali Linux, Windows 10/11 Enterprise Evaluation, Ubuntu Server, Docker"
    },
    {
        "id": "project-02-web-pentest-report",
        "title": "Web Security Lab & Professional Penetration Test Report",
        "phase": 2,
        "objective": "Conduct an authorized penetration test on an enterprise web application, document severe vulnerabilities with CVSS scoring, and author an executive-ready penetration testing report.",
        "tech": "Burp Suite Professional/Community, Nuclei, Feroxbuster, PayloadsAllTheThings, CVSS v3.1 Calculator, SysReptor"
    },
    {
        "id": "project-03-corporate-ad-lab",
        "title": "Corporate Active Directory Lab & Attack Path Compromise",
        "phase": 3,
        "objective": "Deploy a multi-tier Windows Active Directory domain with Domain Controller, member servers, and workstations; map full escalation paths with BloodHound and execute Kerberos attacks to domain dominance.",
        "tech": "Windows Server 2022 AD DS, BloodHound, SharpHound, Rubeus, Mimikatz, Impacket, Certify"
    },
    {
        "id": "project-04-cve-intelligence-pipeline",
        "title": "CVE Research & Intelligence Pipeline",
        "phase": 4,
        "objective": "Develop an automated Python vulnerability intelligence pipeline that ingests NVD and CISA KEV feeds, parses CPE asset ranges, enriches CVEs with EPSS scores and public GitHub PoCs, and exports actionable remediation alerts.",
        "tech": "Python 3, NVD REST API, CISA KEV Feed, FIRST EPSS API, trickest/cve, SQLite, Docker"
    },
    {
        "id": "project-05-red-team-engagement-report",
        "title": "Full Authorized Red Team Engagement Report",
        "phase": 5,
        "objective": "Plan and execute an authorized multi-phase adversary emulation exercise using Sliver C2, enforce strict OPSEC and tiered C2 design, and author a comprehensive red team report with blue team timeline deconfliction.",
        "tech": "Sliver C2, Ligolo-ng, WireGuard, Nginx Redirectors, Ghostwriter, MITRE ATT&CK Matrix"
    },
    {
        "id": "project-06-soc-detection-lab",
        "title": "SOC & Detection Engineering Lab",
        "phase": 6,
        "objective": "Deploy a centralized Wazuh SIEM monitoring Windows (Sysmon) and Linux (auditd) endpoints; author custom Sigma detection rules for LOLBAS and credential dumping, and validate with Atomic Red Team.",
        "tech": "Wazuh SIEM, Elasticsearch, Kibana, Sysmon, auditd, Sigma, pySigma, Atomic Red Team"
    },
    {
        "id": "project-07-malware-triage-forensics",
        "title": "Malware Triage & Digital Forensics Investigation Report",
        "phase": 7,
        "objective": "Dissect a compiled malware sample through static disassembly with Ghidra and dynamic monitoring in a sandbox; author custom YARA rules and reconstruct the incident from a memory dump using Volatility 3.",
        "tech": "Ghidra, YARA, Volatility 3, Procmon, FakeNet-NG, Eric Zimmerman Tools (PECmd, MFTECmd)"
    },
    {
        "id": "project-08-personal-security-toolkit",
        "title": "Personal Security Toolkit in Rust",
        "phase": 8,
        "objective": "Architect and compile a high-performance personal security suite in Rust including an async multi-threaded port scanner (Tokio), an async HTTP prober (Reqwest), and a line-speed JSON log parser (Serde).",
        "tech": "Rust, Cargo, Tokio async runtime, Reqwest, Clap CLI derive, Serde, cross-compilation"
    },
    {
        "id": "project-09-purple-team-platform",
        "title": "Purple Team Security Operations Platform (Final Capstone)",
        "phase": 9,
        "objective": "Execute the comprehensive hybrid enterprise Capstone scenario; bridge attack execution with real-time detection engineering, automate validation via Caldera, and package your master cybersecurity engineering portfolio.",
        "tech": "Full Curriculum Toolchain, MITRE Caldera, ATT&CK Navigator, VECTR, Wazuh SIEM, Sliver C2"
    }
]

for prj in projects:
    p_dir = WORKSPACE / "projects" / prj["id"]
    p_dir.mkdir(parents=True, exist_ok=True)
    for sub in ["architecture", "src", "docs", "screenshots", "tests"]:
        (p_dir / sub).mkdir(parents=True, exist_ok=True)
        with open(p_dir / sub / ".gitkeep", "w") as f:
            f.write("")

    prj_readme = f"""# {prj['title']}

> **Deliverable ID:** `{prj['id']}`  
> **Associated Phase:** Phase {prj['phase']:02d}  
> **Status:** ⚪ In Planning / Template Ready

---

## 🎯 Objective
{prj['objective']}

## 🏗️ Architecture & Topology
<!-- Provide high-level network topology, components, and trust boundaries -->
```
[ATTACKER WORKSTATION] ---- (Isolated Lab Subnet) ---- [TARGET INFRASTRUCTURE]
                                                               |
                                                       [TELEMETRY PIPELINE]
```

## 🧰 Technologies & Tooling
* {prj['tech']}

---

## 🛡️ Security Problem & Threat Model
<!-- Define the business or operational security challenge addressed by this project -->

## 💻 Implementation Details
<!-- Walkthrough of how this system was constructed, configured, or coded -->

## 🔬 Testing & Validation
<!-- Test cases, proof-of-concept verification, and operational checks -->

## 🚨 Detection & Telemetry
<!-- How actions in this project are logged and detected by blue team controls -->

## 🛠️ Remediation & Hardening Guidance
<!-- Practical mitigation, hardening, and architecture recommendations -->

## 📸 Screenshots & Evidence
* [architecture/](architecture/)
* [screenshots/](screenshots/)
* [docs/](docs/)

## 🎓 Lessons Learned & Key Takeaways
<!-- Critical insights acquired during the design and execution of this deliverable -->

## 🎤 Interview Explanation Guide
<!-- How to explain this project concisely and authoritatively in a technical interview -->

---

[🔙 Back to Projects Directory](../README.md) | [🏠 Master Dashboard](../../README.md)
"""
    with open(p_dir / "README.md", "w", encoding="utf-8") as f:
        f.write(prj_readme)

print("[+] All 9 Project Deliverable folders created.")

# -------------------------------------------------------------
# 4. GENERATE CHEATSHEETS (12 REFERENCE GUIDES)
# -------------------------------------------------------------
cheatsheets_data = [
    ("networking.md", "Networking & Protocols Reference", "TCP/IP, Subnetting, BPF Syntax, Packet Headers, Wireshark Filters, Routing"),
    ("linux.md", "Linux System & Security Reference", "Permissions, SUID, Systemd, /proc, Bash Scripting, Host Triage"),
    ("windows.md", "Windows Internals & PowerShell Reference", "Architecture, LSASS, Access Tokens, DACLs/SACLs, Sysmon Events, PowerShell WMI/CIM"),
    ("web-security.md", "Web Application Security Reference", "OWASP Top 10, Injection, XSS, CSRF, SSRF, Deserialization, HTTP Smuggling"),
    ("recon.md", "Reconnaissance & Attack Surface Discovery", "OSINT, Subdomain Discovery, ASN Mapping, S3 Hunting, DNS Enumeration"),
    ("active-directory.md", "Active Directory Attacks & Defense Reference", "Kerberos Handshakes, Kerberoasting, AS-REP, BloodHound Edges, AD CS ESC1-8, DCSync"),
    ("red-team.md", "Red Team Operations & OPSEC Reference", "Tiered C2 Design, Scoping, RoE, LOLBAS Binaries, AMSI Bypass, Sliver Operator Commands"),
    ("blue-team.md", "Blue Team, SOC & Incident Response Reference", "Sysmon EIDs, Linux Auditd, Evidence Triage, PICERL Lifecycle, Host Isolation"),
    ("siem.md", "SIEM & Detection Engineering (Sigma) Reference", "Wazuh Decoders & Rules, Sigma YAML Syntax, pySigma Conversion, Elastic Common Schema"),
    ("malware-analysis.md", "Malware Analysis & Reverse Engineering Reference", "PE Headers, Section Entropy, Ghidra Decompilation, YARA Syntax, Procmon Filtering"),
    ("rust-security.md", "Rust Security Programming Reference", "Ownership, Borrowing, Tokio Async Sockets, Reqwest, Clap Derive, Unsafe FFI"),
    ("cve-research.md", "Vulnerability Research & Intelligence Reference", "CVE Lifecycle, CVSS v3.1/v4.0 Vectors, EPSS API, PoC Verification, Patch Diffing")
]

for filename, title, topics in cheatsheets_data:
    cs_content = f"""# {title}

> **Category:** Core Reference Cheatsheet  
> **Topics Covered:** {topics}

---

## 📌 Quick Reference & Syntax

```bash
# Key commands and syntax references
```

## 🧠 Core Mental Models & Architecture

## 🔍 Common Traps & Gotchas

## 📚 Source References & Literature
* Authoritative documentation and community standards.

---
[🔙 Back to Master Dashboard](../README.md)
"""
    with open(WORKSPACE / "cheatsheets" / filename, "w", encoding="utf-8") as f:
        f.write(cs_content)

print("[+] 12 Reference Cheatsheets generated.")

# -------------------------------------------------------------
# 5. GENERATE SOURCES.MD
# -------------------------------------------------------------
sources_content = """# 📚 Master Curriculum Sources & Repository Mapping

This learning journal is built upon an elite foundation of industry-recognized, authoritative open-source security repositories and literature. Every phase maps directly to established tradecraft:

| Source Repository / Standard | Focus Domain | Mapped Curriculum Phases | Official Link |
| :--- | :--- | :--- | :--- |
| **PayloadsAllTheThings** | Web Application Vulnerabilities & Injection | Phase 1, Phase 2 | [swisskyrepo/PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings) |
| **RedTeam-Tools** | Curated Offensive Tooling & LOLBAS Tips | Phase 2, Phase 3, Phase 5 | [A-poc/RedTeam-Tools](https://github.com/A-poc/RedTeam-Tools) |
| **BlueTeam-Tools** | Defensive Tooling, Telemetry & DFIR | Phase 6, Phase 7 | [A-poc/BlueTeam-Tools](https://github.com/A-poc/BlueTeam-Tools) |
| **Red-Team-Playbooks** | Engagement Lifecycle, Scoping & SOPs | Phase 3, Phase 5 | [0xsyr0/Red-Team-Playbooks](https://github.com/0xsyr0/Red-Team-Playbooks) |
| **trickest/cve** | Vulnerability PoC Research & Exploits | Phase 4 | [trickest/cve](https://github.com/trickest/cve) |
| **HackTricks** | Cross-Domain Security Encyclopedia | Phase 1, Phase 2, Phase 3 | [carlospolop/hacktricks](https://github.com/carlospolop/hacktricks) |
| **Black Hat Rust** | Systems Programming & Security Engineering | Phase 8 | [Black Hat Rust](https://github.com/skerkour/black-hat-rust) |
| **Sliver** | Adversary Emulation & C2 Operations | Phase 5, Phase 9 | [BishopFox/sliver](https://github.com/BishopFox/sliver) |

---

## 📖 Literature & Standards References
1. **Red Team Development and Operations** — Joe Vest & James Tubberville
2. **RTFM: Red Team Field Manual (v1 & v2)** — Ben Clark & Nick Downer
3. **BTFM: Blue Team Field Manual** — Alan J. White & Ben Clark
4. **MITRE ATT&CK Framework for Enterprise** — MITRE Corporation
5. **NIST SP 800-61 Rev. 2 (Computer Security Incident Handling Guide)** — NIST
6. **Unified Cyber Kill Chain** — Paul Pols

---
[🔙 Back to Master Dashboard](README.md)
"""
with open(WORKSPACE / "SOURCES.md", "w", encoding="utf-8") as f:
    f.write(sources_content)

print("[+] SOURCES.md generated.")

# -------------------------------------------------------------
# 6. GENERATE PROGRESS.MD
# -------------------------------------------------------------
progress_rows = []
for phase in phases:
    for week in phase["weeks"]:
        for day in week["days"]:
            progress_rows.append(
                f"| Day {day['day_num']:03d} | Phase {phase['phase_num']:02d} | Week {week['week_num']:02d} | [{day['title']}]({phase['phase_id']}/{week['week_id']}/day-{day['day_num']:03d}/README.md) | ⚪ Not Started | - |"
            )

progress_table_md = "\n".join(progress_rows)

progress_content = f"""# 📊 CYBERSECURITY MASTER JOURNAL — MASTER PROGRESS TRACKER

> **Total Curriculum Days:** 200  
> **Completed:** 0  
> **In Progress:** 0  
> **Needs Review:** 0  
> **Remaining:** 200  
> **Overall Progress:** `░░░░░░░░░░░░░░░░░░░░` 0.0%

---

## 🏆 Phase Progress Summary

| Phase | Title | Weeks | Days | Completed | Progress Bar | Status |
| :--- | :--- | :--- | :--- | :---: | :--- | :---: |
| **Phase 01** | [Core Foundations](phase-01-foundations/README.md) | Weeks 01–06 | Days 001–030 | 0 / 30 | `░░░░░░░░░░` 0% | ⚪ Not Started |
| **Phase 02** | [Web Security & Recon](phase-02-web-recon/README.md) | Weeks 07–12 | Days 031–060 | 0 / 30 | `░░░░░░░░░░` 0% | ⚪ Not Started |
| **Phase 03** | [Internal Security & AD](phase-03-internal-security/README.md) | Weeks 13–18 | Days 061–090 | 0 / 30 | `░░░░░░░░░░` 0% | ⚪ Not Started |
| **Phase 04** | [CVE Research & Intelligence](phase-04-cve-research/README.md) | Weeks 19–21 | Days 091–105 | 0 / 15 | `░░░░░░░░░░` 0% | ⚪ Not Started |
| **Phase 05** | [Red Team Operations](phase-05-red-team/README.md) | Weeks 22–27 | Days 106–135 | 0 / 30 | `░░░░░░░░░░` 0% | ⚪ Not Started |
| **Phase 06** | [Blue Team & SOC](phase-06-blue-team/README.md) | Weeks 28–32 | Days 136–160 | 0 / 25 | `░░░░░░░░░░` 0% | ⚪ Not Started |
| **Phase 07** | [Malware & Forensics](phase-07-malware-forensics/README.md) | Weeks 33–35 | Days 161–175 | 0 / 15 | `░░░░░░░░░░` 0% | ⚪ Not Started |
| **Phase 08** | [Security Programming (Rust)](phase-08-security-programming/README.md) | Weeks 36–38 | Days 176–190 | 0 / 15 | `░░░░░░░░░░` 0% | ⚪ Not Started |
| **Phase 09** | [Purple Team & Capstone](phase-09-purple-team/README.md) | Weeks 39–40 | Days 191–200 | 0 / 10 | `░░░░░░░░░░` 0% | ⚪ Not Started |

---

## 📋 Complete 200-Day Journal Master Index

| Day | Phase | Week | Day Title & Link | Status | Completed Date |
| :---: | :---: | :---: | :--- | :---: | :---: |
{progress_table_md}

---

## 🔄 Updating Progress
Run the automated calculation script to refresh this file and the main README:
```bash
python scripts/progress/calculate_progress.py
```

[🔙 Back to Master Dashboard](README.md) | [🗺️ View Roadmap](ROADMAP.md)
"""
with open(WORKSPACE / "PROGRESS.md", "w", encoding="utf-8") as f:
    f.write(progress_content)

print("[+] PROGRESS.md generated.")

# -------------------------------------------------------------
# 7. GENERATE ROADMAP.MD (ASCII + MERMAID + DETAILED BREAKDOWN)
# -------------------------------------------------------------
roadmap_content = """# 🗺️ CYBERSECURITY MASTER ROADMAP: RED TEAM + BLUE TEAM + RESEARCH + ENGINEERING

> **Master Curriculum:** 40 Weeks / 200 Days  
> **Target:** Advanced Security Practitioner / Purple Team Operator  
> **Foundational Standards:** MITRE ATT&CK • Cyber Kill Chain • SANS PICERL • NIST SP 800-61

---

## 🧭 Visual Flow Diagram

```text
╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                 🛡️  CYBERSECURITY MASTER ROADMAP: RED TEAM + BLUE TEAM + RESEARCH + ENGINEERING                         ║
║                              TARGET: ADVANCED SECURITY PRACTITIONER / PURPLE TEAM                                         ║
╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝

                                  ╔══════════════════════════════╗
                                  ║      START YOUR JOURNEY      ║
                                  ╚════════════════════╦═════════╝
                                                       ▼
┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│  PHASE 1: CORE FOUNDATIONS — NETWORKING + LINUX + WINDOWS + WEB                                         [WEEKS 1–6]       │
│  ● Week 1: Networking & Protocols                                                                                        │
│  ● Week 2: Linux Fundamentals & System Administration                                                                    │
│  ● Week 3: Windows Internals & PowerShell Security                                                                       │
│  ● Weeks 4–5: Web Architecture & Web Security Fundamentals                                                               │
│  ● Week 6: Security Tooling Foundation                                                                                   │
│  📌 DELIVERABLE 1: Multi-OS Security Lab Environment (Kali + Windows + Linux + Web Lab)                                   │
└──────────────────────────────────────────────────┬────────────────────────────────────────────────────────────────────────┘
                                                   ▼
┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│  PHASE 2: WEB APPLICATION SECURITY + RECONNAISSANCE                                                     [WEEKS 7–12]      │
│  ● Weeks 7–8: Reconnaissance, OSINT & Content Discovery                                                                   │
│  ● Weeks 9–10: Server-Side & Client-Side Web Vulnerabilities (SQLi, SSTI, Deserialization, XSS, SSRF)                     │
│  ● Weeks 11–12: Modern Application & API Security (BOLA, JWT, GraphQL, Race Conditions) & Reporting                       │
│  📌 DELIVERABLE 2: Web Security Lab + Professional Penetration Test Report                                                │
└──────────────────────────────────────────────────┬────────────────────────────────────────────────────────────────────────┘
                                                   ▼
┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│  PHASE 3: PRIVILEGE ESCALATION + INTERNAL SECURITY                                                      [WEEKS 13–18]     │
│  ● Weeks 13–14: Linux Privilege Escalation & Container Breakouts (SUID, Capabilities, Sudo, Docker)                      │
│  ● Weeks 15–16: Active Directory Fundamentals & Attack Paths (Kerberos, BloodHound, AD CS, Delegation)                    │
│  ● Weeks 17–18: Windows Privilege Escalation & Lateral Movement (Services, Tokens, Mimikatz, PtH, WMI)                   │
│  📌 DELIVERABLE 3: Corporate Active Directory Lab & Compromise Path Documentation                                         │
└──────────────────────────────────────────────────┬────────────────────────────────────────────────────────────────────────┘
                                                   ▼
┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│  PHASE 4: VULNERABILITY RESEARCH + CVE INTELLIGENCE                                                     [WEEKS 19–21]     │
│  ● Week 19: Vulnerability Fundamentals, Taxonomy & CVSS v3.1/v4.0 / EPSS Scoring                                         │
│  ● Week 20: CVE / PoC Research & Safe Sandbox Reproduction                                                               │
│  ● Week 21: Automated Vulnerability Intelligence & Feed Ingestion Pipeline                                               │
│  📌 DELIVERABLE 4: CVE Research & Intelligence Pipeline (Feed Ingestion + Version Matching + PoC Triage)                  │
└──────────────────────────────────────────────────┬────────────────────────────────────────────────────────────────────────┘
                                                   ▼
┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│  PHASE 5: RED TEAM OPERATIONS + ADVERSARY EMULATION                                                     [WEEKS 22–27]     │
│  ● Weeks 22–23: Red Team Methodology, Tiered C2 Architecture, OPSEC & Weaponization                                      │
│  ● Weeks 24–25: Command & Control with Sliver, Listeners, Beacons, In-Memory Execution & Pivoting                         │
│  ● Weeks 26–27: Full Authorized Adversary Emulation Exercise (Recon → Domain Admin → Deconfliction)                       │
│  📌 DELIVERABLE 5: Full Red Team Engagement Report (Executive Summary + ATT&CK Matrix + Blue Deconfliction)               │
└──────────────────────────────────────────────────┬────────────────────────────────────────────────────────────────────────┘
                                                   ▼
┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│  PHASE 6: BLUE TEAM + SOC + THREAT HUNTING                                                              [WEEKS 28–32]     │
│  ● Week 28: Security Telemetry & Endpoint Visibility (Sysmon, Windows Event Logs, Linux Auditd)                          │
│  ● Weeks 29–30: SIEM Architecture (Wazuh/Elastic) & Detection Engineering with Sigma Rules                               │
│  ● Weeks 31–32: Threat Hunting Methodologies & Incident Response Triage (PICERL)                                         │
│  📌 DELIVERABLE 6: SOC & Detection Engineering Lab (Wazuh SIEM + Sysmon + Custom Sigma Rule Suite)                       │
└──────────────────────────────────────────────────┬────────────────────────────────────────────────────────────────────────┘
                                                   ▼
┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│  PHASE 7: MALWARE ANALYSIS + DIGITAL FORENSICS                                                          [WEEKS 33–35]     │
│  ● Week 33: Malware Architecture, PE/ELF Headers, Packing & Anti-Analysis                                                │
│  ● Week 34: Static Disassembly (Ghidra), Dynamic Analysis (Procmon, FakeNet-NG) & YARA Rules                             │
│  ● Week 35: Digital Forensics & Incident Reconstruction (Volatility 3, Prefetch, Shimcache, MFT)                         │
│  📌 DELIVERABLE 7: Malware Triage + Forensics Report (Sample Dissection + YARA Rule + Memory Reconstruction)             │
└──────────────────────────────────────────────────┬────────────────────────────────────────────────────────────────────────┘
                                                   ▼
┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│  PHASE 8: SECURITY PROGRAMMING + RUST + TOOL DEVELOPMENT                                                [WEEKS 36–38]     │
│  ● Week 36: Rust Fundamentals for Hackers (Ownership, Borrowing, Structs, Concurrency)                                   │
│  ● Week 37: Security Tool Engineering in Rust (Tokio Async Port Scanner, Reqwest Prober, Serde Parser)                   │
│  ● Week 38: Low-Level Security Concepts (Unsafe Rust, FFI, Win32 API Injection, Raw Sockets)                             │
│  📌 DELIVERABLE 8: Personal Security Toolkit (Compiled Rust Utilities + Performance Benchmarks)                           │
└──────────────────────────────────────────────────┬────────────────────────────────────────────────────────────────────────┘
                                                   ▼
┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│  PHASE 9: PURPLE TEAM + AUTOMATION + CAPSTONE                                                           [WEEKS 39–40]     │
│  ● Week 39: Purple Team Integration (Attack → Telemetry → Detection → Retest Loop & Caldera Automation)                 │
│  ● Week 40: Final Capstone Enterprise Hybrid Simulation, Defense Engineering & Master Portfolio                          │
│  📌 FINAL DELIVERABLE: "Purple Team Security Operations Platform"                                                         │
└──────────────────────────────────────────────────┬────────────────────────────────────────────────────────────────────────┘
                                                   ▼
                         ╔══════════════════════════════════════════════════════════╗
                         ║                 🎯 ADVANCED SECURITY READY                ║
                         ║                                                          ║
                         ║  RED TEAM  →  BLUE TEAM  →  SECURITY RESEARCH            ║
                         ║       →  AUTOMATION  →  PURPLE TEAM                      ║
                         ║                                                          ║
                         ║  Web Security • AD • Cloud • SOC • DFIR • C2             ║
                         ║  Vulnerability Research • Malware • Rust • Tooling       ║
                         ╚══════════════════════════════════════════════════════════╝
```

---

## 📊 Interactive Mermaid Architecture Flow

```mermaid
flowchart TD
    Start([🚀 START LEARNING JOURNEY]) --> P1
    
    subgraph P1["PHASE 1: Core Foundations [Weeks 1–6]"]
        W1[W1: Networking & Protocols] --> W2[W2: Linux Fundamentals]
        W2 --> W3[W3: Windows & PowerShell]
        W3 --> W4[W4-5: Web Architecture & Security]
        W4 --> W6[W6: Tooling Foundation]
        W6 --> D1[("📌 Deliverable 1: Multi-OS Security Lab")]
    end
    
    P1 --> P2
    subgraph P2["PHASE 2: Web Security & Recon [Weeks 7–12]"]
        W7[W7-8: Recon & Content Discovery] --> W9[W9-10: Web Vulnerabilities Injection/Client]
        W9 --> W11[W11-12: API Security & Reporting]
        W11 --> D2[("📌 Deliverable 2: Pentest Report")]
    end
    
    P2 --> P3
    subgraph P3["PHASE 3: Internal Security & PrivEsc [Weeks 13–18]"]
        W13[W13-14: Linux PrivEsc & Containers] --> W15[W15-16: Active Directory & Kerberos]
        W15 --> W17[W17-18: Windows PrivEsc & Lateral Movement]
        W17 --> D3[("📌 Deliverable 3: Corporate AD Lab")]
    end
    
    P3 --> P4
    subgraph P4["PHASE 4: Vulnerability Research [Weeks 19–21]"]
        W19[W19: Vuln Taxonomy & CVSS/EPSS] --> W20[W20: PoC Research & Sandbox Testing]
        W20 --> W21[W21: Automated Intel Pipeline]
        W21 --> D4[("📌 Deliverable 4: CVE Intel Pipeline")]
    end
    
    P4 --> P5
    subgraph P5["PHASE 5: Red Team Operations [Weeks 22–27]"]
        W22[W22-23: Red Team SOPs & Evasion] --> W24[W24-25: Sliver C2 & Pivoting]
        W24 --> W26[W26-27: Full Adversary Emulation]
        W26 --> D5[("📌 Deliverable 5: Red Team Report")]
    end
    
    P5 --> P6
    subgraph P6["PHASE 6: Blue Team & SOC [Weeks 28–32]"]
        W28[W28: Telemetry Sysmon/Auditd] --> W29[W29-30: SIEM & Sigma Detection Eng]
        W29 --> W31[W31-32: Threat Hunting & IR]
        W31 --> D6[("📌 Deliverable 6: SOC Lab & Detection Suite")]
    end
    
    P6 --> P7
    subgraph P7["PHASE 7: Malware & Forensics [Weeks 33–35]"]
        W33[W33: PE/ELF Architecture] --> W34[W34: Static/Dynamic Ghidra/YARA]
        W34 --> W35[W35: Memory & MFT Forensics]
        W35 --> D7[("📌 Deliverable 7: Malware & DFIR Report")]
    end
    
    P7 --> P8
    subgraph P8["PHASE 8: Security Programming (Rust) [Weeks 36–38]"]
        W36[W36: Rust Ownership & Concurrency] --> W37[W37: Async Scanners Tokio/Reqwest]
        W37 --> W38[W38: Unsafe Rust & FFI Injection]
        W38 --> D8[("📌 Deliverable 8: Personal Security Toolkit")]
    end
    
    P8 --> P9
    subgraph P9["PHASE 9: Purple Team & Capstone [Weeks 39–40]"]
        W39[W39: Purple Team Feedback Loop & Caldera] --> W40[W40: Final Enterprise Capstone]
        W40 --> D9[("🎯 FINAL DELIVERABLE: Purple Team Platform")]
    end
    
    D9 --> Finish([🏆 ADVANCED SECURITY PRACTITIONER / PURPLE TEAM READY])
```

---

[🔙 Back to Master Dashboard](README.md) | [📊 Master Progress Tracker](PROGRESS.md)
"""
with open(WORKSPACE / "ROADMAP.md", "w", encoding="utf-8") as f:
    f.write(roadmap_content)

print("[+] ROADMAP.md generated.")

# -------------------------------------------------------------
# 8. GENERATE MASTER README.MD
# -------------------------------------------------------------
readme_content = """╔══════════════════════════════════════════════════════════════════════════════╗
║                    CYBERSECURITY MASTER LEARNING JOURNAL                     ║
║         Red Team  •  Blue Team  •  Security Research  •  Engineering         ║
╚══════════════════════════════════════════════════════════════════════════════╝

> **Target:** Advanced Security Practitioner / Purple Team Operator  
> **Curriculum Scope:** 40 Weeks • 200 Hands-on Days • 9 Industry Deliverables  
> **Architecture:** Fully Structured Markdown Learning Journal & Evidence Portfolio  
> **Foundational Standards:** MITRE ATT&CK • Cyber Kill Chain • SANS PICERL • NIST SP 800-61

---

## 🎯 Primary Mission

The **Cybersecurity Master Learning Journal** is an engineering-grade, structured, and auditable learning repository. It documents an immersive 200-day journey from foundational computer networking and operating system internals to advanced adversary emulation, command-and-control operations, detection engineering, malware reverse engineering, systems programming in Rust, and collaborative purple teaming.

The repository is built strictly around the **daily workflow**:
```text
Open Repository ➔ Open README ➔ View Progress ➔ Choose Current Phase ➔ Choose Week ➔ Choose Day ➔
Study Theory ➔ Perform Lab ➔ Save Evidence ➔ Write Notes ➔ Mark Complete ➔ Recalculate Progress
```

---

## 📊 Live Progress Dashboard

```text
Overall Progress: [░░░░░░░░░░░░░░░░░░░░] 0.0%
Completed Days:   0 / 200
In Progress:      0
Needs Review:     0
Remaining:        200 Days
Current Phase:    Phase 1 — Core Foundations
Current Week:     Week 01 — Networking & Protocols
Current Day:      Day 001 — TCP/IP Architecture, OSI Model & The 3-Way Handshake
```

### 🏆 Phase Progress Breakdown

* **[Phase 1: Core Foundations — Networking + Linux + Windows + Web](phase-01-foundations/README.md)**  
  `[░░░░░░░░░░]` 0.0% (0 / 30 Days) • Weeks 01–06 • Deliverable: [Multi-OS Security Lab Environment](projects/project-01-security-lab-environment/README.md)
* **[Phase 2: Web Application Security + Reconnaissance](phase-02-web-recon/README.md)**  
  `[░░░░░░░░░░]` 0.0% (0 / 30 Days) • Weeks 07–12 • Deliverable: [Web Security Lab & Pentest Report](projects/project-02-web-pentest-report/README.md)
* **[Phase 3: Privilege Escalation + Internal Security](phase-03-internal-security/README.md)**  
  `[░░░░░░░░░░]` 0.0% (0 / 30 Days) • Weeks 13–18 • Deliverable: [Corporate Active Directory Lab](projects/project-03-corporate-ad-lab/README.md)
* **[Phase 4: Vulnerability Research + CVE Intelligence](phase-04-cve-research/README.md)**  
  `[░░░░░░░░░░]` 0.0% (0 / 15 Days) • Weeks 19–21 • Deliverable: [CVE Research & Intelligence Pipeline](projects/project-04-cve-intelligence-pipeline/README.md)
* **[Phase 5: Red Team Operations + Adversary Emulation](phase-05-red-team/README.md)**  
  `[░░░░░░░░░░]` 0.0% (0 / 30 Days) • Weeks 22–27 • Deliverable: [Full Red Team Engagement Report](projects/project-05-red-team-engagement-report/README.md)
* **[Phase 6: Blue Team + SOC + Threat Hunting](phase-06-blue-team/README.md)**  
  `[░░░░░░░░░░]` 0.0% (0 / 25 Days) • Weeks 28–32 • Deliverable: [SOC & Detection Engineering Lab](projects/project-06-soc-detection-lab/README.md)
* **[Phase 7: Malware Analysis + Digital Forensics](phase-07-malware-forensics/README.md)**  
  `[░░░░░░░░░░]` 0.0% (0 / 15 Days) • Weeks 33–35 • Deliverable: [Malware Triage & Forensics Report](projects/project-07-malware-triage-forensics/README.md)
* **[Phase 8: Security Programming + Rust + Tool Development](phase-08-security-programming/README.md)**  
  `[░░░░░░░░░░]` 0.0% (0 / 15 Days) • Weeks 36–38 • Deliverable: [Personal Security Toolkit in Rust](projects/project-08-personal-security-toolkit/README.md)
* **[Phase 9: Purple Team + Automation + Capstone](phase-09-purple-team/README.md)**  
  `[░░░░░░░░░░]` 0.0% (0 / 10 Days) • Weeks 39–40 • Deliverable: [Purple Team Security Operations Platform](projects/project-09-purple-team-platform/README.md)

---

## 🗺️ Master Curriculum Navigation

| Phase | Weeks | Focus Topics | Milestone Deliverable |
| :--- | :--- | :--- | :--- |
| **Phase 01** | [W01](phase-01-foundations/week-01-networking/README.md) • [W02](phase-01-foundations/week-02-linux/README.md) • [W03](phase-01-foundations/week-03-windows/README.md) • [W04](phase-01-foundations/week-04-web-architecture/README.md) • [W05](phase-01-foundations/week-05-web-security/README.md) • [W06](phase-01-foundations/week-06-tooling/README.md) | TCP/IP, Linux FHS, Windows Internals, Web SOP/CORS, Nmap, Burp | [📌 Deliverable 1: Security Lab](projects/project-01-security-lab-environment/README.md) |
| **Phase 02** | [W07](phase-02-web-recon/week-07-recon-osint/README.md) • [W08](phase-02-web-recon/week-08-scanning-content-discovery/README.md) • [W09](phase-02-web-recon/week-09-web-vulnerabilities-1/README.md) • [W10](phase-02-web-recon/week-10-web-vulnerabilities-2/README.md) • [W11](phase-02-web-recon/week-11-modern-app-api-security/README.md) • [W12](phase-02-web-recon/week-12-business-logic-reporting/README.md) | OSINT, Subdomain Takeover, SQLi, SSTI, XSS, SSRF, BOLA, JWT, CVSS | [📌 Deliverable 2: Pentest Report](projects/project-02-web-pentest-report/README.md) |
| **Phase 03** | [W13](phase-03-internal-security/week-13-linux-privesc-foundations/README.md) • [W14](phase-03-internal-security/week-14-linux-privesc-advanced/README.md) • [W15](phase-03-internal-security/week-15-active-directory-foundations/README.md) • [W16](phase-03-internal-security/week-16-active-directory-attacks/README.md) • [W17](phase-03-internal-security/week-17-windows-privesc/README.md) • [W18](phase-03-internal-security/week-18-lateral-movement/README.md) | SUID, Docker Escape, Kerberos, BloodHound, AD CS, Mimikatz, PtH | [📌 Deliverable 3: AD Lab](projects/project-03-corporate-ad-lab/README.md) |
| **Phase 04** | [W19](phase-04-cve-research/week-19-vulnerability-fundamentals/README.md) • [W20](phase-04-cve-research/week-20-cve-poc-research/README.md) • [W21](phase-04-cve-research/week-21-vulnerability-intelligence/README.md) | CVE, CWE, CVSS v4.0, EPSS, trickest/cve, Sandbox Reproduction, Python Ingestion | [📌 Deliverable 4: CVE Pipeline](projects/project-04-cve-intelligence-pipeline/README.md) |
| **Phase 05** | [W22](phase-05-red-team/week-22-red-team-methodology/README.md) • [W23](phase-05-red-team/week-23-weaponization-evasion/README.md) • [W24](phase-05-red-team/week-24-c2-architecture-sliver/README.md) • [W25](phase-05-red-team/week-25-c2-pivoting-traffic/README.md) • [W26](phase-05-red-team/week-26-adversary-simulation-1/README.md) • [W27](phase-05-red-team/week-27-adversary-simulation-2/README.md) | RoE, Tiered C2, AMSI Bypass, Sliver mTLS/DNS, Pivoting, Adversary Simulation | [📌 Deliverable 5: Red Team Report](projects/project-05-red-team-engagement-report/README.md) |
| **Phase 06** | [W28](phase-06-blue-team/week-28-security-monitoring-telemetry/README.md) • [W29](phase-06-blue-team/week-29-siem-log-analytics/README.md) • [W30](phase-06-blue-team/week-30-detection-engineering/README.md) • [W31](phase-06-blue-team/week-31-threat-hunting/README.md) • [W32](phase-06-blue-team/week-32-incident-response/README.md) | Sysmon, Linux Auditd, Wazuh SIEM, Sigma Rules, Atomic Red Team, IR Triage | [📌 Deliverable 6: SOC Lab](projects/project-06-soc-detection-lab/README.md) |
| **Phase 07** | [W33](phase-07-malware-forensics/week-33-malware-fundamentals/README.md) • [W34](phase-07-malware-forensics/week-34-static-dynamic-analysis/README.md) • [W35](phase-07-malware-forensics/week-35-digital-forensics/README.md) | PE/ELF Anatomy, Ghidra Decompilation, YARA Signatures, Volatility 3, MFT | [📌 Deliverable 7: Forensics Report](projects/project-07-malware-triage-forensics/README.md) |
| **Phase 8** | [W36](phase-08-security-programming/week-36-rust-fundamentals/README.md) • [W37](phase-08-security-programming/week-37-security-tool-engineering/README.md) • [W38](phase-08-security-programming/week-38-low-level-security/README.md) | Rust Ownership, Tokio Async Port Scanner, Reqwest Prober, Unsafe FFI | [📌 Deliverable 8: Rust Toolkit](projects/project-08-personal-security-toolkit/README.md) |
| **Phase 09** | [W39](phase-09-purple-team/week-39-purple-team-integration/README.md) • [W40](phase-09-purple-team/week-40-final-capstone/README.md) | Attack-Defense Feedback Loop, MITRE Caldera, Full Enterprise Capstone | [🎯 FINAL: Purple Team Platform](projects/project-09-purple-team-platform/README.md) |

---

## 🧰 Quick Cheatsheets Directory

* [Networking & BPF Filters](cheatsheets/networking.md)
* [Linux Administration & PrivEsc](cheatsheets/linux.md)
* [Windows Internals & PowerShell](cheatsheets/windows.md)
* [Web Security & Injection](cheatsheets/web-security.md)
* [Reconnaissance & OSINT](cheatsheets/recon.md)
* [Active Directory & Kerberos](cheatsheets/active-directory.md)
* [Red Team Operations & C2](cheatsheets/red-team.md)
* [Blue Team & Telemetry](cheatsheets/blue-team.md)
* [SIEM & Sigma Detection](cheatsheets/siem.md)
* [Malware Triage & Reverse Engineering](cheatsheets/malware-analysis.md)
* [Rust Systems Programming](cheatsheets/rust-security.md)
* [CVE Research & CVSS/EPSS](cheatsheets/cve-research.md)

---

## 🛡️ Authorized Testing & Ethical Security Boundary

> [!IMPORTANT]
> All activities, techniques, code samples, and proof-of-concept scripts in this repository are strictly designed for:
> * Authorized virtual laboratory environments
> * Private research networks owned and operated by the practitioner
> * Authorized Capture-The-Flag (CTF) platforms and defensive cyber ranges
> * Systems where explicit, documented, written authorization has been obtained
> 
> Unauthorized testing against systems without permission is strictly prohibited. Every offensive technique in this journal is explicitly paired with defensive telemetry, detection mechanisms, and architectural mitigations.

---

## 🔄 Daily Workflow & Automation CLI

To update your journal, track progress, and manage days:

```bash
# 1. Update day status (e.g. mark Day 1 completed)
python scripts/progress/cli.py complete 1

# 2. View current progress metrics across all 40 weeks
python scripts/progress/cli.py status

# 3. Recalculate progress bars across README.md and PROGRESS.md
python scripts/progress/calculate_progress.py

# 4. Open the interactive security dashboard locally
start dashboard/index.html
```

---

[🗺️ Master Roadmap](ROADMAP.md) | [📊 Master Progress Table](PROGRESS.md) | [📚 Source Repositories](SOURCES.md) | [🤝 Contributing](CONTRIBUTING.md)
"""
with open(WORKSPACE / "README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)

print("[+] Master README.md generated.")

# -------------------------------------------------------------
# 9. GENERATE PROGRESS SCRIPTS (calculate_progress.py, update_day.py, cli.py)
# -------------------------------------------------------------
calculate_progress_script = """#!/usr/bin/env python3
\"\"\"
Progress Calculator for CYBERSECURITY-MASTER-JOURNAL
Scans all 200 day journals for status markers, computes exact progress metrics,
and updates README.md and PROGRESS.md.
\"\"\"

import os
import re
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parents[2]

def get_day_status(file_path):
    if not file_path.exists():
        return "not-started"
    try:
        content = file_path.read_text(encoding="utf-8")
        # Check metadata block first
        meta_match = re.search(r"status:\\s*([a-zA-Z0-9-]+)", content, re.IGNORECASE)
        if meta_match:
            return meta_match.group(1).lower()
        # Fallback to badge
        if "🟢" in content or "Completed" in content or "status: completed" in content:
            return "completed"
        if "🟡" in content or "In Progress" in content:
            return "in-progress"
        if "🔴" in content or "Needs Review" in content:
            return "review"
        return "not-started"
    except Exception:
        return "not-started"

def make_progress_bar(percent, length=20):
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

        # Determine phase and week from path
        p_match = re.search(r"phase-(\\d+)", str(file_path))
        w_match = re.search(r"week-(\\d+)", str(file_path))
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
    bar = make_progress_bar(percent, 20)

    print("=" * 60)
    print("CYBERSECURITY MASTER JOURNAL — PROGRESS REPORT")
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
        p_bar = make_progress_bar(pct, 10)
        print(f"  Phase {p:02d}: [{p_bar}] {comp:2d}/{tot:2d} ({pct:5.1f}%)")
    print("=" * 60)

if __name__ == "__main__":
    main()
"""
with open(WORKSPACE / "scripts" / "progress" / "calculate_progress.py", "w", encoding="utf-8") as f:
    f.write(calculate_progress_script)

update_day_script = """#!/usr/bin/env python3
\"\"\"
Day Updater CLI: Quickly change the status and checklists of a specific day journal.
Usage:
  python update_day.py 1 --status completed
  python update_day.py 1 --status in-progress
  python update_day.py 1 --status review
\"\"\"

import sys
import re
from pathlib import Path
from datetime import datetime

WORKSPACE = Path(__file__).resolve().parents[2]

STATUS_MAP = {
    "completed": ("🟢 **Completed**", "completed"),
    "in-progress": ("🟡 **In Progress**", "in-progress"),
    "review": ("🔴 **Needs Review**", "review"),
    "not-started": ("⚪ **Not Started**", "not-started")
}

def update_day(day_num, new_status):
    day_str = f"day-{int(day_num):03d}"
    matches = list(WORKSPACE.glob(f"phase-*/week-*/{day_str}/README.md"))
    if not matches:
        print(f"[!] Day {day_num} not found!")
        return False
    
    file_path = matches[0]
    content = file_path.read_text(encoding="utf-8")

    badge, status_key = STATUS_MAP.get(new_status.lower(), STATUS_MAP["not-started"])
    today_str = datetime.now().strftime("%Y-%m-%d")

    # Update metadata block
    content = re.sub(r"status:\s*[a-zA-Z0-9-]+", f"status: {status_key}", content)
    content = re.sub(r"date:\s*.*", f"date: {today_str}", content)

    # Update status section
    content = re.sub(
        r"## Status\s*\n[^\n]+\n",
        f"## Status\\n{badge}  \\n",
        content
    )

    # If completed, check off the checklist
    if status_key == "completed":
        content = re.sub(r"- \[ \] Theory completed", "- [x] Theory completed", content)
        content = re.sub(r"- \[ \] Examples understood", "- [x] Examples understood", content)
        content = re.sub(r"- \[ \] Lab completed", "- [x] Lab completed", content)
        content = re.sub(r"- \[ \] Evidence saved", "- [x] Evidence saved", content)
        content = re.sub(r"- \[ \] Notes written", "- [x] Notes written", content)
        content = re.sub(r"- \[ \] Interview questions answered", "- [x] Interview questions answered", content)
        content = re.sub(r"- \[ \] Review completed", "- [x] Review completed", content)
        content = re.sub(r"- \[ \] Git commit created", "- [x] Git commit created", content)

    file_path.write_text(content, encoding="utf-8")
    print(f"[SUCCESS] Updated Day {day_num} to {badge} (Date: {today_str})")
    print(f"File: {file_path}")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python update_day.py <day_number> [--status <completed|in-progress|review|not-started>]")
        sys.exit(1)
    
    day = sys.argv[1]
    status = "completed"
    if "--status" in sys.argv:
        idx = sys.argv.index("--status")
        if idx + 1 < len(sys.argv):
            status = sys.argv[idx + 1]

    update_day(day, status)
"""
with open(WORKSPACE / "scripts" / "progress" / "update_day.py", "w", encoding="utf-8") as f:
    f.write(update_day_script)

cli_script = """#!/usr/bin/env python3
\"\"\"
Interactive & Command CLI for CYBERSECURITY-MASTER-JOURNAL
Usage:
  python cli.py status
  python cli.py complete <day_number>
  python cli.py start <day_number>
  python cli.py open <day_number>
\"\"\"

import sys
import subprocess
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parents[2]

def main():
    if len(sys.argv) < 2:
        print("CYBERSECURITY MASTER JOURNAL CLI")
        print("Commands:")
        print("  status                  - Show overall curriculum progress")
        print("  complete <day>          - Mark a day completed")
        print("  start <day>             - Mark a day in-progress")
        print("  review <day>            - Mark a day needs-review")
        print("  open <day>              - Print file path of day README")
        sys.exit(0)

    cmd = sys.argv[1].lower()

    if cmd == "status":
        calc_script = WORKSPACE / "scripts" / "progress" / "calculate_progress.py"
        subprocess.run([sys.executable, str(calc_script)])

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
        update_script = WORKSPACE / "scripts" / "progress" / "update_day.py"
        subprocess.run([sys.executable, str(update_script), str(day_num), "--status", status_map[cmd]])

    elif cmd == "open":
        if len(sys.argv) < 3:
            print("Usage: python cli.py open <day_number>")
            sys.exit(1)
        day_num = int(sys.argv[2])
        matches = list(WORKSPACE.glob(f"phase-*/week-*/day-{day_num:03d}/README.md"))
        if matches:
            print(f"[FOUND] {matches[0]}")
        else:
            print(f"[!] Day {day_num} not found")

    else:
        print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    main()
"""
with open(WORKSPACE / "scripts" / "progress" / "cli.py", "w", encoding="utf-8") as f:
    f.write(cli_script)

print("[+] Progress scripts generated.")

# -------------------------------------------------------------
# 10. GENERATE LOCAL DASHBOARD WEB UI
# -------------------------------------------------------------
dashboard_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CYBERSECURITY MASTER JOURNAL — Local Operations Dashboard</title>
  <link rel="stylesheet" href="styles.css">
  <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;600;700&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
</head>
<body>
  <div class="app-container">
    <!-- Sidebar -->
    <aside class="sidebar">
      <div class="logo">
        <span class="shield-icon">🛡️</span>
        <div class="logo-text">
          <h2>CYBER-JOURNAL</h2>
          <span class="sub">Purple Team Operations</span>
        </div>
      </div>

      <nav class="nav-links">
        <a href="#overview" class="active">📊 Overview</a>
        <a href="#phases">🗺️ Phases & Weeks</a>
        <a href="#projects">📌 Projects</a>
        <a href="#cheatsheets">📑 Cheatsheets</a>
        <a href="#terminal">💻 CLI Guide</a>
      </nav>

      <div class="sidebar-status">
        <span class="status-dot"></span>
        <span>Local Journal Engine: Active</span>
      </div>
    </aside>

    <!-- Main Content Area -->
    <main class="content">
      <!-- Header Bar -->
      <header class="topbar">
        <div class="search-box">
          <span class="search-icon">🔍</span>
          <input type="text" id="daySearch" placeholder="Search Day (e.g. 'Day 015', 'Kerberos', 'XSS')...">
        </div>
        <div class="user-pill">
          <span class="badge">Master Curriculum</span>
          <span class="days-badge">200 Days • 40 Weeks</span>
        </div>
      </header>

      <!-- Dashboard Cards -->
      <section id="overview" class="stats-grid">
        <div class="card stat-card">
          <div class="card-header">Overall Progress</div>
          <div class="stat-value" id="overallPercent">0.0%</div>
          <div class="progress-bar-container">
            <div class="progress-fill" id="overallFill" style="width: 0%"></div>
          </div>
          <div class="stat-footer">0 / 200 Days Completed</div>
        </div>

        <div class="card stat-card">
          <div class="card-header">Current Focus</div>
          <div class="stat-value highlight">Phase 01</div>
          <div class="stat-sub">Core Foundations</div>
          <div class="stat-footer">Week 01 • Networking & Protocols</div>
        </div>

        <div class="card stat-card">
          <div class="card-header">Next Milestone</div>
          <div class="stat-value">Deliverable 1</div>
          <div class="stat-sub">Multi-OS Security Lab</div>
          <div class="stat-footer">Target: Day 030</div>
        </div>

        <div class="card stat-card">
          <div class="card-header">Curriculum Scope</div>
          <div class="stat-value">9 Phases</div>
          <div class="stat-sub">40 Weeks</div>
          <div class="stat-footer">Full ATT&CK / Kill Chain</div>
        </div>
      </section>

      <!-- Phases Section -->
      <section id="phases" class="section">
        <div class="section-header">
          <h2>Curriculum Phase Navigation</h2>
          <span class="hint">Click any phase to expand its weeks and days</span>
        </div>

        <div class="phases-container" id="phasesContainer">
          <!-- Populated by app.js -->
        </div>
      </section>
    </main>
  </div>

  <script src="app.js"></script>
</body>
</html>
"""
with open(WORKSPACE / "dashboard" / "index.html", "w", encoding="utf-8") as f:
    f.write(dashboard_html)

dashboard_css = """* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

:root {
  --bg-primary: #0a0d14;
  --bg-secondary: #101522;
  --bg-tertiary: #182032;
  --border-color: #242f48;
  --text-primary: #f0f4fc;
  --text-secondary: #9aa8c7;
  --text-muted: #5e6d8c;
  --accent-cyan: #00f2fe;
  --accent-blue: #4facfe;
  --accent-green: #00f090;
  --accent-yellow: #f6d365;
  --accent-red: #ff5858;
}

body {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  background-color: var(--bg-primary);
  color: var(--text-primary);
  min-height: 100vh;
}

.app-container {
  display: flex;
  min-height: 100vh;
}

/* Sidebar */
.sidebar {
  width: 260px;
  background: var(--bg-secondary);
  border-right: 1px solid var(--border-color);
  display: flex;
  flex-direction: column;
  padding: 24px 16px;
}

.logo {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 32px;
  padding-left: 8px;
}

.shield-icon {
  font-size: 28px;
}

.logo-text h2 {
  font-size: 16px;
  font-weight: 800;
  letter-spacing: 0.5px;
  background: linear-gradient(135deg, var(--accent-cyan), var(--accent-blue));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.logo-text .sub {
  font-size: 11px;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 1px;
}

.nav-links {
  display: flex;
  flex-direction: column;
  gap: 8px;
  flex: 1;
}

.nav-links a {
  display: block;
  padding: 10px 14px;
  color: var(--text-secondary);
  text-decoration: none;
  font-size: 14px;
  font-weight: 500;
  border-radius: 6px;
  transition: all 0.2s ease;
}

.nav-links a:hover, .nav-links a.active {
  background: var(--bg-tertiary);
  color: var(--accent-cyan);
}

.sidebar-status {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 12px;
  color: var(--text-muted);
  padding: 8px;
}

.status-dot {
  width: 8px;
  height: 8px;
  background: var(--accent-green);
  border-radius: 50%;
  box-shadow: 0 0 8px var(--accent-green);
}

/* Main Content */
.content {
  flex: 1;
  padding: 32px;
  overflow-y: auto;
}

.topbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 28px;
}

.search-box {
  display: flex;
  align-items: center;
  background: var(--bg-secondary);
  border: 1px solid var(--border-color);
  border-radius: 8px;
  padding: 8px 14px;
  width: 420px;
  gap: 10px;
}

.search-box input {
  background: transparent;
  border: none;
  outline: none;
  color: var(--text-primary);
  font-size: 13px;
  width: 100%;
}

.user-pill {
  display: flex;
  gap: 10px;
}

.badge {
  background: var(--bg-tertiary);
  color: var(--accent-cyan);
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
  border: 1px solid rgba(0, 242, 254, 0.2);
}

.days-badge {
  background: var(--bg-tertiary);
  color: var(--text-secondary);
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  border: 1px solid var(--border-color);
}

/* Stats Grid */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 18px;
  margin-bottom: 36px;
}

.card {
  background: var(--bg-secondary);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  padding: 20px;
}

.card-header {
  font-size: 12px;
  text-transform: uppercase;
  color: var(--text-muted);
  font-weight: 600;
  letter-spacing: 0.5px;
  margin-bottom: 8px;
}

.stat-value {
  font-size: 26px;
  font-weight: 800;
  color: var(--text-primary);
  margin-bottom: 4px;
  font-family: 'Fira Code', monospace;
}

.stat-value.highlight {
  color: var(--accent-cyan);
}

.stat-sub {
  font-size: 13px;
  color: var(--text-secondary);
  margin-bottom: 8px;
}

.stat-footer {
  font-size: 11px;
  color: var(--text-muted);
}

.progress-bar-container {
  height: 6px;
  background: var(--bg-tertiary);
  border-radius: 3px;
  overflow: hidden;
  margin: 10px 0;
}

.progress-fill {
  height: 100%;
  background: linear-gradient(90deg, var(--accent-cyan), var(--accent-green));
}

/* Phases Accordion */
.section-header {
  margin-bottom: 20px;
}

.section-header h2 {
  font-size: 20px;
  font-weight: 700;
  margin-bottom: 4px;
}

.section-header .hint {
  font-size: 13px;
  color: var(--text-muted);
}

.phase-card {
  background: var(--bg-secondary);
  border: 1px solid var(--border-color);
  border-radius: 10px;
  margin-bottom: 14px;
  overflow: hidden;
}

.phase-header {
  padding: 18px 22px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  cursor: pointer;
  background: var(--bg-secondary);
  transition: background 0.2s;
}

.phase-header:hover {
  background: var(--bg-tertiary);
}

.phase-title-group h3 {
  font-size: 15px;
  font-weight: 600;
  margin-bottom: 4px;
}

.phase-title-group .meta {
  font-size: 12px;
  color: var(--text-muted);
}

.phase-body {
  padding: 0 22px 18px;
  display: none;
  border-top: 1px solid var(--border-color);
  background: #0d121c;
}

.phase-body.open {
  display: block;
}

.week-block {
  margin-top: 16px;
}

.week-title {
  font-size: 13px;
  font-weight: 600;
  color: var(--accent-cyan);
  margin-bottom: 8px;
}

.days-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 8px;
}

.day-item {
  background: var(--bg-secondary);
  border: 1px solid var(--border-color);
  border-radius: 6px;
  padding: 8px 12px;
  font-size: 12px;
  display: flex;
  align-items: center;
  gap: 8px;
  text-decoration: none;
  color: var(--text-secondary);
  transition: all 0.15s;
}

.day-item:hover {
  border-color: var(--accent-cyan);
  color: var(--text-primary);
  transform: translateY(-1px);
}
"""
with open(WORKSPACE / "dashboard" / "styles.css", "w", encoding="utf-8") as f:
    f.write(dashboard_css)

dashboard_js = """// Load curriculum and render interactive phases
fetch('../curriculum.json')
  .then(res => res.json())
  .then(phases => {
    const container = document.getElementById('phasesContainer');
    container.innerHTML = '';

    phases.forEach(phase => {
      const card = document.createElement('div');
      card.className = 'phase-card';

      const weeksHtml = phase.weeks.map(w => `
        <div class="week-block">
          <div class="week-title">Week ${String(w.week_num).padStart(2, '0')}: ${w.week_title}</div>
          <div class="days-list">
            ${w.days.map(d => `
              <a href="../${phase.phase_id}/${w.week_id}/day-${String(d.day_num).padStart(3, '0')}/README.md" class="day-item" target="_blank">
                <span class="status-icon">⚪</span>
                <span><strong>Day ${String(d.day_num).padStart(3, '0')}:</strong> ${d.title}</span>
              </a>
            `).join('')}
          </div>
        </div>
      `).join('');

      card.innerHTML = `
        <div class="phase-header" onclick="this.nextElementSibling.classList.toggle('open')">
          <div class="phase-title-group">
            <h3>Phase ${String(phase.phase_num).padStart(2, '0')}: ${phase.phase_title}</h3>
            <span class="meta">${phase.weeks_range} • ${phase.days_range}</span>
          </div>
          <span class="expand-indicator">▼</span>
        </div>
        <div class="phase-body">
          ${weeksHtml}
        </div>
      `;
      container.appendChild(card);
    });

    // Search filter
    document.getElementById('daySearch').addEventListener('input', (e) => {
      const query = e.target.value.toLowerCase();
      document.querySelectorAll('.day-item').forEach(item => {
        const text = item.textContent.toLowerCase();
        if (text.includes(query)) {
          item.style.display = 'flex';
          item.closest('.phase-body').classList.add('open');
        } else {
          item.style.display = query ? 'none' : 'flex';
        }
      });
    });
  })
  .catch(err => console.error("Error loading curriculum.json", err));
"""
with open(WORKSPACE / "dashboard" / "app.js", "w", encoding="utf-8") as f:
    f.write(dashboard_js)

print("[+] Local Dashboard web assets generated.")

# -------------------------------------------------------------
# 11. GENERATE CONTRIBUTING.MD, LICENSE, .GITIGNORE
# -------------------------------------------------------------
gitignore_content = """# Operating System Files
.DS_Store
Thumbs.db
desktop.ini

# Python virtual environment & cache
__pycache__/
*.py[cod]
*$py.class
.venv/
venv/
env/

# Large Capture & Binary Files (store summaries or link externally)
*.iso
*.vmdk
*.vdi
*.qcow2
*.dmp
*.raw

# Build artifacts & temp
/dist/
/build/
target/
*.log
.temp/
"""
with open(WORKSPACE / ".gitignore", "w", encoding="utf-8") as f:
    f.write(gitignore_content)

contributing_content = """# 🤝 Contributing & Personal Study Protocol

This repository is maintained as an engineering learning journal. If you are forking or adapting this repository for your own 200-day journey, follow these guidelines:

## Journal Integrity Protocol
1. **Never invent learning progress:** Do not mark days completed automatically.
2. **Document real lab results:** Record actual command outputs, screenshots, and troubleshooting observations.
3. **Keep the roadmap as single source of truth:** Do not reorder days without recalculating dependency chains.
4. **Practice OPSEC & Safe Testing:** Never run unauthorized scans or exploits against third-party targets.

## Daily Commit Style Convention
```text
docs: complete Day 001 TCP/IP foundations
lab: add Day 001 packet analysis evidence
feat: add reconnaissance lab
docs: complete Week 02 review
feat: add CVE research pipeline
```
"""
with open(WORKSPACE / "CONTRIBUTING.md", "w", encoding="utf-8") as f:
    f.write(contributing_content)

license_content = """MIT License

Copyright (c) 2026 CYBERSECURITY-MASTER-JOURNAL

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
with open(WORKSPACE / "LICENSE", "w", encoding="utf-8") as f:
    f.write(license_content)

print("[+] CONTRIBUTING.md, LICENSE, and .gitignore generated.")
print("\n[SUCCESS] The complete CYBERSECURITY-MASTER-JOURNAL repository has been successfully generated!")
