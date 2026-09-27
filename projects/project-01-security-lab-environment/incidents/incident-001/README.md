# Incident 001 — Windows Authentication Failure Spike

> **Scenario type:** Blue Team — Alert Investigation  
> **Difficulty:** Beginner  
> **MITRE ATT&CK:** T1110.001 — Brute Force: Password Guessing  
> **Lab components:** Kali Linux (attacker), Windows Endpoint (target), Wazuh SIEM (detection)

---

## Scenario Overview

The SIEM generates an alert for a large number of failed login attempts against the Windows Endpoint (`192.168.56.30`) over a short time window. Your job is to investigate the alert, determine if it is a true positive, identify the source, and document the incident.

This exercise simulates a credential brute-force attack — one of the most common initial access techniques observed in real-world incidents.

---

## Learning Objectives

- [ ] Navigate the Wazuh Dashboard and filter events by host and time range
- [ ] Identify failed login Event IDs in Windows Security logs (Event ID 4625)
- [ ] Determine attack source IP and targeted user accounts
- [ ] Classify the incident as T1110.001
- [ ] Write a structured incident report

---

## Prerequisites

- [ ] Phase 3 complete (Windows Endpoint configured with Sysmon and Wazuh agent)
- [ ] Phase 6 complete (Wazuh SIEM receiving Windows events)
- [ ] Snapshot taken of Windows Endpoint

---

## Attack Simulation (Red Team Phase)

> **Run from Kali Linux (192.168.56.10) only. Authorized target: 192.168.56.30.**

```bash
# Simulate a brute-force attack against Windows RDP
hydra -l Administrator -P /usr/share/wordlists/rockyou.txt rdp://192.168.56.30 -t 4 -V
```

Stop after a few minutes. The goal is to generate log data — not to succeed.

---

## Investigation (Blue Team Phase)

### Step 1: Check the SIEM Alert

Open Wazuh Dashboard: `http://192.168.56.50:5601`

- Navigate to: **Security Events** → Filter by agent `win-ep`
- Time range: Last 15 minutes
- Look for rule ID **18152** (Multiple Windows login failures)

### Step 2: Pivot to Raw Events

Filter: `data.win.eventdata.logonType:10` (RDP logon type)  
Expected Event ID: **4625** (An account failed to log on)

Questions to answer:
1. What is the source IP of the failed logins?
2. Which user account was targeted?
3. How many attempts per minute?
4. Did any login succeed (Event ID 4624)?

### Step 3: Write the Incident Report

Use the template in [`reports/incident-reports/`](../../reports/incident-reports/)

---

## Evidence Collection

```bash
python3 scripts/evidence/collect_evidence.py \
  --exercise "incident-001-auth-failure" \
  --targets 192.168.56.30 \
  --notes "Brute force simulation against Windows RDP" \
  --files [your nmap/hydra output files]
```

---

## Expected SIEM Output

After the attack, Wazuh should fire:
- Rule 18152: Multiple Windows login failures in a short time
- Rule 18158: Windows login failure (each attempt)

If no alert fires → write a detection rule in [`detection/wazuh/`](../../detection/wazuh/)

---

## Incident Report Template

```
INCIDENT REPORT
===============
Incident ID:      INC-001
Date/Time:        YYYY-MM-DD HH:MM
Analyst:          [Your name]
Status:           Open → Investigated → Closed

SUMMARY
-------
A spike of failed Windows authentication attempts was detected on the
Windows Endpoint (192.168.56.30), consistent with a credential brute-force
attack using the Hydra tool targeting the RDP service on port 3389.

TIMELINE
--------
HH:MM  - Alert fired in Wazuh (Rule 18152)
HH:MM  - Investigation began
HH:MM  - Source IP identified: 192.168.56.10 (Kali Linux)
HH:MM  - Attack confirmed as lab simulation (authorized)

FINDINGS
--------
- X failed login attempts in Y minutes
- Target account: Administrator
- Source: 192.168.56.10 (Kali Linux — authorized attacker)
- Attack type: RDP brute-force (T1110.001)
- Outcome: No successful authentication observed

MITRE ATT&CK
------------
- T1110.001 — Brute Force: Password Guessing

RECOMMENDATIONS
---------------
1. Enable account lockout after N failed attempts (Group Policy)
2. Restrict RDP to specific source IPs via Windows Firewall
3. Enable NLA (Network Level Authentication) for RDP
4. Consider deploying a dedicated jump host for RDP access

EVIDENCE
--------
- SIEM screenshot: [evidence/YYYY-MM-DD_incident-001/screenshots/]
- Windows Event Log extract: [evidence/YYYY-MM-DD_incident-001/logs/]
- Nmap evidence: [evidence/YYYY-MM-DD_incident-001/command-output/]
```

---

[← Back to Incidents](../) | [Incident 002 →](../incident-002/)
