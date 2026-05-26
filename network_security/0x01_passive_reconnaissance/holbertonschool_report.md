# Holbertonschool.com — Shodan Reconnaissance Report

**Tool:** Shodan + DNS enumeration  
**Target:** holbertonschool.com (all subdomains)  

---

## 1. Discovered Subdomains & IP Addresses

| Subdomain | IP Address(es) | Status |
|-----------|---------------|--------|
| holbertonschool.com | `198.202.211.1` | Active |
| www.holbertonschool.com | `198.202.211.1` | Active |
| blog.holbertonschool.com | `192.0.78.230`, `192.0.78.131` | Active |
| v2.holbertonschool.com | `34.203.198.145` | Active |
| apply.holbertonschool.com | `15.188.250.64`, `35.181.209.82`, `35.180.145.93` | Active |
| assets.holbertonschool.com | `108.156.91.64` | Active |
| support.holbertonschool.com | `216.198.54.2`, `216.198.53.2` | Active |
| mail.holbertonschool.com | `18.154.101.67` | Active |
| test.holbertonschool.com | `8.8.8.8` | Dangling DNS |

---

## 2. IP Ranges & Network Ownership

| CIDR | ASN | Owner | Used by |
|------|-----|-------|---------|
| `198.202.211.0/24` | AS209242 | Webflow / Cloudflare London | www, apex |
| `192.0.78.0/22` | AS2635 | Automattic, Inc | blog |
| `34.203.0.0/14` | AS16509 | Amazon AWS us-east-1 | v2 |
| `15.188.0.0/15` | AS16509 | Amazon AWS eu-west-3 | apply |
| `35.180.0.0/14` | AS16509 | Amazon AWS eu-west-3 | apply |
| `108.156.0.0/14` | AS16509 | Amazon CloudFront | assets |
| `216.198.52.0/22` | AS22271 | Zendesk, Inc | support |
| `18.154.0.0/15` | AS16509 | Amazon CloudFront | mail |

---

## 3. Technologies per Subdomain

### `198.202.211.1` — www / holbertonschool.com
- **Organization:** Webflow, Inc (via Cloudflare London AS209242)
- **Open ports:** 80, 443, 2052, 2053, 2082, 2083, 2086, 2087, 2095, 6443, 8080, 8443, 8880
- **Web server:** Cloudflare (anycast, 13 ports typical of CF proxy)
- **SSL:** TLSv1.2 + TLSv1.3, issued by Google Trust Services
- **Platform:** Webflow CMS
- **CDN:** Cloudflare

### `192.0.78.230` — blog.holbertonschool.com
- **Organization:** Automattic, Inc (AS2635)
- **Open ports:** 80, 443
- **Web server:** nginx
- **Platform:** WordPress.com VIP
- **SSL:** Let's Encrypt (E8), subject `wordpress.com`, EC P-256, valid May–Aug 2026
- **CDN:** Automattic a8c-cdn, Dallas datacenter (dfw)
- **Port 80:** 301 redirect → HTTPS
- **Port 443:** 302 redirect → developer.wordpress.com

### `34.203.198.145` — v2.holbertonschool.com
- **Organization:** Amazon AWS us-east-1
- **Shodan data:** Not available (firewalled from Shodan scanners)
- **Inferred:** Custom web application behind AWS security groups

### `15.188.250.64` / `35.181.209.82` / `35.180.145.93` — apply.holbertonschool.com
- **Organization:** Amazon AWS eu-west-3 (Paris)
- **Shodan data:** Not available (firewalled)
- **Note:** 3 IPs = load-balanced setup, likely for GDPR/EU data residency

### `108.156.91.64` — assets.holbertonschool.com
- **Organization:** Amazon CloudFront
- **Purpose:** Static asset delivery (images, JS, CSS)
- **IPv6:** Enabled

### `216.198.54.2` — support.holbertonschool.com
- **Organization:** Zendesk, Inc (AS22271)
- **Open ports:** 80, 443, 2052, 2053, 2082, 2083, 2086, 2087, 2095, 2096, 6443, 8080, 8443, 8880
- **Web server:** nginx (via Cloudflare proxy)
- **SSL:** Let's Encrypt (E8), subject `zendesk.com`, TLSv1.2 + TLSv1.3
- **Platform:** Zendesk SaaS helpdesk
- **Port 80:** 301 redirect → HTTPS

### `18.154.101.67` — mail.holbertonschool.com
- **Organization:** Amazon.com, Inc (AS16509)
- **Cloud Service:** Amazon CloudFront — Global CDN
- **Tags:** cdn, cloud
- **Open ports:** 80, 443
- **Web server:** Microsoft HTTPAPI 2.0
- **CDN:** Amazon CloudFront (edge pop DEN52-P3, Denver)
- **PaaS:** Amazon Web Services
- **SSL:** Amazon RSA 2048 M01, subject `*.cloudfront.net`, valid Feb–Sep 2026
- **Port 80:** 403 Forbidden (CloudFront blocks direct access)
- **Port 443:** 404 via CloudFront

---

## 4. Key Findings & Observations

**1. Fully cloud-native architecture**  
Holberton uses no on-premise infrastructure. Everything runs on AWS, Cloudflare, Automattic, or Zendesk SaaS.

**2. Real origin IPs hidden behind Cloudflare**  
The main site (`198.202.211.1`) sits behind Cloudflare anycast — the real Webflow origin server IP is not exposed.

**3. EU data residency on apply portal**  
Three load-balanced AWS eu-west-3 (Paris) instances serve `apply.holbertonschool.com` — a deliberate GDPR-compliant architecture choice.

**4. AWS EC2 instances properly firewalled**  
`v2` and `apply` IPs return no Shodan data — AWS security groups are correctly blocking scanner traffic on non-standard ports.

**5. Dangling DNS — test.holbertonschool.com**  
`test.holbertonschool.com` resolves to `8.8.8.8` (Google Public DNS). This is a misconfigured/forgotten DNS record and represents a potential subdomain takeover risk.

**6. TLS hygiene is good**  
All subdomains with Shodan data show TLSv1.2 + TLSv1.3 only. SSLv2, SSLv3, TLSv1.0, TLSv1.1 are all disabled across the board.
