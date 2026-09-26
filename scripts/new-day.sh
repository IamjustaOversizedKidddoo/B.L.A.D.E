#!/usr/bin/env bash
# scripts/new-day.sh — Shell wrapper for on-demand day scaffolding

if command -v python3 &>/dev/null; then
    python3 "$(dirname "$0")/new-day.py" "$@"
elif command -v python &>/dev/null; then
    python "$(dirname "$0")/new-day.py" "$@"
else
    echo "Error: Python 3 is required to run new-day.py"
    exit 1
fi
