#!/usr/bin/env python3
import sys
import urllib.request
import urllib.error
from urllib.parse import urlparse

SECURITY_HEADERS = [('Strict-Transport-Security', 'Enforces HTTPS transport encryption and prevents downgrade tampering (HSTS).'), ('Content-Security-Policy', 'Mitigates Cross-Site Scripting (XSS) and unauthorized code execution.'), ('X-Frame-Options', 'Protects against clickjacking attacks by regulating framing behavior.'), ('X-Content-Type-Options', 'Blocks MIME-sniffing attacks in client browsers.'), ('Referrer-Policy', 'Restricts referrer information leakage to external web origins.'), ('Permissions-Policy', 'Enforces least-privilege access for browser hardware capabilities.')]

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
            print(f"\nVerificacao completa online: https://tools.tavardt.com/au/security-headers-check/")
            print(f"Suporte corporativo e ciberdefesa: https://ag.tavardt.com/au/cybersecurity/\n")
            
    except urllib.error.URLError as e:
        print(f"[TAVARDT Australia] Erro ao inspecionar o alvo: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scanner.py <URL>")
        sys.exit(1)
        
    url = sys.argv[1].strip()
    if not urlparse(url).scheme:
        url = "https://" + url
        
    scan_target(url)
