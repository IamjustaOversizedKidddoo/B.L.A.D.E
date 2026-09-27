---
day: 21
phase: 1
week: 5
title: "API Architectures, RESTful Conventions & GraphQL Introspection"
tier: light
status: completed
completed_date: "2026-09-27"
---

# DAY 021 — API Architectures, RESTful Conventions & GraphQL Introspection

## Status
🟢 **Completed** (`status: completed`) • **Date:** September 27, 2026

> **Phase 01:** [Core Foundations — Networking + Linux + Windows + Web](../../phase-01-foundations/README.md)  
> **Week 05:** [Web Security Fundamentals](../../phase-01-foundations/week-05-web-security/README.md)  
> **Tier:** 💡 **LIGHT (Core Foundations & Theory)**

---

## 🎯 Learning Objectives
Enumerate REST and GraphQL APIs, query schema introspection, and map hidden endpoints.

---

## 📚 Topics Covered
* API request methods, JSON payloads, and status code standards
* API attack surfaces: Documentation endpoints (/swagger, /api-docs), hidden routes
* GraphQL core concepts: Schemas, Queries, Mutations, Resolvers
* GraphQL Introspection query mechanics
* API rate limiting, authentication headers (Bearer, API-Key)

---

## 📝 Study Notes & Concepts
API architectures and security: RESTful endpoint conventions, GraphQL schemas and introspection queries, HTTP verb tampering, and Broken Object Level Authorization (BOLA/IDOR).

---

## 💻 Practical Commands & Lab Exercises
```bash
curl -X POST -H 'Content-Type: application/json' -d '{"query":"{__schema{types{name}}}"}' http://target.com/graphql
```

---

## 🛡️ Security Perspective & Key Takeaways
> **Core Rule:** BOLA/IDOR occurs when an API checks if a user is logged in, but fails to check whether that specific user owns the requested object identifier.

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
