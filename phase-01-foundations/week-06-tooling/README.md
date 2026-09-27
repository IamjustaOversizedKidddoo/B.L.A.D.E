# WEEK 06 — Security Tooling Foundation

> **Phase:** [Phase 01 — Core Foundations — Networking + Linux + Windows + Web](../README.md)  
> **Status:** 🟢 Completed
> **Progress:** `████████████████████` 100% (5 / 5 Days Completed)  
> **Curriculum Tiers:** 1 Light (Theory & Reading) • 4 Full (Hands-on Lab & Deliverable)

---

## 🎯 Weekly Objective
Build operational proficiency with essential security toolchains, intercepting proxies, scanning engines, and scripting for automation. Establish the foundational laboratory workbench for offensive and defensive operations.

## 📅 Schedule of Days
- [x] [🟢 Day 026: Security Workstation Setup — Kali Linux, Shell Customization & Git OPSEC](../../days/day-026/README.md) `[LIGHT]`
- [x] [🟢 Day 027: Network Scanning & Port Enumeration with Nmap](../../days/day-027/README.md) `[FULL]`
- [x] [🟢 Day 028: Web Application Interception with Burp Suite](../../days/day-028/README.md) `[FULL]`
- [x] [🟢 Day 029: Python for Security Practitioners — Sockets, Requests & Automation](../../days/day-029/README.md) `[FULL]`
- [x] [🟢 Day 030: Phase 1 Capstone Deliverable — Security Lab Environment](../../days/day-030/README.md) `[FULL]`

---

## 🧰 Tools & Utilities
`Kali Linux`, `Nmap`, `Burp Suite Community`, `Git`, `Python 3`, `VirtualBox / VMware`, `Docker`, `tcpdump`, `curl`, `ss`, `ip`

## 🧠 Major Concepts Mastered
* **Kali Linux Workbench:** Set up as an isolated VM with dual network adapters (NAT adapter for internet downloads/updates; Host-Only adapter for safe, zero-leak testing). Snapshot discipline enforced prior to package modifications.
* **Network Scanning with Nmap:** TCP SYN stealth scan mechanics (`-sS`), version detection (`-sV`), OS fingerprinting (`-O`), and Nmap Scripting Engine (`NSE`). Practice restricted strictly to local VMs and `scanme.nmap.org`.
* **Intercepting Proxies with Burp Suite:** Local proxy listener setup on `127.0.0.1:8080`, PortSwigger CA certificate installation, request inspection, Repeater request replay, and Intruder fuzzing concepts.
* **Security Automation with Python:** Writing custom socket port checkers, executing HTTP requests, handling headers/cookies, and parsing structured API responses.
* **Evidence Collection & Forensic Integrity:** NIST SP 800-86 integration: maintaining timestamped case folders, capturing raw tool outputs, calculating cryptographic hashes (SHA-256) of evidence, and keeping detailed command logs.
* **Git OPSEC:** Proper `.gitignore` usage, preventing accidental credential or sensitive target data commits.

---

## 🔬 Weekly Hands-on Lab & Deliverable
* **[Deliverable 1: Multi-OS Security Lab Environment](../../projects/project-01-security-lab-environment/README.md)**  
  Provisioned Kali Linux, target Linux server, target Windows evaluation machine, and containerized vulnerable web applications on an isolated private virtual network (`192.168.56.0/24`). Verified zero packet leakage to production networks.

---

## 🔍 Weekly Review & Reflection

### Concepts Mastered
* How the eight tooling topics connect: Kali Linux provides the environment, networking utilities offer quick checks, Nmap identifies attack surface, Burp intercepts web requests, Python and Bash automate workflows, Git tracks work safely, and evidence collection ensures forensic reproducibility.
* The imperative rule of testing: only scan and test systems owned or explicitly authorized.

### Weak Areas & Topics to Review Before Phase 2
* SUID/SGID bit manipulation and shell breakouts (`man chmod`).
* SSH server key hardening (`sshd_config`).
* PowerShell pipeline object passing and WMI queries (Microsoft Learn: "PowerShell 101").
* Windows registry hives and Run key persistence.
* Windows token privileges, integrity levels, and UAC mechanics.
* Deepening Nmap NSE scripting and Burp Suite extension workflows via official sources.

---

[🔙 Back to Phase 01](../README.md) | [📊 Master Progress](../../PROGRESS.md) | [🗺️ Master Roadmap](../../ROADMAP.md)
