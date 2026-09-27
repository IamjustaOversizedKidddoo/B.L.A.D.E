#!/usr/bin/env python3
"""
collect_evidence.py — Evidence Collection Script
=================================================
Collects and archives evidence from a security exercise:
  - Creates a timestamped directory
  - Copies files with metadata
  - Generates SHA-256 hashes for all collected files
  - Creates a summary manifest

Usage:
    python3 scripts/evidence/collect_evidence.py --exercise "nmap_recon"
    python3 scripts/evidence/collect_evidence.py --exercise "ssh_brute" --files output.txt screenshot.png

Requirements:
    - Python 3.8+
    - Run on Kali Linux or any lab machine
"""

import argparse
import hashlib
import json
import os
import shutil
import sys
from datetime import datetime
from pathlib import Path


# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURATION
# ─────────────────────────────────────────────────────────────────────────────

# Find the repository root (go up from scripts/evidence/)
SCRIPT_DIR = Path(__file__).parent.resolve()
REPO_ROOT = SCRIPT_DIR.parent.parent
EVIDENCE_BASE = REPO_ROOT / "evidence"


# ─────────────────────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────────────────────

def sha256_file(filepath: Path) -> str:
    """Compute SHA-256 hash of a file."""
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def create_evidence_directory(exercise_name: str) -> Path:
    """Create a timestamped evidence directory for the exercise."""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    safe_name = exercise_name.replace(" ", "_").replace("/", "-").lower()
    dir_name = f"{timestamp}_{safe_name}"
    evidence_dir = EVIDENCE_BASE / dir_name
    evidence_dir.mkdir(parents=True, exist_ok=True)

    # Create subdirectories
    (evidence_dir / "screenshots").mkdir(exist_ok=True)
    (evidence_dir / "command-output").mkdir(exist_ok=True)
    (evidence_dir / "packet-captures").mkdir(exist_ok=True)
    (evidence_dir / "logs").mkdir(exist_ok=True)

    return evidence_dir


def create_scope_file(evidence_dir: Path, exercise_name: str, targets: list, notes: str):
    """Create a scope.txt file documenting the exercise parameters."""
    scope_content = f"""EVIDENCE SCOPE FILE
===================
Exercise Name : {exercise_name}
Collected At  : {datetime.now().isoformat()}
Authorized Range: 192.168.56.0/24
Targets       : {', '.join(targets) if targets else 'All lab hosts'}
Notes         : {notes}

AUTHORIZATION
=============
This evidence was collected during an authorized security exercise
in the isolated lab environment (192.168.56.0/24).
All targets are intentionally vulnerable machines owned by the lab operator.
No external systems were accessed.
"""
    scope_path = evidence_dir / "00_scope.txt"
    scope_path.write_text(scope_content)
    print(f"  ✅ Scope file created: {scope_path.name}")
    return scope_path


def collect_files(evidence_dir: Path, files: list) -> list:
    """Copy provided files into the evidence directory and return their info."""
    collected = []
    for filepath in files:
        src = Path(filepath)
        if not src.exists():
            print(f"  ⚠️  File not found, skipping: {filepath}")
            continue

        # Determine destination subdirectory based on extension
        ext = src.suffix.lower()
        if ext in (".png", ".jpg", ".jpeg", ".webp", ".gif"):
            dest_dir = evidence_dir / "screenshots"
        elif ext in (".pcap", ".pcapng"):
            dest_dir = evidence_dir / "packet-captures"
        elif ext in (".log", ".txt") and "log" in src.name.lower():
            dest_dir = evidence_dir / "logs"
        else:
            dest_dir = evidence_dir / "command-output"

        dest = dest_dir / src.name
        shutil.copy2(src, dest)
        file_hash = sha256_file(dest)
        collected.append({
            "original_path": str(src.resolve()),
            "evidence_path": str(dest.relative_to(evidence_dir)),
            "sha256": file_hash,
            "size_bytes": dest.stat().st_size,
        })
        print(f"  ✅ Collected: {src.name} → {dest.relative_to(evidence_dir)}")
        print(f"     SHA-256: {file_hash}")

    return collected


def create_manifest(evidence_dir: Path, exercise_name: str, collected: list):
    """Create a JSON manifest of all collected evidence."""
    manifest = {
        "exercise": exercise_name,
        "collected_at": datetime.now().isoformat(),
        "evidence_directory": str(evidence_dir.name),
        "authorized_range": "192.168.56.0/24",
        "files": collected,
    }
    manifest_path = evidence_dir / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2))
    print(f"\n  ✅ Manifest created: manifest.json")
    return manifest_path


def generate_hashes_file(evidence_dir: Path):
    """Generate a hashes.sha256 file for all files in the evidence directory."""
    hash_lines = []
    for filepath in sorted(evidence_dir.rglob("*")):
        if filepath.is_file() and filepath.name != "hashes.sha256":
            file_hash = sha256_file(filepath)
            relative = filepath.relative_to(evidence_dir)
            hash_lines.append(f"{file_hash}  {relative}")

    hashes_path = evidence_dir / "hashes.sha256"
    hashes_path.write_text("\n".join(hash_lines) + "\n")
    print(f"  ✅ Hash file created: hashes.sha256")
    print(f"     Verify later with: sha256sum --check evidence/{evidence_dir.name}/hashes.sha256")


# ─────────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Collect and archive evidence from a security exercise",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 collect_evidence.py --exercise "nmap_recon"
  python3 collect_evidence.py --exercise "ssh_brute" --files nmap_output.txt bruteforce.log
  python3 collect_evidence.py --exercise "sqli_dvwa" --targets 192.168.56.40 --notes "SQLi in DVWA login form"
        """
    )
    parser.add_argument("--exercise", required=True, help="Name of the exercise (e.g., nmap_recon)")
    parser.add_argument("--files", nargs="*", default=[], help="Files to collect as evidence")
    parser.add_argument("--targets", nargs="*", default=[], help="Target IPs involved in this exercise")
    parser.add_argument("--notes", default="", help="Additional notes about this exercise")
    args = parser.parse_args()

    print("\n╔════════════════════════════════════════════════╗")
    print("║     EVIDENCE COLLECTION SCRIPT                ║")
    print("╚════════════════════════════════════════════════╝")
    print(f"\n  Exercise: {args.exercise}")
    print(f"  Targets:  {', '.join(args.targets) if args.targets else 'Not specified'}")
    print(f"  Files:    {len(args.files)} provided\n")

    # Create evidence directory
    evidence_dir = create_evidence_directory(args.exercise)
    print(f"  📁 Evidence directory: {evidence_dir}")
    print()

    # Create scope file
    create_scope_file(evidence_dir, args.exercise, args.targets, args.notes)

    # Collect files
    collected = []
    if args.files:
        collected = collect_files(evidence_dir, args.files)
    else:
        print(f"  ℹ️  No files provided. Add command output files using --files")
        print(f"     Example: python3 collect_evidence.py --exercise {args.exercise} --files output.txt")

    # Create manifest and hash file
    create_manifest(evidence_dir, args.exercise, collected)
    generate_hashes_file(evidence_dir)

    print(f"\n  ✅ Evidence archived to:")
    print(f"     evidence/{evidence_dir.name}/")
    print()


if __name__ == "__main__":
    main()
