---
day: 6
phase: 1
week: 2
title: "Linux Filesystem Hierarchy (FHS), Users & Standard Permissions"
tier: light
status: completed
completed_date: "2026-09-27"
---

# DAY 006 — Linux Filesystem Hierarchy (FHS), Users & Standard Permissions

## Status
🟢 **Completed** (`status: completed`) • **Date:** September 27, 2026

> **Phase 01:** [Core Foundations — Networking + Linux + Windows + Web](../../phase-01-foundations/README.md)  
> **Week 02:** [Linux Fundamentals & System Administration](../../phase-01-foundations/week-02-linux/README.md)  
> **Tier:** 💡 **LIGHT (Core Foundations & Theory)**

---

## 🎯 Learning Objectives
Navigate Linux systems with confidence and identify improperly assigned read/write permissions on critical system assets.

---

## 📚 Topics Covered
* Filesystem Hierarchy Standard (/bin, /sbin, /etc, /var, /tmp, /opt)
* User & Group database files (/etc/passwd, /etc/shadow, /etc/group)
* Standard permissions (Read, Write, Execute for User, Group, Others)
* Octal vs symbolic chmod notation
* File ownership management with chown and chgrp

---

## 📝 Study Notes & Concepts
Deconstructed the Linux Filesystem Hierarchy Standard (FHS), user identity model (UID/GID, root as UID 0), standard file permissions (rwx for User, Group, Others), and octal permission math.

---

## 💻 Practical Commands & Lab Exercises
```bash
ls -la /etc/passwd /etc/shadow
stat -c '%a %n' /bin/bash
id
whoami
```

---

## 🛡️ Security Perspective & Key Takeaways
> **Core Rule:** In Linux everything is a file. Overly permissive file rights (especially world-writable configuration files) represent critical privilege escalation vectors.

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
