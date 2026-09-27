---
day: 4
phase: 1
week: 1
title: "Transport & Application Layers — DNS, HTTP/HTTPS & TLS Cryptography"
tier: light
status: completed
completed_date: "2026-09-27"
---

# DAY 004 — Transport & Application Layers — DNS, HTTP/HTTPS & TLS Cryptography

## Status
🟢 **Completed** (`status: completed`) • **Date:** September 27, 2026

> **Phase 01:** [Core Foundations — Networking + Linux + Windows + Web](../../phase-01-foundations/README.md)  
> **Week 01:** [Networking & Protocols](../../phase-01-foundations/week-01-networking/README.md)  
> **Tier:** 💡 **LIGHT (Core Foundations & Theory)**

---

## 🎯 Learning Objectives
Trace DNS resolution end-to-end and inspect encrypted TLS handshakes including Server Hello and Certificate exchange.

---

## 📚 Topics Covered
* TCP vs UDP performance and reliability trade-offs
* DNS hierarchy, query types (A, AAAA, MX, TXT, NS), and recursive vs iterative resolution
* HTTP request/response lifecycle, status codes, and HTTP/1.1 vs HTTP/2
* TLS 1.2 vs TLS 1.3 handshake mechanics
* Public Key Infrastructure (PKI), digital certificates, and Cipher Suites

---

## 📝 Study Notes & Concepts
Studied transport and application layer protocols: DNS name resolution hierarchy (Root -> TLD -> Authoritative), HTTP request/response methods and status codes, and TLS cryptographic handshake (asymmetric key exchange, certificates, symmetric session cipher).

---

## 💻 Practical Commands & Lab Exercises
```bash
dig @8.8.8.8 example.com +trace
openssl s_client -connect example.com:443 -servername example.com
```

---

## 🛡️ Security Perspective & Key Takeaways
> **Core Rule:** Plain HTTP exposes all data in cleartext. TLS encrypts application payloads, but DNS lookups and SNI headers still reveal requested destinations.

* **Attacker View:** Adversaries abuse implicit trust, default configurations, unauthenticated protocols, and missing verification boundaries.
* **Defender View:** Security practitioners enforce least privilege, segment network boundaries, validate input server-side, and enable comprehensive endpoint and network telemetry.

---

## ✅ Day Checklist
- [x] Studied core theory and technical mechanics
- [x] Analyzed real-world security implications
- [x] Executed practical verification commands in isolated lab
- [x] Documented findings, telemetry, and key takeaways

---

[🔙 Back to Week 01](../../phase-01-foundations/week-01-networking/README.md) | [📊 Master Progress](../../PROGRESS.md) | [🗺️ Master Roadmap](../../ROADMAP.md)
