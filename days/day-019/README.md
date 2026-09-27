---
day: 19
phase: 1
week: 4
title: "Modern Federated Identity — OAuth 2.0 & OpenID Connect (OIDC)"
tier: full
status: completed
completed_date: "2026-09-27"
---

# DAY 019 — Modern Federated Identity — OAuth 2.0 & OpenID Connect (OIDC)

## Status
🟢 **Completed** (`status: completed`) • **Date:** September 27, 2026

> **Phase 01:** [Core Foundations — Networking + Linux + Windows + Web](../../phase-01-foundations/README.md)  
> **Week 04:** [Web Architecture & Core Protocols](../../phase-01-foundations/week-04-web-architecture/README.md)  
> **Tier:** 🔬 **FULL (Hands-on Lab & Deliverable)**

---

## 🎯 Learning Objectives
Map out the OAuth 2.0 Authorization Code flow and identify failure points where authorization codes can be intercepted.

---

## 📚 Topics Covered
* OAuth 2.0 roles: Resource Owner, Client, Authorization Server, Resource Server
* Authorization Code Grant Flow step-by-step (with PKCE for public clients)
* Access Tokens vs Refresh Tokens vs ID Tokens
* OpenID Connect (OIDC) identity layer on top of OAuth 2.0
* Common OAuth vulnerabilities: Redirect URI poisoning, CSRF on auth flow, token leakage

---

## 📝 Study Notes & Concepts
Modern federated identity architectures: OAuth 2.0 authorization flows (Authorization Code, PKCE, Client Credentials), token types (Access vs Refresh), and OpenID Connect (OIDC) identity layer.

---

## 💻 Practical Commands & Lab Exercises
```bash
curl -X POST https://auth.target.com/oauth/token -d 'grant_type=authorization_code'
```

---

## 🛡️ Security Perspective & Key Takeaways
> **Core Rule:** OAuth provides delegated authorization (valet key). Loose redirect URI validation or unverified state parameters allow authorization code interception and account takeover.

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
