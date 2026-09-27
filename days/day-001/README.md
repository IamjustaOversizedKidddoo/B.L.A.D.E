---
day: 1
phase: 1
week: 1
title: "TCP/IP Architecture, OSI Model & The 3-Way Handshake"
tier: light
status: completed
completed_date: "2026-09-27"
---

# DAY 001 — TCP/IP Architecture, OSI Model & The 3-Way Handshake

## Status
🟢 **Completed** (`status: completed`) • **Date:** September 27, 2026

> **Phase 01:** [Core Foundations — Networking + Linux + Windows + Web](../../phase-01-foundations/README.md)  
> **Week 01:** [Networking & Protocols](../../phase-01-foundations/week-01-networking/README.md)  
> **Tier:** 💡 **LIGHT (Core Foundations & Theory)**

---

## 🎯 Learning Objectives
Understand TCP connection lifecycles, protocol boundaries, and state transitions at the byte level.

---

## 📚 Topics Covered
* TCP/IP vs OSI model comparison
* IPv4/IPv6 packet headers
* TCP 3-way handshake (SYN, SYN-ACK, ACK)
* TCP flags (FIN, RST, PSH, URG)
* Stateful vs stateless protocols

---

## 📝 Study Notes & Concepts
Explored TCP/IP architecture vs the 7-layer OSI model, examining encapsulation, PDU naming (Bits, Frames, Packets, Segments, Data), and the reliable TCP 3-way handshake (SYN, SYN-ACK, ACK). Analyzed connection state transitions and TCP flag mechanics.

---

## 💻 Practical Commands & Lab Exercises
```bash
ss -tulpn
netstat -ant
curl -I http://example.com
```

---

## 🛡️ Security Perspective & Key Takeaways
> **Core Rule:** TCP establishes a stateful, verified connection before sending data. Packet inspection reveals sequence numbers and acknowledgment states.

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
