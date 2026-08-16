# CWE vs. CVE

## What is CWE?

CWE (Common Weakness Enumeration) is a catalog of general *types* of software and hardware security weaknesses — the underlying flaws or mistakes in design and coding that can lead to vulnerabilities. Examples include CWE-79 (Cross-Site Scripting) and CWE-89 (SQL Injection). CWE is maintained by MITRE.

## How does it differ from CVE?

- **CWE** = a category or "root cause" of weakness (e.g., "Improper Input Validation"). It's general and reusable — it describes a *class* of problem, not a specific incident.
- **CVE** = a specific, publicly disclosed vulnerability found in a specific product/version (e.g., "CVE-2021-44228: Log4Shell in Apache Log4j"). It's a single, real-world instance.

Put simply: **CWE is the "type of mistake," and CVE is the "actual case where that mistake caused a problem."** A CVE entry is often mapped to one or more CWEs to explain *why* the vulnerability exists.

| | CWE | CVE |
|---|---|---|
| Scope | General weakness category | Specific vulnerability instance |
| Example | CWE-89: SQL Injection | CVE-2021-44228: Log4Shell |
| Purpose | Classify root causes | Track real-world disclosed flaws |
| Maintained by | MITRE | MITRE (CVE Program), enriched by NVD |

## Why are both important in cybersecurity?

- **CVE** lets organizations track and respond to specific, real vulnerabilities affecting their actual software — it's what you patch.
- **CWE** helps developers and security teams understand *why* vulnerabilities keep happening, so they can fix root causes in code, training, and design — not just patch one instance at a time.
- Used together, they connect the dots between "what went wrong in this specific product" (CVE) and "what kind of mistake keeps causing these problems" (CWE) — supporting both reactive patching and proactive secure development.
