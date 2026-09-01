# INCIDENT RESPONSE POLICY
**GlobalTech Manufacturing**

| | |
|---|---|
| **Document ID** | POL-SEC-007 |
| **Version** | 2.0 |
| **Classification** | Internal — Restricted |
| **Effective Date** | 01 October 2026 |
| **Next Review** | 01 October 2027 (annual, and after every Critical incident) |
| **Policy Owner** | Chief Information Security Officer |
| **Approved By** | Executive Board |
| **Framework Basis** | NIST SP 800-61r2; ISO/IEC 27001:2022 A.5.24–A.5.28; IEC 62443 (OT); GDPR Art. 33/34; NIS2 Art. 23 |
| **Scope** | All GlobalTech entities in 5 countries; all IT, OT, IoT, and cloud systems; all employees, contractors, and suppliers |

---

## 1. Purpose and Scope

**1.1 Purpose.** To ensure GlobalTech detects, contains, eradicates, and recovers from security incidents in a consistent, timely, and legally defensible way — protecting personnel safety, production continuity, intellectual property, and personal data, and meeting the notification obligations that attach to each.

**1.2 Scope.** This policy covers every information and operational technology asset owned, operated, or used by GlobalTech: corporate IT and cloud, the five manufacturing sites' OT and ICS environments (PLCs, SCADA, HMIs, historians, safety instrumented systems), IoT and connected products, supplier-managed systems holding GlobalTech data, and all personal data processed by the company. It binds all employees, contractors, and third parties with access.

**1.3 Overriding principle — safety first.** In OT and ICS environments, **human safety takes precedence over confidentiality, integrity, and availability, in that order of override.** No containment action may be taken on a production or safety system without the authorization of the site OT Lead and Plant Safety Officer. Where an action would create a physical hazard, it must not be taken; an alternative containment path must be found. This principle overrides every other instruction in this policy.

**1.4 Lifecycle.** GlobalTech follows the NIST SP 800-61r2 lifecycle: **Preparation → Detection & Analysis → Containment, Eradication & Recovery → Post-Incident Activity**, with the loop from post-incident back into preparation treated as mandatory, not optional.

---

## 2. Incident Classification Matrix
*(Deliverable 2)*

**2.1 Severity definitions.** Severity is assigned by the Incident Response Manager at triage and reassessed at every status point. Where IT and OT indicators disagree, **the higher severity applies**. Any incident with a credible safety implication is **Critical** regardless of other factors.

| Severity | Definition | Acknowledge | Triage Complete | Containment Target | Update Cadence |
|---|---|---|---|---|---|
| **Critical (S1)** | Threat to human safety, or loss of a production line, or confirmed breach of personal data or IP at scale, or active adversary in OT/ICS | **15 min**, 24/7 | 1 hour | **4 hours** | Hourly to Exec |
| **High (S2)** | Significant business impact or a credible path to Critical; confined to one site or system group; contained but active threat | **1 hour** | 4 hours | **24 hours** | Every 4 hours |
| **Medium (S3)** | Limited impact, contained, no personal data or OT involvement; workaround available | **4 business hours** | 1 business day | **3 business days** | Daily |
| **Low (S4)** | Minimal impact; policy violation, single-user event, or near-miss with no confirmed compromise | **1 business day** | 3 business days | **10 business days** | At closure |

**2.2 Examples by severity.**

| Severity | Examples |
|---|---|
| **Critical (S1)** | Ransomware encrypting file servers or spreading toward OT · Malware or unauthorized commands on PLC/SCADA/HMI · Compromise or bypass of a Safety Instrumented System · Confirmed exfiltration of product designs, CAD, or process IP · Personal data breach affecting > 1,000 data subjects or any special-category data · Full or partial production shutdown from a cyber cause · Domain Admin or OT engineering workstation compromise · Confirmed nation-state or targeted intrusion · Public exposure of customer or employee data |
| **High (S2)** | Ransomware contained to a single endpoint or segment · Business email compromise with attempted payment fraud · Compromise of a privileged IT account · Malware on an OT-adjacent engineering workstation (no PLC impact) · Personal data breach affecting < 1,000 data subjects, non-special-category · Unauthorized access to a single production database · Critical vulnerability actively exploited in the wild on an internet-facing asset · Supplier breach with possible GlobalTech data exposure · Loss of an unencrypted device containing confidential data · DDoS degrading a customer-facing service |
| **Medium (S3)** | Malware on a single workstation, contained by EDR · Successful phishing with credentials entered but MFA held · Unauthorized IoT or rogue device on a corporate network segment · Misconfigured cloud storage exposed internally only · Repeated failed intrusion attempts against a perimeter device · Insider policy violation with data movement but no confirmed exfiltration · Lost encrypted device with remote wipe confirmed |
| **Low (S4)** | Phishing email reported and blocked, no interaction · Spam or scam attempt · Blocked malware download · Isolated policy violation (unapproved software, shared credential) with no data impact · Failed logon anomalies resolved as user error · Near-miss identified in monitoring · Vulnerability found in scanning with no exploitation |

**2.3 Automatic escalation triggers.** An incident is escalated to the next severity — and to **Critical** where marked ⚠ — on any of:

⚠ Any indication of risk to human safety · ⚠ Any confirmed unauthorized access to Purdue Level 0–2 (control and process) systems · ⚠ Any confirmed exfiltration of personal data or IP · Detection of lateral movement toward the IT/OT boundary · Adversary activity persisting more than 4 hours after containment begins · Media, regulator, or customer enquiry about the incident · Incident affecting more than one country entity · Loss of monitoring or logging visibility during an active incident.

**2.4 De-escalation** requires the Incident Response Manager's decision, documented with the evidence relied on, and — for any incident that touched OT or personal data — the concurrence of the OT Lead or Data Protection Officer respectively.

---

## 3. Incident Response Team

**3.1 Structure.** A permanent **core team** is on 24/7 rotation. An **extended team** is convened by severity: S3/S4 core only; S2 adds IT Support, Legal, and the affected site; S1 adds all roles including the Executive Sponsor and Communications.

| Role | Responsibilities | Authority |
|---|---|---|
| **Incident Response Manager (IRM)** | Owns the incident end to end. Declares and classifies incidents; assigns severity; directs the response; maintains the incident log and timeline; runs status calls; decides containment strategy; declares closure. Single point of coordination — all decisions route through this role. | May direct any GlobalTech resource during an active S1/S2. May isolate IT systems unilaterally. **May not** authorize OT actions alone (see OT Lead). |
| **Security Analysts (SOC)** | Monitor detection sources; perform triage and initial assessment; conduct technical investigation, log and malware analysis, and forensic imaging; execute containment and eradication actions; document all technical findings and IOCs; maintain evidence integrity. | Execute containment on IT endpoints and accounts on IRM direction; isolate an endpoint immediately on credible active-threat evidence. |
| **OT / ICS Lead** *(site-based)* | Assesses safety and production impact of every proposed action in OT; advises on ICS-safe containment; coordinates with plant engineering; validates the integrity of control logic and safety systems before restart; owns OT recovery sequencing. | **Veto over any action affecting OT or safety systems.** Jointly authorizes OT containment with the Plant Safety Officer. |
| **IT Support / Infrastructure** | Provide system access, account actions, network changes, and configuration data; execute rebuild and restoration from validated backups; verify backup integrity; restore service and confirm functionality with business owners. | Execute changes under emergency change authority, logged retrospectively within 24 hours. |
| **Legal Counsel** | Determine legal and regulatory obligations, including GDPR Art. 33/34 and NIS2 Art. 23 across all five jurisdictions; establish and maintain legal privilege over investigation material; advise on evidence admissibility, law enforcement engagement, contractual notification duties, and insurer notification; approve all external written communications. | Decides whether privilege applies; decides law enforcement engagement with the Executive Sponsor. |
| **Data Protection Officer (DPO)** | Assesses whether an incident is a personal data breach; performs the risk-to-data-subjects assessment; owns the Art. 33 notification to the lead supervisory authority and any Art. 34 communication to data subjects; maintains the Art. 33(5) internal breach register. | Independent statutory role — decides the notification assessment; may escalate directly to the Board. |
| **Communications / PR** | Draft and issue all internal and external messaging; hold and maintain pre-approved holding statements; manage media, customer, and employee communication; monitor social and press coverage; coordinate with Sales on customer messaging. | Sole authorized external voice. No other person may speak publicly about an incident. |
| **Human Resources** | Support any insider-related investigation; ensure employee rights and works council obligations are met; manage employee communications and welfare; administer any disciplinary process arising. | Jointly authorizes investigation of an individual with the CISO. |
| **Executive Sponsor** *(CISO for S2; COO or CEO for S1)* | Owns business risk decisions: production shutdown, ransom position, public disclosure timing, extraordinary spend, invoking third-party IR retainer. Removes organizational obstacles. Accountable to the Board. | Final decision authority on business-impacting actions. Sole authority to approve a production shutdown or a ransom-related decision. |
| **Site Incident Coordinators** *(one per country/site)* | Local point of contact; coordinate on-site physical and personnel actions; manage local language communication; liaise with local regulators and works councils. | Act on IRM direction within their site. |

**3.2 Deputies.** Every role has a named, trained deputy. No incident waits on a single person's availability. The on-call roster and escalation tree are published in the IR runbook and tested quarterly.

**3.3 External parties.** Retained forensic and IR provider (contract active, 4-hour response SLA); cyber insurer (notification within 24 hours of any S1/S2 to preserve cover); outside privacy and cyber counsel per jurisdiction; national CERT/CSIRT contacts for all five countries; law enforcement contacts. Vendor call-out for S1 is pre-authorized and requires no procurement cycle.

---

## 4. Detection and Reporting

**4.1 Detection sources.** SIEM correlation across IT, cloud, and OT log feeds · EDR/XDR on endpoints and servers · OT-specific network monitoring (passive protocol inspection at Purdue Levels 1–3; no active scanning of control networks) · IDS/IPS at the IT/OT boundary and perimeter · email security and phishing reports · DLP and cloud access security · vulnerability and attack-surface management · integrity monitoring on PLC logic and engineering workstations · threat intelligence and dark-web monitoring for GlobalTech data · anomaly reports from plant operators and engineers · supplier and customer notifications · external reports (researchers, CERTs, law enforcement).

**4.2 How to report.** Every person with access to a GlobalTech system **must** report a suspected incident **immediately**, and in any case within **1 hour of discovery**, without first investigating or attempting to fix it.

| Channel | Detail | Availability |
|---|---|---|
| Security hotline | ext. **7777** / +XX XXX XXX XXXX | 24/7 — **use this for anything urgent or OT-related** |
| Security email | `soc@globaltech.com` | 24/7 monitored |
| Service Desk portal | `https://servicedesk.globaltech.com` | 24/7 |
| Phishing button | In the mail client | Immediate |
| Anonymous ethics line | `https://globaltech.ethicspoint.com` | 24/7, independently operated |
| Plant floor | Report to the Site Incident Coordinator **and** the Plant Safety Officer in person | Per shift |

**Reporting in good faith never attracts disciplinary action, including where the reporter's own error caused the incident.** Concealment or delay is a serious violation. Retaliation against a reporter is itself a disciplinary matter.

**4.3 Information to collect.** The reporter provides what they know — an incomplete report made now beats a complete report made in an hour:

- **Who:** reporter name, role, site, contact number, and who else is aware
- **What:** what was observed, in plain description; what system, machine, or line; any error or ransom message (photograph the screen, do not transcribe from memory)
- **When:** date and time first observed, and when it is believed to have started
- **Where:** site, plant area, network segment, hostname, IP, asset tag
- **Scope:** what else is affected or behaving abnormally; whether production is affected; whether any safety system is involved
- **Data:** whether personal data, customer data, or IP may be involved, and roughly how much
- **Actions already taken:** anything the reporter or anyone else has already done — critical for forensic accuracy
- **Evidence:** screenshots, photographs, the suspicious email as an attachment, physical items

**4.4 What not to do.** Do not power off, reboot, reimage, delete, "clean," or run antivirus scans on an affected system unless directed by the SOC — these destroy volatile evidence. Do not disconnect an OT device without OT Lead authorization. Do not reply to, pay, or negotiate with an attacker. Do not discuss the incident on external channels, social media, or personal devices. Do not use the potentially compromised system or network to report the incident.

**4.5 Initial assessment (triage).** The SOC completes, within the triage window for the severity:

1. **Validate** — is this a genuine incident or a false positive? Record the basis for the conclusion.
2. **Classify** — assign severity per §2, and record the reasoning.
3. **Scope** — identify affected systems, accounts, data, sites, and countries; determine whether the IT/OT boundary has been crossed.
4. **Assess impact** — safety, production, data, financial, regulatory, reputational.
5. **Identify data involvement** — engage the DPO immediately if personal data may be implicated, so the 72-hour GDPR clock is managed from the outset.
6. **Declare** — open the incident record, assign the IRM, notify per §7, and convene the team appropriate to the severity.

The declaration timestamp is recorded and is the reference point for all notification deadlines.

---

## 5. Response Procedures

### 5.1 Containment

**Short-term containment** — stop the spread, preserve the evidence:

| Environment | Actions |
|---|---|
| **IT** | Network-isolate affected endpoints via EDR (isolate, do not power off) · disable or reset compromised accounts and revoke sessions and tokens · block malicious IPs, domains, and hashes at perimeter and DNS · quarantine mailboxes and pull malicious mail estate-wide · suspend affected integrations and API keys · segment or shut down the affected service where necessary |
| **OT / ICS** | **No action without OT Lead and Plant Safety Officer authorization.** Prefer isolation at the IT/OT boundary firewall over any action on control devices · place affected lines in a controlled safe state rather than an abrupt stop · switch to manual or local control where the process supports it · never power-cycle a PLC or safety controller for containment · document the process state before and after every action |
| **Cloud** | Revoke sessions and tokens · disable compromised identities and applications · snapshot affected resources before change · restrict security groups · enable enhanced logging |

**Evidence preservation** must occur **before** eradication (see §6): image volatile memory first, then disk; export logs before rotation; snapshot cloud resources; photograph screens and physical state; record every action taken in the incident log with a timestamp and the actor.

**Containment decision factors** — recorded by the IRM: risk to human safety; risk of further damage or spread; production and revenue impact; evidence preservation needs; service availability requirements; duration the containment can be sustained; and whether observing the adversary yields intelligence that outweighs the risk of continued access (this option requires Executive Sponsor approval and is never permitted where safety or OT is implicated).

**Long-term containment** — sustainable measures while the environment is rebuilt: temporary firewall rules and segmentation; enhanced monitoring and hunting on the affected estate; emergency patching; forced credential rotation across the affected trust boundary; blocking the initial access vector; deploying temporary compensating controls; and standing up clean systems in parallel with the compromised ones.

### 5.2 Eradication

1. **Root cause analysis** — establish the initial access vector, the full attack path, persistence mechanisms, privilege escalation, lateral movement, dwell time, and what the adversary accessed or took. Map to MITRE ATT&CK (Enterprise and ICS). **The incident is not eradicated until the root cause is known** — removing symptoms without cause guarantees recurrence.
2. **Threat removal** — remove malware, backdoors, web shells, scheduled tasks, services, and registry persistence; delete attacker-created accounts and revoke attacker-added credentials, keys, certificates, and OAuth grants; close the exploited vulnerability; remove unauthorized firewall and configuration changes; restore verified-good PLC logic and controller configuration from a signed baseline.
3. **Credential reset** — reset all credentials in the compromised trust boundary, prioritizing privileged, service, and domain accounts; rotate the domain `krbtgt` account twice where Active Directory is implicated; rotate API keys, certificates, and shared secrets.
4. **Validation** — confirm removal by rescanning with updated signatures and IOCs, hunting for the identified TTPs across the whole estate (not only known-affected systems), reviewing logs for residual activity, verifying configuration against baseline, and independently confirming OT integrity through control-logic comparison and functional safety testing. **Rebuild from known-good media in preference to cleaning**, always for systems where the adversary held administrative access.

### 5.3 Recovery

**Restoration is authorized by the IRM with the system owner, and — for any OT system — the OT Lead and Plant Safety Officer.** Recovery does not begin until eradication is validated.

1. **Preconditions:** root cause identified and closed; adversary access confirmed removed; backups verified clean and integrity-checked; monitoring and logging fully restored; and the restoration plan documented with a rollback path.
2. **Sequence:** restore in priority order — safety systems, then production-critical, then business-critical, then remainder. Restore from the most recent backup predating the compromise. Rebuild rather than restore where backup integrity is uncertain. Bring systems back into a segmented environment before returning them to the production network.
3. **Testing before return to service:** functional testing by the business owner; security validation (patching, hardening, agent presence, configuration baseline); data integrity verification; and, for OT, full functional safety testing and sign-off by the Plant Safety Officer before any line restarts.
4. **Heightened monitoring** for a minimum of **30 days** after an S1 and **14 days** after an S2: IOC and TTP alerting on the affected estate; targeted threat hunting at day 7 and day 30; authentication and privileged access review; and daily review by the SOC for the first week.
5. **Formal return to normal operations** is declared by the IRM, with the Executive Sponsor's concurrence for S1, and recorded with the date, time, and criteria met.

---

## 6. Evidence Handling

**6.1 Principle.** Every incident is treated as potentially leading to litigation, regulatory proceedings, an insurance claim, or prosecution. Evidence is collected accordingly from the first minute, whether or not that outcome currently seems likely.

**6.2 Chain of custody.** Every item of evidence — physical or digital — carries a chain of custody record from the moment of collection:

| Field | Recorded |
|---|---|
| Evidence ID | Unique, sequential, incident-referenced (e.g. `INC-2026-0142-E003`) |
| Description | Item, make, model, serial/asset tag, capacity |
| Source | System, location, site, country |
| Collected by | Name, role, signature |
| Collected at | Date, time (UTC and local), method and tool used, tool version |
| Hash | SHA-256 of every image and file, computed at acquisition and verified at each transfer |
| Transfers | Every custody change: from, to, date, time, purpose, both signatures |
| Storage | Location, access controls, seal number |
| Disposition | Retention basis, release or destruction date and authority |

Any break in the chain must be documented with an explanation; an undocumented gap may render the evidence inadmissible.

**6.3 Preservation.** Collect in **order of volatility** (RFC 3227): memory and running state → network connections and ARP/routing → running processes → temporary files → disk → remote and archived logs → physical media and configuration. Work on forensic copies only, never originals; write-blockers for physical media; verify hashes before and after every operation; store originals in a sealed, access-controlled evidence store. Suspend log rotation, backup expiry, and automatic deletion on all potentially relevant systems the moment an incident is declared (**Legal Hold**, issued by Legal Counsel and overriding all retention schedules). Preserve full packet capture where available. In OT, capture controller configuration and logic before any change, and photograph HMI and panel state.

**6.4 Documentation.** A single contemporaneous incident log records every observation, decision, action, and communication with a UTC timestamp and the named actor — written as events occur, never reconstructed afterwards. Decisions record the options considered, the option chosen, who approved it, and why. All investigation material is marked **Privileged and Confidential — Prepared at the Direction of Legal Counsel** where Legal so directs.

**6.5 Retention.** Incident records and evidence: **7 years** from closure. Records relating to a personal data breach: 7 years (supporting the GDPR Art. 33(5) register). Records subject to a Legal Hold or active proceedings: retained until Legal releases the hold. Disposal only on Legal Counsel's written authority, recorded in the chain of custody.

---

## 7. Communication Plan
*(Deliverable 3)*

**7.1 Principles.** One authorized voice (Communications, with Legal approval). Facts only — no speculation about cause, attribution, or scope. Deadlines are legal obligations, not targets. All external written communication is approved by Legal before release. Internal communication about an active incident uses **out-of-band channels** (pre-agreed phone bridge, alternate messaging) — never the potentially compromised email or chat system.

**7.2 Stakeholder matrix.**

| Stakeholder | When to Notify | Method | Owner |
|---|---|---|---|
| **Incident Response Team** | Immediately on declaration (all severities) | Automated page + out-of-band bridge | SOC |
| **Executive Management** | **S1: within 1 hour.** S2: within 4 hours. S3/S4: weekly summary | Phone call, then secure written brief; hourly updates during S1 | IRM |
| **Executive Board** | S1 within 4 hours; any incident with regulatory notification; any incident affecting production > 24 hours | Direct briefing by CISO and Executive Sponsor | Executive Sponsor |
| **Legal Counsel** | **Immediately on declaration of S1/S2**, and on any incident involving personal data, IP, insider conduct, or a third party — before any external communication | Phone, then privileged written channel | IRM |
| **Data Protection Officer** | **Immediately** where personal data may be involved — at the first suspicion, not on confirmation | Phone + incident record | IRM |
| **Supervisory Authority (GDPR)** | **Within 72 hours** of becoming aware of a personal data breach likely to result in a risk to individuals — via the **lead supervisory authority** (one-stop-shop) with the other four national authorities informed as concerned authorities. Where all facts are not yet known, notify within 72 hours and supplement in phases (Art. 33(4)). Where notification is late, the reasons must be given | Authority's official portal, written | DPO |
| **National CSIRT / NIS2 authority** | **Early warning within 24 hours** of awareness of a significant incident; **incident notification within 72 hours**; **final report within 1 month** (NIS2 Art. 23) — in each affected country | Official national portal | Legal + CISO |
| **Other regulators** *(sector, export control, safety authority)* | Per each regulator's rules; safety authority immediately on any safety-system involvement | Per regulator; documented | Legal |
| **Affected data subjects** | **Without undue delay** where the breach is likely to result in a **high risk** to their rights and freedoms (GDPR Art. 34) — in clear, plain language, in local language, describing the breach, the likely consequences, the measures taken, and the DPO contact | Direct email or letter; public communication where individual contact is disproportionate | DPO + Comms |
| **Affected employees** | S1: within 4 hours of declaration, with clear instructions. Others: as required for action | All-staff message via verified channel; site briefings; works council per local law | HR + Comms |
| **Customers** | Where their data, orders, or deliveries are affected — within 24 hours of confirming impact; contractual notification clauses may be shorter and prevail | Account manager call, then written notice | Comms + Sales |
| **Suppliers / partners** | Where they are the source, a vector, or affected — immediately on identification | Direct contact via security contact in the contract | Procurement + CISO |
| **Cyber insurer** | **Within 24 hours** of any S1/S2 declaration — late notice can void cover | Per policy notification clause | Legal |
| **Law enforcement** | On Executive Sponsor and Legal decision — always for extortion, nation-state activity, or physical safety threat | Established national contacts | Legal |
| **Media / public** | Only when required by law, or when the incident is or will become public. **No comment beyond the approved statement** | Approved written statement only; single spokesperson | Comms |
| **Works councils / employee representatives** | Per local law in each of the five countries, before any employee monitoring or data-processing change | Per local agreement | HR + Legal |

**7.3 Notification decision — personal data.** The DPO documents, for every incident involving personal data, whether it is a breach; whether it is likely to result in a risk (→ Art. 33 authority notification); and whether it is likely to result in a **high** risk (→ Art. 34 individual communication). **A documented decision not to notify is itself a required record** under Art. 33(5). The 72-hour clock starts at the point of **awareness** — a reasonable degree of certainty that a breach has occurred — not at the completion of the investigation.

**7.4 Holding statement.** Pre-approved holding statements are maintained in the runbook in all five local languages, releasable by Communications with Legal approval within 30 minutes of an S1 declaration.

---

## 8. Post-Incident Activities

**8.1 Lessons learned review.** Mandatory for every S1 and S2, and for any S3 with a systemic cause. Held within **10 business days** of closure, chaired by someone who did not lead the response, and attended by everyone materially involved plus the business owner.

The review is **blameless**: it examines systems, controls, and decisions made with the information available at the time — not individual fault. Deliberate misconduct is handled separately through HR and is not the subject of this review.

Questions addressed (NIST SP 800-61r2 §3.4.1): What happened, and when? How well did staff and management perform against the documented procedures? What information was needed sooner? Were any steps taken that inhibited recovery? What would we do differently? What corrective actions prevent recurrence? What additional tooling, detection, or training is needed? What indicators should be monitored for in future?

**8.2 Actions.** Every action from the review has a named owner, a due date, and a priority, and is tracked to closure in the risk register. Actions from an S1 are reported to the Executive Board monthly until closed. Detection gaps identified become new SIEM rules or hunt hypotheses within 30 days. This policy and the runbooks are updated within 30 days of any S1.

**8.3 Reporting requirements.**

| Report | Deadline | Audience |
|---|---|---|
| Initial notification | Per §7.2 by severity | IR team, Executive |
| Situation reports during response | Per §2.1 cadence | Executive, stakeholders |
| Preliminary incident report | Within 5 business days of containment (S1/S2) | Executive, Legal, DPO |
| **Full incident report** | Within 15 business days of closure (S1/S2) | Executive Board, Internal Audit, Legal, insurer |
| Lessons learned report and action plan | Within 20 business days of closure | Executive Board, control owners |
| Regulatory final report (NIS2) | Within 1 month of notification | National authority |
| Quarterly incident trend analysis | Quarterly | Executive Board, Risk Committee |
| Annual IR programme review, including exercise results | Annually | Executive Board, ISO 27001 audit |

**8.4 Metrics.** Tracked and reported quarterly: mean time to detect (MTTD); mean time to acknowledge; mean time to contain (MTTC); mean time to recover (MTTR); incidents by severity, category, site, and root cause; percentage detected internally versus reported externally; repeat incidents from the same root cause; corrective actions closed on time; notification deadlines met; and exercise participation and findings.

**8.5 Preparation (the loop back).** Maintained continuously and tested on this schedule:

| Activity | Frequency |
|---|---|
| IR runbook and contact tree review | Quarterly |
| Tabletop exercise (rotating scenario, including an OT/ransomware scenario at least annually) | Quarterly |
| Full technical simulation across IT and OT | Annually |
| Backup restoration test, including OT controller logic restoration | Quarterly |
| IR team role-specific training | Annually |
| All-staff incident awareness and reporting training | Annually, plus onboarding |
| Third-party IR retainer and insurer contact verification | Annually |
| Out-of-band communication channel test | Quarterly |

---

## 9. Enforcement, Exceptions and Compliance

**9.1** Compliance is mandatory for all persons in scope. Failure to report a known incident, concealment, obstruction of an investigation, tampering with evidence, or unauthorized external disclosure is a serious disciplinary matter, up to and including dismissal and referral to law enforcement. Deliberate destruction of evidence under Legal Hold may constitute a criminal offence.

**9.2** Good-faith reporting and self-disclosure attract no disciplinary action and are treated as mitigating in any related matter.

**9.3** No exception may be granted to the safety-first principle (§1.3), the reporting obligation (§4.2), the evidence preservation requirements (§6), or the regulatory notification timelines (§7). Other exceptions require CISO approval, are time-limited to 6 months, and are recorded in the exception register.

**9.4** Compliance is verified through quarterly exercise results, annual Internal Audit testing, ISO 27001 surveillance audit (A.5.24–A.5.28), and post-incident review of adherence to this policy.

---

## 10. Definitions

| Term | Definition |
|---|---|
| **Event** | Any observable occurrence in a system or network. Most events are not incidents. |
| **Incident** | An event that actually or potentially jeopardizes the confidentiality, integrity, or availability of an information or operational system, or the data it holds, or constitutes a violation of security policy. |
| **Personal data breach** | A breach of security leading to accidental or unlawful destruction, loss, alteration, unauthorized disclosure of, or access to personal data (GDPR Art. 4(12)). |
| **Awareness (GDPR)** | The point at which GlobalTech has a reasonable degree of certainty that a security incident leading to a personal data breach has occurred — the start of the 72-hour clock. |
| **OT / ICS** | Operational Technology / Industrial Control Systems — hardware and software that detect or cause change through direct monitoring and control of physical devices and processes. |
| **Purdue Model** | The reference architecture segmenting enterprise IT (Levels 4–5) from manufacturing operations (Level 3), control (Levels 1–2), and process (Level 0). |
| **SIS** | Safety Instrumented System — the system that brings a process to a safe state. Never subject to unilateral containment action. |
| **IOC / TTP** | Indicator of Compromise / Tactics, Techniques and Procedures. |
| **Legal Hold** | A directive from Legal Counsel suspending all deletion and retention schedules for specified records. |
| **Chain of custody** | The documented, unbroken record of who held each item of evidence, when, and for what purpose. |
| **Dwell time** | The elapsed period between initial compromise and detection. |
| **Must / Shall** | Mandatory. **Should**: recommended. **May**: permitted. |

## 11. Related Documents

**Internal:** POL-SEC-001 Information Security · POL-SEC-002 Acceptable Use · POL-SEC-004 Password and Authentication · POL-SEC-009 Data Classification · POL-SEC-011 Third-Party Security · POL-SEC-015 Business Continuity and Disaster Recovery · POL-SEC-016 OT/ICS Security · POL-PRIV-001 Data Protection Policy and Art. 30 records · IR Runbooks (ransomware, BEC, OT compromise, data breach, insider, DDoS, supplier compromise) · Contact tree and on-call roster · Site emergency and safety procedures.

**External:** NIST SP 800-61 Rev. 2 *Computer Security Incident Handling Guide* · NIST SP 800-86 *Forensic Techniques* · SANS *Incident Handler's Handbook* · ISO/IEC 27001:2022 A.5.24–A.5.28 and ISO/IEC 27035 · IEC 62443-2-1 / 62443-3-3 (OT security) · GDPR Art. 33, 34, and EDPB Guidelines 9/2022 on breach notification · NIS2 Directive Art. 23 · CISA *Federal Government Cybersecurity Incident and Vulnerability Response Playbooks* · MITRE ATT&CK for Enterprise and for ICS · RFC 3227 *Guidelines for Evidence Collection and Archiving*.

## 12. Revision History

| Version | Date | Approved By | Changes |
|---|---|---|---|
| 1.0 | 18 May 2021 | CISO | Initial issue; IT scope only; three severity levels. |
| 1.1 | 02 Sep 2023 | Executive Board | GDPR notification workflow added following supervisory authority guidance. |
| **2.0** | **15 Sep 2026** | **Executive Board** | Full rewrite to NIST SP 800-61r2. OT/ICS brought fully into scope with the safety-first override (§1.3) and OT Lead veto authority. Four-level severity matrix with response times and automatic escalation triggers (§2). Role definitions extended to DPO, OT Lead, HR, and Site Coordinators (§3). Evidence handling and chain of custody formalized (§6). Communication plan extended to NIS2 24h/72h/1-month timelines and the GDPR one-stop-shop across five jurisdictions (§7). Blameless lessons-learned process, metrics, and exercise schedule added (§8). |

---
---

# ANNEX A — INCIDENT REPORT TEMPLATE
*(Deliverable 4)*

*Complete for every S1 and S2 incident within 15 business days of closure. Sections 1–4 are completed during the response; the remainder at closure. Mark **Privileged and Confidential — Prepared at the Direction of Legal Counsel** where Legal has so directed.*

## 1. Incident Summary

| Field | Entry |
|---|---|
| Incident ID | `INC-YYYY-NNNN` |
| Report classification | ☐ Internal — Restricted ☐ Privileged and Confidential |
| Title | |
| Severity (final) | ☐ Critical ☐ High ☐ Medium ☐ Low — *state if reclassified during response, and why* |
| Category | ☐ Malware/Ransomware ☐ Phishing/BEC ☐ Unauthorized access ☐ Data breach ☐ OT/ICS compromise ☐ Insider ☐ DoS ☐ Supplier ☐ Physical ☐ Other |
| Incident Response Manager | |
| Executive Sponsor | |
| Report author / date | |
| Status | ☐ Contained ☐ Eradicated ☐ Recovered ☐ Closed |

**Executive summary** *(maximum 200 words — what happened, what the impact was, what was done, and what is being changed. Written for a Board reader with no technical background.)*

## 2. Timeline

*All times UTC, with local time in parentheses. Every entry states the source of the evidence for it.*

| # | Date / Time (UTC) | Event | Source of evidence | Actor |
|---|---|---|---|---|
| 1 | | *Initial compromise (estimated)* | | |
| 2 | | *First detection / report* | | |
| 3 | | *Incident declared, severity assigned* | | |
| 4 | | *IR team convened* | | |
| 5 | | *Containment initiated* | | |
| 6 | | *Containment confirmed* | | |
| 7 | | *Root cause identified* | | |
| 8 | | *Eradication complete* | | |
| 9 | | *Recovery complete / service restored* | | |
| 10 | | *Incident closed* | | |

**Key intervals:** Dwell time (compromise → detection): ___ · Detection → declaration: ___ · Declaration → containment: ___ · Containment → recovery: ___ · **Total incident duration:** ___

## 3. Detection and Initial Response

| Field | Entry |
|---|---|
| How detected | ☐ SIEM ☐ EDR ☐ OT monitoring ☐ User report ☐ Customer/supplier ☐ External party ☐ Threat intel ☐ Audit ☐ Other |
| Detected internally or externally | ☐ Internal ☐ External *(external detection is itself a finding)* |
| Reported by | |
| Initial indicators observed | |
| Why it was not detected sooner | *(mandatory — control gap, coverage gap, tuning, or "detected as designed")* |
| Triage findings | |

## 4. Scope and Impact

**Affected assets**

| Asset / System | Type (IT/OT/Cloud) | Site / Country | Impact | Restored (date) |
|---|---|---|---|---|
| | | | | |

**Impact assessment**

| Dimension | Assessment |
|---|---|
| **Safety** | ☐ None ☐ Potential ☐ Actual — *describe; mandatory narrative if not "None"* |
| **Production** | Lines affected: ___ · Downtime: ___ hours · Units lost: ___ |
| **Data — personal** | ☐ None ☐ Suspected ☐ Confirmed · Categories: ___ · Data subjects affected: ___ · Special category: ☐ Y ☐ N |
| **Data — IP / commercial** | ☐ None ☐ Suspected ☐ Confirmed — describe |
| **Systems** | Number affected: ___ · Rebuilt: ___ · Restored from backup: ___ |
| **Financial** | Direct response cost: ___ · Production loss: ___ · Third-party/legal: ___ · **Total estimated:** ___ |
| **Regulatory** | ☐ None ☐ GDPR Art. 33 ☐ GDPR Art. 34 ☐ NIS2 ☐ Sector regulator ☐ Other |
| **Reputational** | ☐ None ☐ Customer-aware ☐ Public/media |

## 5. Technical Analysis

**Root cause** *(the underlying control failure, not the symptom — e.g. "unpatched internet-facing VPN appliance, CVE-XXXX-XXXXX, patch available 94 days before exploitation, missed because internet-facing assets were not in the patch SLA scope")*

| Field | Entry |
|---|---|
| Initial access vector | |
| Vulnerability or weakness exploited | |
| Persistence mechanisms | |
| Privilege escalation | |
| Lateral movement | |
| Data accessed / exfiltrated | *(and the evidence establishing this — absence of evidence is not evidence of absence; state which)* |
| Attribution | ☐ Not determined ☐ Commodity ☐ Targeted ☐ Insider ☐ Attributed: ___ |
| **MITRE ATT&CK techniques** | *(Enterprise and/or ICS: TA/T identifiers)* |
| **Indicators of compromise** | *(hashes, IPs, domains, filenames, registry keys, user agents — attach as an appendix if extensive)* |
| **Which controls failed** | |
| **Which controls worked** | *(mandatory — records what to preserve and reinforce)* |

## 6. Response Actions

| # | Action | Phase | Date / Time (UTC) | Performed by | Approved by | Outcome |
|---|---|---|---|---|---|---|
| | | Containment / Eradication / Recovery | | | | |

**Validation of eradication** — how removal was confirmed: ___
**Recovery verification** — testing performed and by whom: ___
**Heightened monitoring** — period, scope, and findings: ___

## 7. Evidence

| Evidence ID | Description | Collected by / when | SHA-256 (abbrev.) | Current custody | Legal Hold |
|---|---|---|---|---|---|
| | | | | | ☐ Y ☐ N |

Chain of custody complete and unbroken: ☐ Yes ☐ No — *if No, explain* ___
External forensic provider engaged: ☐ Yes — ___ ☐ No

## 8. Communications and Notifications

| Stakeholder | Notified (date/time UTC) | Deadline | Met? | Method | By |
|---|---|---|---|---|---|
| Executive Management | | | ☐ | | |
| Legal Counsel | | | ☐ | | |
| Data Protection Officer | | | ☐ | | |
| Supervisory Authority (lead: ___) | | **72 h from awareness** | ☐ | | |
| National CSIRT — early warning | | **24 h** | ☐ | | |
| National CSIRT — notification | | **72 h** | ☐ | | |
| Affected data subjects | | Without undue delay | ☐ | | |
| Customers | | | ☐ | | |
| Employees | | | ☐ | | |
| Cyber insurer | | **24 h** | ☐ | | |
| Law enforcement | | | ☐ | | |

**Awareness timestamp (GDPR clock start):** ___
**Notification decision and rationale** *(including any documented decision NOT to notify — required under Art. 33(5))*: ___
**Any deadline missed** — which, by how long, why, and what has changed to prevent recurrence: ___

## 9. Lessons Learned

*Blameless — systems and decisions, not individuals.*

| Question | Finding |
|---|---|
| What happened, and when? | |
| How well did the team and management perform against documented procedures? | |
| What information was needed sooner, and why wasn't it available? | |
| Were any actions taken that inhibited containment or recovery? | |
| What would we do differently? | |
| What would have prevented this entirely? | |
| What would have detected it sooner? | |

**What went well** *(preserve these)*: ___

## 10. Corrective Actions

| # | Action | Type (Preventive / Detective / Corrective / Process) | Owner | Priority | Due | Status |
|---|---|---|---|---|---|---|
| | | | | ☐ P1 ☐ P2 ☐ P3 | | |

New detection rules created: ___ · Policy or runbook updates required: ___ · Training needs identified: ___ · Risk register entries raised or updated: ___

## 11. Sign-Off

| Role | Name | Signature | Date |
|---|---|---|---|
| Incident Response Manager | | | |
| CISO | | | |
| Data Protection Officer *(if personal data involved)* | | | |
| OT Lead *(if OT involved)* | | | |
| Legal Counsel | | | |
| Executive Sponsor | | | |

**Incident formally closed:** ☐ Yes — date: ___ **All corrective actions closed:** ☐ Yes ☐ Tracked to: ___

*Retain 7 years from closure, or until Legal releases any applicable Legal Hold.*

---

*End of document.*
