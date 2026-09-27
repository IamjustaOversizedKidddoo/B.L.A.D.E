---
day: 7
phase: 1
week: 2
title: "Special Permissions (SUID, SGID, Sticky Bit) & Process Execution"
tier: light
status: completed
completed_date: "2026-09-27"
---

# DAY 007 — Special Permissions (SUID, SGID, Sticky Bit) & Process Execution

## Status
🟢 **Completed** (`status: completed`) • **Date:** September 27, 2026

> **Phase 01:** [Core Foundations — Networking + Linux + Windows + Web](../../phase-01-foundations/README.md)  
> **Week 02:** [Linux Fundamentals & System Administration](../../phase-01-foundations/week-02-linux/README.md)  
> **Tier:** 💡 **LIGHT (Core Foundations & Theory)**

---

## 🎯 Learning Objectives
Discover all SUID/SGID binaries on a Linux host and understand how privilege transitions occur during binary execution.

---

## 📚 Topics Covered
* Set User ID (SUID) mechanics (octal 4000) and security implications
* Set Group ID (SGID) on directories and executables (octal 2000)
* Sticky Bit on shared directories (/tmp) (octal 1000)
* Process execution context: Real UID vs Effective UID
* Auditing the system for non-standard SUID binaries

---

## 📝 Study Notes & Concepts
Analyzed special Linux execution permissions: SUID (executes with owner privileges), SGID (executes with group privileges), and Sticky Bit (restricts deletion to owner). Evaluated process creation and execve execution contexts.

---

## 💻 Practical Commands & Lab Exercises
```bash
find / -perm -4000 -type f 2>/dev/null
find / -perm -2000 -type f 2>/dev/null
ls -ld /tmp
```

---

## 🛡️ Security Perspective & Key Takeaways
> **Core Rule:** Binaries with the SUID bit set run as root regardless of who invokes them. If an SUID binary allows shell breakouts or arbitrary file reads, it yields instant root.

* **Attacker View:** Adversaries abuse implicit trust, default configurations, unauthenticated protocols, and missing verification boundaries.
* **Defender View:** Security practitioners enforce least privilege, segment network boundaries, validate input server-side, and enable comprehensive endpoint and network telemetry.

---

## ✅ Day Checklist
- [x] Studied core theory and technical mechanics
- [x] Analyzed real-world security implications
- [x] Executed practical verification commands in isolated lab
- [x] Documented findings, telemetry, and key takeaways

---

[🔙 Back to Week 02](../../phase-01-foundations/week-02-linux/README.md) | [📊 Master Progress](../../PROGRESS.md) | [🗺️ Master Roadmap](../../ROADMAP.md)
