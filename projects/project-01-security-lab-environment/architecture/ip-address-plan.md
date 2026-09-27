# IP Address Plan — Enterprise Security Lab Environment

> **Subnet:** `192.168.56.0/24`  
> **Mask:** `255.255.255.0`  
> **Gateway:** `192.168.56.1` (VirtualBox Host-Only adapter)  
> **DHCP:** Disabled — all IPs are **statically assigned**

---

## IP Allocation Table

| IP Address | Hostname | VM / Device | Role | Adapters | Notes |
| :---: | :--- | :--- | :--- | :--- | :--- |
| `192.168.56.1` | host-gateway | Host Machine | VirtualBox Host-Only Gateway | — | Auto-created by VirtualBox. Do not assign to any VM. |
| `192.168.56.10` | kali-lab | Kali Linux | Red Team / VAPT Workstation | Host-Only + NAT | NAT adapter for internet updates only. Host-Only for lab traffic. |
| `192.168.56.20` | linux-srv | Ubuntu 22.04 LTS | Enterprise Linux Server | Host-Only only | **No internet route.** Accepts inbound SSH on port 22. |
| `192.168.56.30` | win-ep | Windows 10/11 | Enterprise Windows Endpoint | Host-Only only | **No internet route.** Wazuh agent installed. Sysmon running. |
| `192.168.56.40` | web-lab | Ubuntu 22.04 (Docker) | Vulnerable Web App Host | Host-Only only | **No internet route.** Runs DVWA, Juice Shop, WebGoat in Docker. |
| `192.168.56.50` | siem | Ubuntu 22.04 LTS | Security Monitoring / SIEM | Host-Only only | **No internet route.** Wazuh Manager + Suricata + Dashboard. |
| `192.168.56.51-99` | — | — | Reserved for expansion | — | Reserved for future additions (e.g., AD domain controller, honeypot) |
| `192.168.56.100-199` | — | — | DHCP range (disabled) | — | Keep disabled. All assignments are static. |
| `192.168.56.200-254` | — | — | Reserved for management tools | — | For future Ansible control node, jump host, or monitoring agents |

---

## Service Port Map

### Kali Linux — 192.168.56.10

| Port | Protocol | Service | Notes |
| :---: | :---: | :--- | :--- |
| 4444 | TCP | Metasploit listener (when active) | Manually opened during exercises only |
| 8080 | TCP | Burp Suite proxy (localhost) | Localhost only — used with browser proxy config |
| N/A | — | No persistent open ports | Kali is the attacker — it opens no persistent listening services |

---

### Linux Server — 192.168.56.20

| Port | Protocol | Service | Notes |
| :---: | :---: | :--- | :--- |
| 22 | TCP | OpenSSH | Key-based auth preferred. Password auth for exercises only. |
| 80 | TCP | Apache2 / Nginx HTTP | Default web server for enumeration exercises |
| 443 | TCP | Apache2 / Nginx HTTPS | Self-signed certificate (lab context) |
| 1514 | UDP | Wazuh Agent | Wazuh agent communicates to SIEM at 192.168.56.50 |
| 1515 | TCP | Wazuh Agent (TLS) | Encrypted log shipping to SIEM |

---

### Windows Endpoint — 192.168.56.30

| Port | Protocol | Service | Notes |
| :---: | :---: | :--- | :--- |
| 135 | TCP | MSRPC | Standard Windows service |
| 139 | TCP | NetBIOS | Standard Windows service |
| 445 | TCP | SMB | Used for enumeration exercises (authorized) |
| 3389 | TCP | RDP | Enabled for lab access from Kali (authorized) |
| 1514 | UDP | Wazuh Agent | Log shipping to SIEM |
| 1515 | TCP | Wazuh Agent (TLS) | Encrypted log shipping to SIEM |

---

### Web Lab — 192.168.56.40

| Port | Protocol | Service | Application |
| :---: | :---: | :--- | :--- |
| 80 | TCP | HTTP | Nginx reverse proxy (routes to apps) |
| 8080 | TCP | HTTP | DVWA (Damn Vulnerable Web App) |
| 3000 | TCP | HTTP | OWASP Juice Shop |
| 8090 | TCP | HTTP | WebGoat |
| 2375 | TCP | Docker API | **Disabled** — do not expose Docker socket |

---

### Security Monitoring (SIEM) — 192.168.56.50

| Port | Protocol | Service | Notes |
| :---: | :---: | :--- | :--- |
| 1514 | UDP | Wazuh log receiver | Receives agent events (UDP syslog-style) |
| 1515 | TCP | Wazuh agent enrollment | Agent TLS enrollment endpoint |
| 9200 | TCP | OpenSearch API | Internal API — listen on localhost only |
| 5601 | TCP | Wazuh Dashboard | Browser-accessible UI on host machine via host-only adapter |
| 55000 | TCP | Wazuh API | REST API for management |

---

## Routing Rules

| Source | Destination | Action | Reason |
| :--- | :--- | :---: | :--- |
| Any lab VM | `0.0.0.0/0` (internet) | **BLOCK** | All target VMs have Host-Only adapter only — no route exists |
| Kali NAT | `0.0.0.0/0` (internet) | **ALLOW** | NAT adapter for update downloads only — controlled by host |
| Kali Host-Only | `192.168.56.0/24` | **ALLOW** | Lab testing interface |
| SIEM | `192.168.56.0/24` | **ALLOW** | Log receiving from all agents |
| Any VM | `192.168.56.1` (gateway) | **ALLOW** | VirtualBox Host-Only gateway — used for host connectivity |

---

## Hostname Configuration

Configure `/etc/hosts` on Kali and the Linux Server so human-readable names work:

```
# /etc/hosts — Add to Kali and Linux Server
192.168.56.10   kali-lab
192.168.56.20   linux-srv
192.168.56.30   win-ep
192.168.56.40   web-lab
192.168.56.50   siem

# Web application hostnames (optional — for Host header exercises)
192.168.56.40   dvwa.lab.local
192.168.56.40   juice.lab.local
192.168.56.40   webgoat.lab.local
```

Windows hosts file (`C:\Windows\System32\drivers\etc\hosts`):
```
192.168.56.10   kali-lab
192.168.56.20   linux-srv
192.168.56.50   siem
```

---

## IP Assignment Verification

After each VM is provisioned, run this check from Kali:

```bash
# Verify all lab hosts are reachable
for ip in 192.168.56.20 192.168.56.30 192.168.56.40 192.168.56.50; do
    echo -n "Testing $ip: "
    ping -c 1 -W 1 $ip &>/dev/null && echo "✅ UP" || echo "❌ DOWN"
done
```

Expected output:
```
Testing 192.168.56.20: ✅ UP
Testing 192.168.56.30: ✅ UP
Testing 192.168.56.40: ✅ UP
Testing 192.168.56.50: ✅ UP
```

---

## Reserved Expansion Space

| Range | Purpose | Phase |
| :--- | :--- | :---: |
| `192.168.56.60` | Active Directory Domain Controller (future) | Phase 15+ |
| `192.168.56.70` | Honeypot / Canary system | Phase 15+ |
| `192.168.56.80` | Ansible Control Node | Phase 11+ |
| `192.168.56.90` | Jump Host / Bastion Server | Phase 15+ |

---

[← Architecture](architecture.md) | [Back to README](../README.md) | [Threat Model →](threat-model.md)
