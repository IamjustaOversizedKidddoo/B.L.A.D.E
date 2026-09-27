---
day: 26
phase: 1
week: 6
title: "Security Workstation Setup — Kali Linux, Shell Customization & Git OPSEC"
tier: light
status: completed
completed_date: "2026-09-27"
---

# DAY 026 — Security Workstation Setup — Kali Linux, Shell Customization & Git OPSEC

## Status
🟢 **Completed** (`status: completed`) • **Date:** September 27, 2026

> **Phase 01:** [Core Foundations — Networking + Linux + Windows + Web](../../phase-01-foundations/README.md)  
> **Week 06:** [Security Tooling Foundation](../../phase-01-foundations/week-06-tooling/README.md)  
> **Tier:** 💡 **LIGHT (Core Foundations & Theory)**

---

## 🎯 Learning Objectives
Establish a reproducible, clean, and OPSEC-safe security testing workstation and workflow.

---

## 📚 Topics Covered
* Kali Linux / Parrot OS architecture and package management
* Terminal productivity: Zsh/Bash aliases, tmux multiplexing, curl/jq workflows
* Git version control for security practitioners: branching, tagging, commit discipline
* Git OPSEC: Avoiding committing private keys, API tokens, and sensitive client scopes (.gitignore)
* Setting up isolated virtual environments in Python (venv)

---

## 📝 Study Notes & Concepts
Security workstation setup: Kali Linux installation, shell environment customization (Zsh/Bash), operational security (OPSEC), snapshot hygiene, and Git workflow security (.gitignore, secret hygiene).

---

## 💻 Practical Commands & Lab Exercises
```bash
sudo apt update && sudo apt -y upgrade
git config --global user.name 'Analyst'
cat .gitignore
```

---

## 🛡️ Security Perspective & Key Takeaways
> **Core Rule:** Kali Linux is a dedicated security workbench. Run it in an isolated VM, take snapshots before major tooling modifications, and never commit API keys or sensitive evidence to Git.

* **Attacker View:** Adversaries abuse implicit trust, default configurations, unauthenticated protocols, and missing verification boundaries.
* **Defender View:** Security practitioners enforce least privilege, segment network boundaries, validate input server-side, and enable comprehensive endpoint and network telemetry.

---

## ✅ Day Checklist
- [x] Studied core theory and technical mechanics
- [x] Analyzed real-world security implications
- [x] Executed practical verification commands in isolated lab
- [x] Documented findings, telemetry, and key takeaways

---

[🔙 Back to Week 06](../../phase-01-foundations/week-06-tooling/README.md) | [📊 Master Progress](../../PROGRESS.md) | [🗺️ Master Roadmap](../../ROADMAP.md)
