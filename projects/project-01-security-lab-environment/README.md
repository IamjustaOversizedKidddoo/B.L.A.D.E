# 🛡️ Enterprise Security Lab Environment

> **A professional, reproducible cybersecurity laboratory simulating a small corporate environment for VAPT, SOC operations, Detection Engineering, Threat Hunting, Incident Response, Web Application Security, and Security Automation.**

---

## ⚠️ Security Notice

```
This environment is intended exclusively for authorized security testing,
education, research, and controlled laboratory exercises.

All vulnerable systems MUST remain isolated from untrusted networks.

Never use the techniques demonstrated by this project against systems,
networks, or applications without explicit written authorization.

Unauthorized use of security tools is illegal. You are solely responsible
for ensuring your use of this material complies with all applicable laws.
```

---

## 📋 Overview

This project builds a **MNC-style enterprise security laboratory** inside a completely isolated virtual network. It mirrors the architecture of a real corporate environment: a Windows endpoint, a Linux server, a vulnerable web application, and centralized security monitoring — all connected through a private subnet that cannot reach the public internet.

The lab is designed to teach and demonstrate the **complete security lifecycle**:

```
ATTACK → TELEMETRY → DETECT → INVESTIGATE → CONTAIN → REMEDIATE → VERIFY → DOCUMENT
```

It is not merely an offensive tool collection. It is a **full-spectrum security operations platform**.

---

## 🎯 Objectives

| # | Objective |
| :---: | :--- |
| 1 | Build a reproducible, isolated multi-OS virtual lab |
| 2 | Perform authorized vulnerability assessments against controlled targets |
| 3 | Analyze Windows and Linux endpoint telemetry |
| 4 | Detect, investigate, and respond to simulated security incidents |
| 5 | Practice web application security testing against intentionally vulnerable apps |
| 6 | Build detection rules (Sigma, Wazuh) mapped to MITRE ATT&CK |
| 7 | Automate lab validation, evidence collection, and health checks |
| 8 | Produce professional-grade security reports and documentation |

---

## 🏗️ Architecture

```
                    ┌───────────────────────────────┐
                    │        YOUR HOST MACHINE       │
                    │   (VirtualBox / VMware Host)   │
                    └───────────────┬───────────────┘
                                    │
              ┌─────────────────────┴─────────────────────┐
              │                                           │
       [NAT Adapter]                           [Host-Only Adapter]
    (Internet: Updates only)             (Private Lab: 192.168.56.0/24)
              │                                           │
              ▼                           ┌───────────────┼───────────────┐
       ┌─────────────┐                   │               │               │
       │ Kali Linux  │◄──────────────────►               │               │
       │ 10.0.2.x    │             192.168.56.10          │               │
       │ 192.168.56.10│                  │               │               │
       └─────────────┘                  │               ▼               │
                                        │    ┌─────────────────┐        │
                                        │    │  Windows 10/11  │        │
                                        │    │  192.168.56.30  │        │
                                        │    │  (Enterprise EP)│        │
                                        │    └────────┬────────┘        │
                                        │             │                 ▼
                                        │    ┌────────▼────────┐  ┌───────────────┐
                                        │    │  Linux Server   │  │   Web Lab     │
                                        │    │  192.168.56.20  │  │  192.168.56.40│
                                        │    │  (Ubuntu 22.04) │  │ (DVWA/Juice   │
                                        │    └─────────────────┘  │  Shop/WebGoat)│
                                        │                         └───────────────┘
                                        │
                                        ▼
                              ┌──────────────────────┐
                              │   Security Monitoring │
                              │   192.168.56.50       │
                              │   Wazuh SIEM          │
                              └──────────────────────┘
```

Full architecture documentation: [`architecture/architecture.md`](architecture/architecture.md)

---

## 🖥️ Lab Components

| VM | Role | OS | IP Address | Key Services |
| :--- | :--- | :--- | :---: | :--- |
| **Kali Linux** | Red Team / VAPT Workstation | Kali Rolling | `192.168.56.10` | Nmap, Burp Suite, Wireshark, Python tooling |
| **Linux Server** | Enterprise Application Server | Ubuntu 22.04 LTS | `192.168.56.20` | SSH, Apache/Nginx, auditd, rsyslog |
| **Windows Endpoint** | Enterprise User Workstation | Windows 10/11 Eval | `192.168.56.30` | Sysmon, Event Logging, PowerShell, Defender |
| **Web Lab** | Vulnerable App Target | Docker on Ubuntu | `192.168.56.40` | DVWA, OWASP Juice Shop, WebGoat |
| **Monitoring** | SIEM / Log Aggregator | Ubuntu 22.04 LTS | `192.168.56.50` | Wazuh Manager, Suricata |

---

## 🌐 Network Design

| Property | Value |
| :--- | :--- |
| **Network Subnet** | `192.168.56.0/24` |
| **Subnet Mask** | `255.255.255.0` |
| **Network Type** | Host-Only / Internal (VirtualBox) |
| **Internet Access** | **Blocked** on all targets (Host-Only only) |
| **Kali Internet** | NAT adapter for updates only |
| **Gateway** | `192.168.56.1` (Host VirtualBox adapter) |

Full IP plan: [`architecture/ip-address-plan.md`](architecture/ip-address-plan.md)

---

## 🚀 Installation

### Prerequisites

- Host machine: **16 GB RAM minimum** (32 GB recommended), **200 GB free disk space**
- **VirtualBox 7.x** or **VMware Workstation Pro/Player**
- **Kali Linux ISO** (kali.org/get-kali)
- **Ubuntu Server 22.04 LTS ISO** (ubuntu.com/download/server)
- **Windows 10/11 Evaluation ISO** (microsoft.com/en-us/evalcenter)

### Phase-by-Phase Deployment

```
Phase 1 → Repository + Architecture + Network Design   [YOU ARE HERE]
Phase 2 → Kali Linux + Linux Server setup
Phase 3 → Windows Endpoint configuration
Phase 4 → Web Security Lab deployment
Phase 5 → Centralized Logging
Phase 6 → Security Monitoring (Wazuh)
Phase 7 → Network Monitoring (Suricata)
Phase 8 → Vulnerability Assessment workflows
Phase 9 → Detection Engineering (Sigma/Wazuh rules)
Phase 10→ Incident Response exercises
Phase 11→ Automation scripts
Phase 12→ Professional documentation polish
Phase 13→ Full validation
Phase 14→ Portfolio presentation
```

> **Do not skip phases.** Each phase validates before the next begins.

---

## 📁 Repository Structure

```
project-01-security-lab-environment/
│
├── README.md                    ← This file
├── CHANGELOG.md                 ← Version and change history
├── CONTRIBUTING.md              ← Contribution guidelines
├── SECURITY.md                  ← Security policy
├── .gitignore                   ← Prevents credential/secret commits
│
├── architecture/
│   ├── architecture.md          ← Full architecture document
│   ├── ip-address-plan.md       ← IP allocation table
│   ├── threat-model.md          ← Threat model & assumptions
│   └── network-diagram.md       ← ASCII + described topology
│
├── setup/
│   ├── kali/                    ← Kali configuration & tool inventory
│   ├── windows/                 ← Windows audit policy, Sysmon config
│   ├── linux-server/            ← Ubuntu hardening & service setup
│   ├── web-lab/                 ← Docker Compose for vulnerable apps
│   ├── monitoring/              ← Wazuh deployment guide
│   └── networking/              ← VirtualBox adapter configuration
│
├── scripts/
│   ├── validation/              ← Lab health checks (Python/Bash)
│   ├── evidence/                ← Evidence collection scripts
│   ├── enumeration/             ← Authorized recon scripts
│   ├── logging/                 ← Log collection utilities
│   ├── monitoring/              ← Alert and telemetry tools
│   └── automation/              ← Lab reset and lifecycle scripts
│
├── detection/
│   ├── sigma/                   ← Sigma detection rules
│   ├── wazuh/                   ← Wazuh custom rules & decoders
│   ├── suricata/                ← Suricata IDS rules
│   └── detection-notes/         ← Rule rationale and test cases
│
├── attack-scenarios/
│   ├── reconnaissance/          ← Port scanning, OSINT exercises
│   ├── authentication/          ← Brute-force simulation
│   ├── web-security/            ← OWASP-mapped web attacks
│   ├── endpoint/                ← Windows/Linux post-exploitation
│   └── network/                 ← Traffic analysis exercises
│
├── vulnerability-assessments/
│   ├── network/                 ← Network VA reports
│   ├── web/                     ← Web application VA reports
│   ├── windows/                 ← Windows endpoint assessment
│   └── linux/                   ← Linux server assessment
│
├── incidents/
│   ├── incident-001/            ← Windows authentication failure
│   ├── incident-002/            ← Suspicious PowerShell execution
│   └── incident-003/            ← Web application attack
│
├── reports/
│   ├── vulnerability-reports/   ← Formal VA reports
│   ├── incident-reports/        ← IR reports
│   └── executive-reports/       ← Non-technical summaries
│
├── evidence/
│   ├── screenshots/             ← Named & timestamped screenshots
│   ├── packet-captures/         ← PCAP files with metadata
│   ├── logs/                    ← Exported log samples
│   └── command-output/          ← Terminal session evidence
│
└── docs/
    ├── methodology.md           ← Security testing methodology
    ├── tools.md                 ← Tool inventory with justification
    ├── mitre-mapping.md         ← MITRE ATT&CK mapping
    ├── security-controls.md     ← Controls applied per component
    ├── roles.md                 ← SOC/Red Team/Blue Team role guide
    ├── troubleshooting.md       ← Common issues and fixes
    └── glossary.md              ← Terminology reference
```

---

## 🔐 Security Controls

| Control | Implementation | Documented In |
| :--- | :--- | :--- |
| Network Isolation | Host-Only virtual switch, no internet route | `architecture/architecture.md` |
| No Hardcoded Credentials | Environment variables, `.gitignore` exclusions | `.gitignore`, `SECURITY.md` |
| Evidence Integrity | SHA-256 hash + timestamp naming convention | `scripts/evidence/` |
| Snapshot Hygiene | Before/after snapshots at each phase | `setup/*/README.md` |
| OPSEC Boundary | Explicit no-scan rules beyond `192.168.56.0/24` | `SECURITY.md` |

---

## 📖 Documentation Index

| Document | Description |
| :--- | :--- |
| [`architecture/architecture.md`](architecture/architecture.md) | Full lab architecture and design rationale |
| [`architecture/ip-address-plan.md`](architecture/ip-address-plan.md) | IP allocation and service mapping |
| [`architecture/threat-model.md`](architecture/threat-model.md) | Assets, threats, and security assumptions |
| [`docs/methodology.md`](docs/methodology.md) | Security testing methodology (PTES/OWASP-aligned) |
| [`docs/tools.md`](docs/tools.md) | Tool inventory with purpose and security role |
| [`docs/roles.md`](docs/roles.md) | Which lab components each security role uses |
| [`docs/mitre-mapping.md`](docs/mitre-mapping.md) | MITRE ATT&CK technique coverage |
| [`docs/security-controls.md`](docs/security-controls.md) | Security controls per component |

---

## 🎓 Learning Outcomes

After completing this lab, you will be able to demonstrate:

- [x] Design and deploy an isolated multi-OS virtual network
- [x] Perform authorized vulnerability assessments against real services
- [x] Analyze Windows Event Logs and Sysmon telemetry
- [x] Investigate Linux SSH authentication events and audit logs
- [x] Intercept and analyze web application traffic with Burp Suite
- [x] Build detection rules mapped to MITRE ATT&CK techniques
- [x] Execute and document full incident response workflows
- [x] Write professional vulnerability and incident reports
- [x] Automate lab validation and evidence collection

---

## 👥 Who Can Use This Lab

| Role | Primary Lab Components |
| :--- | :--- |
| **SOC Analyst** | Wazuh dashboard, Windows Events, Linux logs, incident scenarios |
| **VAPT Analyst** | Kali, Nmap, Burp Suite, web-lab, VA reports |
| **Detection Engineer** | Sigma rules, Wazuh rules, Suricata, MITRE mapping |
| **Incident Responder** | Incident scenarios, evidence collection, timeline analysis |
| **Threat Hunter** | Wazuh, Sysmon, network captures, behavioral analysis |
| **Security Engineer** | Network design, hardening scripts, automation, CI/CD |

Full role guide: [`docs/roles.md`](docs/roles.md)

---

## 📊 Current Project Status

| Phase | Status | Completion |
| :--- | :---: | :---: |
| Phase 1: Repository & Architecture | ✅ Complete | 100% |
| Phase 2: Kali + Linux Server | 🔲 Pending | 0% |
| Phase 3: Windows Endpoint | 🔲 Pending | 0% |
| Phase 4: Web Security Lab | 🔲 Pending | 0% |
| Phase 5: Centralized Logging | 🔲 Pending | 0% |
| Phase 6: Security Monitoring | 🔲 Pending | 0% |
| Phase 7: Network Monitoring | 🔲 Pending | 0% |
| Phase 8: Vulnerability Assessment | 🔲 Pending | 0% |
| Phase 9: Detection Engineering | 🔲 Pending | 0% |
| Phase 10: Incident Response | 🔲 Pending | 0% |
| Phase 11: Automation | 🔲 Pending | 0% |
| Phase 12: Documentation Polish | 🔲 Pending | 0% |
| Phase 13: Full Validation | 🔲 Pending | 0% |
| Phase 14: Portfolio Presentation | 🔲 Pending | 0% |

---

## 🔮 Future Improvements

- Active Directory domain controller integration (Phase 15+)
- Cloud-mirrored architecture (AWS/Azure hybrid simulation)
- Elastic Stack (ELK) as SIEM alternative to Wazuh
- Sliver / Havoc C2 framework for advanced red team simulation
- Automated threat emulation with Atomic Red Team
- CI/CD security pipeline integration

---

*Built as part of the [B.L.A.D.E Cybersecurity Master Curriculum](https://github.com/IamjustaOversizedKidddoo/B.L.A.D.E) — 40 Weeks / 200 Days*
