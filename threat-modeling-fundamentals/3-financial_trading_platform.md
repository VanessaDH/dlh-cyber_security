# Threat Model — Financial Trading Platform

**System:** real-time prices · buy/sell orders · fund transfers · automated trading rules
**Requirements:** 99.99% uptime · under 100ms per trade · SEC and FINRA compliance

---

## 1. CIA Priority, and the Conflict with Performance

The **CIA Triad** describes what "secure" means: **C**onfidentiality (only the right people see it), **I**ntegrity (it's correct and unaltered), **A**vailability (it's there when needed).

### Integrity comes first

In trading, integrity means: the order you placed is the order that executed, at the price shown, for the quantity you chose, against your balance and nobody else's — and the record of it can't be rewritten afterwards.

Compare the three failure modes by how bad the worst day looks:

| Failure | What actually happens |
|---|---|
| **Confidentiality breach** — positions and personal data leak | Serious: reputational damage, regulatory penalties, users exposed to targeted fraud. But the money is still there and the ledger is still correct. |
| **Integrity breach** — balances, orders or trade records altered | Catastrophic: money is created, destroyed or moved. Prices displayed can be manipulated to induce bad trades. Worst of all, **you can no longer trust your own records**, so you can't even determine the correct state to restore. Trades are legally binding and often irreversible once they hit the market. |
| **Availability outage** — platform down | Very bad: users can't exit positions in a falling market, real losses accumulate, and regulators will want an explanation. But when it comes back the records are intact and losses can be identified and compensated. |

The decisive point is *recoverability*. A leak is permanent but doesn't corrupt the system. An outage is painful but temporary. Corrupted financial records are both permanent **and** leave you unable to reconstruct the truth — and SEC/FINRA rules (notably the requirement to keep records in unalterable, write-once form) exist precisely because regulators consider record integrity the foundation everything else stands on. Without integrity you're not a regulated broker; you're an unauditable business.

**Availability is a close second** — much closer than in most systems. A trading platform that is down during a crash inflicts direct, quantifiable financial harm on users who can't sell, which is why 99.99% (under an hour of downtime per year) is a stated requirement rather than an aspiration. **Confidentiality is third** — genuinely important, and non-public order flow is valuable enough to front-run, but a leak doesn't stop you operating or destroy the truth.

> **Priority: Integrity → Availability → Confidentiality.**

### Yes, security and performance genuinely conflict

The 100ms budget is small, and every security control spends some of it. This is a real engineering tension, not a talking point:

- **Multi-factor authentication** adds seconds — unacceptable on every order, essential on withdrawals.
- **Fraud and anomaly checks** need to look at history and patterns; done synchronously on the order path, they blow the budget.
- **Encryption and signing** cost CPU time on every message.
- **Full synchronous audit logging** to durable, tamper-proof storage adds latency to each write.
- **Rate limiting and bot detection** add a hop and can throttle legitimate high-frequency users.
- **Strict replication** for consistency across data centres costs round trips — and the alternative, relaxed consistency, is exactly what lets the same balance be spent twice.

**How the conflict is actually resolved:** stop treating "security" as one uniform cost and separate the checks that *must* happen before the action from the ones that can happen alongside it.

- **Authenticate once, cheaply, per session** — heavy identity verification at login and at high-risk moments, then a fast token check per order. Not MFA on every trade.
- **Match the control to the risk.** Placing a €500 order is low-risk and fast-path. Withdrawing €50,000 to a new bank account is high-risk: add MFA, add a delay, add manual review. Nobody's latency requirement covers withdrawals.
- **Keep synchronous checks to the ones that prevent unrecoverable harm** — authentication, ownership, balance/margin sufficiency, position limits. These are simple, in-memory and cheap.
- **Run detection asynchronously.** Anomaly scoring, pattern analysis and compliance surveillance happen on a parallel stream that can flag, freeze or reverse within seconds — without sitting in the order path.
- **Write audit logs to a fast append-only stream** that is durable immediately and archived to write-once storage afterwards.
- **Precompute and cache** permissions, limits and risk profiles rather than recalculating them per request.

The honest summary: you can meet 100ms *and* be secure, but only by deciding deliberately which checks block the trade and which ones run beside it — and by refusing to apply the latency budget to money leaving the platform.

---

## 2. Threat Model: Automated Trading Rules

This feature is uniquely dangerous because it removes the human from the loop. A rule like *"if TSLA drops below €200, buy 500 shares"* executes at machine speed, repeatedly, with no one watching — often while the user is asleep. Every other feature requires the attacker to act; this one lets them set a trap and walk away.

### Risk 1 — Unauthorised creation or modification of rules

**The threat:** an attacker with access to the account (stolen session, phished credentials, an API key leaked in a GitHub repo, or a permissions bug letting them edit another user's rules) creates or quietly edits automated rules. The most effective version is subtle: not "sell everything," but a small change to an existing rule's threshold or quantity that the owner won't notice for weeks.

**Why it's the top risk:** rule changes are usually treated as *settings*, not as *transactions* — so they typically bypass the extra checks applied to trades and withdrawals. Yet a rule is a standing instruction to move money. It's also the ideal tool for **market manipulation**: an attacker holding a position in a thinly traded stock modifies many compromised accounts' rules to buy it automatically, pushing the price up so they can sell into it.

**Mitigation:**
- Treat rule changes as high-risk actions, not settings: re-authenticate, require MFA to create or modify a rule, and notify the user through a separate channel (email/SMS) on every change — including "no changes were made this week" summaries so silence isn't ambiguous.
- Add a **cooling-off delay** before a new or modified rule becomes active (e.g. 15–60 minutes), during which the user can cancel. This single control defeats most smash-and-grab account takeovers, because attackers don't wait around.
- Enforce ownership checks server-side on the specific rule ID, every time — never trust a rule ID supplied by the client.
- Version every rule with a full history: who changed it, when, from where, what the old and new values were.
- Cap what any rule can do, independently of what the rule says: maximum order size, maximum daily spend, maximum position concentration in one instrument.

### Risk 2 — Race conditions and repeated execution

**The threat:** the same rule fires multiple times before the system registers that it already executed. A price oscillates around the trigger threshold and the rule fires on every crossing; or two servers process the same market tick simultaneously and both place the order; or the balance check and the order placement aren't atomic, so ten concurrent orders each pass a balance check for funds that only cover one.

**Why it's serious:** this is a *self-inflicted* wound that needs no attacker — and it's actively made more likely by the low-latency architecture, because speed pushes you towards parallel processing and relaxed consistency, which is precisely where duplicate execution lives. An attacker who understands the timing can deliberately trigger it. Historically, this class of bug has bankrupted trading firms in minutes (Knight Capital lost roughly $440m in 45 minutes to a runaway automated system).

**Mitigation:**
- **Idempotency keys**: each rule evaluation produces a unique key, and the order system rejects duplicates. If the same key arrives twice, the second is a no-op.
- **Atomic check-and-reserve**: verify funds and reserve them in a single database transaction with proper row locking, so ten concurrent orders cannot all pass the same balance check.
- **Locking per rule** — only one evaluation of a given rule may run at a time, cluster-wide.
- **Cooldowns and hysteresis**: after firing, a rule is dormant for a defined period, and the trigger price to re-arm is meaningfully different from the trigger price to fire — this stops oscillation around a threshold.
- **Circuit breakers**: automatic suspension of a rule (and alerting) if it fires more than N times in a window, or if total automated volume exceeds a per-account threshold.
- **A kill switch** — global and per-account — that halts all automated trading instantly, with defined criteria and rehearsed use.

### Risk 3 — Logic flaws and unsafe rules the system accepts

**The threat:** the rule engine accepts inputs it shouldn't, or behaves unexpectedly at the edges. Negative or fractional quantities. A rule that buys triggering a rule that sells triggering the first rule again — an infinite loop. Rules that reference stale or unavailable price data and fire on a bad tick. Rules that behave one way in normal conditions and catastrophically during a market halt, a stock split, or a gap opening. Contradictory rules that fight each other, racking up fees and slippage.

**Why it's serious:** the harm arrives at full speed with nobody watching, and it can be triggered without any account compromise at all — the attacker just needs to understand your engine, which they can learn from a free demo account. It's also the hardest category to detect in testing, because the failure only appears in market conditions your test data didn't contain.

**Mitigation:**
- **Strict validation and safe limits** on every rule: positive integer quantities, sane price bounds, a maximum number of active rules, and a hard cap on notional value per rule and per account per day.
- **Cycle detection**: analyse the rule set as a graph and reject configurations where rules can trigger each other in a loop.
- **Data quality gates**: refuse to act on stale, missing or implausible prices (a tick far outside recent range is treated as bad data, not as an opportunity). Pause automation during market halts and around corporate actions.
- **Mandatory simulation** — backtest and dry-run every new rule against historical and stressed market data, and show the user what it would have done, before it goes live.
- **Independent pre-trade risk checks** in a separate service from the rule engine, so a bug in the engine doesn't disable its own safety limits. This separation is a regulatory expectation (SEC Rule 15c3-5, the "market access rule"), not just good design.
- **Real-time surveillance** with automatic suspension on abnormal patterns, plus a full audit trail of every evaluation — inputs, decision and outcome — so any incident can be reconstructed exactly.

---

## 3. Defence in Depth After an Account Compromise

**Defence in depth** means assuming any single control will eventually fail, and layering others behind it so a breach becomes an inconvenience rather than a disaster. Here the assumption is explicit: *the attacker is logged in as a legitimate user.* Authentication has already failed. Every layer below is designed to work anyway.

The attacker's realistic goals, in order of value to them: move money out, sell the victim's positions and buy something they can profit from, plant automated rules for later, or harvest data.

### Layer 1 — Step-up authentication on high-risk actions

Being logged in gets you a session, not permission to do anything. Withdrawals, adding a new payout destination, changing contact details, creating automated rules and unusually large orders each require fresh authentication — MFA, ideally a hardware key or app-based approval rather than SMS.

*Why first:* it directly blocks the attacker's primary goal. A hijacked session that can browse and place small trades is a fraction of the damage of one that can wire funds out. Crucially, this defends against **session hijacking**, where the attacker never had the password at all.

### Layer 2 — Transaction limits and withdrawal friction

Hard caps regardless of who's asking: per-transaction, daily and rolling limits on withdrawals, order size and total exposure. New payout destinations are subject to a mandatory **holding period** (24–48 hours) before they can be used, with out-of-band notification when one is added. Cooling-off delays on newly created automated rules.

*Why:* fraud is a race — attackers need the money out before anyone notices. Time is the defence. Nearly every attacker abandons an account that won't pay out today, and the delay is exactly the window in which the real user sees the alert and the fraud team acts. Legitimate users are barely inconvenienced, because genuine large withdrawals are rarely urgent to the minute.

### Layer 3 — Behavioural anomaly detection

Continuous scoring of what the account is doing against what it normally does: logging in from a new country or device, a sudden change of trading style, liquidating a long-held portfolio, trading illiquid penny stocks for the first time, activity at 04:00 for someone who trades at lunchtime, or a spike in API calls. High scores trigger step-up authentication, temporary holds or a freeze.

*Why:* this is the layer that catches attacks the static rules didn't anticipate, and it works even when the attacker's every individual action is technically permitted. Run it asynchronously so it doesn't sit inside the 100ms path — it can still act within seconds.

### Layer 4 — Session management and API key hygiene

Short session lifetimes with idle timeout; tokens bound to device and client characteristics so a stolen token fails elsewhere; a fresh session identifier issued at login; visible active-session list with one-click "log out everywhere"; concurrent sessions from distant locations blocked or challenged. API keys are separate credentials with their own **scopes** (read-only by default; trading and withdrawal permissions granted explicitly and separately), IP allowlisting, and rotation.

*Why:* it shrinks the attacker's window and stops one leaked credential becoming unlimited access. A read-only API key leaked to a public repo should never be able to move money — and scoping is what guarantees that rather than hoping.

### Layer 5 — Immutable audit trails and real-time alerting to the user

Every action recorded in append-only, write-once storage the application cannot rewrite: who, what, when, from which device and IP. Simultaneously, the user is told what's happening through a channel the attacker doesn't control — email and SMS on login from a new device, on any withdrawal or payout-destination change, and on every automated rule change.

*Why:* the audit trail is a legal requirement (SEC 17a-4 write-once record retention) and the only way to determine afterwards exactly what happened, which trades to unwind and who bears the loss. The out-of-band alerting is what turns a slow, silent, weeks-long compromise into a fifteen-minute one — the real user is usually the fastest detector you have, provided you actually tell them.

### Supporting layers worth naming

- **Network and edge controls** — DDoS protection, rate limiting, bot detection, credential-stuffing defences at the front door.
- **Least privilege inside the system** — services and staff get the minimum access needed; no support tool should be able to initiate a withdrawal unilaterally. Insider abuse is a real threat class in trading platforms.
- **Segregated, verified fund flows** — withdrawals only to pre-verified accounts in the user's own name, with dual approval above a threshold.
- **Reconciliation** — automated daily comparison of internal ledgers against custodian and bank records; a mismatch is the tamper alarm that catches what everything above missed.
- **Incident response and reversibility** — a rehearsed procedure to freeze an account, cancel open orders, void automated rules and unwind fraudulent trades, with defined authority to act in minutes rather than hours.

### In one line

> Assume the attacker is logged in — then make sure they still can't move money quickly, can't act invisibly, and can't do anything you can't undo.
