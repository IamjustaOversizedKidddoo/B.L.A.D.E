# Contributing Guidelines — Enterprise Security Lab

Thank you for your interest in contributing to the Enterprise Security Lab project.

---

## What You Can Contribute

- **New attack scenarios** — documented exercises with evidence workflow and MITRE ATT&CK mapping
- **Detection rules** — Sigma or Wazuh rules with test cases
- **Setup guides** — Phase-specific configuration guides for lab components
- **Validation scripts** — Automated checks for lab health and exercise verification
- **Documentation improvements** — Fixing typos, improving clarity, adding missing context

---

## What NOT to Contribute

- Real malware samples or weaponized exploits
- Credentials, API keys, or any sensitive information
- Instructions that encourage illegal or unauthorized testing
- Configurations that would weaken the lab's isolation controls

---

## Contribution Process

### 1. Review Existing Documentation

Before contributing, review:
- [`docs/methodology.md`](docs/methodology.md) — testing approach
- [`architecture/threat-model.md`](architecture/threat-model.md) — security assumptions
- [`SECURITY.md`](SECURITY.md) — what is and isn't permitted

### 2. Branch Naming

```
feature/description-of-change
fix/what-you-are-fixing
docs/what-document-you-are-improving
detection/rule-name-and-technique
```

### 3. Documentation Standard

All new exercises and scenarios must include:

```
attack-scenarios/CATEGORY/EXERCISE-NAME/
├── README.md          ← Exercise overview, MITRE mapping, prerequisites
├── procedure.md       ← Step-by-step with commands and expected output
├── detection.md       ← What should trigger in SIEM, what rule covers it
└── evidence/          ← Example evidence format (no real data)
```

### 4. No Sensitive Data in Commits

Before committing, always run:

```bash
git status          # Review what you're staging
git diff --cached   # Review exact changes
```

Ensure no passwords, IPs of real production systems, or credentials appear.

### 5. Commit Messages

Follow this format:

```
type(scope): short description

Longer explanation if needed.

MITRE: T1046, T1018 (if applicable)
Phase: 2 (if applicable)
```

Types: `feat`, `fix`, `docs`, `detection`, `scripts`, `refactor`

---

## Code Style (Python Scripts)

- Python 3.8+ compatible
- Type hints where appropriate
- Docstrings on all functions
- No hardcoded credentials or paths (use relative paths from `Path(__file__)`)

---

*For security-sensitive issues, see [`SECURITY.md`](SECURITY.md)*
