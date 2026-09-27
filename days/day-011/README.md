---
day: 11
phase: 1
week: 3
title: "Windows OS Architecture — User Mode, Kernel Mode & PE Basics"
tier: light
status: completed
completed_date: "2026-09-27"
---

# DAY 011 — Windows OS Architecture — User Mode, Kernel Mode & PE Basics

## Status
🟢 **Completed** (`status: completed`) • **Date:** September 27, 2026

> **Phase 01:** [Core Foundations — Networking + Linux + Windows + Web](../../phase-01-foundations/README.md)  
> **Week 03:** [Windows Internals & PowerShell Security](../../phase-01-foundations/week-03-windows/README.md)  
> **Tier:** 💡 **LIGHT (Core Foundations & Theory)**

---

## 🎯 Learning Objectives
Understand how the Windows kernel isolates process memory and enforces execution boundaries.

---

## 📚 Topics Covered
* Ring 3 (User Mode) vs Ring 0 (Kernel Mode) separation
* Executive subsystems: ntdll.dll, win32k.sys, HAL
* Process architecture: Process ID, PEB, TEB
* Threads, virtual memory allocation, and page protection flags
* Introduction to Portable Executable (PE) headers (MZ, PE signature, sections)

---

## 📝 Study Notes & Concepts
Explored Windows operating system architecture, user mode (Ring 3) vs kernel mode (Ring 0), system call transitions, and Portable Executable (PE) file structure (Headers, Sections, Imports, Exports).

---

## 💻 Practical Commands & Lab Exercises
```bash
Get-Process | Select-Object Id, ProcessName, Path
Get-Service | Where-Object Status -eq 'Running'
```

---

## 🛡️ Security Perspective & Key Takeaways
> **Core Rule:** Understanding normal Windows process hierarchy (smss -> csrss/wininit -> services -> svchost) enables rapid detection of masquerading malware.

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
