# Threat Model — IoT Smart Thermostat

**Device:** connects to home Wi-Fi · controls heating/cooling · collects temperature data · takes commands from a mobile app · updates its own firmware over the air

**The core difference from a web app:** a website lives on servers you own, in a building you control, and you can patch it in five minutes. A thermostat lives on a wall in a stranger's house for ten years, has no screen worth speaking of, no security team, and belongs to someone who will never think about it again after installation day. Every threat below flows from that.

---

## 1. Five IoT-Specific Threats

### 1. Physical access to the device itself

Anyone who can reach the wall — a guest, a tenant, a contractor, a previous owner, or the buyer of a second-hand unit on eBay — can open the case, attach wires to the circuit board and read the chips directly. Web apps simply don't have this problem: attackers can't walk up to a data centre rack with a screwdriver.

**Why it matters:** physical access defeats most software protections, and it only has to work once. An attacker buys one unit, takes it apart at home with no time pressure and no risk of being noticed, and whatever they learn applies to every identical device in the world.

### 2. Weak or shared default credentials

Devices ship with a default password like `admin/admin`, or — far worse — with the *same* key or password baked into every unit off the production line. Most owners never change it, and many devices don't let them.

**Why it matters:** search engines like Shodan index internet-exposed devices, so attackers don't scan for victims, they look them up. This is precisely how the Mirai botnet assembled hundreds of thousands of devices: it tried a list of about sixty default passwords. A web app can force a password change at first login; a thermostat with three buttons often can't.

### 3. Unpatchable, long-lived firmware

The software is burned into the device and expected to run for a decade or more. The vendor may stop issuing updates after two years, or go out of business entirely. Owners aren't notified about vulnerabilities and wouldn't act on them if they were. Devices sit powered off in a cupboard for months and come back online running ancient code.

**Why it matters:** a known vulnerability in a website is fixed the day it's found. The same vulnerability in a thermostat stays exploitable for years across millions of units, and there is no mechanism to force the fix. The population of vulnerable devices *grows* over time instead of shrinking.

### 4. Unencrypted or weakly protected local communication

Constrained hardware tempts vendors into skipping proper encryption, or into using it badly — no certificate checking, hardcoded keys, plain HTTP for the "unimportant" telemetry channel, or a wide-open local API on the home network so the mobile app can talk to it without the cloud.

**Why it matters:** anyone on the same Wi-Fi — a guest, a neighbour with the shared password, a compromised laptop — can then read or forge commands. And unlike a browser, which shouts about a bad certificate, a thermostat fails silently: neither the device nor the owner has any way to notice a machine-in-the-middle.

### 5. Physical-world consequences and safety impact

A compromised website leaks data. A compromised thermostat changes the temperature of a real house. Turn the heating off in a family's home during a February cold snap and pipes freeze and burst; do it at scale and you cause serious damage across a region. Turn heating to maximum in summer with vulnerable occupants inside and you have a health emergency. Cycle the HVAC compressor rapidly and you physically destroy expensive equipment.

**Why it matters:** the harm is measured in property damage, energy bills and human safety, not in leaked records. It also can't be undone with a password reset. Coordinated attacks across many devices can even manipulate demand on the electricity grid.

### Also genuinely IoT-specific, worth a mention

- **Privacy through side channels.** Temperature data reveals occupancy patterns: when you leave, when you sleep, when the house is empty for a fortnight. That's burglary reconnaissance derived from data nobody thinks of as sensitive.
- **A foothold on the home network.** The thermostat sits *inside* the firewall alongside laptops, NAS drives and cameras. Compromising it gives an attacker a permanent, always-on position on a trusted network — and it's the least-monitored device on it.
- **No user interface for security.** No screen for a warning, no way to see who's connected, no log the owner can read, often no way to know the device has been compromised at all.
- **Supply chain and end-of-life.** Third-party chips and firmware libraries the vendor never audited; devices resold or discarded with credentials and Wi-Fi passwords still inside.

---

## 2. Physical Access: The Attack Chain

The attacker's goal usually isn't *this one* thermostat. It's to extract the secrets and understand the design well enough to attack every device of that model remotely, at scale. One unit bought online funds an attack on all of them.

### Step 1 — Open the case and find the debug ports

Most devices have manufacturing and debugging connections left on the board: **UART** (a serial console, often just four solder pads) and **JTAG/SWD** (direct control of the processor). They exist because engineers need them in the factory and are frequently left enabled in shipped products.

*What the attacker gets:* UART often drops straight into a root shell or a boot log full of useful detail — no password, no exploit needed. JTAG allows halting the processor, reading memory live and stepping through code.

### Step 2 — Extract the firmware

If the ports are locked, the attacker desolders the flash memory chip (or clips onto it in place) and reads it with a cheap programmer. This is a €20 tool and a YouTube tutorial, not a state-level capability.

*What the attacker gets:* the complete firmware image — the actual code running on every unit of that model.

### Step 3 — Analyse it offline

At home, unhurried and undetectable, they unpack the image and read it: hardcoded passwords and API keys, encryption keys, cloud endpoint URLs, certificates, the update mechanism, and the code itself, where memory-safety bugs can be hunted at leisure.

*What the attacker gets:* the device's secrets — and if the vendor used the same key across the product line, everyone's secrets.

### Step 4 — Modify and reflash

Firmware is patched to add a backdoor or disable security checks, then written back to the chip. Without **secure boot**, the device happily runs it. A tampered unit can be returned to a shop, resold, or installed in a target's home.

*What the attacker gets:* a device that looks and behaves completely normally while under someone else's control.

### Step 5 — Pivot to the network and the cloud

The extracted Wi-Fi credentials open the home network. The extracted cloud credentials open the vendor's back end — and if the API trusts device identity without checking *which* device is asking, one stolen identity may be enough to read or command other people's thermostats.

*What the attacker gets:* remote access to a home network, and potentially a path to the entire installed fleet.

### Impacts

- **Fleet-wide compromise.** One shared key, extracted once, breaks every device ever sold. This is the outcome that actually matters.
- **Home network intrusion.** Wi-Fi password in hand, plus a permanent listening post inside the firewall.
- **Physical harm.** Heating disabled in winter (burst pipes, uninhabitable house), heating maxed in summer, HVAC equipment destroyed by rapid cycling.
- **Surveillance.** Occupancy patterns leaked; a device that knows when the house is empty.
- **Botnet recruitment.** Thousands of always-on devices assembled for DDoS attacks.
- **The owner never knows.** No screen, no log, no indication. Compromise is indefinite.

### Countermeasures

Physical access can never be fully prevented — it can only be made expensive and made useless:

- **Disable or lock debug ports in production** (blow the JTAG fuse, require authentication on UART, remove the pads from the shipped board).
- **Encrypt the flash, and store keys in a secure element or TPM** so reading the chip yields ciphertext rather than secrets.
- **Give every device its own unique keys**, provisioned at manufacture. This is the single most important control: it caps the damage from one extracted device at exactly one device.
- **Secure boot** so modified firmware refuses to run.
- **Server-side device identity checks** — the cloud verifies not just that *a* valid device is calling, but that this device is asking about its own data, with the ability to revoke a device instantly.
- **Tamper evidence** (seals, case-open detection that wipes keys) and a factory reset that genuinely erases Wi-Fi credentials and keys before resale.

---

## 3. Securing the Over-The-Air (OTA) Update Process

OTA updates are the most dangerous feature in the device, because they are the one legitimate path to replacing all its software remotely. If an attacker controls updates, they control the entire installed base at once — and permanently. It is also the *only* way to fix vulnerabilities across millions of devices, so it can't be removed. It must simply be right.

### The essential requirements

**1. Code signing — non-negotiable, the foundation.**
The vendor signs each firmware image with a private key held offline (ideally in a hardware security module). Each device holds only the matching public key and installs nothing without a valid signature. This is what makes the device trust *the vendor*, rather than *whoever is talking to it right now*. Without it, every other control is decoration.

**2. Secure boot — verification at every start-up.**
Signatures are checked again each time the device powers on, in a chain anchored in read-only hardware. This closes the gap where an attacker with physical access writes firmware directly to the flash chip, bypassing the update process entirely. Signing proves the update was genuine; secure boot proves the *running* code still is.

**3. Encrypted, authenticated download channel.**
Fetch updates over TLS with proper server certificate verification (ideally pinned), never plain HTTP. Encryption protects the image's contents from analysis, and — more importantly — verifying the server's identity stops an attacker on the home network from redirecting the device to their own update server. Note the division of labour: TLS protects the *delivery*; signing protects the *content*. You need both, and signature checks must happen on the device even if the channel was secure.

**4. Rollback protection (anti-downgrade).**
Every image carries a version number that only moves forward, enforced by a counter the device can't decrease. Otherwise an attacker simply installs a genuine, correctly signed, *old* firmware with a known vulnerability — a perfectly valid signature on a deliberately broken version. Old signing keys and images for known-vulnerable versions should also be revocable.

**5. Atomic updates with automatic recovery.**
Use two firmware slots: write the new image to the inactive slot, verify it fully, then switch over — and if the new firmware doesn't confirm it booted successfully, fall back automatically to the previous slot. Power cuts and dropped Wi-Fi happen constantly in real homes. A half-written update produces a dead thermostat, which in winter is a safety problem and in fleet terms is a mass outage the vendor cannot fix remotely.

**6. Integrity and target checks before installing.**
Verify a hash of the complete image, and check that the update is actually intended for this hardware model and version. This catches corrupted downloads and prevents an image for a different product from bricking the device.

### Supporting practices

- **Device-initiated updates.** The device asks the server whether an update exists, rather than accepting pushed connections. This removes the need for any inbound listening port.
- **Staged rollout.** Ship to 1%, then 10%, then everyone, watching failure rates. A bad update pushed to 100% at once is a self-inflicted fleet-wide outage.
- **Protect the build pipeline.** The signing key is the crown jewel: offline or HSM-held, multi-person approval to use, and a documented plan for rotating it if it's ever exposed. A stolen signing key means attacker firmware that every device accepts as genuine — the worst outcome in the entire system.
- **Fail safe, not open.** If verification fails, the device keeps running its current firmware and reports the failure. It must never "try installing it anyway."
- **Keep the heating working.** Whatever goes wrong with an update, the device should retain basic local thermostat function without the cloud. A house shouldn't go cold because a server is down.

### In one line

> Signed by the vendor, delivered over a verified channel, checked again at every boot, never downgradable, and safely reversible if it fails.
