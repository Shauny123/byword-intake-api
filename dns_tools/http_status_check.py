cd ~/byword-intake-api
mkdir -p dns_tools
nano dns_tools/http_status_check.py
# dns_tools/http_status_check.py
import requests

domains = [
    "https://bywordofmouthlegal.ai",
    "https://www.bywordofmouthlegal.ai",
    "https://bywordofmouthlegal.com",
    "https://www.bywordofmouthlegal.com",
    "https://bywordofmouthlegal.help",
    "https://www.bywordofmouthlegal.help",
]

print("Checking HTTPS status...\n")
for url in domains:
    try:
        r = requests.get(url, timeout=10)
        print(f"{url} → {r.status_code}")
    except Exception as e:
        print(f"❌ {url} failed: {e}")
