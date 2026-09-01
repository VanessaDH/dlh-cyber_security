# Task 0 — Policy Analysis

## Part A — Missing Components

| Missing Component | Why It's Important |
|---|---|
| **Header / document control block** (title, document ID, version number, effective date, approval authority, classification) | Without a version and effective date, no one can tell which copy is authoritative. In an audit or a legal dispute, an undated policy is unenforceable evidence — you cannot prove what rule was in force on the day of an incident. "Updated: Sometime last year" is not a date. |
| **Policy owner / approver** | Every policy needs a named accountable owner (role, not person) and a documented approval by management. Without approval, the document carries no organizational authority; without an owner, no one is responsible for keeping it current or answering interpretation questions. |
| **Purpose statement** | States *why* the policy exists and what risk it mitigates. Employees comply far more readily with rules whose rationale they understand, and auditors use the purpose to judge whether the controls actually address the stated risk. |
| **Scope definition** | Defines *who* and *what* the policy covers: which people (employees, contractors, interns, third parties), which systems (corporate, cloud, BYOD, OT), which locations, and any exclusions. Undefined scope creates gaps — contractors and SaaS accounts routinely fall outside "employees" and become the attack path. |
| **Specific, measurable policy statements** | The operative core of the document. Requirements must be testable (length, complexity, MFA, rotation, storage, lockout) so that compliance can be verified technically and a violation can be demonstrated objectively. "Good passwords" is not a control. |
| **Roles and responsibilities** | Assigns concrete duties to named roles (users, managers, IT/system administrators, CISO, HR, Internal Audit). "IT will handle security stuff" assigns everything to one function and therefore assigns nothing to anyone — accountability that is universal is accountability that is absent. |
| **Compliance / exception process** | Real environments contain legacy systems that cannot meet the standard. Without a formal exception path (request, risk assessment, compensating control, expiry date, approver), staff simply ignore the policy and shadow non-compliance goes unrecorded. |
| **Enforcement section** | States the consequences of violation and who applies them. Without stated consequences the policy is advisory; HR cannot take disciplinary action for breaching a rule that specified no sanction, and the organization loses its defensible position. |
| **Definitions / glossary** | Terms such as "password", "passphrase", "privileged account", "MFA", "credential", and "shared account" must mean one thing across the organization. Ambiguous vocabulary produces inconsistent implementation and disputed violations. |
| **Related documents / references** | Links the policy to its supporting standards, procedures, and external frameworks (NIST SP 800-63B, ISO/IEC 27001 A.5.17, SANS templates, internal Acceptable Use and Access Control policies). This prevents contradiction between documents and shows auditors the control lineage. |
| **Review and revision history** | A table of version, date, author, and change summary, plus a mandated review cycle (e.g. annually). Demonstrates the policy is a living control rather than a shelf document — a standing requirement of ISO 27001 and SOC 2. |
| **Incident reporting procedure and channel** | Specifies exactly where, how, and within what timeframe to report (e.g. Service Desk, security@company.com, ext. 4357, within 1 hour). "Report problems to someone" gives a worried employee no actionable next step, which in practice means the report never happens. |
| **Technical enforcement / control mapping** | Identifies which requirements are enforced by system configuration (password policy objects, MFA enrolment, lockout thresholds) versus by user behaviour. Requirements that are not technically enforced must be explicitly monitored, or they will be silently unmet. |
| **Training and awareness requirement** | Users cannot comply with a policy they have never read. A mandated acknowledgement at onboarding and annually thereafter creates the evidence trail that the requirement was communicated. |
| **Password storage and handling standards for the organization itself** | The sample addresses users only. The organization must also commit to salted hashing, prohibition of plaintext storage/transmission, and breach-corpus screening — otherwise strong user passwords are undermined by weak custodianship. |

---

## Part B — Weaknesses in Existing Language

| Weakness (quote) | Problem | Impact |
|---|---|---|
| "All employees **should** use good passwords." | "Should" is advisory, not mandatory. Policy language must use "must" / "shall" for binding requirements; "should" is reserved for recommendations. | Nothing is actually required. An employee using `password1` has not violated the policy, so no disciplinary or corrective action is defensible. |
| "…use **good** passwords." | Wholly subjective and unmeasurable. No minimum length, character/passphrase guidance, blocklist check, reuse restriction, or account-type differentiation. | Every user applies a personal definition of "good". Credentials become trivially guessable or crackable, and the control cannot be tested by audit or enforced by system configuration. |
| "**All employees**" | Scope is limited to employees, silently excluding contractors, consultants, temporary staff, interns, vendors, service accounts, and automated/system accounts. | Third-party and service accounts are among the most common initial access vectors. The policy leaves the highest-risk identity population entirely ungoverned. |
| "**Don't share them.**" | States a prohibition without boundaries, exceptions, or consequences. It does not address shared/generic accounts, credential storage (sticky notes, spreadsheets, browsers), transmission by email or chat, delegated access, or emergency break-glass procedures. | Users improvise. Passwords are emailed to colleagues "just this once", stored in shared drives, or kept in unmanaged personal password managers — and individual accountability and audit-trail integrity are destroyed. |
| "**IT will handle security stuff.**" | Vague, non-delegable, and factually wrong as a security model. "Stuff" defines no duty; assigning security wholly to IT removes responsibility from users, managers, HR, and executives. | Creates the "security is IT's problem" culture that underpins most successful social-engineering attacks. No role can be held accountable for a specific failure because no specific duty was ever assigned. |
| "**Report problems to someone.**" | No defined recipient, channel, timeframe, or definition of "problem". No non-retaliation assurance and no escalation path. | Incidents go unreported or are reported to a colleague who takes no action. Detection-to-response time — the single largest driver of breach cost — increases dramatically, and regulatory notification deadlines (e.g. GDPR 72 hours) are missed. |
| "**Updated: Sometime last year**" | No version number, no specific date, no author, no approver, no review cycle, no revision history. | The document's currency and authority cannot be established. It fails document-control requirements under ISO/IEC 27001 and SOC 2, and cannot be used as evidence of a control in force at a given time. |
| *(Absent)* No enforcement or consequence clause anywhere in the document. | The policy states expectations but attaches no sanction and names no enforcing authority. | Compliance is effectively voluntary. HR has no documented basis for disciplinary action, and the organization has no defensible position if a breach traces back to a credential violation. |
| *(Absent)* No mention of multi-factor authentication. | MFA is the single highest-impact credential control available and is a baseline expectation in NIST SP 800-63B and virtually every modern framework. | The organization remains fully exposed to credential stuffing, phishing, and password-spraying attacks, which passwords alone cannot mitigate. |

---

## Part C — Rewritten Policy

---

# PASSWORD AND AUTHENTICATION POLICY

| Field | Value |
|---|---|
| **Document ID** | POL-SEC-004 |
| **Version** | 2.0 |
| **Classification** | Internal Use Only |
| **Effective Date** | 01 September 2026 |
| **Last Reviewed** | 01 September 2026 |
| **Next Review Date** | 01 September 2027 |
| **Policy Owner** | Chief Information Security Officer (CISO) |
| **Author** | Information Security Team |
| **Approved By** | Chief Executive Officer / Executive Management Committee |
| **Supersedes** | "Security Policy" (undated) |

---

## 1. Purpose

Passwords are the primary means by which the organization verifies the identity of a user before granting access to its information systems. Weak, reused, shared, or compromised credentials are among the most frequent root causes of unauthorized access and data breach.

The purpose of this policy is to:

1. Establish minimum, measurable standards for the creation, use, storage, protection, and lifecycle management of authentication credentials.
2. Reduce the risk of unauthorized access to organizational systems and data arising from credential compromise.
3. Define clear accountability for credential security across all roles.
4. Support the organization's compliance obligations under ISO/IEC 27001:2022, SOC 2, and applicable data protection law.

## 2. Scope

**2.1 Persons covered.** This policy applies to all individuals who are issued credentials to access organizational information systems, including permanent and temporary employees, contractors, consultants, interns, volunteers, and authorized third-party personnel (collectively, "Users").

**2.2 Systems covered.** This policy applies to all accounts and authentication mechanisms used to access organizational information, regardless of location or ownership, including:

- Corporate workstations, laptops, mobile devices, and servers
- Domain, directory, and single sign-on (SSO) accounts
- Cloud and SaaS applications procured or sanctioned by the organization
- Network infrastructure and security devices
- Databases and application administrative interfaces
- Service, system, and application accounts
- Remote access services (VPN, VDI, bastion hosts)
- Personally owned devices used to access organizational data (BYOD)

**2.3 Exclusions.** Personal accounts used exclusively for personal purposes on personally owned equipment, with no access to organizational data, are outside the scope of this policy.

## 3. Policy Statements

### 3.1 Password Composition

| Account Type | Minimum Length | Additional Requirements |
|---|---|---|
| Standard user account | 12 characters | Passphrase form recommended |
| Privileged / administrative account | 16 characters | Must be unique to that account; must not match any standard account password |
| Service / system / application account | 25 characters | Randomly generated; stored only in the approved secrets manager |
| Account protected by phishing-resistant MFA | 8 characters (minimum permitted) | Only where hardware-token or FIDO2 MFA is enforced |

3.1.1 All printable ASCII characters, Unicode characters, and spaces **must** be accepted by systems in scope. Passwords **must not** be truncated.

3.1.2 Users **are encouraged** to use passphrases of four or more unrelated words (e.g. `correct-battery-lantern-staple`), which achieve high entropy while remaining memorable.

3.1.3 Composition rules mandating a mix of character classes **shall not** be imposed, in line with NIST SP 800-63B, which finds that such rules degrade usability without a corresponding security benefit.

3.1.4 All new and changed passwords **must** be screened in real time against the organization's blocklist, which **shall** include: known-breached credentials, dictionary words, repetitive or sequential strings (`aaaaaa`, `123456`), context-specific terms (organization name, product names, `password`), and previously used credentials for that account.

3.1.5 Users **must not** reuse any of their previous 10 passwords for a given account, and **must not** reuse an organizational password on any external or personal service.

### 3.2 Multi-Factor Authentication (MFA)

3.2.1 MFA **is mandatory** for: all remote access, all cloud and SaaS applications holding organizational data, all administrative and privileged accounts, and all access to systems processing personal, financial, or otherwise restricted data.

3.2.2 Approved second factors, in order of preference: FIDO2/WebAuthn hardware security keys; platform authenticators (Windows Hello, Touch ID); TOTP authenticator applications.

3.2.3 SMS and voice-call delivery of one-time codes **must not** be used for privileged accounts and **shall** be phased out for all other accounts by 31 December 2026.

3.2.4 Users **must** register at least two MFA methods to prevent lockout, and **must** report the loss or compromise of an authentication device to the Service Desk within **1 hour** of discovery.

### 3.3 Password Confidentiality and Handling

3.3.1 Passwords are personal to the User and **must not** be shared with any other person, including managers, IT staff, or the Service Desk. Authorized personnel will never request a User's password.

3.3.2 Passwords **must not** be transmitted in cleartext by email, SMS, instant message, ticket, or voice call.

3.3.3 Passwords **must not** be written on paper, stored in unencrypted files, embedded in scripts or source code, committed to version control, or saved in unapproved browser password stores.

3.3.4 Users **must** store non-memorized credentials only in the organization's approved enterprise password manager. Personal password managers **must not** be used for organizational credentials.

3.3.5 Shared or generic accounts are **prohibited** except where formally approved under the exception process in Section 6; where approved, credentials **must** be held in the enterprise password manager with per-user checkout logging.

3.3.6 Where a User must grant another person access to resources, this **must** be achieved through delegation, group membership, or role assignment — never by disclosing a password.

### 3.4 Password Lifecycle

3.4.1 Scheduled periodic password expiry **shall not** be enforced for user accounts, consistent with NIST SP 800-63B guidance that forced rotation encourages predictable, weakened variants.

3.4.2 Passwords **must** be changed immediately, and in any case within **4 hours** of notification, where: the credential is known or suspected to be compromised; the credential appears in a breach corpus identified by monitoring; or the account was accessed under a temporary or initial password.

3.4.3 Initial and reset passwords **must** be issued as single-use values that expire within **24 hours** and **must** be changed at first logon.

3.4.4 Service account credentials **must** be rotated at least every **365 days**, and immediately upon the departure or role change of any person who had access to them.

3.4.5 Accounts **must** be disabled within **4 hours** of a User's termination of employment or engagement, and within **24 hours** of a role change that removes the access requirement.

3.4.6 Accounts inactive for **90 days** **shall** be automatically disabled; accounts inactive for **180 days** **shall** be deleted or archived in accordance with the Data Retention Policy.

### 3.5 System and Technical Controls

3.5.1 The organization **shall** store all passwords using a salted, computationally expensive one-way hash function (Argon2id, scrypt, or bcrypt with a work factor reviewed annually). Plaintext or reversibly encrypted storage of user passwords is **prohibited**.

3.5.2 All authentication traffic **must** be protected in transit using TLS 1.2 or higher.

3.5.3 Accounts **shall** be locked for **15 minutes** after **10** consecutive failed authentication attempts. Failed attempts **shall** be logged and rate-limited at the source IP to mitigate password spraying.

3.5.4 All authentication events — success, failure, lockout, password change, MFA enrolment and reset — **must** be logged to the central SIEM and retained for a minimum of **12 months**.

3.5.5 Default vendor credentials **must** be changed before any system is connected to a production network.

3.5.6 Password reset procedures **must** verify identity through a method independent of the password being reset; knowledge-based questions using publicly discoverable information **must not** be used.

3.5.7 Systems **must** allow the "paste" function in password fields and **should** offer a "show password" toggle, to support the use of password managers and long passphrases.

### 3.6 Incident Reporting

3.6.1 Users **must** report any suspected credential compromise, phishing attempt, unauthorized access, or MFA prompt they did not initiate, **within 1 hour of discovery**, via any of:

- **Service Desk portal:** `https://servicedesk.[organization].com`
- **Email:** `security@[organization].com`
- **Telephone (24/7):** ext. **4357** / +XXX XXX XXXX

3.6.2 Users **must not** delay reporting in order to investigate or remediate independently.

3.6.3 Reports made in good faith **shall not** result in disciplinary action against the reporting User, even where the User's own error contributed to the incident. Retaliation against a good-faith reporter is itself a violation of this policy.

## 4. Roles and Responsibilities

| Role | Responsibilities |
|---|---|
| **All Users** | Comply with all requirements of this policy; create and protect credentials as specified; use the approved password manager; complete annual security awareness training; report suspected compromise within 1 hour; acknowledge this policy at onboarding and annually. |
| **Line Managers** | Ensure direct reports acknowledge and complete training; notify IT and HR of departures and role changes in advance; approve access requests for their teams; escalate observed non-compliance. |
| **IT Operations / System Administrators** | Implement and maintain the technical controls in Section 3.5; provision and de-provision accounts within stated timeframes; operate the enterprise password manager and secrets vault; execute identity verification on reset requests; never request or accept a User's password. |
| **Information Security Team** | Maintain the credential blocklist and breach-corpus monitoring; monitor authentication logs and investigate anomalies; conduct quarterly password-strength audits and annual credential-control testing; lead incident response for credential compromise; deliver awareness training. |
| **CISO (Policy Owner)** | Own, maintain, and annually review this policy; approve or deny exception requests; report compliance metrics to executive management quarterly; sponsor remediation of identified gaps. |
| **Human Resources** | Notify IT of all joiners, movers, and leavers within agreed SLAs; incorporate policy acknowledgement into onboarding; administer disciplinary action arising from confirmed violations. |
| **Internal Audit** | Independently test compliance with this policy at least annually and report findings to the Audit Committee. |
| **Executive Management** | Approve this policy, allocate resources for its implementation, and visibly model compliance. |

## 5. Compliance Measurement

5.1 The Information Security Team **shall** measure compliance through automated configuration monitoring, quarterly credential audits (including offline strength testing of a sampled password hash set under CISO authorization), MFA enrolment reporting, and review of exception records.

5.2 Compliance metrics **shall** be reported to the CISO monthly and to executive management quarterly. Target: **100%** MFA enrolment for in-scope accounts and **zero** unremediated critical findings older than 30 days.

## 6. Exceptions

6.1 Any deviation from this policy requires a documented exception submitted to the Information Security Team, containing: the specific requirement to be excepted, the business justification, the systems and accounts affected, an assessment of residual risk, the compensating controls to be applied, and a proposed expiry date.

6.2 Exceptions **must** be approved by the CISO (and by the CEO where the residual risk is assessed as High), **must not** exceed **12 months**, and **must** be re-justified to be renewed.

6.3 The Information Security Team **shall** maintain a central exception register, reviewed quarterly.

## 7. Enforcement

7.1 Compliance with this policy is a condition of continued access to organizational information systems and, for employees, a term of employment.

7.2 Violations **shall** be handled proportionately to their severity and intent:

| Severity | Examples | Consequence |
|---|---|---|
| **Minor / first occurrence** | Password below required length; failure to complete MFA enrolment within the grace period | Documented coaching by line manager; mandatory remedial training; correction required within 5 business days |
| **Moderate / repeated** | Repeated non-compliance after coaching; storing credentials outside the approved manager; use of an unapproved shared account | Formal written warning; access restriction pending remediation; notation in the employee record |
| **Serious** | Sharing credentials; deliberate circumvention of MFA or lockout controls; failure to report a known compromise | Suspension of access; formal disciplinary process up to and including termination of employment or contract |
| **Severe / malicious** | Unauthorized use of another User's credentials; theft or sale of credentials; intentional facilitation of unauthorized access | Immediate revocation of access; termination of employment or contract; referral to law enforcement; civil recovery where losses are incurred |

7.3 For contractors and third parties, violations **shall** be escalated to the vendor management function and may constitute a breach of contract.

7.4 Disciplinary action **shall** be administered by Human Resources in accordance with the organization's disciplinary procedure and applicable employment law. Section 3.6.3 (protection for good-faith reporters) takes precedence over this section.

## 8. Definitions

| Term | Definition |
|---|---|
| **Authentication** | The process of verifying the claimed identity of a user, process, or device. |
| **Credential** | Any secret or token used to authenticate, including passwords, passphrases, API keys, certificates, and MFA seeds. |
| **Passphrase** | A password composed of multiple words, generally longer and more memorable than a conventional password. |
| **Privileged account** | Any account with elevated rights beyond those of a standard user — including domain admin, local admin, root, database administrator, and cloud tenant administrator accounts. |
| **Service account** | A non-human account used by an application, script, or system to authenticate to another system. |
| **Shared account** | An account whose credentials are known to more than one individual. |
| **MFA (Multi-Factor Authentication)** | Authentication requiring two or more independent factors from different categories: something you know, something you have, something you are. |
| **Phishing-resistant MFA** | An MFA method cryptographically bound to the legitimate site or service, such that credentials cannot be relayed to an attacker — principally FIDO2/WebAuthn and PIV/smart cards. |
| **Blocklist** | A maintained set of prohibited password values screened at the point of password creation or change. |
| **Compromise** | Any known or suspected disclosure of a credential to an unauthorized party. |
| **User** | Any individual issued credentials under the scope of this policy (see Section 2.1). |
| **Must / Shall** | Denotes a mandatory requirement. |
| **Should** | Denotes a recommendation; deviation does not constitute a violation but should be justifiable. |

## 9. Related Documents

**Internal**

- POL-SEC-001 Information Security Policy
- POL-SEC-002 Acceptable Use Policy
- POL-SEC-003 Access Control Policy
- POL-SEC-007 Incident Response Policy
- POL-SEC-011 Remote Access Policy
- POL-HR-002 Disciplinary Procedure
- STD-SEC-004a Password Manager Standard Operating Procedure
- STD-SEC-004b Account Provisioning and De-provisioning Procedure

**External**

- NIST SP 800-63B — *Digital Identity Guidelines: Authentication and Authenticator Management*
- NIST SP 800-12 Rev. 1 — *An Introduction to Information Security*
- ISO/IEC 27001:2022 — Annex A control A.5.17 (Authentication information)
- CIS Controls v8 — Control 5 (Account Management), Control 6 (Access Control Management)
- SANS Institute — Password Protection Policy Template

## 10. Revision History

| Version | Date | Author | Approved By | Summary of Changes |
|---|---|---|---|---|
| 1.0 | 14 March 2024 | IT Department | — | Original informal "Security Policy" — undated, unapproved, no measurable requirements. |
| 2.0 | 01 September 2026 | Information Security Team | CEO / Executive Management Committee | Complete rewrite as a formal Password and Authentication Policy. Added document control, purpose, scope, measurable composition and lifecycle requirements, mandatory MFA, technical controls, defined reporting channels and timeframes, roles and responsibilities, compliance measurement, exception process, tiered enforcement, definitions, and references. Aligned with NIST SP 800-63B (removed forced periodic expiry and composition-complexity rules; added blocklist screening). |

## 11. Policy Acknowledgement

> I confirm that I have read, understood, and agree to comply with the Password and Authentication Policy (POL-SEC-004 v2.0). I understand that violation may result in disciplinary action up to and including termination of employment or contract.
>
> Name: ______________________  Role: ______________________
>
> Signature: __________________  Date: ______________________

---

*End of document.*
