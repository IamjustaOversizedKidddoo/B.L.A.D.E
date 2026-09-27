# Changelog — Enterprise Security Lab Environment

All notable changes to this project are documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [1.0.0] — Phase 1 Complete — Repository & Architecture

### Added

**Repository Foundation**
- `README.md` — Full project overview with architecture diagram, component table, phase roadmap, and learning outcomes
- `SECURITY.md` — Security policy covering authorized use, credential policy, and legal disclaimer
- `CONTRIBUTING.md` — Contribution guidelines with documentation standards
- `CHANGELOG.md` — This file

**Architecture Documentation** (`architecture/`)
- `architecture.md` — Full architecture document: design philosophy, network topology, component roles, data flows, security assumptions, and design rationale
- `ip-address-plan.md` — Complete IP allocation table, service port maps, hostname configuration, and routing rules
- `threat-model.md` — STRIDE-based threat model covering assets, threat actors, STRIDE analysis by category, attack tree, controls summary, security assumptions, out-of-scope definition, and residual risk acceptance
- `network-diagram.md` — ASCII network topology diagram and data flow diagrams (red team and blue team perspectives)

**Documentation** (`docs/`)
- `methodology.md` — PTES/OWASP-aligned security testing methodology with 5 phases and evidence standards
- `tools.md` — Tool inventory organized by role with MITRE ATT&CK mappings
- `roles.md` — Role guide explaining which lab components apply to SOC Analyst, VAPT Analyst, Detection Engineer, Incident Responder, Threat Hunter, and Security Engineer
- `mitre-mapping.md` — MITRE ATT&CK Enterprise technique-to-exercise mapping table with coverage overview
- `security-controls.md` — Security controls matrix with implementation type and status for each control
- `troubleshooting.md` — Guide for 7 most common lab issues

**Scripts** (`scripts/`)
- `scripts/validation/validate_lab.py` — Python lab health check: connectivity, service ports, isolation guidance, repo structure verification
- `scripts/evidence/collect_evidence.py` — Evidence collection with SHA-256 hashing, timestamped directories, and JSON manifest

### Pending (Phase 2+)
- Setup guides for each VM (`setup/kali/`, `setup/linux-server/`, `setup/windows/`, `setup/web-lab/`, `setup/monitoring/`)
- Networking configuration guide (`setup/networking/`)
- Docker Compose for web lab (`setup/web-lab/docker-compose.yml`)
- Wazuh deployment guide (`setup/monitoring/`)

---

## [Unreleased] — Phase 2

*Kali Linux and Linux Server configuration*

---

*See [README.md](README.md) for the full phase roadmap.*
