# HTTP Security Headers Scanner | TAVARDT Australia

[![Scope of Perimeter Verification](https://img.shields.io/badge/TAVARDT-Technical%20Audit-5b3cf5.svg)](https://tools.tavardt.com/au/security-headers-check/)
Automated technical audit of HTTP security headers aligned with ACSC Essential Eight Maturity Model and Australian Privacy Principles.

Developed and maintained by the cybersecurity and cyber resilience division of **TAVARDT Australia**.

***

## 1. Scope of Perimeter Verification

This command-line tool audits essential browser protection directives and secure transport configurations for Australian systems:

* **Strict-Transport-Security (HSTS):** Enforces HTTPS encryption and prevents SSL-stripping and downgrade attacks.
* **Content-Security-Policy (CSP):** Restricts unauthorized script execution and mitigates Cross-Site Scripting (XSS).
* **X-Frame-Options:** Prevents clickjacking by controlling framing and iframe permissions.
* **X-Content-Type-Options:** Blocks MIME-sniffing vulnerabilities in client web browsers.
* **Referrer-Policy:** Protects sensitive URL path parameters from leaking to external origins.
* **Permissions-Policy:** Applies least-privilege control to browser hardware interfaces and sensors.

***

## 2. Quick Start Guide

Run this tool directly via Python without installing third-party packages:

```bash
python scanner.py example.com.au
```

***

## 3. Online Diagnostic Tools (Australia)

Audit your public infrastructure using the TAVARDT Australia diagnostic suite:

* HTTP Security Headers Checker
* [Consent Mode v2 & Privacy Act Validator](https://tools.tavardt.com/au/consent-mode-v2-checker/)
* [DMARC & Anti-Spoofing Verifier](https://tools.tavardt.com/au/dmarc-checker/)
* [Exposed Credentials & Secret Scanner](https://tools.tavardt.com/au/exposed-files-scanner/)
* [Full Australian Tools Portal](https://tools.tavardt.com/au/)

***

## 4. Technical Advisory & Remediation

For enterprise ACSC Essential Eight alignment, penetration testing, and incident response in Australia, contact **TAVARDT Australia**.
