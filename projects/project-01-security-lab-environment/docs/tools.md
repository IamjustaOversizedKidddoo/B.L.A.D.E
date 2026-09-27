# Tool Inventory — Enterprise Security Lab

> Tools are organized by security role. Each tool has a clear justification for inclusion.

---

## Red Team / Offensive Tools (on Kali Linux)

| Tool | Version | Purpose | MITRE Technique |
| :--- | :---: | :--- | :--- |
| **Nmap** | Latest | Network discovery, port scanning, service enumeration, script scanning | T1046, T1018 |
| **Burp Suite Community** | Latest | HTTP proxy, web application testing, repeater, intruder | T1190 |
| **Gobuster / Feroxbuster** | Latest | Directory and file brute-forcing on web servers | T1595.002 |
| **Hydra** | Latest | Password brute-force against SSH, RDP, HTTP, FTP | T1110.001 |
| **Netcat (nc)** | Built-in | Reverse shells, port forwarding, connection testing | T1059.004 |
| **Metasploit Framework** | Latest | Vulnerability exploitation framework | T1190, T1059 |
| **Nikto** | Latest | Web server vulnerability scanning | T1595.002 |
| **SQLmap** | Latest | Automated SQL injection discovery and exploitation | T1190 |
| **Wireshark** | Latest | Packet capture and protocol analysis | T1040 |
| **tcpdump** | Built-in | Command-line packet capture | T1040 |
| **enum4linux** | Latest | SMB / Samba enumeration | T1135 |
| **CrackMapExec (CME)** | Latest | Windows domain / SMB enumeration and testing | T1135, T1110.003 |
| **Python 3** | 3.11+ | Custom scripts, automation, exploit PoC development | T1059.006 |
| **curl / wget** | Built-in | HTTP request crafting, file download | T1105 |

---

## Defensive / Blue Team Tools (on SIEM)

| Tool | Version | Purpose |
| :--- | :---: | :--- |
| **Wazuh Manager** | 4.7+ | SIEM, log aggregation, rule-based alerting, compliance |
| **Wazuh Dashboard** | 4.7+ | Browser-based UI for log investigation and alert management |
| **OpenSearch** | Latest | Backend log search and indexing |
| **Suricata** | 7.x | Network intrusion detection, protocol analysis, traffic inspection |
| **Sigma** | Latest | Generic detection rule format converted to Wazuh/Splunk/Elastic rules |

---

## Monitoring Tools (on Linux Server and Windows Endpoint)

| Tool | Component | Purpose |
| :--- | :--- | :--- |
| **Wazuh Agent** | Linux Server, Windows EP, Web Lab | Forwards logs and events to Wazuh Manager |
| **Sysmon** | Windows Endpoint | Process creation, network connections, registry changes telemetry |
| **auditd** | Linux Server | Kernel-level audit trail for system calls, file access, user commands |
| **rsyslog** | Linux Server | Syslog forwarding |
| **Windows Event Logging** | Windows Endpoint | Security events: login, process creation, service installation |

---

## Web Security Lab (on Web Lab VM)

| Application | Port | Vulnerability Focus |
| :--- | :---: | :--- |
| **DVWA** (Damn Vulnerable Web App) | 8080 | SQLi, XSS, CSRF, Command Injection, File Upload, File Inclusion |
| **OWASP Juice Shop** | 3000 | OWASP Top 10, JWT, API Security, Broken Auth, SSRF |
| **WebGoat** | 8090 | Auth bypass, Access Control, Insecure Deserialization, XXE |

---

## Documentation Tools

| Tool | Purpose |
| :--- | :--- |
| **Markdown** | All documentation — readable in GitHub and VS Code |
| **asciinema** | Terminal session recording for evidence |
| **Flameshot / Greenshot** | Screenshot with annotation |

---

[← Back to README](../README.md)
