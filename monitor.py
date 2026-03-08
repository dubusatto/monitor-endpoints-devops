import requests

# Adicionamos uma URL falsa para forçar e testar o erro
URLS = ["https://google.com", "https://github.com", "https://site-que-nao-existe.com"]

def check_endpoints():
    for url in URLS:
        try:
            # O timeout evita que o script fique travado para sempre esperando
            response = requests.get(url, timeout=5)
            print(f"Site: {url} | Status: {response.status_code}")
        except requests.exceptions.RequestException:
            # Se o site não existir ou der timeout, cai aqui e o script continua
            print(f"Site: {url} | ERRO: Fora do ar ou inacessível")

if __name__ == "__main__":
    check_endpoints()