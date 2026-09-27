# Security Policy — Enterprise Security Lab Environment

## Purpose

This document defines the security policy for the `project-01-security-lab-environment` project. It establishes the rules under which this project may be used and how security concerns related to the project itself should be reported.

---

## Authorized Use

This project is **authorized only** for:

1. Educational and research purposes in your **own private lab environment**
2. Exercises performed against **virtual machines you own and operate**
3. Authorized penetration testing engagements with **written client authorization**

---

## Out of Scope — Strictly Prohibited

The following are **strictly prohibited** under all circumstances:

- Using techniques documented here against systems, networks, or applications you do not own or have explicit written authorization to test
- Exposing intentionally vulnerable applications (DVWA, Juice Shop, WebGoat) to untrusted networks
- Running real malware samples in this lab environment (use REMnux/FlareVM or an air-gapped analysis VM for malware analysis)
- Attacking systems outside the defined lab subnet (`192.168.56.0/24`)
- Sharing or publishing credentials, keys, or tokens committed to this repository

---

## Credential Policy

This repository **MUST NOT** contain:

- VM login passwords or SSH private keys
- API keys or tokens for any external service
- VPN credentials
- Personal or organizational identifiers

If you discover that sensitive information has been accidentally committed:

1. Do not push to remote
2. Remove the file and its history: `git filter-branch` or `git filter-repo`
3. Rotate any exposed credentials immediately

The `.gitignore` in this repository is configured to exclude common credential file patterns. **Review it before every commit.**

---

## Reporting Security Issues in This Project

If you discover a security issue **in this project's own documentation or scripts** (e.g., a script that creates insecure configurations, logic that could accidentally expose lab VMs, etc.):

1. **Do NOT open a public GitHub issue** if the disclosure could cause harm
2. Contact the repository owner directly
3. Provide a clear description of the issue and reproduction steps
4. Allow reasonable time for remediation before public disclosure

---

## Network Safety Requirements

Before running any lab exercises:

1. Verify all target VMs use **Host-Only** adapter (not Bridged or NAT)
2. Confirm internet isolation: `ping 8.8.8.8` from each target VM must **fail**
3. Verify Kali's NAT adapter cannot reach lab targets (`ping 192.168.56.20` from Kali's NAT interface — use correct interface)
4. Run the lab health check: `python3 scripts/validation/validate_lab.py`

---

## Legal Disclaimer

The authors and contributors of this project are not responsible for:

- Misuse of techniques or tools documented here
- Damage caused by improper lab configuration
- Legal consequences arising from unauthorized testing

**You are solely responsible for complying with all applicable laws and regulations in your jurisdiction.**

---

*Last updated: Phase 1 — Project initialization*
