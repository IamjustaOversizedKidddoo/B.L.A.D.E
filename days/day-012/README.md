---
day: 12
phase: 1
week: 3
title: "Windows Security Subsystem — LSASS, SAM, Tokens & ACLs"
tier: light
status: completed
completed_date: "2026-09-27"
---

# DAY 012 — Windows Security Subsystem — LSASS, SAM, Tokens & ACLs

## Status
🟢 **Completed** (`status: completed`) • **Date:** September 27, 2026

> **Phase 01:** [Core Foundations — Networking + Linux + Windows + Web](../../phase-01-foundations/README.md)  
> **Week 03:** [Windows Internals & PowerShell Security](../../phase-01-foundations/week-03-windows/README.md)  
> **Tier:** 💡 **LIGHT (Core Foundations & Theory)**

---

## 🎯 Learning Objectives
Examine token privileges (e.g. SeDebugPrivilege) and evaluate security descriptors on files and registry keys.

---

## 📚 Topics Covered
* Local Security Authority Subsystem Service (LSASS) role and memory space
* Security Account Manager (SAM) database and system hives
* Windows Access Tokens: Primary vs Impersonation tokens, Token Privileges
* Security Identifiers (SIDs): Administrator, SYSTEM, Everyone
* Discretionary ACLs (DACLs) vs System ACLs (SACLs) and Access Control Entries (ACEs)

---

## 📝 Study Notes & Concepts
Deconstructed the Windows Security Subsystem: Local Security Authority Subsystem Service (LSASS), Security Accounts Manager (SAM), Security Identifiers (SIDs), Access Tokens, and Access Control Lists (DACLs/SACLs).

---

## 💻 Practical Commands & Lab Exercises
```bash
whoami /user
whoami /priv
whoami /groups
icacls C:\Windows\System32
```

---

## 🛡️ Security Perspective & Key Takeaways
> **Core Rule:** Every Windows process inherits an access token defining its SID and privileges. Token manipulation (impersonation, delegation) is a cornerstone of Windows privilege escalation.

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
