# Security Controls — Enterprise Security Lab

| Control | Type | Component | Implementation | Status |
| :--- | :---: | :--- | :--- | :---: |
| Network isolation via Host-Only adapter | Preventive | All VMs | VirtualBox Host-Only network, no bridged adapter on targets | ✅ By design |
| No default internet gateway on target VMs | Preventive | Linux Srv, Windows EP, Web Lab, SIEM | Static IP without default route | ✅ By design |
| Kali NAT internet access (updates only) | Compensating | Kali | Separate NAT adapter that cannot reach lab subnet targets | ✅ By design |
| Static IP assignments | Preventive | All VMs | Netplan (Linux) / Manual (Windows) | 📋 Phase 2 |
| Hostname resolution via `/etc/hosts` | Operational | Kali, Linux Srv | No DNS needed; fixed host entries | 📋 Phase 2 |
| Wazuh agents on all targets | Detective | Linux Srv, Windows EP, Web Lab | Wazuh agent with TLS enrollment | 📋 Phase 6 |
| Sysmon on Windows Endpoint | Detective | Windows EP | SwiftOnSecurity baseline configuration | 📋 Phase 3 |
| auditd on Linux Server | Detective | Linux Srv | Audit rules for privileged operations | 📋 Phase 2 |
| Suricata IDS on lab subnet | Detective | SIEM VM | Passive tap on `192.168.56.0/24` | 📋 Phase 7 |
| File integrity monitoring | Detective | Linux Srv, Windows EP | Wazuh FIM module | 📋 Phase 6 |
| PowerShell Script Block Logging | Detective | Windows EP | GPO / registry configuration | 📋 Phase 3 |
| Windows Firewall logging | Detective | Windows EP | Enabled drop and allow logging | 📋 Phase 3 |
| SSH key-based authentication | Hardening | Linux Srv | Disable password auth after setup | 📋 Phase 2 |
| No hardcoded credentials in repo | Preventive | Repository | `.gitignore` patterns + documented policy | ✅ By design |
| SHA-256 evidence hashing | Detective | Kali | `scripts/evidence/collect.py` | 📋 Phase 11 |
| VM snapshots before exercises | Corrective | All VMs | VirtualBox Snapshot Manager | 📋 Phase 2 |
| DVWA/Juice Shop isolated to web-lab | Preventive | Web Lab | Docker on Host-Only adapter only | 📋 Phase 4 |
| Wazuh Dashboard TLS | Preventive | SIEM | Let's Encrypt (lab CA) or self-signed | 📋 Phase 6 |

**Legend:** ✅ Implemented | 📋 Pending (Phase noted) | ⚠️ Requires manual step

---

[← Back to README](../README.md)
