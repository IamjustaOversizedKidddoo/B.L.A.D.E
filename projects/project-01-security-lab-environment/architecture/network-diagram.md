# Network Diagram — Enterprise Security Lab Environment

> **Topology type:** Star with Host-Only private subnet  
> **Hypervisor:** VirtualBox 7.x (or VMware Workstation)  
> **Subnet:** `192.168.56.0/24`

---

## Full Topology Diagram

```
╔══════════════════════════════════════════════════════════════════════════════════╗
║                        ENTERPRISE SECURITY LAB                                 ║
║                     Network: 192.168.56.0/24                                   ║
╠══════════════════════════════════════════════════════════════════════════════════╣
║                                                                                 ║
║  ┌──────────────────────────────────────────────────────────────┐               ║
║  │                    YOUR HOST MACHINE                         │               ║
║  │                                                              │               ║
║  │  VirtualBox Host-Only Adapter: 192.168.56.1                  │               ║
║  │  (This is the gateway for all lab machines)                  │               ║
║  │                                                              │               ║
║  └──────────────────────────┬───────────────────────────────────┘               ║
║                             │                                                   ║
║                    HOST-ONLY SWITCH (vboxnet0)                                  ║
║                    192.168.56.0/24                                               ║
║          ┌──────────────────┼──────────────────┬─────────────────┐              ║
║          │                  │                  │                 │              ║
║          ▼                  ▼                  ▼                 ▼              ║
║  ┌───────────────┐  ┌───────────────┐  ┌──────────────┐  ┌──────────────────┐  ║
║  │  KALI LINUX   │  │ LINUX SERVER  │  │  WINDOWS     │  │    WEB LAB       │  ║
║  │ 192.168.56.10 │  │ 192.168.56.20 │  │  ENDPOINT    │  │  192.168.56.40   │  ║
║  │               │  │               │  │192.168.56.30 │  │                  │  ║
║  │ [Host-Only]   │  │ [Host-Only]   │  │ [Host-Only]  │  │ [Host-Only]      │  ║
║  │ [NAT]─────────┼──┼───────────────┼──┼──────────────┼──┼──── INTERNET     │  ║
║  │  ↑            │  │               │  │              │  │ (only Kali NAT   │  ║
║  │  Updates only │  │  SSH :22      │  │  RDP :3389   │  │  has this route) │  ║
║  │               │  │  HTTP :80     │  │  SMB :445    │  │                  │  ║
║  │  TOOLS:       │  │  HTTPS :443   │  │  Sysmon      │  │  DVWA    :8080   │  ║
║  │  nmap         │  │  auditd       │  │  Event Logs  │  │  JuiceShop :3000 │  ║
║  │  burpsuite    │  │  rsyslog      │  │  PowerShell  │  │  WebGoat :8090   │  ║
║  │  wireshark    │  │  Wazuh Agent  │  │  Wazuh Agent │  │  Docker          │  ║
║  │  metasploit   │  │               │  │              │  │  Wazuh Agent     │  ║
║  └───────────────┘  └───────┬───────┘  └──────┬───────┘  └────────┬─────────┘  ║
║                             │                 │                   │             ║
║                             │ Wazuh Agent     │ Wazuh Agent       │ Wazuh Agent ║
║                             │ (TLS :1515)     │ (TLS :1515)       │ (TLS :1515) ║
║                             └─────────────────┴───────────────────┘             ║
║                                               │                                 ║
║                                               ▼                                 ║
║                              ┌────────────────────────────┐                     ║
║                              │    SECURITY MONITORING     │                     ║
║                              │      192.168.56.50         │                     ║
║                              │                            │                     ║
║                              │  Wazuh Manager  :1514/1515 │                     ║
║                              │  Wazuh Dashboard     :5601 │                     ║
║                              │  OpenSearch API      :9200 │                     ║
║                              │  Suricata (IDS)            │                     ║
║                              │  [Host-Only]               │                     ║
║                              └────────────────────────────┘                     ║
║                                                                                 ║
╠══════════════════════════════════════════════════════════════════════════════════╣
║  RULE: All traffic stays within 192.168.56.0/24                                 ║
║        Kali's NAT adapter = update downloads only, cannot reach lab targets      ║
║        Target machines have NO internet route (Host-Only adapter only)           ║
╚══════════════════════════════════════════════════════════════════════════════════╝
```

---

## Data Flow Diagram

```
══════════════════════════════════════════════════════════════════
     SECURITY DATA FLOW — LOG AND EVENT COLLECTION
══════════════════════════════════════════════════════════════════

  WINDOWS ENDPOINT (192.168.56.30)
  ┌─────────────────────────────────────┐
  │ • Sysmon Events (Event ID 1,3,7,8…) │
  │ • Windows Security Events (4624,    │
  │   4625, 4688, 4697, 4720…)          │
  │ • PowerShell Script Block Logs      │
  │ • Windows Firewall Logs             │
  │           │                         │
  │    Wazuh Agent (encrypted TLS)      │
  └───────────┼─────────────────────────┘
              │
              │────────────────────────────────────────┐
              ▼                                        │
  LINUX SERVER (192.168.56.20)                         │
  ┌─────────────────────────────────────┐              │
  │ • /var/log/auth.log (SSH attempts)  │              │
  │ • auditd events (syscall tracking)  │              │
  │ • Apache/Nginx access & error logs  │              │
  │ • /var/log/syslog                   │              │
  │           │                         │              │
  │    Wazuh Agent (encrypted TLS)      │              │
  └───────────┼─────────────────────────┘              │
              │                                        │
              │────────────────────────────────────────┤
              ▼                                        │
  WEB LAB (192.168.56.40)                              │
  ┌─────────────────────────────────────┐              │
  │ • Nginx/Apache access logs          │              │
  │ • Application error logs            │              │
  │ • Docker container stdout/stderr    │              │
  │           │                         │              │
  │    Wazuh Agent (encrypted TLS)      │              │
  └───────────┼─────────────────────────┘              │
              │                                        │
              └────────────────────────────────────────┘
                                │
                                ▼
  SECURITY MONITORING (192.168.56.50)
  ┌────────────────────────────────────────────────────┐
  │                                                    │
  │  Wazuh Manager                                     │
  │    ├── Log parsing & decoding                      │
  │    ├── Rule matching (3000+ built-in rules)        │
  │    ├── Custom rules (detection/ directory)         │
  │    └── Alert generation                            │
  │                                                    │
  │  Suricata                                          │
  │    ├── Passive network tap on lab subnet           │
  │    ├── IDS rule matching (Emerging Threats)        │
  │    └── Alerts forwarded to Wazuh                   │
  │                                                    │
  │  Wazuh Dashboard (port 5601)                       │
  │    ├── Real-time alert dashboard                   │
  │    ├── Log search & investigation                  │
  │    ├── MITRE ATT&CK mapping view                   │
  │    └── Compliance reports                          │
  │                                                    │
  └────────────────────────────────────────────────────┘

══════════════════════════════════════════════════════════════════
     ATTACK FLOW — RED TEAM PERSPECTIVE
══════════════════════════════════════════════════════════════════

  KALI LINUX (192.168.56.10)
  │
  ├─── RECONNAISSANCE
  │     nmap -sV -sC 192.168.56.0/24
  │     → Discovers open ports on all lab machines
  │
  ├─── WEB TESTING
  │     burpsuite → proxy → web-lab:8080/3000/8090
  │     → Intercepts and modifies HTTP requests
  │
  ├─── AUTHENTICATION TESTING
  │     hydra → linux-srv:22 / win-ep:3389
  │     → Brute-force simulation (controlled wordlists)
  │
  ├─── VULNERABILITY EXPLOITATION
  │     metasploit → linux-srv or win-ep
  │     → Controlled, authorized exploitation
  │
  └─── ALL TRAFFIC OBSERVED BY SIEM
        Suricata sees raw packets on the subnet
        Wazuh Agents see endpoint-level events
        → Everything generates alerts for blue team exercises

══════════════════════════════════════════════════════════════════
```

---

## VirtualBox Network Adapter Reference

| VM | Adapter 1 | Adapter 2 |
| :--- | :--- | :--- |
| Kali Linux | **Host-Only** (`vboxnet0`, IP: `192.168.56.10`) | **NAT** (dynamic, internet access only) |
| Linux Server | **Host-Only** (`vboxnet0`, IP: `192.168.56.20`) | None |
| Windows Endpoint | **Host-Only** (`vboxnet0`, IP: `192.168.56.30`) | None |
| Web Lab | **Host-Only** (`vboxnet0`, IP: `192.168.56.40`) | None |
| SIEM | **Host-Only** (`vboxnet0`, IP: `192.168.56.50`) | None |

---

[← Back to README](../README.md) | [Architecture →](architecture.md) | [IP Plan →](ip-address-plan.md)
