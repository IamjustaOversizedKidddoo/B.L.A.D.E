# Threat Model — Enterprise Security Lab Environment

> **Framework:** STRIDE + Attack Tree  
> **Scope:** `192.168.56.0/24` isolated lab subnet  
> **Version:** 1.0.0 (Phase 1)  
> **Last Updated:** Phase 1 completion

---

## 1. What is a Threat Model?

A threat model answers four questions:

1. **What are we building?** — The assets and components of the lab
2. **What can go wrong?** — Threats to those assets
3. **What are we doing about it?** — Controls and mitigations
4. **Did we do a good enough job?** — Validation checks

In a real organization, threat modeling is done before code ships. In a security lab, it is done before VMs are powered on. The goal is not to eliminate every risk, but to understand every risk intentionally.

---

## 2. Assets

| Asset ID | Asset | Classification | Why It Matters |
| :---: | :--- | :--- | :--- |
| A-01 | Lab virtual machines (all 5) | **High** | Compromise could allow tools to test real networks |
| A-02 | Host machine (your computer) | **Critical** | If a VM escapes to the host, your real data is at risk |
| A-03 | Credentials and passwords | **High** | Lab credentials reused on real systems = real breach |
| A-04 | Network isolation (Host-Only) | **Critical** | The primary control preventing external harm |
| A-05 | SIEM log data | **Medium** | Contains real attack patterns — could aid malicious actors |
| A-06 | Evidence and report files | **Medium** | Contains vulnerability details and methodology |
| A-07 | GitHub repository | **Medium** | Accidental push of credentials or sensitive configs |

---

## 3. Threat Actors

In a lab environment, we define threat actors not as external adversaries, but as **failure modes** and **accidental scenarios**:

| Actor | Description | Likelihood | Impact |
| :--- | :--- | :---: | :---: |
| **Misconfiguration** | VM bridged to physical network instead of Host-Only | Medium | Critical |
| **Credential Reuse** | Lab passwords used on real accounts | Low | High |
| **Repository Leak** | Sensitive configs accidentally committed to GitHub | Low | High |
| **VM Escape** | Vulnerability in VirtualBox/VMware exploited from inside VM | Very Low | Critical |
| **Scope Creep** | Testing outside the authorized `192.168.56.0/24` range | Medium | High |
| **Malware Escape** | Downloading and running real malware without isolation | Low | High |

---

## 4. STRIDE Analysis

STRIDE is a threat categorization framework developed by Microsoft:
- **S**poofing, **T**ampering, **R**epudiation, **I**nformation Disclosure, **D**enial of Service, **E**levation of Privilege

### 4.1 Spoofing

| Threat | Component Affected | Control |
| :--- | :--- | :--- |
| IP spoofing within the lab subnet | All VMs | Suricata monitors for ARP anomalies; static IP assignments prevent DHCP-based spoofing |
| Kali presenting itself as a legitimate server | Linux Server, Windows Endpoint | Sysmon and auditd log all connection origins; Wazuh alerts on unexpected source IPs |

---

### 4.2 Tampering

| Threat | Component Affected | Control |
| :--- | :--- | :--- |
| Attacker modifying SIEM logs to hide activity | Wazuh | Log integrity monitoring enabled in Wazuh; SHA-256 evidence hashing |
| VM snapshots not taken — state corrupted after exercises | All VMs | **Mandatory:** snapshot before and after every exercise (documented in setup guides) |
| GitHub commit of modified config without review | Repository | `.gitignore` blocks sensitive files; branch protection rules recommended |

---

### 4.3 Repudiation

| Threat | Component Affected | Control |
| :--- | :--- | :--- |
| No record of what actions were performed during exercises | All | Wazuh stores all agent telemetry; evidence collection scripts capture command output with timestamps |
| Terminal session not recorded | Kali | Use `script` or `asciinema` to record terminal sessions for evidence |

---

### 4.4 Information Disclosure

| Threat | Component Affected | Control |
| :--- | :--- | :--- |
| Lab credentials exposed in GitHub commits | Repository | `.gitignore` exclusions; pre-commit scan recommended |
| Vulnerable application accessible from real network | Web Lab | Host-Only adapter only; no Bridged adapter; firewall rules verified |
| SIEM dashboard accessible from outside lab | Monitoring | Port 5601 listens only on `192.168.56.50` — not reachable from internet |

---

### 4.5 Denial of Service

| Threat | Component Affected | Control |
| :--- | :--- | :--- |
| Aggressive scanning crashes target VM | Linux Server, Windows Endpoint, Web Lab | Lab exercises use rate-limited scanning parameters; VMs can be restored from snapshots |
| SIEM overwhelmed by log volume during stress tests | Wazuh | Log rate limiting configured; SIEM runs on dedicated VM |
| Host machine runs out of RAM | All VMs | Start with 2-3 VMs at a time; minimum 16GB host RAM documented |

---

### 4.6 Elevation of Privilege

| Threat | Component Affected | Control |
| :--- | :--- | :--- |
| Lab exercise escalates privileges on host machine | Host | VMs run as non-root VirtualBox processes on the host; VM isolation relies on hypervisor security |
| Student inadvertently uses admin credentials on real production systems | Real systems | Lab credentials are unique strings not matching any real account — documented in setup guide |

---

## 5. Attack Tree — Primary Risk: Network Isolation Failure

```
GOAL: Lab traffic reaches real network or internet
    │
    ├── VM has Bridged adapter enabled
    │       ├── Accidentally set during VM creation ← MOST LIKELY
    │       └── Changed after initial setup
    │
    ├── Host machine forwards lab traffic
    │       ├── IP routing enabled on host OS
    │       └── VPN client on host routes lab traffic externally
    │
    └── VM escape via hypervisor vulnerability
            ├── Known CVE in VirtualBox/VMware version in use
            └── Guest-to-host attack via shared folder or clipboard
```

**Mitigations:**
- Verify adapter type in VM settings before every session (procedure documented in `setup/networking/`)
- Verify isolation with `ping 8.8.8.8` from each target VM — must fail
- Keep VirtualBox/VMware updated

---

## 6. Controls Summary

| Control | Category | Implementation | Verified By |
| :--- | :--- | :--- | :--- |
| Network isolation | Preventive | Host-Only adapter; no default gateway on targets | `ping 8.8.8.8` → fail |
| Static IP assignment | Preventive | Netplan/nmcli on Linux; manual on Windows | `ip a` / `ipconfig` |
| No internet route on targets | Preventive | Missing default gateway | `ip route` → no default |
| `.gitignore` credential exclusion | Preventive | `.gitignore` patterns | `git status` before push |
| VM snapshots | Corrective | VirtualBox Snapshot Manager | Snapshot names logged |
| Wazuh log integrity | Detective | File integrity monitoring rules | Wazuh dashboard |
| Evidence SHA-256 hashing | Detective | `scripts/evidence/collect.py` | Hash verification |
| Suricata IDS | Detective | Network-level anomaly detection | Wazuh alert integration |
| Scope documentation | Preventive | This document + SECURITY.md | Checklist in setup guide |

---

## 7. Security Assumptions (Explicit)

The following assumptions must hold for this threat model to be valid:

1. The host machine is not compromised before lab deployment.
2. VirtualBox/VMware version is current and unpatched vulnerabilities are not known against it.
3. Lab credentials are **not reused** on any external system.
4. The private `192.168.56.0/24` subnet is not routed anywhere outside the host machine.
5. All GitHub commits are reviewed before push — no automated CI push of untested configs.
6. Exercises are performed only on VMs within the authorized range.
7. Real malware samples are **not** run in this lab without an additional isolated analysis environment (e.g., a dedicated REMnux/FlareVM environment or a cloud sandbox).

---

## 8. Out of Scope

The following are explicitly **out of scope** for this lab:

- Attacking any system outside `192.168.56.0/24`
- Testing against cloud infrastructure (AWS, Azure, GCP) that is not explicitly provisioned for this purpose
- Running real ransomware, worms, or self-propagating malware
- Bypassing virtualization to test host OS vulnerabilities
- Social engineering real people

---

## 9. Residual Risk Acceptance

| Risk | Residual Likelihood | Accepted? | Notes |
| :--- | :---: | :---: | :--- |
| VM escape via 0-day in VirtualBox | Very Low | ✅ Yes | Mitigated by keeping hypervisor updated; residual risk accepted |
| Lab credential reuse | Low | ✅ Yes | Mitigated by documented password policy in setup guide |
| Accidental out-of-scope scanning | Low | ✅ Yes | Mitigated by documented scope; Kali NAT adapter cannot reach lab targets |

---

[← Architecture](architecture.md) | [← IP Plan](ip-address-plan.md) | [Back to README](../README.md)
