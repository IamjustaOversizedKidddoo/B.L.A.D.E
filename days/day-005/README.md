---
day: 5
phase: 1
week: 1
title: "Network Traffic Analysis — tcpdump & Wireshark Stream Reconstruction"
tier: full
status: completed
completed_date: "2026-09-27"
---

# DAY 005 — Network Traffic Analysis — tcpdump & Wireshark Stream Reconstruction

## Status
🟢 **Completed** (`status: completed`) • **Date:** September 27, 2026

> **Phase 01:** [Core Foundations — Networking + Linux + Windows + Web](../../phase-01-foundations/README.md)  
> **Week 01:** [Networking & Protocols](../../phase-01-foundations/week-01-networking/README.md)  
> **Tier:** 🔬 **FULL (Hands-on Lab & Deliverable)**

---

## 🎯 Learning Objectives
Capture raw traffic on headless interfaces and extract files, credentials, and conversation streams from PCAPs.

---

## 📚 Topics Covered
* tcpdump CLI capture filters vs display filters
* Berkeley Packet Filters (BPF) syntax
* Wireshark GUI navigation, coloring rules, and conversation statistics
* Follow TCP/UDP Stream analysis
* Detecting anomalous network patterns (port scans, cleartext credentials)

---

## 📝 Study Notes & Concepts
Hands-on packet inspection using tcpdump and Wireshark. Reconstructed TCP streams, isolated credential leaks in cleartext protocols, identified TLS handshakes, and applied Berkeley Packet Filters (BPF).

---

## 💻 Practical Commands & Lab Exercises
```bash
sudo tcpdump -i eth0 -nn -s 0 -w capture.pcap
sudo tcpdump -r capture.pcap 'tcp port 80 and (((ip[2:2] - ((ip[0]&0xf)<<2)) - ((tcp[12:2]>>12)<<2)) != 0)'
```

---

## 🛡️ Security Perspective & Key Takeaways
> **Core Rule:** Packet captures provide ground truth during incidents. Filtering down to specific streams and flags isolates malicious communications rapidly.

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
