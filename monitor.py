import requests
from datetime import datetime

URLS = ["https://google.com", "https://github.com", "https://site-que-nao-existe.com"]

def check_endpoints():
    # Pega a data e hora atual e formata para ficar legível
    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"--- Iniciando monitoramento em: {agora} ---")
    
    for url in URLS:
        try:
            response = requests.get(url, timeout=5)
            print(f"Site: {url} | Status: {response.status_code}")
        except requests.exceptions.RequestException:
            print(f"Site: {url} | ERRO: Fora do ar ou inacessível")

if __name__ == "__main__":
    check_endpoints()