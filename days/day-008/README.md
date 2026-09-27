---
day: 8
phase: 1
week: 2
title: "Systemd Services, Daemons, Cron Tasks & SSH Key Hardening"
tier: light
status: completed
completed_date: "2026-09-27"
---

# DAY 008 — Systemd Services, Daemons, Cron Tasks & SSH Key Hardening

## Status
🟢 **Completed** (`status: completed`) • **Date:** September 27, 2026

> **Phase 01:** [Core Foundations — Networking + Linux + Windows + Web](../../phase-01-foundations/README.md)  
> **Week 02:** [Linux Fundamentals & System Administration](../../phase-01-foundations/week-02-linux/README.md)  
> **Tier:** 💡 **LIGHT (Core Foundations & Theory)**

---

## 🎯 Learning Objectives
Configure persistent daemons, schedule automated tasks securely, and establish cryptographic SSH access.

---

## 📚 Topics Covered
* Systemd unit files (.service, .timer, .target) and systemctl management
* Creating and securing custom systemd services
* Cron daemon architecture (/etc/crontab, /etc/cron.*, /var/spool/cron)
* SSH architecture, sshd_config hardening (disabling root login, password auth)
* Ed25519 vs RSA SSH key generation and authorized_keys file security

---

## 📝 Study Notes & Concepts
Studied systemd daemon architecture, unit files, service management via systemctl, scheduled automation with cron (/etc/crontab, /etc/cron.d/), and OpenSSH key-based authentication hardening.

---

## 💻 Practical Commands & Lab Exercises
```bash
systemctl list-units --type=service --state=running
cat /etc/crontab
crontab -l
sudo sshd -T | grep -E 'permitrootlogin|passwordauthentication'
```

---

## 🛡️ Security Perspective & Key Takeaways
> **Core Rule:** Services and scheduled tasks are primary persistence mechanisms. A root-owned cron job that executes a script writable by unprivileged users grants root access.

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
