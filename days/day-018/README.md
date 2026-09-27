---
day: 18
phase: 1
week: 4
title: "Authentication Architectures — Passwords, Sessions & JSON Web Tokens (JWT)"
tier: light
status: completed
completed_date: "2026-09-27"
---

# DAY 018 — Authentication Architectures — Passwords, Sessions & JSON Web Tokens (JWT)

## Status
🟢 **Completed** (`status: completed`) • **Date:** September 27, 2026

> **Phase 01:** [Core Foundations — Networking + Linux + Windows + Web](../../phase-01-foundations/README.md)  
> **Week 04:** [Web Architecture & Core Protocols](../../phase-01-foundations/week-04-web-architecture/README.md)  
> **Tier:** 💡 **LIGHT (Core Foundations & Theory)**

---

## 🎯 Learning Objectives
Decode and cryptographically verify JWTs and contrast stateful session stores with stateless bearer tokens.

---

## 📚 Topics Covered
* Password hashing algorithms: MD5/SHA vs bcrypt, Argon2, PBKDF2 (work factor, salt)
* Session-based stateful authentication vs Token-based stateless authentication
* JWT structure: Header (Base64Url), Payload (Claims), Signature
* Standard JWT claims (iss, sub, aud, exp, nbf, iat)
* Cryptographic verification of symmetric (HS256) vs asymmetric (RS256) signatures

---

## 📝 Study Notes & Concepts
Authentication architectures: stateful server-side sessions vs stateless JSON Web Tokens (JWT). Analyzed JWT structure (Header.Payload.Signature), cryptographic verification, and common signature bypass pitfalls.

---

## 💻 Practical Commands & Lab Exercises
```bash
echo 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9' | base64 -d
```

---

## 🛡️ Security Perspective & Key Takeaways
> **Core Rule:** JWTs are readable by anyone; encryption is not signing. If the server does not strictly verify the signature using a secure key and algorithm, claims can be forged.

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
