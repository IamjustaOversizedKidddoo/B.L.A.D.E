# Security Testing Methodology — Enterprise Security Lab

> **Frameworks referenced:** PTES (Penetration Testing Execution Standard), OWASP Testing Guide v4.2, NIST SP 800-115  
> **Scope:** All exercises performed exclusively within `192.168.56.0/24`

---

## 1. Pre-Engagement

Before any test begins, the following checklist must be completed:

```
[ ] Target IP range confirmed: 192.168.56.0/24
[ ] Authorization reviewed: This is a private lab — all machines are owned by you
[ ] Snapshot taken of all target VMs
[ ] Wazuh dashboard open and receiving events
[ ] Suricata active
[ ] Evidence directory created with timestamp: evidence/YYYY-MM-DD_EXERCISE_NAME/
[ ] Testing machine (Kali) isolated: ping 8.8.8.8 fails from target VMs
```

---

## 2. Methodology Phases

### Phase A: Reconnaissance

**Objective:** Discover what is running in the lab network. Simulate what an attacker would learn in the initial discovery stage.

**Techniques:**
1. Host discovery: `nmap -sn 192.168.56.0/24`
2. Port scan: `nmap -sV -sC -p- 192.168.56.20`
3. OS detection: `nmap -O 192.168.56.30`
4. Service enumeration: Banner grabbing, version detection
5. Web crawling: `gobuster`, `feroxbuster` against web targets

**MITRE ATT&CK Mapping:**
- T1046 — Network Service Scanning
- T1018 — Remote System Discovery

---

### Phase B: Vulnerability Analysis

**Objective:** Identify specific weaknesses in discovered services.

**Techniques:**
1. Automated scan: `nmap --script vuln 192.168.56.20`
2. Web vulnerability scanning: OWASP ZAP, Nikto
3. Manual review of service configurations
4. CVE lookup for discovered service versions
5. SMB enumeration: `enum4linux`, `smbclient`

**MITRE ATT&CK Mapping:**
- T1595.002 — Vulnerability Scanning
- T1592 — Gather Victim Host Information

---

### Phase C: Exploitation

**Objective:** Confirm vulnerabilities by exercising them against intentionally vulnerable targets.

**Scope restriction:** Only DVWA, Juice Shop, WebGoat, or intentionally configured services on Linux Server and Windows Endpoint.

**Techniques:**
1. SQL injection: Manual + sqlmap against DVWA
2. XSS: Stored, reflected, and DOM-based XSS in Juice Shop
3. Authentication bypass: Burp Suite intercept + parameter manipulation
4. SSH brute force simulation: Hydra with controlled 10-attempt wordlist
5. Windows exploitation: Metasploit against intentionally vulnerable services

---

### Phase D: Post-Exploitation Analysis (Blue Team Phase)

**Objective:** After each attack, switch to the SIEM and investigate what was logged.

**Workflow:**
1. Open Wazuh Dashboard: `http://192.168.56.50:5601`
2. Filter events by target IP (e.g., `192.168.56.20`)
3. Identify which events correspond to the attack performed
4. Document: What was logged? What was NOT logged? What should have been logged?
5. Write detection rule if no alert fired

---

### Phase E: Reporting

**Objective:** Document findings in a professional format.

**Required for each exercise:**
1. Executive Summary (1 paragraph — non-technical)
2. Findings table (Vulnerability, CVSS, Impact, Evidence)
3. Technical details (reproduction steps, tool output)
4. Screenshots with timestamps and context
5. Recommendations (specific, actionable)

Templates: [`reports/`](../reports/)

---

## 3. Evidence Standards

Every test must produce captured evidence using the naming convention:

```
evidence/
└── YYYY-MM-DD_EXERCISE-NAME/
    ├── 00_scope.txt              ← Target IPs and authorized scope
    ├── 01_recon_nmap.txt         ← nmap output
    ├── 02_findings.md            ← Vulnerability findings
    ├── screenshots/
    │   └── HHMMSS_description.png
    └── packet-captures/
        └── HHMMSS_exercise.pcap
```

Hash all evidence files on collection:
```bash
sha256sum evidence/YYYY-MM-DD_EXERCISE/* > evidence/YYYY-MM-DD_EXERCISE/hashes.sha256
```

---

## 4. Rules of Engagement

| Rule | Requirement |
| :--- | :--- |
| **Authorized targets only** | Only `192.168.56.0/24` unless explicitly documented |
| **No real malware** | No actual ransomware, worms, or botnet code |
| **Snapshot before exercise** | All VMs must be snapshotted before destructive tests |
| **Evidence collected** | Every meaningful finding must have a screenshot or log extract |
| **Detection review** | After every attack, check SIEM — document what fired and what didn't |

---

[← Back to README](../README.md)
