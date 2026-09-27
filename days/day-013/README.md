---
day: 13
phase: 1
week: 3
title: "Windows Services, Registry Architecture, Scheduled Tasks & UAC"
tier: light
status: completed
completed_date: "2026-09-27"
---

# DAY 013 — Windows Services, Registry Architecture, Scheduled Tasks & UAC

## Status
🟢 **Completed** (`status: completed`) • **Date:** September 27, 2026

> **Phase 01:** [Core Foundations — Networking + Linux + Windows + Web](../../phase-01-foundations/README.md)  
> **Week 03:** [Windows Internals & PowerShell Security](../../phase-01-foundations/week-03-windows/README.md)  
> **Tier:** 💡 **LIGHT (Core Foundations & Theory)**

---

## 🎯 Learning Objectives
Query and inspect service binary paths, scheduled task configurations, and registry values.

---

## 📚 Topics Covered
* Windows Service Control Manager (SCM), service accounts (LocalSystem, NetworkService)
* Windows Registry structure (HKLM, HKCU, HKCR)
* Common persistence autostart keys (Run, RunOnce, Winlogon)
* Task Scheduler mechanics, XML definition files, and triggers
* User Account Control (UAC) architecture, integrity levels (Low, Medium, High, System)

---

## 📝 Study Notes & Concepts
Analyzed Windows Services (services.exe / SCM), Registry hive architecture (HKLM, HKCU), Run/RunOnce keys, Scheduled Tasks (schtasks / Task Scheduler), and User Account Control (UAC) integrity levels.

---

## 💻 Practical Commands & Lab Exercises
```bash
Get-ItemProperty HKLM:\Software\Microsoft\Windows\CurrentVersion\Run
Get-ScheduledTask
sc.exe query type= service
```

---

## 🛡️ Security Perspective & Key Takeaways
> **Core Rule:** Persistence and privilege escalation on Windows heavily center on weak service permissions, unquoted service paths, hijacked registry run keys, and writable scheduled task scripts.

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
