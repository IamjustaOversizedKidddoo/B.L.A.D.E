---
day: 2
phase: 1
week: 1
title: "IPv4, IPv6, CIDR Subnetting & Packet Fragmentation"
tier: light
status: completed
completed_date: "2026-09-27"
---

# DAY 002 — IPv4, IPv6, CIDR Subnetting & Packet Fragmentation

## Status
🟢 **Completed** (`status: completed`) • **Date:** September 27, 2026

> **Phase 01:** [Core Foundations — Networking + Linux + Windows + Web](../../phase-01-foundations/README.md)  
> **Week 01:** [Networking & Protocols](../../phase-01-foundations/week-01-networking/README.md)  
> **Tier:** 💡 **LIGHT (Core Foundations & Theory)**

---

## 🎯 Learning Objectives
Perform mental and scripted subnetting, calculate broadcast/network addresses, and diagnose fragmentation attacks.

---

## 📚 Topics Covered
* IPv4 addressing classes and RFC 1918 private scopes
* CIDR notation and bitwise subnet calculations
* IPv6 address format, link-local vs global unicast
* IP fragmentation, MTU, and offset calculations
* Defensive implications of fragmented packets

---

## 📝 Study Notes & Concepts
Mastered IPv4 and IPv6 addressing schemes, CIDR notation, subnet mask calculations, and MTU-driven packet fragmentation. Understood network segmentation boundaries and how subnets isolate broadcast domains.

---

## 💻 Practical Commands & Lab Exercises
```bash
ip addr show
ip route show
ping -s 1472 -M do 192.168.1.1
```

---

## 🛡️ Security Perspective & Key Takeaways
> **Core Rule:** Subnets divide address space into manageable security zones, allowing firewalls and access controls to govern cross-segment traffic.

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
