# CVSS Score Calculation: Remote Code Execution Vulnerability

## The Scenario

A remote code execution (RCE) vulnerability in a widely used web server allows an attacker to execute arbitrary code remotely, without requiring authentication.

## Step 1: Identify the Base Metrics

Using the metrics provided for this exercise:

| Metric | Value | Meaning |
|---|---|---|
| Attack Vector (AV) | Network (N) | Exploitable remotely over a network |
| Attack Complexity (AC) | Low (L) | No special conditions needed to exploit |
| Privileges Required (PR) | Required → treated as Low (L) | Attacker needs some minimal privilege |
| User Interaction (UI) | Required (R) | A victim/user must do something (e.g., click a link) |
| Scope (S) | Unchanged (U) | Impact stays within the vulnerable component |
| Confidentiality (C) | High (H) | Assumed — RCE typically exposes all data |
| Integrity (I) | High (H) | Assumed — attacker can modify anything |
| Availability (A) | High (H) | Assumed — attacker can fully disrupt the system |

**Note on a discrepancy:** the scenario text says the exploit needs "no authentication," which normally maps to **Privileges Required: None (N)** and often **User Interaction: None (N)** too — this is the classic profile for real-world unauthenticated RCEs (e.g., Log4Shell). The metrics table for this exercise instead lists Privileges Required and User Interaction as "Required." I calculated the score using the table as given, and included the alternate (fully unauthenticated) score below for comparison.

## Step 2: Calculate the Base Score (CVSS v3.1 formula)

**Metric weights used:**
AV:N = 0.85, AC:L = 0.77, PR:L (Scope Unchanged) = 0.62, UI:R = 0.62, C/I/A High = 0.56 each

**Impact Sub-Score (ISC):**
```
ISCBase = 1 - [(1-0.56) × (1-0.56) × (1-0.56)]
        = 1 - [0.44 × 0.44 × 0.44]
        = 1 - 0.0852
        = 0.9148

Impact = 6.42 × ISCBase   (Scope Unchanged)
        = 6.42 × 0.9148
        ≈ 5.87
```

**Exploitability Sub-Score:**
```
Exploitability = 8.22 × AV × AC × PR × UI
               = 8.22 × 0.85 × 0.77 × 0.62 × 0.62
               ≈ 2.07
```

**Base Score:**
```
BaseScore = Roundup(Impact + Exploitability)
          = Roundup(5.87 + 2.07)
          = Roundup(7.94)
          = 8.0
```

**Result: CVSS Base Score = 8.0 → Severity: High**

*(For comparison: if Privileges Required and User Interaction were both "None" — matching the "no authentication needed" description — the score would be ~9.8, Critical, which is typical for real-world unauthenticated RCE vulnerabilities like Log4Shell.)*

## Step 3: Interpret the Score

CVSS severity ranges: Low (0.1–3.9), Medium (4.0–6.9), High (7.0–8.9), Critical (9.0–10.0).

An **8.0 (High)** score means:
- The vulnerability is remotely exploitable and easy to trigger (network access, low complexity).
- Successful exploitation gives an attacker full control — reading, modifying, or destroying data, or crashing the system.
- It poses a serious risk to confidentiality, integrity, and availability, but the requirement for some privilege/user interaction slightly lowers urgency compared to a fully unauthenticated, zero-click exploit (which would push it to Critical).
- For an organization, this level of vulnerability threatens business-critical operations, data breaches, regulatory exposure, and reputational damage if left unpatched.

## Step 4: Recommended Mitigation Strategies

Because this is High (or Critical, depending on the exact scoring assumptions):

- **Patch immediately**: Apply the vendor's security update as top priority — treat within 24–72 hours given the severity.
- **Virtual patching**: If a patch isn't yet available, deploy a Web Application Firewall (WAF) rule or intrusion prevention signature to block known exploit patterns.
- **Network segmentation**: Restrict access to the affected web server from untrusted networks; limit exposure to only what's necessary.
- **Reduce attack surface**: Disable unused features/modules of the web server that may be tied to the vulnerable code path.
- **Enhanced monitoring**: Watch logs and network traffic for exploitation attempts or indicators of compromise (IOCs) related to this CVE.
- **Least privilege**: Ensure service accounts running the web server have minimal permissions, so even if exploited, the blast radius is limited.
- **Incident response readiness**: Prepare to isolate and investigate affected systems quickly in case exploitation is detected before patching completes.
- **Communicate and track**: Log this as a critical/high-priority ticket, notify stakeholders, and confirm remediation via a follow-up scan.
