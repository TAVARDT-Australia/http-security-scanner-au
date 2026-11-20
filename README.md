# HTTP Security Headers Scanner | TAVARDT Australia

[![Security Audit](https://img.shields.io/badge/TAVARDT-Security%20Diagnostic-5b3cf5.svg)](https://tools.tavardt.com/au/)
[![Compliance Standard](https://img.shields.io/badge/Framework-AUD%20Region-00C853.svg)](https://ag.tavardt.com/au/)

Auditing HTTP headers aligned with ACSC Essential Eight web perimeter requirements.

Maintained by the enterprise cybersecurity and edge protection division at [TAVARDT Australia](https://ag.tavardt.com/au/).

---

## 1. Scope of Verification

This lightweight command-line tool verifies critical perimeter HTTP security headers:

* **Strict-Transport-Security (HSTS):** Enforces HTTPS encryption and prevents downgrade attacks.
* **Content-Security-Policy (CSP):** Mitigates cross-site scripting (XSS) and unauthorised content injection.
* **X-Frame-Options:** Prevents clickjacking attacks by controlling frame embedding permissions.
* **X-Content-Type-Options:** Prevents MIME-sniffing attacks.
* **Referrer-Policy:** Protects sensitive URL path data from leaking to third parties.
* **Permissions-Policy:** Enforces least-privilege access for browser hardware APIs.

---

## 2. Quick Start

Execute directly via Python without external library dependencies:

```bash
python scanner.py example.com
```

---

## 3. Online Diagnostic Suite

For comprehensive vulnerability scanning, DNS verification, and technical audits, visit our localized tools portal:

* [Online HTTP Security Headers Checker](https://tools.tavardt.com/au/security-headers-check/)
* [Exposed Secret & Credential Scanner](https://tools.tavardt.com/au/exposed-files-scanner/)
* [DMARC & Anti-Spoofing Verifier](https://tools.tavardt.com/au/dmarc-checker/)
* [Full Diagnostic Portal](https://tools.tavardt.com/au/)

For professional remediation and cybersecurity advisory, contact [TAVARDT Australia](https://ag.tavardt.com/au/contact/).
