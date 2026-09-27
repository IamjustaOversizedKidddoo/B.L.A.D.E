---
day: 24
phase: 1
week: 5
title: "Server-Side Request Forgery (SSRF) Mechanics & Cloud Metadata"
tier: full
status: completed
completed_date: "2026-09-27"
---

# DAY 024 — Server-Side Request Forgery (SSRF) Mechanics & Cloud Metadata

## Status
🟢 **Completed** (`status: completed`) • **Date:** September 27, 2026

> **Phase 01:** [Core Foundations — Networking + Linux + Windows + Web](../../phase-01-foundations/README.md)  
> **Week 05:** [Web Security Fundamentals](../../phase-01-foundations/week-05-web-security/README.md)  
> **Tier:** 🔬 **FULL (Hands-on Lab & Deliverable)**

---

## 🎯 Learning Objectives
Understand how attackers pivot through vulnerable backend web services to query internal infrastructure and cloud credentials.

---

## 📚 Topics Covered
* Server-Side Request Forgery (SSRF) concept: Coercing servers into sending outbound requests
* Internal network scanning via SSRF (accessing localhost, 127.0.0.1, internal subnets)
* Cloud Instance Metadata Service (IMDS) targeting: AWS 169.254.169.254, GCP, Azure
* IMDSv1 vs IMDSv2 (Session token requirement via PUT header)
* Defenses: Whitelisting, blocking private IP ranges (RFC 1918), disabling unused URL schemes

---

## 📝 Study Notes & Concepts
Server-Side Request Forgery (SSRF) mechanics: coercing backend web applications into initiating requests to internal systems, localhost services, and cloud instance metadata endpoints (169.254.169.254).

---

## 💻 Practical Commands & Lab Exercises
```bash
curl 'http://target.com/fetch?url=http://169.254.169.254/latest/meta-data/'
```

---

## 🛡️ Security Perspective & Key Takeaways
> **Core Rule:** SSRF breaches the internal perimeter from the outside. In cloud environments, unmitigated SSRF leads to immediate IAM role token theft via the metadata service.

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
