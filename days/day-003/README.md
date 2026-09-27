---
day: 3
phase: 1
week: 1
title: "Core Protocols — ARP, ICMP, DHCP, NAT & Routing Mechanics"
tier: light
status: completed
completed_date: "2026-09-27"
---

# DAY 003 — Core Protocols — ARP, ICMP, DHCP, NAT & Routing Mechanics

## Status
🟢 **Completed** (`status: completed`) • **Date:** September 27, 2026

> **Phase 01:** [Core Foundations — Networking + Linux + Windows + Web](../../phase-01-foundations/README.md)  
> **Week 01:** [Networking & Protocols](../../phase-01-foundations/week-01-networking/README.md)  
> **Tier:** 💡 **LIGHT (Core Foundations & Theory)**

---

## 🎯 Learning Objectives
Map out how hosts discover gateways, resolve physical addresses, and how Layer 2 spoofing works.

---

## 📚 Topics Covered
* Address Resolution Protocol (ARP) mechanics and ARP cache poisoning
* ICMP message types (Echo, Destination Unreachable, TTL Exceeded)
* DHCP DORA process and DHCP starvation
* Network Address Translation (SNAT, DNAT, PAT)
* Static routing vs Dynamic routing (OSPF, BGP basics)

---

## 📝 Study Notes & Concepts
Investigated fundamental link and network layer protocols: ARP (MAC address discovery), ICMP (diagnostics & errors), DHCP (dynamic IP leasing), NAT (private to public translation), and hop-by-hop packet routing mechanics.

---

## 💻 Practical Commands & Lab Exercises
```bash
ip neigh show
traceroute -n 8.8.8.8
ping -c 4 1.1.1.1
```

---

## 🛡️ Security Perspective & Key Takeaways
> **Core Rule:** Unauthenticated protocols like ARP and DHCP trust replies without proof, making ARP spoofing and rogue DHCP servers a classic local attack vector.

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
