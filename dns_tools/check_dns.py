cd ~/byword-intake-api
mkdir -p dns_tools
nano dns_tools/check_dns.py
# dns_tools/check_dns.py
import socket

domains = [
    "bywordofmouthlegal.ai",
    "www.bywordofmouthlegal.ai",
    "bywordofmouthlegal.com",
    "www.bywordofmouthlegal.com",
    "bywordofmouthlegal.help",
    "www.bywordofmouthlegal.help",
]

print("Checking DNS resolution...\n")
for domain in domains:
    try:
        ip = socket.gethostbyname(domain)
        print(f"{domain} resolves to {ip}")
    except socket.gaierror:
        print(f"❌ Failed to resolve {domain}")
