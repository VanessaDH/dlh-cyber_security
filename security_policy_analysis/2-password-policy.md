# PASSWORD AND AUTHENTICATION POLICY
**SecureBank Financial Services**

| | |
|---|---|
| **Document ID** | POL-SEC-004 |
| **Version** | 3.0 |
| **Classification** | Internal — Restricted |
| **Effective Date** | 01 October 2026 |
| **Next Review** | 01 October 2027 (annual) |
| **Policy Owner** | Chief Information Security Officer |
| **Approved By** | Board Risk Committee |
| **Regulatory Basis** | PCI-DSS v4.0.1 Req. 8; SOX §404 (ITGC); FFIEC; GLBA; NIST SP 800-63B |
| **Supersedes** | POL-SEC-004 v2.1 |

---

## 1. Purpose

Compromised credentials are the leading initial access vector in financial services. This policy sets mandatory, auditable requirements for the creation, use, protection, storage, and lifecycle of all authentication credentials at SecureBank, so that access to customer funds, cardholder data, and financially significant systems is granted only to verified, authorized identities — and so that SecureBank can demonstrate compliance with PCI-DSS, SOX, FFIEC, and GLBA.

## 2. Scope

**Persons:** all employees, contractors, vendors, auditors, and — where stated — customers.

**Systems:**

| System Group | Tier |
|---|---|
| Core banking (ledger, payments, wire, card management) | **0 — Critical** |
| Customer portal (online/mobile banking, customer APIs) | **0 — Critical** |
| Administrative systems (domain, hypervisor, cloud, network, PAM, backup) | **0 — Critical** |
| Development environment (source control, CI/CD, test) | 1 — High |
| Employee workstations and corporate SSO | 2 — Moderate |

**Accounts:** standard, privileged, service/application, shared (where exceptionally approved), break-glass, third-party, and customer.

Systems in the Cardholder Data Environment (CDE) carry additional **[PCI]** requirements, which prevail on conflict. Financially significant systems carry **[SOX]** requirements. No exclusions without written Information Security confirmation.

## 3. Password Requirements

**3.1 Minimum length** (floors; systems must accept ≥ 64 characters and must not truncate):

| Account Type | Minimum |
|---|---|
| Customer portal | 12 |
| Employee workstation / SSO / development | 14 |
| Core banking user; CDE **[PCI §8.3.6 requires 12]** | 16 |
| Privileged / administrative | 20 (PAM-generated) |
| Service / application | 32 (randomly generated) |

**3.2 Composition.** All printable Unicode and spaces must be accepted. Arbitrary character-class rules **shall not** be imposed (NIST SP 800-63B); the length floors above exceed the PCI minimum and satisfy its intent. Passphrases of four or more unrelated words are recommended.

**3.3 Prohibited passwords.** All new and changed passwords **must** be screened in real time, before acceptance, and rejected if they: appear in a breach corpus (≥ 1 billion entries, refreshed monthly); are dictionary words or in the top 100,000 common passwords; contain repetition or keyboard sequences; contain context terms (`securebank`, `bank`, `password`, product or branch names, current year); derive from the user's name, username, or employee ID; or are leet-speak variants of any of these (`P@ssw0rd!`, `SecureBank2026!`). Screening normalizes case, diacritics, and leet substitutions before checking, and **fails closed** — if the service is unavailable, the change is refused.

**3.4 Reuse.** No reuse of the previous **12** passwords (PCI §8.3.7 requires 4), no reuse across SecureBank accounts, no reuse on any external service. Trivial variants count as reuse.

## 4. Password Management

**4.1 Initial and reset credentials.** Unique, randomly generated, delivered separately from the username, expire in **24 hours**, must be changed at first logon **[PCI §8.3.5]**. Default vendor credentials changed before any system reaches a production network **[PCI §2.2.2]**.

**4.2 Expiry.**

| Account | Rule |
|---|---|
| Any account protected by MFA (employee, CDE, customer) | **No scheduled expiry** |
| Password as the **sole** authentication factor | 90 days **[PCI §8.3.9]** |
| Privileged (interactive) | Rotated on every PAM check-in; ≤ 24 hours regardless |
| Service / application | ≤ 365 days, and immediately on personnel change **[PCI §8.6.3]** |

> **Reconciliation.** NIST SP 800-63B discourages rotation; PCI §8.3.9 mandates it. §8.3.9 applies **only where a password is the sole factor** — broad MFA deployment removes that condition, so both are satisfied. Position agreed with the QSA and recorded in the Report on Compliance.

**4.3 Mandatory change on event** — within 4 hours of notification: known or suspected compromise; breach-corpus match; access under an initial/reset password; departure of anyone holding a shared or service credential; or direction by Information Security.

**4.4 Reset procedure.** Identity must be verified by a factor independent of the credential being reset.

| Population | Method |
|---|---|
| Employee self-service | Registered MFA; disabled where no MFA is enrolled |
| Employee via Service Desk | Video identity verification against the HR record **plus** out-of-band confirmation; agent actions logged and sampled monthly |
| Privileged holders | Self-service **prohibited**; manager + Information Security approval, dual control |
| Customers | FFIEC risk-based: device recognition and out-of-band code to a channel registered ≥ 24 hours; contact-detail changes not accepted in the same session |

Knowledge-based questions using publicly discoverable information (mother's maiden name, first school) **must not** be used. Service Desk staff must never request, accept, or set a user-chosen password.

**4.5 Lockout.**

| Parameter | Standard | Core Banking | Privileged | Customer |
|---|---|---|---|---|
| Failed attempts | 6 (PCI max. 10) | 5 | 3 | 6, with progressive delay |
| Lockout duration | 30 min **[PCI §8.3.4]** | Manual unlock | Manual unlock + incident review | Verified reset flow |

Counter resets after 30 minutes. Independent rate limiting by source IP and ASN mitigates password spraying that stays below per-account thresholds. Lockouts on privileged, service, or core banking accounts raise a real-time SOC alert.

**4.6 Session timeouts.**

| Context | Idle | Absolute |
|---|---|---|
| CDE **[PCI §8.2.8]** | **15 min** | 8 h |
| Core banking; workstation lock; administrative/PAM | 10 min | 8 h / 4 h (PAM) |
| Customer portal | 10 min | 30 min; re-auth for funds movement |
| Development; standard corporate apps | 30 min | 12 h |

Sessions terminate server-side on timeout, logout, and password change; session IDs regenerate on privilege elevation. Concurrent privileged sessions are **prohibited**.

**4.7 Lifecycle.** Least-privilege provisioning on approved request. Access revoked **immediately** on termination — within 1 hour for involuntary terminations and privileged holders, 4 hours otherwise **[PCI §8.2.5]**. Role changes actioned within 24 hours. Third-party accounts enabled only for the period required and monitored **[PCI §8.2.7]**. Accounts disabled after 90 days' inactivity **[PCI §8.2.6]**. Access certified quarterly by business owners, monthly for privileged accounts; evidence retained **7 years [SOX]**.

**4.8 Confidentiality.** Passwords must never be shared, disclosed to any person including IT staff, transmitted in cleartext, written down, embedded in scripts or code, or committed to version control **[PCI §8.6.2]**. No SecureBank employee will ever legitimately ask for a password; any such request must be reported within 1 hour. Shared accounts are **prohibited** — without exception in the CDE **[PCI §8.2.2]**; where a legacy platform cannot support individual accounts, the credential is vaulted in PAM with per-user checkout so attribution is preserved. Access is granted by group, role, or delegation — never by disclosing a credential.

## 5. Multi-Factor Authentication

**5.1 Where MFA is mandatory** — no standing exemptions:

| Access | Requirement |
|---|---|
| All access into the CDE, from any location | Mandatory **[PCI §8.4.2]** |
| All remote access to the network | Mandatory **[PCI §8.4.3]** |
| All administrative and privileged access | Mandatory, **Tier 1 only** **[PCI §8.4.1]** |
| Core banking; administrative systems; PAM; password manager | Mandatory, **Tier 1 only** |
| Employee workstation, SSO, cloud consoles, development environment | Mandatory |
| SOX-relevant financial reporting systems | Mandatory **[SOX]** |
| Customer portal logon | Mandatory (risk-based step-up permitted on a bound device) — FFIEC |
| Customer high-risk actions (new payee, transfer above threshold, contact change, card issue) | Mandatory step-up, out-of-band — FFIEC |

MFA is enforced at the identity provider so no application can be reached around it; all factors must succeed before a session is issued **[PCI §8.5.1]**. Legacy protocols that cannot carry MFA (IMAP, POP3, SMTP AUTH, NTLM, WS-Trust) must be disabled.

**5.2 Approved methods**, ranked by phishing resistance:

| Tier | Method | Approved For |
|---|---|---|
| **1 — Phishing-resistant** | FIDO2/WebAuthn security keys (user verification required, attestation checked); PIV/smart card; hardware-backed platform authenticators | **Required** for privileged, core banking, administrative, CDE. Approved everywhere. |
| **2 — Cryptographic** | TOTP (RFC 6238, ±1 period drift, single-use); push **with number matching and context display** | Standard employee and customer access only |
| **3 — Deprecated** | SMS / voice OTP | **Prohibited for employees.** Customer fallback only, until 31 Dec 2027 |
| **Prohibited** | Push without number matching; knowledge-based questions; static PINs as a second factor | Never |

**5.3 Enrolment and recovery.** At least **two** authenticators of the required tier. New enrolment requires an existing authenticator or in-person verification, and alerts all registered channels. Recovery codes are single-use and hashed at rest. Self-service MFA reset with no remaining authenticator is **prohibited**.

**5.4 MFA fatigue.** Deny and report unrequested prompts within 1 hour. Push is rate-limited to 3 prompts per 5 minutes; 3 denials in 15 minutes suspends the account and alerts the SOC.

**5.5 Deprecation schedule.** Phishing-resistant MFA mandatory for all Tier 0 access by **31 Dec 2026**; SMS/voice removed for employees by **30 Jun 2027**; removed for customers by **31 Dec 2027**.

## 6. Password Storage

**6.1 Algorithms.** All passwords stored using a salted, computationally expensive one-way KDF **[PCI §8.3.2]**:

| Context | Algorithm and Parameters |
|---|---|
| FIPS-scope systems (core banking, CDE, customer portal, SOX-relevant) | **PBKDF2-HMAC-SHA-256**, ≥ **600,000** iterations, 32-byte output |
| Systems outside FIPS scope | **Argon2id**, m = 64 MiB, t = 3, p = 4 |
| Registered legacy platforms (transitional) | **bcrypt**, cost ≥ 12; inputs > 72 bytes pre-hashed |
| **Prohibited everywhere, including development and test** | MD5, SHA-1, bare SHA-2, unsalted hashes, reversible encryption, plaintext |

> Argon2id is cryptographically preferable but is not FIPS-validated; regulated systems therefore use PBKDF2. Iteration counts are reviewed annually to keep verification between 250 ms and 1 s.

**6.2 Salt and pepper.** Unique 16-byte CSPRNG salt per password. A ≥ 32-byte server-side pepper, held in the **HSM** and never stored with the hash, is applied via HMAC before the KDF; rotated every 24 months or on suspected compromise.

**6.3 Handling.** Constant-time comparison. Transparent rehash to current parameters on successful authentication. Generic, constant-time failure responses so usernames cannot be enumerated. Passwords, hashes, salts, and peppers must never appear in logs, error messages, stack traces, or telemetry — automated log scanning runs daily.

**6.4 Transmission.** TLS 1.2 minimum (1.3 preferred), forward-secret AEAD cipher suites, HSTS with preload **[PCI §4.2.1]**. Passwords in the POST body only — never a URL or query string. Cookies: `Secure`, `HttpOnly`, `SameSite=Strict`.

**6.5 Password managers.** The enterprise password manager is **mandatory** for all employee credentials not committed to memory, protected by a 16-character master passphrase and MFA, with zero-knowledge encryption. Personal password managers, personal cloud accounts, and browser sync **must not** hold SecureBank credentials. Customers are encouraged to use a reputable manager; customer-facing password fields **must** permit paste and offer a show-password toggle.

**6.6 Non-production environments.** Production credentials, production hashes, and production customer data **must never** be copied into development or test. Hard-coded secrets are blocked by pre-commit and CI/CD secret scanning; any detected secret is treated as compromised and rotated within 4 hours.

**6.7 Breach monitoring.** Employee and customer identifiers are monitored continuously against breach corpora and credential-stuffing feeds; a confirmed match forces a reset within **4 hours**.

## 7. Privileged Accounts

**7.1 Definition.** Any account able to alter security configuration, access data beyond individual entitlement, affect financial record integrity, or grant access to others — domain and cloud administrators, root and local admin, core banking override functions, DBAs, hypervisor and network administrators, backup and PAM administrators, CI/CD administrators, and any production write access.

**7.2 Separate identities.** Privileged access is exercised through a distinct named account (`adm-jsmith`), never the holder's standard account, never for email or browsing, with a credential different from the standard account, and only from a hardened Privileged Access Workstation or approved jump host **[SOX segregation of duties]**.

**7.3 Mandatory PAM and just-in-time access.** All privileged credentials are vaulted. **Standing privilege is prohibited.** Workflow: **request** (target system, task, ticket reference, duration) → **approve** (manager *and* system owner; dual approval for core banking, CDE, and PAM itself; self-approval technically blocked) → **grant** (PAM injects the credential; the user never sees it) → **time-box** (maximum 4 hours, non-extendable) → **record** (full keystroke and screen capture, high-risk commands alerted) → **rotate** (automatically on check-in, and every 24 hours regardless).

**7.4 Enhanced parameters.** 20-character generated password; Tier 1 phishing-resistant MFA re-verified at every checkout; lockout at 3 attempts with manual unlock and incident review; 10-minute idle and 4-hour absolute session limits; no concurrent sessions; PAW-only source enforced at the network layer; administrative interfaces reachable only from the management segment; behavioural analytics and off-hours alerting.

**7.5 Service and application accounts.** Vaulted in the secrets manager and retrieved at runtime — never hard-coded or held in config files **[PCI §8.6.2]**. Interactive logon **technically denied** **[PCI §8.6.1]**. One account per application, least privilege, no interactive administrative rights. Rotated ≤ 365 days and on any personnel change **[PCI §8.6.3]**. A named owning role recertifies quarterly. Migration to workload identity, certificates, and short-lived tokens in preference to static secrets is on the roadmap.

**7.6 Break-glass accounts.** Registered and limited in number; 32-character credential under split knowledge and dual control; excluded from SSO dependency so they survive an identity platform outage; non-suppressible CISO and SOC alert on any use; usable only under a declared incident; rotated immediately after use; justified-use review within 24 hours, retained 7 years.

**7.7 Vendor privileged access.** Brokered exclusively through PAM, enabled only for the approved window, individually attributed, fully recorded, supervised by a SecureBank employee for core banking and CDE, disabled on completion **[PCI §8.2.7, §12.8]**.

**7.8 Review.**

| Review | Frequency | Retention |
|---|---|---|
| Privileged account inventory and certification | Monthly | 7 years **[SOX]** |
| Standard user access certification | Quarterly | 7 years **[SOX]** |
| Service account owner recertification | Quarterly | 7 years |
| PAM session recording sample (≥ 10% of core banking and CDE) | Weekly | 7 years |
| Segregation of duties conflict analysis | Quarterly | 7 years **[SOX]** |
| Full authentication control testing (Internal Audit; QSA for CDE) | Annually | 7 years |

## 8. Logging and Monitoring

All authentication successes and failures, lockouts, password changes and resets, MFA events, PAM checkouts and session recordings, break-glass use, and account and configuration changes are logged with user, source, device, and UTC timestamp, forwarded to the SIEM in near real time, and written to tamper-evident storage **[PCI §10.2, §10.3]**. Retention: 12 months minimum with 3 months immediately searchable **[PCI §10.5.1]**; **7 years** for SOX-relevant access, certification evidence, and session recordings.

Critical alerts — paged to the on-call SOC with a 15-minute acknowledgement SLA — include: privileged logon without a PAM checkout; break-glass use; service account interactive logon; authentication logging disabled; and credentials detected in a repository. High alerts include password spraying (≥ 10 accounts from one source in 15 minutes), credential stuffing, impossible travel, MFA denial bursts, and privileged access outside an approved window.

Users have no expectation of privacy in authentication or session activity on SecureBank systems.

## 9. Incident Reporting

Report **within 1 hour of discovery**, without investigating first: suspected credential compromise, including credentials entered on a phishing page; any MFA prompt you did not initiate; loss of an authenticator or security key; any request for your password; credentials found stored insecurely or committed to a repository; suspected misuse of a privileged, service, or break-glass account; any observed policy violation.

**Channels:** Service Desk `https://servicedesk.securebank.com` · `security@securebank.com` · Security hotline ext. **4357** (24/7) · "Report Phishing" button · anonymous ethics line.

Good-faith reports — including of one's own error — attract no disciplinary action. Concealment or delay is an aggravating factor. Confirmed compromise of customer credentials or cardholder data triggers POL-SEC-007, including GLBA, state breach law, and card-brand notification assessment.

## 10. Roles and Responsibilities

| Role | Responsibilities |
|---|---|
| **All Users** | Meet the credential standards; use the enterprise password manager; enrol and protect two authenticators; never disclose credentials; report within 1 hour; complete annual training; acknowledge annually. |
| **Privileged Holders** | Use separate privileged identities from a PAW; request access just-in-time with ticket justification; accept full session recording; never use privileged accounts for routine work. |
| **Line Managers** | Approve access on genuine business need; complete quarterly certification; notify HR and IAM of leavers and movers within SLA; escalate non-compliance. |
| **System Owners** | Configure to STD-SEC-004; certify privileged access monthly and all access quarterly; own exceptions for their systems. |
| **IAM Team** | Operate identity, MFA, and PAM platforms; provision and deprovision within SLA; maintain the blocklist and breach feed; run rotation and certification campaigns. |
| **Information Security** | Own the technical standard; monitor and investigate; quarterly credential strength testing; approve authenticator types; lead credential-compromise response. |
| **CISO (Owner)** | Own and annually review this policy; approve exceptions; report quarterly to the Executive Risk Committee and annually to the Board. |
| **Service Desk** | Execute verified reset procedures; never request or record passwords; submit to monthly sampling. |
| **Human Resources** | Notify IAM of joiners, movers, and leavers (immediately for involuntary terminations); retain acknowledgements 7 years; administer discipline. |
| **Compliance** | Interpret PCI-DSS, SOX, FFIEC, GLBA; liaise with the QSA and examiners; maintain the control mapping. |
| **Internal Audit** | Independently test annually; report to the Audit Committee; validate remediation. |
| **Developers** | Implement to STD-SEC-004; never hard-code credentials; never use production credentials or data in non-production. |
| **Board Risk Committee** | Approve this policy; receive compliance and exception reporting; accept or reject High residual risk. |

## 11. Compliance Measurement

| Metric | Target | Frequency |
|---|---|---|
| MFA enrolment across in-scope accounts | 100% | Monthly |
| Phishing-resistant MFA on Tier 0 access | 100% by 31 Dec 2026 | Monthly |
| Privileged credentials vaulted in PAM | 100% | Monthly |
| Standing (non-JIT) privileged access | 0 | Monthly |
| Shared accounts in the CDE | 0 | Monthly |
| Deprovisioning within SLA of termination | 100% | Monthly |
| Access certification completed by due date | 100% | Quarterly |
| Sampled hashes failing strength testing | < 1% | Quarterly |
| Breach-corpus matches not reset within 4 hours | 0 | Continuous |
| Hard-coded secrets reaching a protected branch | 0 | Continuous |
| Policy acknowledgement | 100% within 14 days and annually | Monthly |

Verification methods: weekly configuration compliance scanning; quarterly offline hash strength audit under written CISO authorization (aggregate statistics only, recovered passwords never recorded); quarterly MFA bypass and lockout testing; annual credential-attack penetration test; annual QSA assessment and SOX ITGC testing.

## 12. Exceptions

Requests to Information Security must state the requirement, systems and users affected, justification, residual risk, compensating controls, remediation plan, and expiry date.

| Residual Risk | Approver | Maximum Duration |
|---|---|---|
| Low | CISO | 12 months |
| Medium | CISO + system owner | 6 months |
| High | CISO + CRO + Executive Risk Committee | 3 months |
| Affecting the CDE | As above **plus QSA concurrence**, disclosed in the ROC | 3 months |
| Affecting a SOX system | As above **plus** Internal Audit and external auditor notification | 3 months |

**No exception may be granted** to: plaintext or reversible password storage; shared accounts in the CDE; MFA for CDE, core banking, administrative, or privileged access; privileged session recording; or production credentials in non-production environments. The exception register is reviewed quarterly and examined annually by Internal Audit and the QSA.

## 13. Enforcement

Compliance is a condition of system access and a term of employment; for third parties it is a contractual obligation. Independently of any disciplinary process, SecureBank may without notice suspend access, terminate sessions, force resets, revoke privileges, and preserve and examine logs and session recordings.

| Tier | Conduct | Consequence |
|---|---|---|
| **1 — Minor** | Sub-standard password on a non-critical system; late MFA enrolment or training | Documented coaching; remedial training; correction within 5 business days |
| **2 — Moderate** | Credentials stored outside the password manager; password reused externally; missed access certification; repeated Tier 1 | Written warning on file; access restriction pending remediation; 12-month ineligibility for privileged entitlements |
| **3 — Serious** | Sharing credentials; routine use of a privileged account; circumventing MFA or session recording; hard-coding credentials; failing to report a known compromise; certifying access without review | Final warning or suspension; immediate revocation of privileged access; process up to dismissal; referred to Compliance for regulatory assessment |
| **4 — Severe** | Using another person's credentials; unauthorized break-glass or service account use; deliberate exfiltration of credentials or customer data; disabling authentication logging; falsifying certification evidence | Immediate revocation of all access; summary dismissal or contract termination; law enforcement referral; civil recovery; regulatory notification |

Conduct affecting financial reporting integrity or customer funds is presumptively Tier 4 and is reported to the CRO and Audit Committee. Good-faith self-disclosure is a significant mitigating factor; concealment is itself at least Tier 3. Discipline is administered by HR under POL-HR-002, with rights of representation and appeal.

## 14. Definitions

| Term | Definition |
|---|---|
| **CDE** | Cardholder Data Environment — systems that store, process, or transmit cardholder data, and connected systems. |
| **Credential** | Any secret used to authenticate: password, passphrase, API key, certificate, MFA seed, session token. |
| **KDF** | Key derivation function — a deliberately slow one-way function (Argon2id, bcrypt, PBKDF2) used for password storage. |
| **Salt / Pepper** | Salt: a unique random value stored with each hash. Pepper: a secret held separately (in the HSM) and applied before hashing. |
| **MFA** | Authentication using two or more factors from different categories: something you know, have, or are. |
| **Phishing-resistant MFA** | Authentication cryptographically bound to the legitimate site, so credentials cannot be relayed — FIDO2/WebAuthn, PIV. |
| **PAM** | Privileged Access Management — the platform brokering, recording, and rotating privileged credentials and sessions. |
| **PAW** | Privileged Access Workstation — a hardened endpoint used exclusively for administrative work. |
| **Just-in-time access** | Privilege granted only for an approved task and revoked automatically afterwards. |
| **Break-glass account** | An emergency privileged account under dual control, usable only during a declared incident. |
| **Service account** | A non-human account used by an application or system to authenticate. |
| **Step-up authentication** | Additional authentication demanded at a higher-risk action rather than at session start. |
| **Must / Shall** | Mandatory; non-compliance is a violation. **Should**: recommended. **May**: permitted. |

## 15. Related Documents

**Internal:** POL-SEC-001 Information Security · POL-SEC-002 Acceptable Use · POL-SEC-003 Access Control · POL-SEC-007 Incident Response · POL-SEC-014 Cryptographic Controls · POL-HR-002 Disciplinary Procedure · **STD-SEC-004 Authentication Technical Standard** (per-system parameters, cryptographic configuration, detection rules) · STD-SEC-005 PAM Operating Procedure · STD-IAM-001 Joiner–Mover–Leaver · PCI-DSS Scoping Document and current ROC · SOX ITGC Matrix.

**External:** NIST SP 800-63B *Digital Identity Guidelines* · NIST SP 800-132 (PBKDF2) · PCI-DSS v4.0.1 Requirements 8, 2, 7, 10, 12 · OWASP *Authentication* and *Password Storage* Cheat Sheets · CISA *Implementing Phishing-Resistant MFA* · FFIEC *Authentication and Access to Financial Institution Services and Systems* (2021) · SOX §302/§404 · GLBA Safeguards Rule, 16 CFR 314 · ISO/IEC 27001:2022 A.5.15–A.5.18, A.8.2, A.8.5.

## 16. Revision History

| Version | Date | Approved By | Changes |
|---|---|---|---|
| 1.0 | 12 Jan 2019 | CISO | Initial issue: 8-character minimum, complexity rules, 60-day expiry. |
| 2.0 | 03 Feb 2022 | Executive Risk Committee | MFA for remote access; PAM introduced; minimum length raised to 12. |
| 2.1 | 01 Mar 2024 | Executive Risk Committee | PCI-DSS v4.0 remediation: lockout and session timeout alignment. |
| **3.0** | **15 Sep 2026** | **Board Risk Committee** | Full rewrite to the NIST SP 800-63B model: composition rules removed, scheduled expiry removed where MFA is enforced (§4.2), blocklist screening mandated (§3.3). Length floors raised to 12–32 by account type. MFA mandatory estate-wide with a phishing-resistant tier and deprecation schedule (§5). PAM just-in-time model with mandatory vaulting, session recording, and 24-hour rotation (§7). Storage moved to FIPS-validated PBKDF2 with HSM-held pepper (§6). Added compliance metrics (§11) and companion standard STD-SEC-004. |

## 17. Acknowledgement

*Required within 14 days of joining, within 14 days of the effective date, and annually thereafter. Recorded in the HR system and retained 7 years as SOX evidence.*

- [ ] I have read and understood POL-SEC-004 v3.0 and have had the opportunity to ask questions.
- [ ] I understand the password requirements for each system I access, and that they differ by system criticality.
- [ ] I understand I must never disclose my password to anyone, including IT staff and my manager, and that no one at SecureBank will legitimately ask for it.
- [ ] I will use the enterprise password manager for SecureBank credentials, and not a personal one.
- [ ] I have enrolled at least two authenticators of the required tier, and will deny and report any prompt I did not initiate within 1 hour.
- [ ] I understand my authentication activity is logged and monitored, and that I have no expectation of privacy in it.
- [ ] I understand I must report suspected credential compromise within **1 hour**, and I know the channels.
- [ ] I understand violation may result in dismissal, law enforcement referral, and regulatory notification.

**Privileged holders additionally:**

- [ ] I understand my privileged access is just-in-time, time-limited, and requires a ticket reference and approval on each use.
- [ ] I consent to full keystroke and screen recording of privileged sessions and to their review.
- [ ] I will use my privileged account only for authorized administrative tasks, from an approved PAW.
- [ ] I understand break-glass credentials may be used only under a declared incident, that every use alerts the CISO, and that unjustified use is a severe violation.

| | |
|---|---|
| **Name / Employee ID** | ____________________________________ |
| **Job title / Department** | ____________________________________ |
| **Systems in scope** | ☐ Core banking ☐ Customer portal ☐ Workstation ☐ Administrative ☐ Development |
| **Privileged holder** | ☐ Yes (supplement completed) ☐ No |
| **Signature / Date** | ____________________________________ |

*Questions: `security@securebank.com` or the IAM team via the Service Desk.*

---

*End of document.*
