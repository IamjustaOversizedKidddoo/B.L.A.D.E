# Architecture — Enterprise Security Lab Environment

> **Version:** 1.0.0 (Phase 1)  
> **Status:** Designed — Pre-Deployment  
> **Network:** `192.168.56.0/24` — Isolated Host-Only

---

## 1. Design Philosophy

This lab is designed around a single constraint: **every test, scan, and attack must stay inside the private subnet.** This mirrors how professional security teams work in isolated "purple team range" environments, where the blast radius of any test is bounded by the network boundary.

The architecture also embodies **defense-in-depth** not just as a target configuration, but as a documentation standard: every component records what it does, and the monitoring layer aggregates those records so detection exercises become realistic.

---

## 2. Network Topology

```
═══════════════════════════════════════════════════════════════
       ENTERPRISE SECURITY LAB — NETWORK TOPOLOGY
       Isolated Subnet: 192.168.56.0/24
═══════════════════════════════════════════════════════════════

  [ YOUR HOST MACHINE ]
         │
         │ HOST-ONLY ADAPTER (VirtualBox/VMware)
         │ 192.168.56.1 (host gateway — no route to internet)
         │
  ═══════╪══════════════════ LAB SWITCH ══════════════════════
         │
  ┌──────┴──────────────────────────────────────────────┐
  │                                                     │
  │  ┌────────────────────┐    ┌──────────────────────┐ │
  │  │   KALI LINUX       │    │   LINUX SERVER       │ │
  │  │   192.168.56.10    │    │   192.168.56.20      │ │
  │  │   Red Team /       │    │   Ubuntu 22.04 LTS   │ │
  │  │   VAPT Station     │    │   SSH · Apache       │ │
  │  │                    │    │   auditd · rsyslog   │ │
  │  │   [NAT adapter]    │    └──────────┬───────────┘ │
  │  │   for updates only │               │             │
  │  └────────────────────┘               │ Logs        │
  │                                       ▼             │
  │  ┌────────────────────┐    ┌──────────────────────┐ │
  │  │   WINDOWS 10/11    │    │   WEB LAB            │ │
  │  │   192.168.56.30    │    │   192.168.56.40      │ │
  │  │   Enterprise EP    │    │   Docker Host        │ │
  │  │   Sysmon · Defender│    │   DVWA · Juice Shop  │ │
  │  │   Event Logging    │    │   WebGoat            │ │
  │  └────────────────────┘    └──────────┬───────────┘ │
  │           │                           │             │
  │           │ Logs                      │ Logs        │
  │           └──────────────┬────────────┘             │
  │                          ▼                          │
  │           ┌──────────────────────────┐              │
  │           │   SECURITY MONITORING    │              │
  │           │   192.168.56.50          │              │
  │           │   Wazuh SIEM Manager     │              │
  │           │   Suricata IDS           │              │
  │           └──────────────────────────┘              │
  │                                                     │
  └─────────────────────────────────────────────────────┘

  RULE: No traffic from 192.168.56.0/24 exits to the internet.
        Kali's NAT adapter is for OS/tool updates ONLY.
        All target machines use Host-Only adapter ONLY.
═══════════════════════════════════════════════════════════════
```

---

## 3. Component Roles

### 3.1 Kali Linux (192.168.56.10)

**Role:** Security Workstation / Red Team Operator / VAPT Platform

**Why this machine:**  
Security practitioners need a dedicated workstation with pre-installed tools. Running security tools from your personal machine risks contaminating evidence, leaking traffic, and introducing credential risk. A dedicated Kali VM in the lab isolates the attack surface to the private subnet.

**Network adapters:**
- **Adapter 1 (NAT):** Outbound-only access to the internet for `apt update`, tool downloads. No inbound connections accepted.
- **Adapter 2 (Host-Only):** Active testing interface. All scans, Burp Suite traffic, and attack simulations go through this adapter.

**Isolation guarantee:** Kali's NAT adapter cannot reach `192.168.56.x`. Target machines have no NAT adapter and cannot reach the internet. Cross-contamination is architecturally impossible.

---

### 3.2 Linux Server (192.168.56.20)

**Role:** Enterprise Application & SSH Server

**Why this machine:**  
Most corporate environments run Linux-based servers for file sharing, web services, and application hosting. This VM simulates that role: a hardened (but auditable) server with realistic services running, generating real log telemetry.

**Adapter:** Host-Only only. No internet route. Cannot reach `8.8.8.8`.

**Key services:**
- OpenSSH with key authentication
- Apache2 / Nginx web server
- `auditd` for kernel-level audit
- `rsyslog` for log forwarding to Wazuh
- Custom test users for authentication exercises

---

### 3.3 Windows Endpoint (192.168.56.30)

**Role:** Enterprise User Workstation

**Why this machine:**  
The majority of real-world corporate breaches pivot through Windows endpoints. This VM replicates that environment with production-quality telemetry enabled: Sysmon, PowerShell Script Block Logging, and Windows Security Event Auditing.

**Adapter:** Host-Only only.

**Key configurations:**
- Sysmon v15+ with SwiftOnSecurity baseline config
- PowerShell Script Block Logging (Event ID 4104)
- Process creation auditing (Event ID 4688 with command-line)
- Windows Firewall — logging enabled
- Wazuh agent forwarding events to SIEM

---

### 3.4 Web Lab (192.168.56.40)

**Role:** Intentionally Vulnerable Web Application Target

**Why this machine:**  
Web vulnerabilities are the leading entry point in real-world breaches. Testing web security skills requires a legal target that actually has vulnerabilities to find. DVWA, OWASP Juice Shop, and WebGoat are purpose-built for this.

**Adapter:** Host-Only only.

**Deployment:** Docker Compose. Multiple apps run on different ports.

| Application | Port | Focus Area |
| :--- | :---: | :--- |
| DVWA | 8080 | SQL Injection, XSS, CSRF, File Upload, Command Injection |
| OWASP Juice Shop | 3000 | OWASP Top 10, API security, modern web vulnerabilities |
| WebGoat | 8090 | Authentication, Access Control, JWT, SSRF, Deserialization |

---

### 3.5 Security Monitoring (192.168.56.50)

**Role:** SIEM / IDS / Centralized Log Aggregator

**Why this machine:**  
A lab without visibility is a toy, not a learning environment. This machine replicates the "Security Operations Center" data pipeline: logs flow in from all other machines, get correlated, and trigger alerts. This is where blue team exercises happen.

**Adapter:** Host-Only only (agents push data to this IP).

**Stack:**
- Wazuh Manager (SIEM, log analysis, custom rules)
- Suricata (network-layer intrusion detection on the lab subnet)
- Wazuh Dashboard (Kibana-based UI)

---

## 4. Data Flow

```
Windows Endpoint (192.168.56.30)
│  ├─ Windows Security Events
│  ├─ Sysmon Events
│  └─ PowerShell Script Block Logs
│              │ Wazuh Agent (TLS)
│              ▼
Linux Server (192.168.56.20)                 Wazuh Manager
│  ├─ auth.log / SSH logs                    192.168.56.50
│  ├─ auditd events                ─────────►              ├─ Log storage
│  └─ Apache access/error logs               │             ├─ Correlation
│              │ Wazuh Agent (TLS)           │             ├─ Alerting
│              ▼                             │             └─ Dashboard
Web Lab (192.168.56.40)                      │
   ├─ Nginx/Apache access logs               │
   ├─ Application error logs     ────────────┘
   └─ Docker container logs
                         │
Network Traffic ─────────┤ Suricata
   (All subnet)          └─ IDS alerts → Wazuh
```

---

## 5. Security Assumptions

1. **Isolation is the primary control.** All security guarantees depend on Host-Only networking. If a VM is accidentally configured as Bridged, the safety of the network topology collapses.
2. **No credentials are stored in this repository.** All service passwords are set manually during setup and documented only in local, untracked configuration files.
3. **Vulnerable services exist by design.** DVWA and Juice Shop contain real, exploitable vulnerabilities. They must never be exposed beyond `192.168.56.0/24`.
4. **This lab does not simulate a production environment.** Security controls are deliberately weakened on target machines to create learning opportunities. Do not mirror these configurations in production systems.
5. **All attack scenarios use authorized targets only.** The permitted target range is strictly `192.168.56.0/24`. Any activity outside this range is unauthorized and illegal.

---

## 6. Virtualization Decision Rationale

| Component | Virtualization | Rationale |
| :--- | :--- | :--- |
| Kali Linux | **Full VM** | Requires access to physical network adapters and raw socket capabilities for accurate packet operations |
| Ubuntu Linux Server | **Full VM** | Simulates a persistent enterprise server with configurable kernel parameters and service state |
| Windows Endpoint | **Full VM** | Requires actual Windows kernel for authentic Event ID telemetry, token manipulation, and Sysmon visibility |
| Web Applications | **Docker (on Linux VM)** | Lightweight, reproducible, easily reset between exercises; no kernel-level behavior analysis needed |
| Wazuh SIEM | **Full VM** | Requires stable persistent storage for log history and enough RAM for Elasticsearch indexing |

---

## 7. References

- [VirtualBox Networking Modes](https://www.virtualbox.org/manual/ch06.html)
- [Kali Linux Documentation](https://www.kali.org/docs/)
- [Wazuh Documentation](https://documentation.wazuh.com/)
- [OWASP Testing Guide v4.2](https://owasp.org/www-project-web-security-testing-guide/)
- [MITRE ATT&CK Framework](https://attack.mitre.org/)
- [Sysmon SwiftOnSecurity Config](https://github.com/SwiftOnSecurity/sysmon-config)

---

[← Back to Project README](../README.md) | [IP Address Plan →](ip-address-plan.md) | [Threat Model →](threat-model.md)
