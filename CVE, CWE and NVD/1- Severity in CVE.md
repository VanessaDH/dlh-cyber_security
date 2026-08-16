# CVE Severity and Security Prioritization

## 1. How does CVE severity affect prioritization?

Every CVE gets a severity score (usually via CVSS, 0–10) that reflects how dangerous it is — how easy it is to exploit and how much damage it could cause. Organizations use this score to decide **what to fix first**. Limited time and resources mean teams can't patch everything at once, so severity acts like a triage system: the most dangerous, easiest-to-exploit vulnerabilities get handled immediately, while minor ones can wait or be scheduled for routine maintenance.

## 2. Examples by severity level

**Low (0.1–3.9)**
A minor issue that's hard to exploit or has little impact (e.g., a bug that only leaks non-sensitive info). Response: log it, fix it during regular patch cycles, no urgency.

**Medium (4.0–6.9)**
A moderate risk — maybe it needs specific conditions to exploit, or causes limited damage (e.g., a flaw that lets an attacker crash one service). Response: schedule a fix within weeks, monitor for any active exploitation.

**High (7.0–8.9)**
A serious vulnerability that could lead to significant impact, like unauthorized data access (e.g., a flaw allowing an attacker to bypass authentication). Response: prioritize patching within days, may require temporary workarounds (like restricting access) until fixed.

**Critical (9.0–10.0)**
A severe, easily exploitable flaw that could lead to full system compromise (e.g., remote code execution like Log4Shell). Response: emergency action — patch immediately, possibly take affected systems offline, notify stakeholders, and monitor closely for signs of attack.

In short: the higher the severity, the faster and more aggressively an organization must respond.
