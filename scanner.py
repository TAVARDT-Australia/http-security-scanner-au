#!/usr/bin/env python3
import sys
import urllib.request
import urllib.error
from urllib.parse import urlparse

SECURITY_HEADERS = [('Strict-Transport-Security', 'Enforces HTTPS encryption and prevents SSL-stripping and downgrade attacks.'), ('Content-Security-Policy', 'Restricts unauthorized script execution and mitigates Cross-Site Scripting (XSS).'), ('X-Frame-Options', 'Prevents clickjacking by controlling framing and iframe permissions.'), ('X-Content-Type-Options', 'Blocks MIME-sniffing vulnerabilities in client web browsers.'), ('Referrer-Policy', 'Protects sensitive URL path parameters from leaking to external origins.'), ('Permissions-Policy', 'Applies least-privilege control to browser hardware interfaces and sensors.')]

def scan_target(target_url):
    print(f"\n[TAVARDT Australia] Starting HTTP security headers perimeter audit for: {target_url}\n")
    try:
        req = urllib.request.Request(
            target_url,
            headers={"User-Agent": "TAVARDT-Security-Scanner/3.0 (en-AU)"}
        )
        with urllib.request.urlopen(req, timeout=12) as response:
            headers = dict(response.headers.items())
            
            score = 0
            total = len(SECURITY_HEADERS)
            
            for header_name, desc in SECURITY_HEADERS:
                found = any(h.lower() == header_name.lower() for h in headers.keys())
                if found:
                    print(f"  [PASS] {header_name}")
                    score += 1
                else:
                    print(f"  [FAIL] {header_name}: {desc}")
                    
            print(f"\n[TAVARDT Australia] Audit Score: {score}/{total}")
            print(f"\nFull online diagnostic tool: https://tools.tavardt.com/au/security-headers-check/")
            print(f"Corporate cyber resilience and consulting: https://ag.tavardt.com/au/cybersecurity/\n")
            
    except urllib.error.URLError as e:
        print(f"[TAVARDT Australia] Error inspecting target: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scanner.py <URL>")
        sys.exit(1)
        
    url = sys.argv[1].strip()
    if not urlparse(url).scheme:
        url = "https://" + url
        
    scan_target(url)
