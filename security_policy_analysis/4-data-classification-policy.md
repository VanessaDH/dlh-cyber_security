# DATA CLASSIFICATION POLICY
**HealthPlus Medical Group**

| | |
|---|---|
| **Document ID** | POL-SEC-009 |
| **Version** | 3.0 |
| **Classification** | INTERNAL |
| **Effective Date** | 01 October 2026 |
| **Next Review** | 01 October 2027 (annual, and on material regulatory change) |
| **Policy Owner** | Chief Information Security Officer |
| **Co-Owners** | HIPAA Privacy Officer; Data Protection Officer (GDPR) |
| **Approved By** | Executive Committee / Board Compliance Committee |
| **Regulatory Basis** | HIPAA Privacy, Security & Breach Notification Rules (45 CFR 164); HITECH; GDPR Art. 4, 5, 9, 32; 42 CFR Part 2; applicable state privacy and medical-records laws; NIST SP 800-60, SP 800-88, SP 800-111 |
| **Applies To** | All workforce members, contractors, vendors, business associates, students, and volunteers; all HealthPlus data in any form or location |
| **Supersedes** | POL-SEC-009 v2.1 |

---

## 1. Purpose and Scope

**1.1 Purpose.** HealthPlus holds information whose exposure ranges from harmless to devastating — a press release and a psychiatric record cannot be protected by the same controls. This policy establishes four classification levels, assigns every category of HealthPlus data to one, and defines the mandatory handling requirements for each, so that protection is proportionate, consistent, and demonstrable to regulators.

**1.2 Scope.** All data created, received, maintained, or transmitted by HealthPlus, in any form — electronic, paper, imaging, verbal, or physical specimen labelling — in any location, including cloud services, mobile devices, home offices, removable media, and business associate systems. It applies for the full data lifecycle: creation, classification, storage, use, transmission, sharing, retention, and disposal.

**1.3 Governing principles.**

- **Classify at creation.** Every item of data is classified by the person who creates or receives it, at that moment. Unclassified data defaults to **CONFIDENTIAL** until classified.
- **Highest level governs.** A file, database, email, or backup containing data of mixed levels is handled at the **highest** level present. One line of PHI in a spreadsheet makes the whole spreadsheet RESTRICTED.
- **Minimum necessary.** Access to PHI is limited to the minimum necessary for the role and task (45 CFR 164.502(b)) — having access is not authorization to use it.
- **Classification follows the data.** It survives copying, export, transformation, transmission, and sharing with a third party.
- **Aggregation escalates.** Individually innocuous data may become CONFIDENTIAL or RESTRICTED in volume or combination; the data owner reassesses on any material aggregation.
- **Doubt resolves upward.** Where the level is unclear, apply the higher one and ask the data owner.

---

## 2. Classification Levels

| Level | Definition — impact if disclosed | Regulatory driver | Default |
|---|---|---|---|
| **PUBLIC** | No harm. Explicitly approved for release outside HealthPlus by an authorized approver. | None | Requires positive approval to be PUBLIC |
| **INTERNAL** | Minor harm — embarrassment, operational friction, minor competitive loss. Not for release, but no legal duty attaches. | Contractual | — |
| **CONFIDENTIAL** | Significant harm — financial loss, regulatory penalty, competitive damage, harm to an individual's privacy or finances. | GDPR (general personal data); state privacy law; PCI-DSS | **Default for unclassified data** |
| **RESTRICTED** | Severe or catastrophic harm — patient safety risk, serious harm to an individual, major regulatory enforcement, loss of licence or accreditation, existential reputational damage. | HIPAA (PHI/ePHI); GDPR Art. 9 special category; 42 CFR Part 2; state genetic and reproductive privacy law | All PHI is RESTRICTED |

### 2.1 Data type mapping

| Data Type | Level | Notes |
|---|---|---|
| Marketing materials, website content, published research, press releases, public job postings, directions and opening hours | **PUBLIC** | Only after approval by Marketing (and, for research, the Research Office) |
| Internal memos, org charts, staff directories, meeting minutes, non-sensitive policies, training material, general project plans | **INTERNAL** | |
| Employee PII — home address, personal contact details, national ID, date of birth, emergency contacts, employment records, performance reviews | **CONFIDENTIAL** | GDPR personal data; state PII laws |
| Payroll, compensation, benefits enrolment | **CONFIDENTIAL** | Employee *health* benefit and occupational health records are **RESTRICTED** |
| Financial data — budgets, forecasts, accounts, contracts, vendor pricing, billing and claims (non-patient-identifiable) | **CONFIDENTIAL** | |
| Business operations — supplier contracts, strategic plans, M&A, internal audit findings, litigation files | **CONFIDENTIAL** | Litigation and M&A material may be designated RESTRICTED by Legal |
| Security data — vulnerability reports, network diagrams, incident records, audit logs | **CONFIDENTIAL** | Credentials, keys, and certificates are **RESTRICTED** |
| De-identified data (HIPAA Safe Harbor or Expert Determination), aggregate statistics | **INTERNAL** | Re-identification attempts are prohibited; re-identifiable data reverts to RESTRICTED |
| Limited Data Set (research, under a Data Use Agreement) | **CONFIDENTIAL** | DUA required before release; still PHI under HIPAA |
| **Patient medical records / PHI** — diagnoses, treatment notes, medications, imaging, lab results, appointment and admission data, patient demographics linked to care, insurance and claims data, patient billing | **RESTRICTED** | 45 CFR 164; GDPR Art. 9 |
| **Especially sensitive PHI** — mental and behavioural health, substance use disorder records (42 CFR Part 2), HIV/STI status, genetic and genomic data, reproductive and sexual health, minors' records, employee-patient records, VIP/employee-of-HealthPlus records | **RESTRICTED — Elevated** | Additional access break-glass logging and separate consent rules apply |
| Identifiable research data, clinical trial data with subject identifiers, biospecimen linkage keys, IRB submissions containing identifiers | **RESTRICTED** | Common Rule and IRB protocol also apply |
| Credentials, encryption keys, API tokens, certificates, MFA seeds | **RESTRICTED** | Never appear in documents, tickets, or code |
| Payment card data | **RESTRICTED** | PCI-DSS; never stored outside the approved payment environment |

### 2.2 Reclassification and declassification

Classification is reviewed by the data owner at least annually and on any material change of use. **Downgrading requires the data owner's written approval and, for anything derived from PHI, the Privacy Officer's approval** — recorded with the date, approver, and rationale. PHI may be downgraded only through validated de-identification (Safe Harbor removal of the 18 identifiers, or Expert Determination under 45 CFR 164.514(b)), documented and retained. Upgrading requires no approval and may be done by anyone who identifies the need.

---

## 3. Handling Requirements Matrix

| Requirement | PUBLIC | INTERNAL | CONFIDENTIAL | RESTRICTED |
|---|---|---|---|---|
| **Labeling required** | Optional | **Yes** | **Yes** | **Yes** — level + handling caveat |
| **Encryption at rest** | No | Recommended | **Yes** — AES-256 | **Yes** — AES-256, FIPS 140-3 validated module |
| **Encryption in transit** | No (TLS by default) | **Yes** — TLS 1.2+ | **Yes** — TLS 1.2+ | **Yes** — TLS 1.3 preferred, TLS 1.2 minimum; end-to-end where available |
| **Access control model** | Open | Authenticated (all workforce) | **RBAC**, least privilege, documented approval | **RBAC + minimum necessary**, named authorization by data owner, purpose-limited |
| **MFA required** | No | Yes | **Yes** | **Yes — phishing-resistant** |
| **External sharing** | Unrestricted | Manager approval | Data owner approval + NDA | **Privacy Officer approval + BAA/DUA + patient authorization where required** |
| **Email transmission** | Permitted | Permitted internally | Encrypted; external requires approval | **Only via secure messaging portal or forced-TLS gateway with encryption**; never in the body or as an unprotected attachment |
| **Removable media** | Permitted | Discouraged | Encrypted, approved media only | **Prohibited** without written Privacy Officer and CISO approval |
| **Personal / BYOD devices** | Permitted | Managed container only | Managed container only | **Prohibited** outside the managed container; no local storage |
| **Cloud storage** | Any approved | Approved corporate tenant | Approved tenant, encrypted | **Approved tenant under a BAA only**, encrypted, geo-restricted |
| **Printing** | Permitted | Permitted | Secure-release printing, collect immediately | **Secure-release only**, collect immediately, logged, minimum necessary |
| **Audit logging of access** | No | System-level | **Yes** | **Yes — every access logged, retained 6 years, reviewed** |
| **Retention** | Business need | 3 years default | Per retention schedule | **Per state medical-records law; HIPAA documentation 6 years minimum** |
| **Disposal method** | Standard | Standard delete / recycling | **Cryptographic erase / cross-cut shred** | **Purge or Destroy (NIST SP 800-88) + certificate of destruction** |
| **Backup encryption** | No | Yes | Yes | **Yes**, with separate key management |
| **DLP enforcement** | Monitor | Monitor | **Block on external egress** | **Block, alert, and quarantine** |
| **Incident reporting on exposure** | Not required | 1 business day | **Within 1 hour** | **Immediately — within 1 hour; triggers HIPAA breach risk assessment** |
| **Workforce training** | General | General | Annual role-based | **Annual role-based + HIPAA-specific** |

---

## 4. Labeling

**4.1 Requirement.** All INTERNAL, CONFIDENTIAL, and RESTRICTED data must carry a visible classification label. Where a system cannot display a label, the classification is recorded in the system's data inventory entry.

**4.2 Electronic documents.** Label in the **header or footer of every page**, in the document properties/metadata, and — for RESTRICTED — as a first-page cover marking:

```
CONFIDENTIAL — HealthPlus Medical Group
```
```
RESTRICTED — PROTECTED HEALTH INFORMATION
Unauthorized access, use, or disclosure is prohibited by federal law.
Handle per POL-SEC-009. Report exposure immediately: ext. 4357
```

**4.3 File naming.** Prefix the classification tag; never place patient identifiers in a filename, path, or folder name (filenames appear in backups, logs, indexes, and email subject lines):

| Level | Prefix | Example |
|---|---|---|
| PUBLIC | `PUB_` | `PUB_2026_Community_Health_Report.pdf` |
| INTERNAL | `INT_` | `INT_Nursing_Org_Chart_Q3.pptx` |
| CONFIDENTIAL | `CONF_` | `CONF_Payroll_Reconciliation_2026Q2.xlsx` |
| RESTRICTED | `RESTR_` | `RESTR_Cardiology_Outcomes_Extract_MRN-suppressed.csv` |

**4.4 Email.** Apply the sensitivity label in the mail client (which drives encryption and DLP automatically). Prefix the subject line: `[CONFIDENTIAL]` or `[RESTRICTED]`. **Never place PHI, patient names, or MRNs in a subject line** — subject lines are logged, indexed, and displayed on lock screens.

**4.5 Physical materials.** Stamp or print the classification on the cover and every page of printed CONFIDENTIAL and RESTRICTED material. Label removable media and specimen containers with the classification and a contact number, never with patient identifiers on the exterior.

**4.6 Systems, databases and dashboards.** Display the classification banner in the interface; record the classification in the data inventory and in the Art. 30 record of processing; label database schemas and reporting datasets at their highest contained level.

**4.7 Verbal information.** State the classification before discussing RESTRICTED information in a meeting, and confirm the audience is authorized. Do not discuss PHI in corridors, elevators, waiting areas, cafeterias, or on public transport.

---

## 5. Storage

**5.1 Approved locations by level.**

| Level | Approved | Prohibited |
|---|---|---|
| **PUBLIC** | Any approved system; public website; CDN | — |
| **INTERNAL** | Corporate SharePoint/OneDrive tenant; approved collaboration platforms; managed file shares; corporate devices | Personal cloud accounts; personal email; unmanaged devices |
| **CONFIDENTIAL** | Access-controlled corporate SharePoint sites and file shares; approved encrypted cloud tenant; approved business applications; encrypted corporate devices | Personal cloud or email; unencrypted removable media; unmanaged devices; consumer file-transfer or note-taking apps; public code repositories; unapproved AI or LLM services |
| **RESTRICTED** | The EHR and clinical systems of record; the designated secure enclave; approved cloud services **under an executed BAA**, encrypted and geo-restricted; encrypted corporate devices with no local persistence where avoidable | **Everything not expressly approved**, including: personal devices outside the managed container, personal cloud, personal email, removable media, home printers, unapproved SaaS, unapproved AI services, local desktop folders, shared drives without access control, physical filing outside a locked clinical area |

**5.2 Universal rules.** Store data in the system of record — copies proliferate risk. Minimize local copies; where one is unavoidable, full-disk encryption is mandatory and the copy is deleted when the task ends. Never store PHI in ticketing systems, chat messages, screenshots, email folders, test or training environments, or personal notes.

**5.3 Non-production environments.** Production PHI, PII, and payment data **must never** be copied to development, test, training, or demonstration environments. Test data must be synthetic or de-identified to Safe Harbor standard. Screenshots for documentation or training must use synthetic data.

**5.4 Physical storage.** CONFIDENTIAL and RESTRICTED paper is stored in locked cabinets in access-controlled areas, signed out when removed, never left unattended, and never taken home without written approval. Clear desk and clear screen apply at all times: screens lock after 10 minutes and on leaving the workstation; workstations in patient-facing areas use privacy filters and are positioned away from public view; charts and printouts are face-down or filed when not in active use.

**5.5 Cloud and third parties.** No cloud service may hold CONFIDENTIAL or RESTRICTED data without security review, an executed contract (and a **BAA** for any PHI, and an Art. 28 processor agreement for GDPR-scope data), documented data residency, and confirmation of the provider's deletion and sanitization commitments. Business associates must be inventoried, risk-assessed, and reviewed annually.

---

## 6. Transmission

**6.1 Email.**

| Level | Internal | External |
|---|---|---|
| PUBLIC | Permitted | Permitted |
| INTERNAL | Permitted | Manager approval |
| CONFIDENTIAL | Permitted with sensitivity label | **Encryption required** (label-driven); data owner approval; verify the recipient address |
| RESTRICTED | Permitted with label; minimum necessary only | **Secure patient/provider portal or forced-TLS encrypted gateway only.** Requires Privacy Officer approval, a BAA or patient authorization as applicable, and confirmation of the recipient's identity out of band |

Auto-forwarding of HealthPlus mail to any external or personal address is **blocked and prohibited**. Distribution lists must be checked before sending anything above INTERNAL. Misdirected email containing CONFIDENTIAL or RESTRICTED data must be reported within 1 hour — recall is not remediation.

**6.2 File transfer.** Use the approved secure file transfer service for anything above INTERNAL: recipient-specific access, link expiry (maximum 30 days; 7 days for RESTRICTED), download limits, and access logging. "Anyone with the link" sharing is prohibited for INTERNAL and above. Bulk PHI extracts require Privacy Officer approval, a documented purpose, and minimum-necessary field selection.

**6.3 Other channels.**

- **Messaging/chat:** approved enterprise platform only; PHI permitted only in clinical-approved secure messaging with retention controls. Consumer messaging apps are prohibited for any HealthPlus data.
- **Fax:** only to a pre-verified number, with a cover sheet carrying a confidentiality notice; confirm receipt for RESTRICTED; misdials reported within 1 hour.
- **Telephone/voicemail:** verify identity before disclosing PHI; leave only minimum-necessary callback messages, never diagnoses or results.
- **Post/courier:** tracked, sealed, opaque envelopes for CONFIDENTIAL and above; RESTRICTED by tracked courier with signature, double-enveloped, contents encrypted if electronic.
- **In person / hand-carry:** RESTRICTED material carried outside a facility must be encrypted (electronic) or in a locked container (paper), never left in a vehicle.
- **APIs and interfaces:** authenticated, TLS 1.2+, mutual TLS for RESTRICTED, least-privilege scopes, logged, with a documented interface agreement.
- **Remote access:** VPN or approved Zero Trust access, MFA, managed device; no PHI over public Wi-Fi without VPN; no screen-sharing of PHI in a public location.

**6.4 Prohibited transmission.** Personal email; unapproved AI, LLM, translation, transcription, formatting, or conversion services; consumer file-sharing; unencrypted removable media through the post; social media; and any channel not listed above without CISO approval.

---

## 7. Access Control

**7.1 Who may access.** Access is granted on **role plus purpose**: the person's job requires it, and the specific access is for treatment, payment, healthcare operations, an authorized research protocol, or another permitted purpose. A workforce member may access a patient record only when they have a treatment or business relationship with that patient. **Accessing one's own record, a family member's, a colleague's, or a public figure's record outside a care relationship is prohibited and is grounds for dismissal**, even where the system technically permits it.

**7.2 How access is granted.**

| Level | Model | Approval | Provisioning |
|---|---|---|---|
| PUBLIC | Open | None | — |
| INTERNAL | Authenticated workforce | Automatic on hire | Standard role bundle |
| CONFIDENTIAL | RBAC, least privilege | Manager + data owner | Documented request, ticketed |
| RESTRICTED | RBAC + minimum necessary, purpose-limited | Manager + **data owner** + **Privacy Officer** for bulk or non-clinical access | Documented request stating purpose and scope; time-bound where appropriate |

**7.3 Break-glass access.** Emergency access to a record outside normal authorization is available for genuine clinical need. Every use generates an immediate alert, requires a recorded reason at the time, and is reviewed by the Privacy Officer within 24 hours. Unjustified break-glass use is treated as unauthorized access.

**7.4 Monitoring.** All access to RESTRICTED data is logged with user, patient/record, timestamp, and action, retained **6 years** (45 CFR 164.312(b) and 164.316(b)(2)), and monitored by automated proactive auditing for: same-surname access, employee-record access, VIP-record access, high-volume access, off-hours access, access without an appointment or encounter, and post-termination access attempts.

**7.5 Reviews.**

| Review | Frequency | Owner |
|---|---|---|
| Access certification — all systems holding CONFIDENTIAL or RESTRICTED data | Quarterly | Data owners and managers |
| Privileged and administrative access certification | Monthly | Information Security |
| Break-glass use review | Within 24 hours of each use | Privacy Officer |
| Proactive PHI access audit (sampled and rule-driven) | Continuous, reported monthly | Privacy Officer |
| Business associate and vendor access review | Annually, and on contract change | Vendor Management |
| Role definition and minimum-necessary review | Annually | Privacy Officer + data owners |

**7.6 Joiners, movers, leavers.** Access granted only after training completion and confidentiality agreement. On role change, old access is removed within 24 hours — not merely supplemented. On termination, all access is revoked **immediately**, within 1 hour for involuntary departures, including physical access, remote access, and business associate portals.

---

## 8. Disposal and Sanitization

**8.1 Principle.** Data is disposed of when its retention period expires or it is no longer needed, using a method matched to its classification and media type, per **NIST SP 800-88 Rev. 1** (*Clear* → *Purge* → *Destroy*). Deletion must be irreversible and, above INTERNAL, evidenced.

**8.2 Required methods.**

| Media | INTERNAL | CONFIDENTIAL | RESTRICTED |
|---|---|---|---|
| **Paper** | Recycling | **Cross-cut shred** (≤ 4×40 mm) via secure bins | **Cross-cut shred or incineration**, witnessed or by certified vendor with **certificate of destruction** |
| **Hard disk (magnetic)** | Clear (overwrite) | **Purge** — cryptographic erase or degauss | **Purge**, then **Destroy** (shred/disintegrate) at end of life; certificate required |
| **SSD / flash / mobile** | Clear | **Purge** — cryptographic erase or vendor sanitize command | **Cryptographic erase + physical destruction**; overwriting alone is not sufficient on flash media |
| **Optical media** | — | Shred or incinerate | Shred or incinerate; certificate |
| **Cloud storage** | Platform delete | Platform delete + confirm backup/snapshot purge on cycle | Cryptographic erase (key destruction) + written confirmation from the provider under the BAA |
| **Backups / archives** | Expire per schedule | Expire per schedule; key destruction | Key destruction; documented |
| **Imaging / film** | — | Secure destruction | Certified destruction; certificate |
| **Devices returned, leased, or repaired** | Sanitize before release | Sanitize to Purge before release | **Sanitize to Purge, or retain the drive** — no RESTRICTED media leaves HealthPlus control un-sanitized, including under warranty |

**8.3 Records.** A destruction record is kept for all CONFIDENTIAL and RESTRICTED disposal: date, description, volume, method, operator, witness or vendor, and certificate reference. Records are retained **6 years**. Vendors performing destruction must hold a **BAA** and provide certificates.

**8.4 Legal Hold overrides everything.** No data subject to a Legal Hold, active investigation, audit, or regulatory proceeding may be destroyed, regardless of its retention schedule, until Legal releases the hold in writing. Destruction of data under hold may constitute spoliation.

**8.5 Prohibited.** Placing CONFIDENTIAL or RESTRICTED paper in general waste or open recycling; leaving material in unsecured bins; reformatting or "quick erase" as a sanitization method; selling, donating, or disposing of devices without documented sanitization; taking material home for disposal.

---

## 9. Roles and Responsibilities

| Role | Responsibilities |
|---|---|
| **All Workforce Members** | Classify data at creation; apply labels; handle data per the matrix in §3; access only the minimum necessary; report suspected exposure within 1 hour; complete annual training; sign the confidentiality agreement. |
| **Data Owners** *(department heads and clinical leaders)* | Own classification for their data domains; approve access and downgrades; complete quarterly access certification; maintain their data inventory entries; approve external sharing at CONFIDENTIAL. |
| **Data Custodians** *(IT, application and database administrators)* | Implement the technical controls the classification requires; enforce encryption, logging, and retention; execute sanitization; maintain the data inventory. |
| **HIPAA Privacy Officer** | Owns PHI classification decisions and de-identification approvals; approves external PHI disclosures; conducts proactive access auditing and break-glass review; runs breach risk assessments and Breach Notification Rule determinations; maintains the accounting of disclosures. |
| **Data Protection Officer (GDPR)** | Assesses GDPR obligations; maintains Art. 30 records of processing; runs DPIAs; handles data subject rights requests; owns Art. 33/34 breach notification. |
| **CISO** | Owns this policy and the technical control standards; operates DLP, encryption, and monitoring; leads incident response; reports compliance metrics quarterly. |
| **Compliance / Legal** | Interpret HIPAA, GDPR, and state law; issue Legal Holds; execute BAAs and DUAs; manage regulatory reporting and investigations. |
| **Human Resources** | Confidentiality agreements at onboarding; training administration; disciplinary action for violations; immediate leaver notification. |
| **Research Office / IRB** | Approve research data use; ensure protocol, consent, and DUA requirements are met before any identifiable data is released. |
| **Vendor Management** | Ensure a BAA or processor agreement exists before any third party receives data above INTERNAL; annual vendor review. |
| **Internal Audit** | Independently test compliance annually; report to the Board Compliance Committee. |

---

## 10. Training, Compliance and Enforcement

**10.1 Training.** Classification and HIPAA training at onboarding before access is granted, annually thereafter, and on any material policy change. Role-based training for those handling RESTRICTED data. Completion is tracked; access is suspended for non-completion beyond 30 days.

**10.2 Compliance measurement.**

| Metric | Target |
|---|---|
| Workforce training completion | 100% annually |
| Data inventory coverage of systems holding CONFIDENTIAL/RESTRICTED data | 100% |
| Encryption at rest on RESTRICTED data stores | 100% |
| Quarterly access certification completed on time | 100% |
| Break-glass uses reviewed within 24 hours | 100% |
| Unauthorized access events identified by proactive audit | Trend to zero |
| DLP blocks on outbound PHI | Monitored monthly |
| Vendors holding PHI with an executed BAA | 100% |
| Destruction certificates on file for RESTRICTED disposal | 100% |

Verified through automated DLP and configuration scanning, quarterly access reviews, proactive PHI access auditing, annual Internal Audit testing, annual HIPAA Security Risk Analysis (45 CFR 164.308(a)(1)(ii)(A)), and vendor assessments.

**10.3 Enforcement.**

| Tier | Conduct | Consequence |
|---|---|---|
| **1 — Minor** | Missing label; unattended INTERNAL document; failure to lock a screen | Coaching; remedial training; correction within 5 business days |
| **2 — Moderate** | Storing CONFIDENTIAL data in an unapproved location; unencrypted external email of CONFIDENTIAL data; improper paper disposal; repeated Tier 1 | Written warning; access restriction; mandatory retraining |
| **3 — Serious** | Unauthorized access to a patient record; transmitting PHI through a prohibited channel; sharing credentials; failing to report a known exposure; copying PHI to personal storage | Final warning or suspension; access revocation; process up to dismissal; reported to the Privacy Officer for breach assessment and potential regulatory notification |
| **4 — Severe** | Accessing records of a family member, colleague, or public figure out of curiosity; deliberate exfiltration or sale of PHI; disclosure to media; falsifying access justification or destroying records under Legal Hold | Immediate revocation and dismissal; referral to law enforcement; reporting to licensing boards; individual criminal liability under HITECH (up to 10 years' imprisonment for disclosure for personal gain); civil action |

Good-faith self-reporting is a significant mitigating factor; concealment is an aggravating one. Retaliation against a good-faith reporter is itself a serious violation.

**10.4 Exceptions.** Requests to the CISO stating the requirement, justification, residual risk, compensating controls, and expiry. Approved by the CISO; RESTRICTED-data exceptions additionally require the Privacy Officer, and High-risk exceptions the Executive Committee. Maximum 6 months. **No exception is available** for: encryption of RESTRICTED data at rest or in transit; BAA requirements before disclosure to a third party; audit logging of PHI access; or the prohibition on production PHI in non-production environments.

---

## 11. Definitions

| Term | Definition |
|---|---|
| **PHI / ePHI** | Protected Health Information — individually identifiable health information created, received, maintained, or transmitted by a covered entity; ePHI is its electronic form (45 CFR 160.103). |
| **PII** | Personally Identifiable Information — data that identifies or can be linked to an individual. |
| **Personal data (GDPR)** | Any information relating to an identified or identifiable natural person (Art. 4(1)); health data is special-category data under Art. 9. |
| **De-identification** | Removal of the 18 HIPAA identifiers (Safe Harbor, 164.514(b)(2)) or a qualified Expert Determination that re-identification risk is very small. |
| **Limited Data Set** | PHI with direct identifiers removed but retaining dates and geography, disclosable for research, public health, or operations under a Data Use Agreement (164.514(e)). |
| **Minimum necessary** | The standard requiring PHI use and disclosure to be limited to what is needed for the purpose (164.502(b)). |
| **BAA** | Business Associate Agreement — the contract required before a third party may handle PHI on HealthPlus's behalf (164.308(b), 164.502(e)). |
| **Break-glass** | Emergency override access to a record outside normal authorization, logged and reviewed. |
| **Data Owner** | The accountable business or clinical leader for a data domain — classification, access, and retention decisions. |
| **Data Custodian** | The technical role operating the systems holding the data. |
| **Clear / Purge / Destroy** | NIST SP 800-88 sanitization categories of increasing assurance. |
| **Legal Hold** | A directive suspending all deletion for specified records. |
| **Must / Shall** | Mandatory. **Should**: recommended. **May**: permitted. |

## 12. Related Documents

**Internal:** POL-SEC-001 Information Security · POL-SEC-002 Acceptable Use · POL-SEC-003 Access Control · POL-SEC-004 Password and Authentication · POL-SEC-007 Incident Response · POL-PRIV-001 HIPAA Privacy Policy · POL-PRIV-002 Breach Notification Procedure · POL-PRIV-003 GDPR Data Protection Policy and Art. 30 records · STD-SEC-009a Data Inventory · STD-SEC-009b Media Sanitization Procedure · Records Retention Schedule · Business Associate Agreement template · Data Use Agreement template.

**External:** HIPAA Privacy, Security and Breach Notification Rules (45 CFR Parts 160, 164) · HITECH Act · 42 CFR Part 2 (substance use disorder records) · GDPR Art. 4, 5, 9, 28, 30, 32, 33, 34 · applicable state privacy, genetic-privacy and medical-records laws · NIST SP 800-60 Rev. 1 *Guide for Mapping Types of Information and Systems to Security Categories* · NIST SP 800-88 Rev. 1 *Guidelines for Media Sanitization* · NIST SP 800-111 *Storage Encryption* · NIST SP 800-66 Rev. 2 *Implementing the HIPAA Security Rule* · ISO/IEC 27001:2022 A.5.12, A.5.13, A.5.33, A.8.10, A.8.12.

## 13. Revision History

| Version | Date | Approved By | Changes |
|---|---|---|---|
| 1.0 | 09 Apr 2019 | CISO | Initial issue; three levels; HIPAA only. |
| 2.0 | 14 Jun 2022 | Executive Committee | GDPR added; four-level model adopted; BAA requirements formalized. |
| 2.1 | 03 Mar 2024 | Executive Committee | State privacy law updates; cloud storage rules tightened. |
| **3.0** | **15 Sep 2026** | **Executive Committee / Board Compliance Committee** | Full rewrite. Complete handling matrix across all four levels (§3). RESTRICTED–Elevated category added for behavioural health, 42 CFR Part 2, genetic and reproductive data. Labeling and file-naming conventions specified (§4). Storage, transmission, and disposal requirements defined per level (§5–§8). NIST SP 800-88 sanitization methods mandated with certificates of destruction. Break-glass review, proactive PHI access auditing, and prohibition on production PHI in non-production environments added. Quick Reference Guide added (Annex A). |

---
---

# ANNEX A — QUICK REFERENCE GUIDE
*(Deliverable 2 — one page. Print, laminate, post at every workstation.)*

## HealthPlus Data Classification — Know Your Level

| | 🟢 **PUBLIC** | 🔵 **INTERNAL** | 🟡 **CONFIDENTIAL** | 🔴 **RESTRICTED** |
|---|---|---|---|---|
| **What it is** | Approved for release | Staff only | Would cause real harm | Would cause severe harm |
| **Examples** | Website, brochures, press releases | Memos, org charts, minutes, training decks | Employee PII, payroll, budgets, contracts, vendor pricing | **All PHI**, medical records, credentials, research with identifiers, card data |
| **Label it?** | Optional | **Yes** | **Yes** | **Yes** + handling notice |
| **Encrypt at rest?** | No | Recommended | **Yes** | **Yes** (AES-256, FIPS) |
| **Encrypt in transit?** | No | **Yes** | **Yes** | **Yes** (TLS 1.3 preferred) |
| **Who can access?** | Anyone | All staff | Role-based, approved | Role + **minimum necessary**, named authorization |
| **Email externally?** | Yes | Manager approval | Encrypted + owner approval | **Secure portal only** + Privacy Officer approval |
| **USB / removable media?** | OK | Avoid | Encrypted only | **Prohibited** |
| **Personal device?** | OK | Managed container | Managed container | **Prohibited** |
| **Disposal** | Normal | Normal | Cross-cut shred / crypto-erase | **Certified destruction + certificate** |

---

### The 6 rules that prevent most violations

1. **Unsure? It's CONFIDENTIAL.** Unclassified data defaults to CONFIDENTIAL until someone classifies it.
2. **Mixed content takes the highest level.** One patient name in a spreadsheet makes the whole file RESTRICTED.
3. **Access ≠ authorization.** You may only open a record you have a *treatment or business reason* to open. The system letting you in is not permission.
4. **Never look up yourself, family, colleagues, or public figures.** This is the single most common cause of dismissal at healthcare organizations. It is detected by automated auditing, every time.
5. **PHI never goes in a subject line, filename, chat message, screenshot, ticket, or AI tool.**
6. **Report exposure within 1 hour — even if you caused it.** Good-faith reporting protects you. Concealment does not.

---

### Before you send, store, or print — ask:

- **Is it labeled?**
- **Is the recipient authorized, and is this the minimum necessary?**
- **Did I check the address / the distribution list / the fax number?**
- **Is this channel approved for this level?** (§6 of the policy)
- **If it prints — will I collect it immediately?**
- **If it's PHI going outside HealthPlus — is there a BAA or patient authorization?**

---

### Quick don'ts

❌ Personal email, personal cloud (Dropbox, iCloud, personal Google Drive), personal phone storage
❌ Unapproved AI, transcription, translation, or file-conversion websites — pasting PHI into one is a reportable disclosure
❌ Consumer messaging apps (WhatsApp, SMS, personal Messenger) for anything HealthPlus
❌ Production PHI in test, training, demo, or screenshot material — use synthetic data
❌ Discussing patients in corridors, elevators, cafeterias, or on public transport
❌ Leaving charts, screens, or printouts unattended — lock it, file it, or take it with you
❌ Confidential paper in general waste or open recycling — secure bins only

---

### Report immediately — within 1 hour

| | |
|---|---|
| **Security hotline (24/7)** | ext. **4357** |
| **Email** | `security@healthplus.org` |
| **Privacy Officer** | ext. **4400** · `privacy@healthplus.org` |
| **Anonymous ethics line** | `https://healthplus.ethicspoint.com` |

**Report if:** you sent something to the wrong person · you found data where it shouldn't be · you lost a device or paperwork · you clicked a phishing link · you accessed a record you shouldn't have · you're not sure whether something is a problem.

> **Reporting your own mistake in good faith will not get you disciplined. Hiding it will.**
> A misdirected email reported in 10 minutes is usually containable. The same email reported in three days is a breach notification to the regulator and to every patient involved.

*POL-SEC-009 v3.0 · Questions: `privacy@healthplus.org` · Full policy on the intranet*

---

*End of document.*
