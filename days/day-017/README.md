---
day: 17
phase: 1
week: 4
title: "Browser Security Model — Same-Origin Policy (SOP), CORS & CSP"
tier: light
status: completed
completed_date: "2026-09-27"
---

# DAY 017 — Browser Security Model — Same-Origin Policy (SOP), CORS & CSP

## Status
🟢 **Completed** (`status: completed`) • **Date:** September 27, 2026

> **Phase 01:** [Core Foundations — Networking + Linux + Windows + Web](../../phase-01-foundations/README.md)  
> **Week 04:** [Web Architecture & Core Protocols](../../phase-01-foundations/week-04-web-architecture/README.md)  
> **Tier:** 💡 **LIGHT (Core Foundations & Theory)**

---

## 🎯 Learning Objectives
Evaluate browser origin boundaries, identify exploitable CORS configurations, and audit CSP headers.

---

## 📚 Topics Covered
* Same-Origin Policy definition: Protocol, Host, Port matching rules
* DOM access vs Network request cross-origin restrictions
* Cross-Origin Resource Sharing (CORS) architecture: Preflight OPTIONS, Access-Control-Allow-Origin, Credentials
* CORS misconfigurations: Wildcard with credentials, Origin reflection, null origin trust
* Content Security Policy (CSP): Directives (script-src, default-src), nonces, and hashes

---

## 📝 Study Notes & Concepts
The browser security boundary: Same-Origin Policy (SOP) isolating origin tuples (scheme, host, port), Cross-Origin Resource Sharing (CORS) headers and preflight checks, and Content Security Policy (CSP).

---

## 💻 Practical Commands & Lab Exercises
```bash
curl -H 'Origin: https://attacker.com' -I https://api.target.com/data
```

---

## 🛡️ Security Perspective & Key Takeaways
> **Core Rule:** SOP prevents malicious websites from reading data across domains in the browser. Misconfigured CORS (Access-Control-Allow-Origin: * with credentials) completely bypasses this barrier.

* **Attacker View:** Adversaries abuse implicit trust, default configurations, unauthenticated protocols, and missing verification boundaries.
* **Defender View:** Security practitioners enforce least privilege, segment network boundaries, validate input server-side, and enable comprehensive endpoint and network telemetry.

---

## ✅ Day Checklist
- [x] Studied core theory and technical mechanics
- [x] Analyzed real-world security implications
- [x] Executed practical verification commands in isolated lab
- [x] Documented findings, telemetry, and key takeaways

---

[🔙 Back to Week 04](../../phase-01-foundations/week-04-web-architecture/README.md) | [📊 Master Progress](../../PROGRESS.md) | [🗺️ Master Roadmap](../../ROADMAP.md)
