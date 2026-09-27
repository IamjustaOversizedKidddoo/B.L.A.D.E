---
day: 22
phase: 1
week: 5
title: "Cross-Site Scripting (XSS) Core Mechanics — Stored, Reflected & DOM"
tier: light
status: completed
completed_date: "2026-09-27"
---

# DAY 022 — Cross-Site Scripting (XSS) Core Mechanics — Stored, Reflected & DOM

## Status
🟢 **Completed** (`status: completed`) • **Date:** September 27, 2026

> **Phase 01:** [Core Foundations — Networking + Linux + Windows + Web](../../phase-01-foundations/README.md)  
> **Week 05:** [Web Security Fundamentals](../../phase-01-foundations/week-05-web-security/README.md)  
> **Tier:** 💡 **LIGHT (Core Foundations & Theory)**

---

## 🎯 Learning Objectives
Distinguish between server-reflected, persistent, and client-side DOM XSS vulnerabilities with safe demonstration payloads.

---

## 📚 Topics Covered
* XSS definition and execution context in the browser
* Reflected XSS: Parameter reflection without encoding
* Stored XSS: Database persistence and payload delivery to multiple users
* DOM-based XSS: Sources and Sinks (innerHTML, eval, document.write)
* Defenses: Context-aware output encoding, input validation, CSP

---

## 📝 Study Notes & Concepts
Cross-Site Scripting (XSS) core mechanics: Reflected XSS (immediate reflection), Stored XSS (persistent database injection), and DOM-based XSS (client-side execution via sources and sinks).

---

## 💻 Practical Commands & Lab Exercises
```bash
curl -s 'http://target.com/search?q=<script>alert(1)</script>' | grep 'script'
```

---

## 🛡️ Security Perspective & Key Takeaways
> **Core Rule:** XSS occurs when untrusted user input is rendered into HTML context without context-aware output encoding. It allows session hijacking, DOM manipulation, and credential harvesting.

* **Attacker View:** Adversaries abuse implicit trust, default configurations, unauthenticated protocols, and missing verification boundaries.
* **Defender View:** Security practitioners enforce least privilege, segment network boundaries, validate input server-side, and enable comprehensive endpoint and network telemetry.

---

## ✅ Day Checklist
- [x] Studied core theory and technical mechanics
- [x] Analyzed real-world security implications
- [x] Executed practical verification commands in isolated lab
- [x] Documented findings, telemetry, and key takeaways

---

[🔙 Back to Week 05](../../phase-01-foundations/week-05-web-security/README.md) | [📊 Master Progress](../../PROGRESS.md) | [🗺️ Master Roadmap](../../ROADMAP.md)
