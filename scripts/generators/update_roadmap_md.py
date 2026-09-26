import json
import os
import sys

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
CURRICULUM_PATH = os.path.join(ROOT_DIR, 'curriculum.json')
ROADMAP_PATH = os.path.join(ROOT_DIR, 'ROADMAP.md')

with open(CURRICULUM_PATH, 'r', encoding='utf-8') as f:
    phases = json.load(f)

# Build ASCII Flowchart
ascii_chart = """╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                 🛡️  CYBERSECURITY MASTER ROADMAP: RED TEAM + BLUE TEAM + RESEARCH + ENGINEERING                         ║
║                              TARGET: ADVANCED SECURITY PRACTITIONER / PURPLE TEAM                                         ║
╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝

                                  ╔══════════════════════════════╗
                                  ║      START YOUR JOURNEY      ║
                                  ╚════════════════════╦═════════╝
                                                       ▼
┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│  PHASE 1: CORE FOUNDATIONS — NETWORKING + LINUX + WINDOWS + WEB                                         [WEEKS 1–6]       │
│  ● Week 1: Networking & Protocols (TCP/IP, OSI, Subnetting, BPF, Wireshark)                        [4 Light • 1 Full]     │
│  ● Week 2: Linux Fundamentals & System Administration (FHS, Permissions, systemd, Audit)            [3 Light • 2 Full]     │
│  ● Week 3: Windows Internals & PowerShell Security (Registry, Tokens, ACLs, Sysmon)                 [3 Light • 2 Full]     │
│  ● Weeks 4–5: Web Architecture & Web Security Fundamentals (HTTP, Cookies, SOP/CORS, SSRF, SQLi)    [6 Light • 4 Full]     │
│  ● Week 6: Security Tooling Foundation (Kali, Nmap, Burp Suite, Python Automation)                  [1 Light • 4 Full]     │
│  📌 DELIVERABLE 1: Multi-OS Security Lab Environment (Kali + Windows + Linux + Web Lab)                                   │
└──────────────────────────────────────────────────┬────────────────────────────────────────────────────────────────────────┘
                                                   ▼
┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│  PHASE 2: WEB APPLICATION SECURITY + RECONNAISSANCE                                                     [WEEKS 7–12]      │
│  ● Weeks 7–8: Reconnaissance, OSINT & Content Discovery (DNS, Shodan, CT Logs, FFUF, Nuclei)        [5 Light • 5 Full]     │
│  ● Weeks 9–10: Server-Side & Client-Side Web Vulnerabilities (SQLi, SSTI, Deserialization, XSS, SSRF)[3 Light • 7 Full]     │
│  ● Weeks 11–12: Modern Application & API Security (BOLA, JWT, GraphQL, Race Conditions) & Reporting  [3 Light • 7 Full]     │
│  📌 DELIVERABLE 2: Web Security Lab + Professional Penetration Test Report                                                │
└──────────────────────────────────────────────────┬────────────────────────────────────────────────────────────────────────┘
                                                   ▼
┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│  PHASE 3: PRIVILEGE ESCALATION + INTERNAL SECURITY                                                      [WEEKS 13–18]     │
│  ● Weeks 13–14: Linux Privilege Escalation & Container Breakouts (SUID, Capabilities, Sudo, Docker) [2 Light • 8 Full]     │
│  ● Weeks 15–16: Active Directory Fundamentals & Attack Paths (Kerberos, BloodHound, AD CS, Delegation)[4 Light • 6 Full]   │
│  ● Weeks 17–18: Windows Privilege Escalation & Lateral Movement (Services, Tokens, Mimikatz, PtH, WMI)[2 Light • 8 Full]   │
│  📌 DELIVERABLE 3: Corporate Active Directory Lab & Compromise Path Documentation                                         │
└──────────────────────────────────────────────────┬────────────────────────────────────────────────────────────────────────┘
                                                   ▼
┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│  PHASE 4: VULNERABILITY RESEARCH + CVE INTELLIGENCE                                                     [WEEKS 19–21]     │
│  ● Week 19: Vulnerability Fundamentals, Taxonomy & CVSS v3.1/v4.0 / EPSS Scoring                     [4 Light • 1 Full]     │
│  ● Week 20: CVE / PoC Research & Safe Sandbox Reproduction                                          [2 Light • 3 Full]     │
│  ● Week 21: Automated Vulnerability Intelligence & Feed Ingestion Pipeline (trickest/cve)           [2 Light • 3 Full]     │
│  📌 DELIVERABLE 4: CVE Research & Intelligence Pipeline (Feed Ingestion + Version Matching + PoC Triage)                  │
└──────────────────────────────────────────────────┬────────────────────────────────────────────────────────────────────────┘
                                                   ▼
┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│  PHASE 5: RED TEAM OPERATIONS + ADVERSARY EMULATION                                                     [WEEKS 22–27]     │
│  ● Weeks 22–23: Red Team Methodology, Tiered C2 Architecture, OPSEC & Weaponization                 [6 Light • 4 Full]     │
│  ● Weeks 24–25: Command & Control with Sliver, Listeners, Beacons, In-Memory Execution & Pivoting    [2 Light • 8 Full]     │
│  ● Weeks 26–27: Full Authorized Adversary Emulation Exercise (Recon → Domain Admin → Deconfliction)  [2 Light • 8 Full]     │
│  📌 DELIVERABLE 5: Full Red Team Engagement Report (Executive Summary + ATT&CK Matrix + Blue Deconfliction)               │
└──────────────────────────────────────────────────┬────────────────────────────────────────────────────────────────────────┘
                                                   ▼
┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│  PHASE 6: BLUE TEAM + SOC + THREAT HUNTING                                                              [WEEKS 28–32]     │
│  ● Week 28: Security Telemetry & Endpoint Visibility (Sysmon, Windows Event Logs, Linux Auditd)     [2 Light • 3 Full]     │
│  ● Weeks 29–30: SIEM Architecture (Wazuh/Elastic) & Detection Engineering with Sigma Rules          [3 Light • 7 Full]     │
│  ● Weeks 31–32: Threat Hunting Methodologies & Incident Response Triage (PICERL)                    [3 Light • 7 Full]     │
│  📌 DELIVERABLE 6: SOC & Detection Engineering Lab (Wazuh SIEM + Sysmon + Custom Sigma Rule Suite)                       │
└──────────────────────────────────────────────────┬────────────────────────────────────────────────────────────────────────┘
                                                   ▼
┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│  PHASE 7: MALWARE ANALYSIS + DIGITAL FORENSICS                                                          [WEEKS 33–35]     │
│  ● Week 33: Malware Architecture, PE/ELF Headers, Packing & Anti-Analysis                           [4 Light • 1 Full]     │
│  ● Week 34: Static Disassembly (Ghidra), Dynamic Analysis (Procmon, FakeNet-NG) & YARA Rules        [0 Light • 5 Full]     │
│  ● Week 35: Digital Forensics & Incident Reconstruction (Volatility 3, Prefetch, Shimcache, MFT)    [2 Light • 3 Full]     │
│  📌 DELIVERABLE 7: Malware Triage + Forensics Report (Sample Dissection + YARA Rule + Memory Reconstruction)             │
└──────────────────────────────────────────────────┬────────────────────────────────────────────────────────────────────────┘
                                                   ▼
┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│  PHASE 8: SECURITY PROGRAMMING + RUST + TOOL DEVELOPMENT                                                [WEEKS 36–38]     │
│  ● Week 36: Rust Fundamentals for Hackers (Ownership, Borrowing, Structs, Concurrency)              [4 Light • 1 Full]     │
│  ● Week 37: Security Tool Engineering in Rust (Tokio Async Port Scanner, Reqwest Prober, Serde)     [1 Light • 4 Full]     │
│  ● Week 38: Low-Level Security Concepts (Unsafe Rust, FFI, Win32 API Injection, Raw Sockets)        [1 Light • 4 Full]     │
│  📌 DELIVERABLE 8: Personal Security Toolkit (Compiled Rust Utilities + Performance Benchmarks)                           │
└──────────────────────────────────────────────────┬────────────────────────────────────────────────────────────────────────┘
                                                   ▼
┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│  PHASE 9: PURPLE TEAM + AUTOMATION + CAPSTONE                                                           [WEEKS 39–40]     │
│  ● Week 39: Purple Team Integration (Attack → Telemetry → Detection → Retest Loop & Automation)     [2 Light • 3 Full]     │
│  ● Week 40: Final Capstone Enterprise Hybrid Simulation, Defense Engineering & Master Portfolio     [1 Light • 4 Full]     │
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
                         ╚══════════════════════════════════════════════════════════╝"""

# Build 40-Week Schedule Table
schedule_rows = []
for p in phases:
    pnum = p['phase_num']
    pid = p.get('phase_id', f"phase-{pnum:02d}")
    for w in p['weeks']:
        wnum = w['week_num']
        wid = w.get('week_id', f"week-{wnum:02d}")
        days_range = f"Day {w['days'][0]['day_num']:03d}–{w['days'][-1]['day_num']:03d}"
        light_count = sum(1 for d in w['days'] if d.get('tier') == 'light')
        full_count = sum(1 for d in w['days'] if d.get('tier') == 'full')
        tier_str = f"{light_count}L • {full_count}F"
        row = f"| [**Week {wnum:02d}**]({pid}/{wid}/README.md) | {w['week_title']} | Phase {pnum:02d} | `{days_range}` | `{tier_str}` | {w.get('deliverable', '')} |"
        schedule_rows.append(row)
schedule_table = "\n".join(schedule_rows)

# Build 200 Days Master Index Table
day_rows = []
for p in phases:
    pnum = p['phase_num']
    pid = p.get('phase_id', f"phase-{pnum:02d}")
    for w in p['weeks']:
        wnum = w['week_num']
        wid = w.get('week_id', f"week-{wnum:02d}")
        for d in w['days']:
            dnum = d['day_num']
            dtier = d.get('tier', 'light').upper()
            tier_badge = f"`[{dtier}]`"
            row = f"| [**Day {dnum:03d}**](days/day-{dnum:03d}/README.md) | {d['title']} | {tier_badge} | [W{wnum:02d}]({pid}/{wid}/README.md) | [Phase {pnum:02d}]({pid}/README.md) |"
            day_rows.append(row)
day_table = "\n".join(day_rows)

roadmap_content = f"""# 🗺️ CYBERSECURITY MASTER ROADMAP: RED TEAM + BLUE TEAM + RESEARCH + ENGINEERING

> **Master Curriculum:** 40 Weeks • 200 Days • 9 Industry Deliverables  
> **Target:** Advanced Security Practitioner / Purple Team Operator  
> **Curriculum Composition:** 76 Light Days (Theory & Reading) • 124 Full Days (Hands-on Lab & Deliverable)  
> **Standards:** MITRE ATT&CK • Cyber Kill Chain • SANS PICERL • NIST SP 800-61

---

## 🧭 Visual Flow Diagram

```text
{ascii_chart}
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
    
    P8 --> P9
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

## 📅 Master 40-Week Schedule & Tier Allocation

| Week | Title | Phase | Day Span | Tiers (Light/Full) | Milestone Deliverable |
| :--- | :--- | :--- | :---: | :---: | :--- |
{schedule_table}

---

## 📑 200 Days Master Index

| Day | Title | Tier | Week | Phase |
| :---: | :--- | :---: | :---: | :---: |
{day_table}

---

[🔙 Back to Master Dashboard](README.md) | [📊 Master Progress Tracker](PROGRESS.md)
"""

with open(ROADMAP_PATH, 'w', encoding='utf-8') as f:
    f.write(roadmap_content)

print(f"[✓] ROADMAP.md successfully updated with tier allocations and flat day links.")
