# MITRE ATT&CK Mapping — Enterprise Security Lab

> **Framework:** MITRE ATT&CK Enterprise v14  
> **Reference:** https://attack.mitre.org/  
> **Coverage:** This document maps each lab exercise to ATT&CK techniques

---

## Coverage Overview

| Phase | Tactics Covered |
| :--- | :--- |
| Reconnaissance | Reconnaissance |
| Vulnerability Analysis | Discovery |
| Exploitation | Initial Access, Execution, Credential Access |
| Post-Exploitation | Persistence, Privilege Escalation, Defense Evasion, Lateral Movement |
| Detection Engineering | Detection of all above |

---

## Technique Mapping Table

| ATT&CK ID | Technique | Exercise | Lab Component | Detection Status |
| :---: | :--- | :--- | :--- | :---: |
| T1046 | Network Service Scanning | nmap full port scan | Kali → All targets | 🔲 Rule pending |
| T1018 | Remote System Discovery | nmap ping sweep | Kali → All targets | 🔲 Rule pending |
| T1110.001 | Brute Force: Password Guessing | Hydra SSH brute force | Kali → Linux Server | 🔲 Rule pending |
| T1110.003 | Brute Force: Password Spraying | CrackMapExec to Windows | Kali → Windows EP | 🔲 Rule pending |
| T1595.002 | Active Scanning: Vulnerability Scanning | Nikto, OpenVAS | Kali → Web Lab | 🔲 Rule pending |
| T1059.001 | PowerShell | PowerShell commands on Windows | Windows EP | 🔲 Rule pending |
| T1059.004 | Unix Shell | Bash commands on Linux Server | Linux Server | 🔲 Rule pending |
| T1190 | Exploit Public-Facing Application | SQLi, SSRF against web apps | Kali → Web Lab | 🔲 Rule pending |
| T1098 | Account Manipulation | Create backdoor user | Linux Server | 🔲 Rule pending |
| T1053.003 | Scheduled Task: Cron | Malicious cron job | Linux Server | 🔲 Rule pending |
| T1548.003 | Abuse Elevation: sudo | sudo misconfig abuse | Linux Server | 🔲 Rule pending |
| T1021.001 | Remote Services: RDP | RDP lateral movement | Kali → Windows EP | 🔲 Rule pending |
| T1021.004 | Remote Services: SSH | SSH to Linux Server | Kali → Linux Server | 🔲 Rule pending |
| T1083 | File and Directory Discovery | ls, find, dir enumeration | Linux + Windows | 🔲 Rule pending |
| T1057 | Process Discovery | ps, tasklist enumeration | Linux + Windows | 🔲 Rule pending |
| T1082 | System Information Discovery | uname, systeminfo | Linux + Windows | 🔲 Rule pending |

---

## Tactic Coverage Map

```
Initial Access  ██████░░░░  60%
Execution       ████░░░░░░  40%
Persistence     ██░░░░░░░░  20%
Priv Escalation ████░░░░░░  40%
Defense Evasion ██░░░░░░░░  20%
Discovery       ██████████  100%
Lateral Move    ████░░░░░░  40%
Collection      ██░░░░░░░░  20%
Exfiltration    ░░░░░░░░░░  0% (not in scope for this lab)
C2              ░░░░░░░░░░  0% (Phase 10+ planned)
```

---

> **Note:** Detection rules for all mapped techniques are created in [`detection/`](../detection/) as lab exercises progress.

[← Back to README](../README.md)
