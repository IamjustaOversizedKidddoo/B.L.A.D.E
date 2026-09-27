---
day: 20
phase: 1
week: 4
title: "Web Infrastructure — Reverse Proxies, CDNs, WebSockets & APIs"
tier: full
status: completed
completed_date: "2026-09-27"
---

# DAY 020 — Web Infrastructure — Reverse Proxies, CDNs, WebSockets & APIs

## Status
🟢 **Completed** (`status: completed`) • **Date:** September 27, 2026

> **Phase 01:** [Core Foundations — Networking + Linux + Windows + Web](../../phase-01-foundations/README.md)  
> **Week 04:** [Web Architecture & Core Protocols](../../phase-01-foundations/week-04-web-architecture/README.md)  
> **Tier:** 🔬 **FULL (Hands-on Lab & Deliverable)**

---

## 🎯 Learning Objectives
Understand how perimeter reverse proxies translate and forward client requests to internal upstream servers.

---

## 📚 Topics Covered
* Reverse proxies (Nginx, HAProxy) role in SSL termination, caching, and routing
* Content Delivery Networks (CDNs) and web application caching behavior
* WebSockets protocol: HTTP Upgrade handshake, bi-directional full-duplex communication
* RESTful API conventions vs RPC architectures
* Header forwarding: X-Forwarded-For, X-Forwarded-Host, X-Real-IP security implications

---

## 📝 Study Notes & Concepts
Web application infrastructure: Reverse proxies (Nginx, HAProxy), TLS termination, load balancing, Content Delivery Networks (CDNs), WebSockets, and API gateway routing.

---

## 💻 Practical Commands & Lab Exercises
```bash
curl -H 'X-Forwarded-For: 127.0.0.1' http://target.internal
wscat -c wss://echo.websocket.events
```

---

## 🛡️ Security Perspective & Key Takeaways
> **Core Rule:** Reverse proxies and CDNs shield backend origins. If backend servers trust client-controlled headers like X-Forwarded-For or are directly reachable around the CDN, security controls fail.

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
