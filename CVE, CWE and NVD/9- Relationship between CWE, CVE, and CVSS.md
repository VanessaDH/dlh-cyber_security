# The Relationship Between CWE, CVE, and CVSS

## What each one does

- **CWE (Common Weakness Enumeration)**: Classifies the general *type* of security flaw — the root cause (e.g., "Improper Input Validation," "SQL Injection").
- **CVE (Common Vulnerabilities and Exposures)**: Identifies a *specific* publicly disclosed vulnerability in a specific product/version (e.g., "CVE-2021-44228: Log4Shell").
- **CVSS (Common Vulnerability Scoring System)**: Assigns a *severity score* (0–10) to a specific vulnerability, based on factors like how it's exploited and what damage it can cause.

## How they relate to each other

Think of it as a chain from general to specific to measured:

**CWE (the type of mistake) → CVE (a real case of that mistake) → CVSS (how bad that case is)**

- A CVE entry describes one real vulnerability, and it's usually mapped to one or more CWEs to explain *why* it exists (its root cause).
- That same CVE is then scored using CVSS to show *how severe* it is — how easily it can be exploited and what impact it could have.
- The NVD ties all three together: it publishes CVE entries, links them to relevant CWE categories, and attaches CVSS scores — giving a full picture in one place.

**Example**: CVE-2021-44228 (Log4Shell) is mapped to CWE-502 (Deserialization of Untrusted Data) and CWE-917 (Expression Language Injection), and was scored 10.0 (Critical) under CVSS — showing the weakness type, the real-world case, and its severity all at once.

## How they work together in a vulnerability management strategy

1. **Detect and identify**: Scanners and asset inventories flag known CVEs affecting the organization's software.
2. **Understand root cause**: The CWE(s) linked to each CVE explain *why* the vulnerability exists, helping teams fix the underlying pattern — not just the one instance.
3. **Prioritize by severity**: CVSS scores tell teams *how urgently* each CVE needs attention, enabling risk-based triage instead of treating everything equally.
4. **Fix systemically**: By tracking which CWE categories keep showing up across multiple CVEs, teams can address root causes in coding standards, training, and code review — reducing future vulnerabilities of that type.
5. **Report and communicate**: Together, these frameworks let security teams explain risk clearly to stakeholders — what's wrong (CWE), where it is (CVE), and how bad it is (CVSS) — supporting informed, data-driven decisions.
6. **Continuous improvement**: Over time, patterns across CWE/CVE/CVSS data reveal whether security practices are actually reducing weaknesses, or if certain categories need more investment.

In short: CWE explains the "why," CVE identifies the "what and where," and CVSS quantifies the "how bad." Used together, they let an organization move from simply reacting to individual vulnerabilities toward a structured, prioritized, and root-cause-focused vulnerability management strategy.
