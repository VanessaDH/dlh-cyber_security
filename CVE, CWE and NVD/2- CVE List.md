# How CVE IDs Are Assigned

## 1. The process, step by step

1. **Discovery**: A vulnerability is found by a researcher, vendor, security company, or bug bounty program.
2. **Report**: The discoverer reports it to a CVE Numbering Authority (CNA) — often the affected vendor itself, or a third-party CNA.
3. **ID reserved**: The CNA reserves a CVE ID (format: CVE-YYYY-NNNNN) for the vulnerability, often before it's made public.
4. **Details added**: The CNA writes a short description, adds affected products/versions, and references (advisories, patches, etc.).
5. **Publication**: Once details are ready (and usually once a fix is available), the entry is published to the public CVE List.
6. **Enrichment**: Other databases, like the NVD, pick up the published CVE and add extra data such as CVSS severity scores and mitigation guidance.

## 2. Who manages the CVE List?

The CVE Program is run by **MITRE Corporation**, a non-profit that operates it under funding from the U.S. Department of Homeland Security (CISA). MITRE maintains the overall CVE List, sets the rules for the program, and oversees the network of CNAs.

## 3. What do CNAs do?

CVE Numbering Authorities are organizations authorized to assign CVE IDs within their own scope. This includes major software vendors (e.g., Microsoft, Apple, Google), security companies, open-source projects, and research organizations.

Their role:
- **Assign CVE IDs** to vulnerabilities they discover or that are reported to them (usually for their own products).
- **Write and publish** the vulnerability details and descriptions.
- **Follow CVE Program rules** to keep entries consistent and accurate.
- **Reduce bottlenecks** — by distributing the work across many CNAs instead of one central authority, vulnerabilities get IDs and get published faster.

In short: MITRE oversees the whole CVE system, while CNAs are the "authorized issuers" who actually assign IDs and publish details for vulnerabilities within their scope.
