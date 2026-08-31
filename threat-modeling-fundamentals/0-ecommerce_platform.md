# Threat Model — E-Commerce Platform

**System:** React frontend · Node.js API · PostgreSQL database · Stripe payments
**Rules:** browsing and adding to cart are open to anyone; checkout and order history require login.

---

## 1. Three STRIDE Threats in Checkout

STRIDE is a checklist of six ways things go wrong: **S**poofing, **T**ampering, **R**epudiation, **I**nformation disclosure, **D**enial of service, **E**levation of privilege.

### Threat A — Tampering: the customer changes the price

| | |
|---|---|
| **Category** | Tampering |
| **What happens** | The web page in the browser sends the order to the server. If it also sends the price, the attacker can edit that message before it arrives and change €899 to €0.01. Anything the browser sends can be edited — the browser belongs to the attacker, not to you. |
| **Impact** | You ship real products for almost no money. Worse, it looks normal in your records, because the fake price is the price you saved. You may not notice until the accounts are reconciled weeks later. And it is easy to copy: one person finds it, then shares it. |
| **Fix** | Never accept a price from the browser. Accept only *which product* and *how many*, then look up the real price in your own database and calculate the total on the server. Tell Stripe that server-calculated amount. Only ship the goods after Stripe confirms — directly to your server — that the correct amount was actually paid. |

### Threat B — Information Disclosure: payment and personal data leak

| | |
|---|---|
| **Category** | Information Disclosure |
| **What happens** | Two versions. (1) Card numbers pass through your own server and end up written into log files or error reports, where they sit in plain text. (2) The connection isn't properly locked down, so someone on the same public Wi-Fi reads the customer's address, email and login cookie as it travels. |
| **Impact** | If card numbers ever touch your servers, your whole system falls under strict payment-industry rules (PCI-DSS) — expensive audits, fines, and possibly losing the ability to take card payments at all. Even without card numbers, leaked names and addresses are a data breach under GDPR, which you must report within 72 hours. |
| **Fix** | Use Stripe's own payment fields so the card number goes straight from the customer's browser to Stripe and never touches your server. Encrypt every connection (HTTPS everywhere, no exceptions). Automatically strip sensitive fields out of logs and error reports. Only return the data a page actually needs. |

### Threat C — Repudiation: no proof of who ordered what

| | |
|---|---|
| **Category** | Repudiation ("denying you did it") |
| **What happens** | A customer says "I never made that order." Your only record is a single row in the database that anyone with database access — a staff member, or an attacker — could have quietly edited. There is no separate, unchangeable record of who ordered, when, from where, and which Stripe payment it matched. |
| **Impact** | You lose payment disputes because you can't produce evidence. You can't tell real fraud apart from a customer lying. After a security incident you have no reliable timeline. Too many lost disputes and your payment provider can drop you. |
| **Fix** | Keep a separate log that can only be added to, never edited or deleted — user, time, IP address, what was in the cart, the Stripe payment reference. Store it somewhere the main application can't rewrite. Use 3-D Secure ("verified by your bank") where it applies, which also shifts liability for disputes to the bank. Compare your records against Stripe's every day; a mismatch is your alarm. |

**Also worth noting:** *Spoofing* — if the cart's ID stays the same after login, an attacker can slip their cart into a victim's session (fix: issue a fresh session ID at login). *Elevation of privilege* — if order history is fetched by order number without checking who owns it, any logged-in user can read everyone's orders (fix: always filter by the logged-in user in the query itself).

---

## 2. Trust Boundaries

A **trust boundary** is any line where data moves between two parts that trust each other differently. Every crossing needs checking — that's where security controls belong.

**1. Browser → your API.** The big one. The React app runs on the customer's machine, so they can change its code, its data and its requests. Treat everything arriving from it as possibly hostile: prices, quantities, user IDs, headers, all of it. Check identity, check permissions, and validate every field on arrival.

**2. Not-logged-in → logged-in.** This boundary sits inside your own app, and this design draws it clearly: browsing and cart are open, checkout and order history are not. At the crossing point, issue a new session ID, merge the guest cart carefully (a guest cart must not be able to attach itself to someone else's account), and re-check prices and stock, since they may have changed.

**3. API → PostgreSQL.** Only the API should be able to talk to the database, using credentials the customer never sees. Keep the database off the public internet, encrypt the connection, and give each part of the app only the access it needs — the product search should be able to read products and nothing else.

**4. Your system ↔ Stripe.** Data leaves your control here, in three directions: card details go browser → Stripe (deliberately skipping your server); your server calls Stripe using a secret key that must never reach the frontend; and Stripe calls *your* server back with payment confirmations ("webhooks"). That last one is a public address on the internet — if you don't verify Stripe's signature on those messages, anyone who finds the URL can mark any order as paid.

**5. Customer side ↔ staff/admin side.** Admin tools, refunds and the deployment pipeline operate at a higher trust level and need separate logins, multi-factor authentication and network separation. A refund button reachable with an ordinary customer login is the same problem as Threat A, only faster.

---

## 3. DREAD Rating — SQL Injection in Product Search

**SQL injection** means typing database commands into a normal input box (like a search bar) and having the database run them, because the code glued the user's text straight into its query.

**Assumption:** this rates the danger *if the flaw is present*. If the code uses parameterized queries (see the fix below), the risk is essentially zero.

| Factor | Score /10 | Why |
|---|---|---|
| **Damage** | 9 | Getting into one query means getting into the whole database — user accounts, password hashes, addresses, order history. Not a 10 only because card numbers live at Stripe, not in your tables. |
| **Reproducibility** | 10 | It works every single time. No luck, no timing, no special conditions — the same crafted text works from anywhere until the code is fixed. |
| **Exploitability** | 9 | **No login needed** — search is open to everyone, which is exactly what makes it the juiciest target here. Free tools (sqlmap) do the whole attack automatically; no real skill required. |
| **Affected users** | 10 | A database dump affects 100% of customers — including former ones whose data is still stored. |
| **Discoverability** | 9 | The search box is the most obvious input on any shop: visible on every page, in the URL, and probed by automated bots within hours of the site going live. It's usually the first thing anyone tests. |

**Average: 9.4 / 10 — Critical.** In plain terms: a stranger on the internet, with no account and a free tool, can take your entire customer database. This is a fix-before-launch finding.

**How to fix it (in order of importance):**

1. **Parameterized queries.** Send the user's text to the database as *data*, never as part of the command. This is the actual fix; everything below is a backup layer.
2. **Allowlists for sort options.** Things like "sort by price" can't be parameterized, so only accept values from a fixed, approved list.
3. **Minimum database permissions.** Let the search function read products only — so even a successful attack can't reach the user table.
4. **Generic error messages.** Never show database errors to visitors; those messages are what make an attack fast.
5. **Rate limiting and a web application firewall** — a speed bump against bots, never the main defence.
6. **A dedicated search index** (PostgreSQL full-text search, or Elasticsearch) so typed text never reaches a hand-built query at all.

**One honest caveat:** DREAD scores are subjective, and averaging opinion-based numbers implies more precision than really exists — two engineers will often disagree by a couple of points per factor. Microsoft itself retired the method for that reason. It's fine for ranking your own threats consistently against each other, which is what it's doing here. For anything shared outside the team, CVSS or the OWASP Risk Rating Methodology is easier to defend.
