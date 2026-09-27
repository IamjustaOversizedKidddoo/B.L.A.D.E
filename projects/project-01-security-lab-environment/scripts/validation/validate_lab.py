#!/usr/bin/env python3
"""
validate_lab.py — Enterprise Security Lab Health Check
=====================================================
Runs a series of connectivity and configuration checks
to validate that the lab is correctly set up.

Usage:
    Run from Kali Linux (192.168.56.10):
        python3 scripts/validation/validate_lab.py

    Run with verbose output:
        python3 scripts/validation/validate_lab.py --verbose

    Run only specific checks:
        python3 scripts/validation/validate_lab.py --only network

Requirements:
    - Python 3.8+
    - Run on Kali Linux (192.168.56.10) only
    - All target VMs must be powered on before running
"""

import subprocess
import sys
import argparse
import socket
import time
from datetime import datetime

# ─────────────────────────────────────────────────────────────────────────────
# LAB CONFIGURATION
# ─────────────────────────────────────────────────────────────────────────────

LAB_HOSTS = {
    "linux-srv":  "192.168.56.20",
    "win-ep":     "192.168.56.30",
    "web-lab":    "192.168.56.40",
    "siem":       "192.168.56.50",
}

KALI_IP = "192.168.56.10"

# Services expected to be available on each host
EXPECTED_SERVICES = {
    "192.168.56.20": [22, 80],           # Linux Server: SSH, HTTP
    "192.168.56.30": [3389, 445],        # Windows: RDP, SMB
    "192.168.56.40": [8080, 3000, 8090], # Web Lab: DVWA, JuiceShop, WebGoat
    "192.168.56.50": [5601, 1514],       # SIEM: Dashboard, Wazuh listener
}

# Internet isolation check: these hosts must NOT reach the internet
INTERNET_IP = "8.8.8.8"

# ─────────────────────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────────────────────

PASS = "✅ PASS"
FAIL = "❌ FAIL"
WARN = "⚠️  WARN"
INFO = "ℹ️  INFO"

results = []


def log(level, message, verbose_only=False):
    """Print a log message."""
    if verbose_only and not ARGS.verbose:
        return
    print(f"  {level}  {message}")


def record(check_name, passed, message=""):
    """Record a check result."""
    results.append({
        "check": check_name,
        "passed": passed,
        "message": message,
    })


def ping_host(ip: str, count: int = 1, timeout: int = 1) -> bool:
    """Ping a host and return True if reachable."""
    try:
        result = subprocess.run(
            ["ping", "-c", str(count), "-W", str(timeout), ip],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=5,
        )
        return result.returncode == 0
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return False


def check_port(ip: str, port: int, timeout: float = 2.0) -> bool:
    """Check if a TCP port is open on a host."""
    try:
        with socket.create_connection((ip, port), timeout=timeout):
            return True
    except (socket.timeout, ConnectionRefusedError, OSError):
        return False


# ─────────────────────────────────────────────────────────────────────────────
# CHECKS
# ─────────────────────────────────────────────────────────────────────────────

def check_network_connectivity():
    """Verify all lab hosts are reachable from Kali."""
    print("\n[1/4] NETWORK CONNECTIVITY CHECKS")
    print("─" * 50)

    all_passed = True
    for hostname, ip in LAB_HOSTS.items():
        reachable = ping_host(ip)
        if reachable:
            log(PASS, f"{hostname} ({ip}) is reachable")
            record(f"ping_{hostname}", True)
        else:
            log(FAIL, f"{hostname} ({ip}) is NOT reachable — is the VM running?")
            record(f"ping_{hostname}", False, f"{ip} not responding to ping")
            all_passed = False

    return all_passed


def check_service_ports():
    """Verify expected services are listening on each host."""
    print("\n[2/4] SERVICE PORT CHECKS")
    print("─" * 50)

    all_passed = True
    for ip, ports in EXPECTED_SERVICES.items():
        hostname = next((k for k, v in LAB_HOSTS.items() if v == ip), ip)
        for port in ports:
            if check_port(ip, port):
                log(PASS, f"{hostname}:{port} is open")
                record(f"port_{ip}_{port}", True)
            else:
                log(WARN, f"{hostname}:{port} is closed (service may not be configured yet)")
                record(f"port_{ip}_{port}", False, f"Port {port} on {ip} not reachable")
                # Port checks are WARN not FAIL (services may not be set up yet in Phase 1)

    return all_passed


def check_internet_isolation():
    """Verify that target VMs cannot reach the internet (important safety check).

    NOTE: This check pings 8.8.8.8 FROM KALI only.
    To fully verify isolation, manually run `ping 8.8.8.8` on each target VM.
    The script reminds you to do this.
    """
    print("\n[3/4] INTERNET ISOLATION VERIFICATION")
    print("─" * 50)

    print(f"  {INFO}  Checking internet access from Kali (should succeed — NAT adapter)...")
    kali_has_internet = ping_host(INTERNET_IP)

    if kali_has_internet:
        log(PASS, "Kali has internet access via NAT adapter (expected)")
        record("kali_internet", True)
    else:
        log(WARN, "Kali cannot reach internet — apt update will fail. Check NAT adapter.")
        record("kali_internet", False, "Kali has no internet access")

    print()
    print(f"  {INFO}  MANUAL STEP REQUIRED:")
    print(f"         Run the following on each target VM to verify isolation:")
    print(f"         Linux Server (192.168.56.20):  ping -c 1 8.8.8.8   # Must FAIL")
    print(f"         Windows EP (192.168.56.30):    ping -n 1 8.8.8.8   # Must FAIL")
    print(f"         Web Lab (192.168.56.40):       ping -c 1 8.8.8.8   # Must FAIL")
    print(f"         SIEM (192.168.56.50):          ping -c 1 8.8.8.8   # Must FAIL")
    print()
    print(f"  {WARN}  Isolation cannot be automatically verified from Kali.")
    print(f"         You MUST manually verify this before running any exercises.")

    return True


def check_lab_structure():
    """Verify the repository directory structure is correctly set up."""
    import os

    print("\n[4/4] REPOSITORY STRUCTURE CHECKS")
    print("─" * 50)

    # Find repository root (search upwards from script location)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.abspath(os.path.join(script_dir, "..", ".."))

    required_dirs = [
        "architecture",
        "setup",
        "scripts",
        "detection",
        "attack-scenarios",
        "vulnerability-assessments",
        "incidents",
        "reports",
        "evidence",
        "docs",
    ]

    required_files = [
        "README.md",
        "SECURITY.md",
        "CONTRIBUTING.md",
        "architecture/architecture.md",
        "architecture/ip-address-plan.md",
        "architecture/threat-model.md",
        "architecture/network-diagram.md",
        "docs/methodology.md",
        "docs/tools.md",
        "docs/roles.md",
        "docs/mitre-mapping.md",
    ]

    all_passed = True

    for d in required_dirs:
        path = os.path.join(repo_root, d)
        if os.path.isdir(path):
            log(PASS, f"Directory exists: {d}/", verbose_only=True)
            record(f"dir_{d}", True)
        else:
            log(FAIL, f"Missing directory: {d}/")
            record(f"dir_{d}", False, f"Directory not found: {d}")
            all_passed = False

    for f in required_files:
        path = os.path.join(repo_root, f)
        if os.path.isfile(path):
            log(PASS, f"File exists: {f}", verbose_only=True)
            record(f"file_{f.replace('/', '_')}", True)
        else:
            log(FAIL, f"Missing file: {f}")
            record(f"file_{f.replace('/', '_')}", False, f"File not found: {f}")
            all_passed = False

    return all_passed


# ─────────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────────

def print_summary():
    """Print a summary of all check results."""
    print("\n" + "═" * 60)
    print("  LAB VALIDATION SUMMARY")
    print("═" * 60)

    passed = sum(1 for r in results if r["passed"])
    failed = sum(1 for r in results if not r["passed"])
    total = len(results)

    if failed == 0:
        print(f"\n  ✅ ALL CHECKS PASSED ({passed}/{total})")
    else:
        print(f"\n  Results: {passed} passed, {failed} failed, {total} total")
        print(f"\n  Failed checks:")
        for r in results:
            if not r["passed"]:
                msg = f" — {r['message']}" if r["message"] else ""
                print(f"    ❌ {r['check']}{msg}")

    print(f"\n  Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("═" * 60)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Validate the Enterprise Security Lab environment",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Show all checks including passing ones"
    )
    parser.add_argument(
        "--only",
        choices=["network", "ports", "isolation", "structure"],
        help="Run only a specific check category"
    )
    return parser.parse_args()


if __name__ == "__main__":
    ARGS = parse_args()

    print("╔════════════════════════════════════════════════════════╗")
    print("║     ENTERPRISE SECURITY LAB — HEALTH CHECK            ║")
    print("║     Run from: Kali Linux (192.168.56.10)              ║")
    print("╚════════════════════════════════════════════════════════╝")

    only = ARGS.only

    if only is None or only == "structure":
        check_lab_structure()

    if only is None or only == "network":
        check_network_connectivity()

    if only is None or only == "ports":
        check_service_ports()

    if only is None or only == "isolation":
        check_internet_isolation()

    print_summary()
