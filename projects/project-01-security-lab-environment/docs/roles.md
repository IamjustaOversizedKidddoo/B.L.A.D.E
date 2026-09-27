# Role Guide — Enterprise Security Lab

> This guide explains which parts of the lab apply to each cybersecurity role.

---

## SOC Analyst

**Primary lab components:**
- Wazuh Dashboard (192.168.56.50:5601) — alert triage and investigation
- Windows Endpoint events (Sysmon, Security Events)
- Linux Server logs (auth.log, auditd)
- Incident scenario exercises (`incidents/`)

**Skills practiced:**
- Alert triage and prioritization
- Log analysis and timeline reconstruction
- Writing incident tickets with evidence
- Identifying false positives vs. true positives

**Start here:** [`incidents/incident-001/`](../incidents/incident-001/)

---

## VAPT Analyst (Penetration Tester)

**Primary lab components:**
- Kali Linux (192.168.56.10) — attack workstation
- Web Lab (192.168.56.40) — DVWA, Juice Shop, WebGoat
- Linux Server (192.168.56.20) — SSH, web services
- Windows Endpoint (192.168.56.30) — Windows testing target

**Skills practiced:**
- Vulnerability scanning and enumeration
- Web application exploitation (OWASP Top 10)
- Network service exploitation
- Professional report writing

**Start here:** [`attack-scenarios/reconnaissance/`](../attack-scenarios/reconnaissance/)

---

## Detection Engineer

**Primary lab components:**
- Sigma rules (`detection/sigma/`)
- Wazuh custom rules (`detection/wazuh/`)
- Suricata IDS rules (`detection/suricata/`)
- MITRE ATT&CK mapping (`docs/mitre-mapping.md`)

**Skills practiced:**
- Writing detection rules in Sigma and Wazuh XML format
- Testing rules against real attack telemetry
- MITRE ATT&CK technique coverage analysis
- Tuning rules to reduce false positives

**Start here:** [`detection/detection-notes/`](../detection/detection-notes/)

---

## Incident Responder

**Primary lab components:**
- Incident scenarios (`incidents/`)
- Evidence collection scripts (`scripts/evidence/`)
- SIEM investigation (Wazuh Dashboard)

**Skills practiced:**
- Alert → Investigation → Containment → Remediation workflow
- Building investigation timelines from logs
- Writing professional IR reports
- Chain of custody for digital evidence

**Start here:** [`incidents/`](../incidents/) and [`docs/methodology.md`](methodology.md)

---

## Threat Hunter

**Primary lab components:**
- Wazuh Dashboard for log hunting
- Sysmon telemetry from Windows
- Network captures (Suricata, Wireshark)

**Skills practiced:**
- Hypothesis-driven threat hunting
- Behavioral analysis of legitimate vs. malicious activity
- Identifying attacker TTPs from raw telemetry
- Documenting hunts with findings

---

## Security Engineer

**Primary lab components:**
- Network design (`architecture/`)
- Hardening scripts (`setup/`)
- Automation scripts (`scripts/`)
- GitHub workflow (`.github/workflows/`)

**Skills practiced:**
- Secure network design and documentation
- Linux and Windows hardening
- Infrastructure as Code mindset
- Lab automation and reproducibility

---

[← Back to README](../README.md)
