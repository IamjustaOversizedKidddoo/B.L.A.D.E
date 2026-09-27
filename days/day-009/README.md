---
day: 9
phase: 1
week: 2
title: "Virtual Filesystems (/proc, /sys), Environment Variables & Bash Automation"
tier: full
status: completed
completed_date: "2026-09-27"
---

# DAY 009 — Virtual Filesystems (/proc, /sys), Environment Variables & Bash Automation

## Status
🟢 **Completed** (`status: completed`) • **Date:** September 27, 2026

> **Phase 01:** [Core Foundations — Networking + Linux + Windows + Web](../../phase-01-foundations/README.md)  
> **Week 02:** [Linux Fundamentals & System Administration](../../phase-01-foundations/week-02-linux/README.md)  
> **Tier:** 🔬 **FULL (Hands-on Lab & Deliverable)**

---

## 🎯 Learning Objectives
Query process memory and environment directly from /proc and write robust Bash scripts for system triage.

---

## 📚 Topics Covered
* The /proc pseudo-filesystem: /proc/<PID>/cmdline, environ, fd, maps
* The /sys filesystem and kernel subsystem interaction
* Environment variables (PATH, LD_PRELOAD, LD_LIBRARY_PATH, SHELL)
* Bash scripting essentials: arguments, loops, pipes, conditional tests, exit codes
* Automating administrative and security tasks with shell scripts

---

## 📝 Study Notes & Concepts
Deep dive into virtual pseudo-filesystems (/proc and /sys), environment variable inheritance, PATH search precedence, and defensive/offensive Bash automation scripting.

---

## 💻 Practical Commands & Lab Exercises
```bash
ls -l /proc/$$/fd
cat /proc/$$/environ | tr '\0' '\n'
echo $PATH
```

---

## 🛡️ Security Perspective & Key Takeaways
> **Core Rule:** /proc exposes live memory, open file descriptors, and command-line arguments of every active process, making it essential for incident triage.

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
