#!/usr/bin/env python3
"""Screen the full SAP-C02 question bank for AWS lifecycle terms.

Usage: python3 scripts/scan_aws_lifecycle.py
Output: reports/aws-lifecycle-candidates.json
Only stem and answer choices are scanned, not explanatory/audit prose.
This is keyword screening, NOT a determination that a question is outdated.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RULES = {
    "full-shutdown": [
        ("AWS CodeStar", r"\b(?:AWS\s+)?CodeStar\b(?!\s+(?:Connections|Notifications))"),
        ("AWS OpsWorks", r"\bOpsWorks\b"),
        ("Amazon QLDB", r"\b(?:Amazon\s+)?QLDB\b|Quantum Ledger Database"),
        ("AWS IoT Analytics", r"\bIoT Analytics\b"),
        ("Elastic Transcoder", r"\bElastic Transcoder\b"),
        ("Amazon WorkDocs", r"\bWorkDocs\b"),
        ("CloudWatch Evidently", r"\b(?:CloudWatch\s+)?Evidently\b"),
        ("Kinesis Data Analytics SQL", r"\bKinesis Data Analytics\b"),
        ("AWS Server Migration Service", r"\bServer Migration Service\b|\bAWS SMS\b"),
        ("AWS IoT Events", r"\bIoT Events\b"),
        ("Amazon Inspector Classic", r"\bInspector Classic\b"),
        ("AWS Snowball Edge", r"\bSnowball Edge\b"),
        ("AWS Snowcone", r"\bSnowcone\b"),
    ],
    "sunset": [
        ("AWS App Mesh", r"\bApp\s*Mesh\b"),
        ("AWS Proton", r"\bAWS Proton\b"),
        ("AWS WAF Classic", r"\bWAF Classic\b"),
        ("Amazon Pinpoint", r"\b(?:Amazon\s+)?Pinpoint\b"),
        ("AWS IoT Greengrass v1", r"\bGreengrass\s+(?:v1|version\s+1)\b"),
        ("Amazon DevOps Guru", r"\bDevOps Guru\b"),
    ],
    "maintenance-or-legacy": [
        ("CloudTrail Lake", r"\bCloudTrail Lake\b"),
        ("Aurora Serverless v1", r"\bAurora Serverless\s*(?:v1|version\s*1)\b"),
        ("EFS Max I/O", r"\bMax\s*I/O\b"),
        ("AWS Cloud9", r"\bCloud9\b"),
        ("S3 Select", r"\bS3 Select\b"),
        ("Amazon CloudSearch", r"\bCloudSearch\b"),
        ("AWS App Runner", r"\bApp Runner\b"),
        ("Amazon Kendra", r"\bKendra\b"),
        ("Amazon Q Business", r"\bQ Business\b"),
        ("AWS Migration Hub", r"\bMigration Hub\b"),
        ("AWS CodeCatalyst", r"\bCodeCatalyst\b"),
        ("AWS Audit Manager", r"\bAudit Manager\b"),
    ],
}
SOURCES = {
    "full-shutdown": "https://docs.aws.amazon.com/general/latest/gr/full_shutdown_services.html",
    "sunset": "https://docs.aws.amazon.com/general/latest/gr/sunset_services.html",
    "maintenance-or-legacy": "https://docs.aws.amazon.com/general/latest/gr/maintenance_services.html",
}
questions = json.loads((ROOT / "src/data/questions.json").read_text(encoding="utf-8"))
if not isinstance(questions, list):
    raise SystemExit("Expected questions.json to be an array")
hits = []
for q in questions:
    text = " ".join([q.get("stem", ""), *(o.get("text", "") for o in q.get("options", []))])
    matches = [
        {"service": name, "category": category, "source": SOURCES[category]}
        for category, rules in RULES.items()
        for name, pattern in rules
        if re.search(pattern, text, re.I)
    ]
    if matches:
        hits.append({"id": q["id"], "matches": matches, "status": "needs-manual-review"})
report = {
    "note": "Automated candidate detection only. Matches are not necessarily outdated answers.",
    "totalQuestions": len(questions),
    "candidateQuestions": len(hits),
    "candidates": hits,
}
path = ROOT / "reports/aws-lifecycle-candidates.json"
path.parent.mkdir(parents=True, exist_ok=True)
path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
print(f"Scanned {len(questions)} questions; found {len(hits)} lifecycle candidates; saved {path.relative_to(ROOT)}")
