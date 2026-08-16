# Common CWEs and Their Impact

## Examples of common CWEs

**CWE-79: Cross-Site Scripting (XSS)**
Occurs when an application includes untrusted input in a web page without proper sanitization. Impact: attackers can inject malicious scripts to steal session cookies, hijack accounts, or deface pages.

**CWE-89: SQL Injection**
Happens when user input is inserted into SQL queries without proper validation or parameterization. Impact: attackers can read, modify, or delete database data, or bypass authentication entirely.

**CWE-20: Improper Input Validation**
A broad category where an application doesn't properly check input before using it. Impact: can lead to a wide range of issues, from crashes to injection attacks to data corruption.

**CWE-287: Improper Authentication**
Occurs when an application doesn't correctly verify a user's identity. Impact: attackers can impersonate legitimate users or bypass login mechanisms entirely.

**CWE-269: Improper Privilege Management**
Happens when an application doesn't properly restrict what actions a user can perform based on their role. Impact: users can gain unauthorized access to admin functions or sensitive data (privilege escalation).

**CWE-798: Use of Hard-coded Credentials**
Occurs when passwords, API keys, or secrets are embedded directly in source code. Impact: attackers who access the code (e.g., via a public repo) get instant access to systems.

**CWE-22: Path Traversal**
Happens when an application uses user input to build a file path without proper sanitization. Impact: attackers can access files outside the intended directory, exposing sensitive system or config files.

**CWE-352: Cross-Site Request Forgery (CSRF)**
Occurs when an app doesn't verify that a request truly came from an authenticated user's intended action. Impact: attackers can trick users into unknowingly performing actions (like changing account settings) on their behalf.

## Prioritizing which weaknesses to address

1. **Assess exploitability and exposure**: Weaknesses reachable by unauthenticated, remote attackers (e.g., SQLi, XSS on public-facing pages) generally rank higher than ones requiring local access or special conditions.
2. **Consider impact severity**: Prioritize weaknesses that could lead to full compromise — data breach, authentication bypass, privilege escalation — over lower-impact issues like minor info disclosure.
3. **Use recognized rankings as a starting point**: The CWE Top 25 Most Dangerous Software Weaknesses and OWASP Top 10 reflect real-world prevalence and impact, and are a good baseline for prioritization.
4. **Factor in business context**: A weakness in a core payment feature matters more than the same weakness in an internal admin tool rarely used.
5. **Check for known active exploitation**: If a weakness type is commonly exploited in the wild (e.g., via CVEs tied to that CWE), treat it as higher priority.
6. **Balance fix effort vs. risk**: Some fixes (like adding parameterized queries) are relatively simple and high-impact — tackle "quick wins" with high risk reduction first.
7. **Bake it into the SDLC**: Rather than only fixing after the fact, integrate CWE-aware checks into design review, secure coding standards, static analysis, and testing so high-risk categories (injection, auth, access control) are caught early and consistently — not just triaged late.

In short: prioritize by combining *how easily* a weakness can be exploited, *how bad* the consequences would be, and *how critical* the affected system is to the business — using standard lists like CWE Top 25 as a reliable starting point.
