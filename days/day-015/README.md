---
day: 15
phase: 1
week: 3
title: "Windows Auditing — Security Event Logs, Sysmon & Endpoint Visibility"
tier: full
status: completed
completed_date: "2026-09-27"
---

# DAY 015 — Windows Auditing — Security Event Logs, Sysmon & Endpoint Visibility

## Status
🟢 **Completed** (`status: completed`) • **Date:** September 27, 2026

> **Phase 01:** [Core Foundations — Networking + Linux + Windows + Web](../../phase-01-foundations/README.md)  
> **Week 03:** [Windows Internals & PowerShell Security](../../phase-01-foundations/week-03-windows/README.md)  
> **Tier:** 🔬 **FULL (Hands-on Lab & Deliverable)**

---

## 🎯 Learning Objectives
Install and configure Sysmon with an industry-standard configuration (SwiftOnSecurity) and analyze security telemetry in Event Viewer.

---

## 📚 Topics Covered
* Windows Event Log architecture (.evtx format, System, Security, Application channels)
* Critical Security Event IDs: 4624 (Logon), 4625 (Failed Logon), 4688 (Process Creation), 4672 (Admin Logon)
* Enabling Advanced Audit Policies (Command Line Auditing)
* System Monitor (Sysmon) architecture, configuration schema, and filtering
* Key Sysmon Event IDs: EID 1 (Process Create), EID 3 (Network Connect), EID 10 (Process Access)

---

## 📝 Study Notes & Concepts
Windows auditing architecture: Security Event Log analysis (Event IDs 4624, 4625, 4720, 4732, 4688, 7045, 1102), Sysmon installation and configuration, Script Block Logging (4104), and endpoint visibility.

---

## 💻 Practical Commands & Lab Exercises
```bash
Get-WinEvent -FilterHashtable @{LogName='Security';Id=4624} -MaxEvents 5
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-Sysmon/Operational';Id=1} -MaxEvents 5
```

---

## 🛡️ Security Perspective & Key Takeaways
> **Core Rule:** Detection requires telemetry to be enabled before an incident. Sysmon Event ID 1 (Process Create with hashes and parent PIDs) is the gold standard for endpoint visibility.

* **Attacker View:** Adversaries abuse implicit trust, default configurations, unauthenticated protocols, and missing verification boundaries.
* **Defender View:** Security practitioners enforce least privilege, segment network boundaries, validate input server-side, and enable comprehensive endpoint and network telemetry.

---

## ✅ Day Checklist
- [x] Studied core theory and technical mechanics
- [x] Analyzed real-world security implications
- [x] Executed practical verification commands in isolated lab
- [x] Documented findings, telemetry, and key takeaways

---

[🔙 Back to Week 03](../../phase-01-foundations/week-03-windows/README.md) | [📊 Master Progress](../../PROGRESS.md) | [🗺️ Master Roadmap](../../ROADMAP.md)
