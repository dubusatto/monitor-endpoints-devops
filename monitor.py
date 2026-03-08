import requests
from datetime import datetime

URLS = ["https://google.com", "https://github.com", "https://site-que-nao-existe.com"]
LOG_FILE = "monitor_log.txt"

def check_endpoints():
    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mensagem_inicio = f"--- Iniciando monitoramento em: {agora} ---\n"
    
    print(mensagem_inicio.strip())
    
    # Abre o arquivo em modo 'a' (append) para adicionar no final sem apagar o anterior
    with open(LOG_FILE, "a") as file:
        file.write(mensagem_inicio)
        
        for url in URLS:
            try:
                response = requests.get(url, timeout=5)
                resultado = f"Site: {url} | Status: {response.status_code}\n"
            except requests.exceptions.RequestException:
                resultado = f"Site: {url} | ERRO: Fora do ar ou inacessível\n"
            
            print(resultado.strip())
            file.write(resultado)
        
        file.write("\n") # Pula uma linha no final do bloco para organizar o arquivo

if __name__ == "__main__":
    check_endpoints()