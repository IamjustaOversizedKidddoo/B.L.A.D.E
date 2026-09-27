---
day: 25
phase: 1
week: 5
title: "SQL Injection Fundamentals — Error-based, Union-based & Blind"
tier: full
status: completed
completed_date: "2026-09-27"
---

# DAY 025 — SQL Injection Fundamentals — Error-based, Union-based & Blind

## Status
🟢 **Completed** (`status: completed`) • **Date:** September 27, 2026

> **Phase 01:** [Core Foundations — Networking + Linux + Windows + Web](../../phase-01-foundations/README.md)  
> **Week 05:** [Web Security Fundamentals](../../phase-01-foundations/week-05-web-security/README.md)  
> **Tier:** 🔬 **FULL (Hands-on Lab & Deliverable)**

---

## 🎯 Learning Objectives
Explain why SQL injection occurs and construct safe UNION and Blind SQLi payloads against an authorized database lab.

---

## 📚 Topics Covered
* SQL query construction and the flaw of string concatenation
* Authentication bypass payloads (' OR 1=1 --)
* UNION-based SQLi: Column count determination and data type matching
* Error-based SQLi: Extracting data through database engine error messages
* Blind SQLi concepts: Boolean-based true/false response differences and time delays
* Defenses: Parameterized queries (Prepared Statements), ORMs

---

## 📝 Study Notes & Concepts
SQL Injection (SQLi) root causes and attack classes: In-band Error-based, UNION-based data extraction, and Inferential Blind SQLi (Boolean and Time-based). Defenses: parameterized queries (prepared statements).

---

## 💻 Practical Commands & Lab Exercises
```bash
curl 'http://target.com/items?id=1%20UNION%20SELECT%20null,username,password%20FROM%20users--'
```

---

## 🛡️ Security Perspective & Key Takeaways
> **Core Rule:** SQLi occurs when untrusted input is concatenated directly into SQL query strings. Parameterized queries completely eliminate SQLi by treating input strictly as data, never executable code.

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
