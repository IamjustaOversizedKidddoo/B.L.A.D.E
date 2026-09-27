---
day: 14
phase: 1
week: 3
title: "PowerShell for Security Operations — WMI, CIM & WinRM"
tier: full
status: completed
completed_date: "2026-09-27"
---

# DAY 014 — PowerShell for Security Operations — WMI, CIM & WinRM

## Status
🟢 **Completed** (`status: completed`) • **Date:** September 27, 2026

> **Phase 01:** [Core Foundations — Networking + Linux + Windows + Web](../../phase-01-foundations/README.md)  
> **Week 03:** [Windows Internals & PowerShell Security](../../phase-01-foundations/week-03-windows/README.md)  
> **Tier:** 🔬 **FULL (Hands-on Lab & Deliverable)**

---

## 🎯 Learning Objectives
Automate security telemetry gathering and remote system queries using native PowerShell cmdlets and WMI.

---

## 📚 Topics Covered
* PowerShell execution policies, Cmdlet architecture, and object pipeline
* Windows Management Instrumentation (WMI) and Common Information Model (CIM)
* Querying system hardware, operating system, and processes via WMI/CIM
* Windows Remote Management (WinRM) and PowerShell Remoting (Enter-PSSession)
* PowerShell security features: Script Block Logging (EID 4104), Transcription, AMSI overview

---

## 📝 Study Notes & Concepts
Operational PowerShell for security engineers: Windows Management Instrumentation (WMI), Common Information Model (CIM), WinRM remote management, and script-based host telemetry collection.

---

## 💻 Practical Commands & Lab Exercises
```bash
Get-CimInstance -ClassName Win32_Process
Get-CimInstance -ClassName Win32_Service
Test-WSMan -ComputerName localhost
```

---

## 🛡️ Security Perspective & Key Takeaways
> **Core Rule:** WMI and WinRM provide deep administrative and investigation access across Windows fleets, but adversaries also leverage them for living-off-the-land execution.

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
