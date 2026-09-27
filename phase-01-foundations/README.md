# PHASE 01 — Core Foundations — Networking + Linux + Windows + Web

> **Phase Status:** 🟢 **Completed & Reviewed**  
> **Progress:** `████████████████████` 100% (30 / 30 Days Completed)  
> **Curriculum Composition:** 17 Light Days (Theory) • 13 Full Days (Labs/Deliverables)  
> **Comprehensive Review:** [📖 Read Phase 01 Master Review & Synthesis](PHASE_01_REVIEW.md)

---

## 🎯 Phase Objective
Master the foundational principles of computer networking, Linux systems administration, Windows internals, web application security architectures, and security tooling workbenches.

---

## 📅 Weeks in Phase 01
- [x] **[Week 01: Networking & Protocols](week-01-networking/README.md)** — 5 Days (4 Light, 1 Full) • Deliverable: *Network Traffic Analysis Portfolio (PCAP captures, filter cheatsheet, and Wireshark stream reconstructions)*
- [x] **[Week 02: Linux Fundamentals & System Administration](week-02-linux/README.md)** — 5 Days (3 Light, 2 Full) • Deliverable: *Linux Security Baseline Script & Host Audit Report*
- [x] **[Week 03: Windows Internals & PowerShell Security](week-03-windows/README.md)** — 5 Days (3 Light, 2 Full) • Deliverable: *Windows Host Auditing & Telemetry Baseline (Sysmon config + PowerShell triage script)*
- [x] **[Week 04: Web Architecture & Core Protocols](week-04-web-architecture/README.md)** — 5 Days (3 Light, 2 Full) • Deliverable: *Web Security Header & Architecture Audit Matrix*
- [x] **[Week 05: Web Security Fundamentals](week-05-web-security/README.md)** — 5 Days (3 Light, 2 Full) • Deliverable: *Web Vulnerability Root-Cause & Remediation Notebook*
- [x] **[Week 06: Security Tooling Foundation](week-06-tooling/README.md)** — 5 Days (1 Light, 4 Full) • Deliverable: *Deliverable 1: Security Lab Environment (Kali + Windows Target + Linux Target + Web Lab + GitHub Documentation)*

---

## 📌 Major Deliverables in Phase 01
* [x] **[Deliverable 1: Multi-OS Security Lab Environment](../projects/project-01-security-lab-environment/README.md)** — Isolated VirtualBox/VMware host-only network (`192.168.56.0/24`) with Kali Linux workstation (dual adapters NAT + Host-only), target Linux, target Windows, and vulnerable containerized web applications.

---

## 🧠 Core Competencies & Skills Acquired
* **Networking Ground Truth:** Deep comprehension of TCP 3-way handshake, state transitions, unauthenticated broadcast trust (ARP/DHCP), IP routing, and Wireshark/tcpdump stream reconstruction.
* **Linux Security Administration:** Filesystem FHS, DAC permissions, SUID/SGID audit paths, systemd service management, cron scheduling, `/proc` memory introspection, and volatile host triage.
* **Windows Internals & Auditing:** Process parentage analysis (`services.exe` -> `svchost.exe`), token privileges, registry hive persistence, PowerShell WMI/CIM querying, and key event ID correlation (4624, 4688, 7045, 4104, Sysmon Event 1).
* **Web Security Boundaries:** Stateless HTTP mechanics, session management, cookie attributes (`HttpOnly`, `SameSite`), SOP enforcement, CORS relaxation pitfalls, JWT signing verification, and server-side authorization enforcement.
* **Security Workbench OPSEC:** Kali Linux VM deployment, host-only segregation to prevent leakage, snapshot discipline, Nmap SYN/version scanning, Burp Suite interception, and custom Python automation.

---

## 🏆 Phase Completion Criteria
- [x] All 30 daily journals completed in `days/day-001/` through `days/day-030/`
- [x] All weekly hands-on labs executed and documented
- [x] Phase deliverable completed: [project-01-security-lab-environment](../projects/project-01-security-lab-environment/README.md)
- [x] Comprehensive review and self-test passed: [PHASE_01_REVIEW.md](PHASE_01_REVIEW.md)

---

[🔙 Master Dashboard](../README.md) | [📊 Master Progress](../PROGRESS.md) | [🗺️ Master Roadmap](../ROADMAP.md)
