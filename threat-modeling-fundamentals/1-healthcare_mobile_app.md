# Threat Model — Healthcare Mobile App

**System:** iOS/Android app · REST API backend · cloud-hosted database · integration with hospital systems
**Features:** view medical records · schedule appointments · message providers · request prescription refills

---

## 1. The Most Critical Asset

**The patient's medical record** — diagnoses, test results, medications, clinical notes, and the messages with doctors that become part of it.

Everything else in the system exists to serve this data. Appointments and refills are *actions*; the record is the thing being protected, and it's the thing the law (HIPAA in the US, GDPR in Europe) treats as most sensitive.

The **CIA Triad** is the standard way to describe what "secure" means — **C**onfidentiality (only the right people can see it), **I**ntegrity (it's correct and unaltered), **A**vailability (it's there when needed). Medical records are unusual because *all three* matter severely:

| | Why it matters here |
|---|---|
| **Confidentiality** | Health data can't be reissued. A leaked card number is cancelled in ten minutes; a leaked HIV status, mental-health history or pregnancy is public forever. Consequences are social and personal — discrimination at work, insurance problems, damaged relationships — plus regulatory fines running into millions. |
| **Integrity** | This is the one people underestimate, and in healthcare it's the deadliest. A silently altered allergy field, a changed drug dosage, or a lab result attached to the wrong patient can kill someone. Confidentiality failures cause harm; integrity failures cause *clinical* harm. |
| **Availability** | If a doctor can't reach a record during an emergency, treatment is delayed or given blind. Ransomware attacks on hospitals have measurably increased patient mortality — availability here is a safety property, not a convenience. |

**Priority within the triad:** integrity first, because a wrong record can directly injure a patient and the error may go unnoticed. Confidentiality second, because the damage is permanent and irreversible. Availability third — serious, but usually there are fallback paths (phone, fax, paper) that don't exist for the other two.

**Runner-up asset:** the authentication system. It isn't valuable in itself, but whoever controls it controls every record in the system — it's the key to the vault rather than the vault.

---

## 2. STRIDE Applied to "Message Healthcare Providers"

STRIDE is a checklist of six ways things go wrong. All six apply to messaging.

### S — Spoofing: someone pretends to be a doctor (or a patient)

An attacker with a stolen password, or a hijacked session, sends messages as "Dr. Roberts": *"Stop taking your blood thinner before Friday."* Or the reverse — someone impersonates a patient to extract information from a provider, or requests a prescription change in their name.

**Impact:** Patients follow medical instructions from an unverified source. This can cause direct physical harm, and it's also an effective phishing channel — a message inside a trusted medical app carries far more authority than an email.

**Fix:** Multi-factor authentication for providers (they're the high-value accounts). Show a verified identity badge on provider messages, drawn from the hospital directory rather than a display name the sender controls. Short session lifetimes and re-authentication for sensitive actions. Detect logins from new devices or impossible locations.

### T — Tampering: a message is altered

A message is changed in transit or in storage — a dosage "10mg" becomes "100mg", or an instruction is quietly edited in the database after the fact.

**Impact:** Potentially fatal. Unlike a leak, this can be invisible: both sides believe they're reading the original, and nothing looks wrong until the patient is harmed.

**Fix:** Encrypt every connection (TLS, with certificate pinning in the mobile app so a fake network can't sit in the middle). Store messages as write-once — corrections are new messages, never edits to old ones. Give each message an integrity check (a hash or signature) that reveals any change. Never let raw text from a message be used to build a database query.

### R — Repudiation: someone denies sending a message

A provider denies giving advice a patient acted on, or a patient denies requesting a medication change — and there's no reliable record to settle it, because the message row can be edited or deleted by anyone with system access.

**Impact:** Malpractice and liability disputes with no evidence either way. In healthcare, the clinical record *is* the legal record — if it can be quietly rewritten, it's worthless in court and non-compliant with HIPAA's record-integrity requirements.

**Fix:** An append-only audit log — who sent what, when, from which device and IP, and who read it — stored where the application itself can't rewrite it. Digitally sign or hash-chain entries so tampering is detectable. Keep records for the legally required retention period.

### I — Information Disclosure: messages leak

Several realistic routes: the app caches message content in plain text on the phone (readable if the device is lost or backed up to a personal cloud), full message text appears in push notifications on a lock screen, screenshots are allowed, or the API returns another patient's thread because it fetched by message ID without checking who owns it.

**Impact:** Exposure of the most sensitive category of personal data, with permanent consequences for the patient and regulatory penalties for the provider. The lock-screen case is the most common and most overlooked — a diagnosis visible to anyone glancing at the phone on a table.

**Fix:** Push notifications say "You have a new message" and nothing more. Encrypt local storage and keep it out of device backups. Block screenshots on message screens. Every message request must check *this user owns this thread*, enforced in the query itself. Automatically wipe cached data after a period of inactivity.

### D — Denial of Service (also worth listing)

Flooding the messaging endpoint, or a provider's inbox, so urgent clinical messages are delayed or buried.

**Impact:** In healthcare, delay is harm — an unread message about worsening symptoms has clinical consequences.

**Fix:** Rate limiting per account, urgency flags with separate handling, and a clearly communicated rule that the app is not for emergencies (call emergency services instead).

### E — Elevation of Privilege (also worth listing)

A patient account, or a low-privilege staff account, reaches messages it shouldn't — typically because the API checks *that you're logged in* but not *whether this conversation is yours*, or because a hidden "role" field in the request can be changed by the client.

**Impact:** One ordinary account becomes access to every conversation in the system — the classic route from a small foothold to a full breach.

**Fix:** Check permissions on the server for every single request, on the specific record being touched — never rely on the app hiding a button. Roles come from the server, never from the request. Enforce least privilege: staff see only their own patients.

---

## 3. Five Security Controls, in Priority Order

**1. Strong authentication (multi-factor, mandatory for providers).**
Everything else depends on knowing who is asking. Stolen and reused passwords are the most common way healthcare systems are breached, and a provider account is a skeleton key to hundreds of patient records. MFA blocks the overwhelming majority of account-takeover attempts, and no amount of encryption or logging helps once an attacker is legitimately logged in. First because it's the precondition for every other control being meaningful.

**2. Authorization checks on every request (least privilege).**
Authentication asks *who are you*; authorization asks *are you allowed to see this specific record*. The single most common serious flaw in healthcare APIs is an endpoint that verifies the login but not the ownership — change the ID in the request and read someone else's chart. Enforce it server-side, on the exact record, every time; and give each role the minimum access it needs so a compromised receptionist account can't read the whole hospital. Second because it converts "one account stolen" into "one patient affected" instead of "all patients affected."

**3. Encryption in transit and at rest.**
TLS on every connection with certificate pinning in the mobile app; encrypted database storage with keys managed separately from the data; encrypted local storage on the phone, excluded from device backups. This is the control that limits the damage when something else fails — a stolen backup, a lost phone or an intercepted connection yields unreadable data rather than a breach. It's also explicitly expected by HIPAA and GDPR, and it's what makes the difference between a reportable breach and a non-event. Third because it protects the data itself, but doesn't help against an attacker who is properly authenticated.

**4. Audit logging that cannot be altered.**
Record every access, change and message — who, what, when, from where — in an append-only store the application can't rewrite. This is a legal requirement in healthcare, not just good practice: HIPAA requires you to know who looked at a record. It's also the only way to detect insider misuse (staff browsing a celebrity's or an ex-partner's file), to answer "what exactly was taken" after an incident, and to resolve disputes about what was said. Fourth because it doesn't *prevent* attacks — but without it you can't detect, investigate or prove anything, and every earlier control becomes unverifiable.

**5. Mobile client hardening and safe data handling.**
Content stripped from push notifications, screenshots blocked on record and message screens, short auto-logout, jailbreak/root detection, no sensitive data in logs or crash reports, and no personal health data used in test environments. The phone is the part of the system you don't control — it gets lost, shared, backed up to personal cloud accounts and left unlocked on tables. Fifth because it addresses real, frequent, low-effort exposure routes, but the failures are usually one patient at a time rather than system-wide.

**Just below the line, and worth naming:** securing the hospital-system integration. Those connections are often older, trusted by default, and given broad access — a weak link there can bypass everything above. Treat the hospital integration as its own trust boundary with its own authentication, its own minimum permissions, and its own audit trail.
