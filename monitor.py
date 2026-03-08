import requests
from datetime import datetime

URLS = ["https://google.com", "https://github.com"]

def check_endpoints():
    print(f"--- Verificação iniciada em: {datetime.now()} ---")
    for url in URLS:
        try:
            response = requests.get(url, timeout=5)
            print(f"[OK] {url} - Status: {response.status_code}")
        except Exception as e:
            print(f"[ERRO] {url} - Falha: {e}")

if __name__ == "__main__":
    check_endpoints()