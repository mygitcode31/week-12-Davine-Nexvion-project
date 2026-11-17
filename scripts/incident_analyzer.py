#!/usr/bin/env python3

import re
import sys
from pathlib import Path

INCIDENTS = [
    (
        "CRITICAL",
        "Kubernetes pod failure",
        r"CrashLoopBackOff|OOMKilled",
        "Inspect pod status, events and container resource limits."
    ),
    (
        "HIGH",
        "Application server error",
        r"\b5\d\d\b",
        "Inspect application logs and the failing HTTP request."
    ),
    (
        "HIGH",
        "Service connectivity failure",
        r"connection refused|connection reset",
        "Verify service availability, ports and network connectivity."
    ),
    (
        "MEDIUM",
        "Health probe failure",
        r"readiness probe failed|liveness probe failed",
        "Check application health endpoint and probe configuration."
    ),
]

def analyze(log_file):
    path = Path(log_file)

    if not path.is_file():
        print(f"ERROR: Log file not found: {path}")
        return 1

    findings = 0

    for line_number, line in enumerate(
        path.read_text(errors="replace").splitlines(), start=1
    ):
        for severity, incident, pattern, recommendation in INCIDENTS:
            if re.search(pattern, line, re.IGNORECASE):
                findings += 1
                print(f"\n[{severity}] {incident}")
                print(f"Line: {line_number}")
                print(f"Log: {line}")
                print(f"Recommendation: {recommendation}")
                break

    if findings == 0:
        print("No recognized incident patterns found.")
    else:
        print(f"\nAnalysis complete: {findings} incident(s) detected.")

    return 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 scripts/incident_analyzer.py <log-file>")
        sys.exit(1)

    sys.exit(analyze(sys.argv[1]))
