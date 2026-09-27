---
day: 10
phase: 1
week: 2
title: "Linux Logging (/var/log, journalctl), Networking & Host Investigation"
tier: full
status: completed
completed_date: "2026-09-27"
---

# DAY 010 — Linux Logging (/var/log, journalctl), Networking & Host Investigation

## Status
🟢 **Completed** (`status: completed`) • **Date:** September 27, 2026

> **Phase 01:** [Core Foundations — Networking + Linux + Windows + Web](../../phase-01-foundations/README.md)  
> **Week 02:** [Linux Fundamentals & System Administration](../../phase-01-foundations/week-02-linux/README.md)  
> **Tier:** 🔬 **FULL (Hands-on Lab & Deliverable)**

---

## 🎯 Learning Objectives
Extract security events from system logs and identify unauthorized processes or suspicious outbound network sockets.

---

## 📚 Topics Covered
* Log architecture: /var/log/auth.log, syslog, dmesg, wtmp, btmp
* Querying systemd journal with journalctl (time filters, unit filters, priority)
* Linux networking CLI: ip, ss, netstat, iptables, nftables
* Live host investigation triage methodology
* Identifying unauthorized users, listening sockets, and active connections

---

## 📝 Study Notes & Concepts
Examined Linux logging architecture (/var/log/auth.log, syslog, journalctl), network socket investigation (ss, lsof), host auditing, and automated baseline triage with baseline_check.sh.

---

## 💻 Practical Commands & Lab Exercises
```bash
journalctl -xeu ssh
grep -i 'failed' /var/log/auth.log
ss -tulpn
lsof -i :22
```

---

## 🛡️ Security Perspective & Key Takeaways
> **Core Rule:** Host investigations rely on order of volatility: capture volatile memory, network sockets, and running processes first before inspecting persistent log files.

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
