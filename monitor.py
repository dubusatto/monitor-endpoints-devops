import requests
from datetime import datetime

URLS = ["https://google.com", "https://github.com", "https://site-que-nao-existe.com"]
LOG_FILE = "monitor_log.txt"

# Códigos de cor ANSI para o terminal do Linux
VERDE = '\033[92m'
VERMELHO = '\033[91m'
RESET = '\033[0m'

def check_endpoints():
    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mensagem_inicio = f"--- Iniciando monitoramento em: {agora} ---\n"
    
    print(mensagem_inicio.strip())
    
    with open(LOG_FILE, "a") as file:
        file.write(mensagem_inicio)
        
        for url in URLS:
            try:
                response = requests.get(url, timeout=5)
                resultado_log = f"Site: {url} | Status: {response.status_code}\n"
                
                # Imprime verde no terminal
                print(f"{VERDE}Site: {url} | Status: {response.status_code}{RESET}")
            except requests.exceptions.RequestException:
                resultado_log = f"Site: {url} | ERRO: Fora do ar ou inacessível\n"
                
                # Imprime vermelho no terminal
                print(f"{VERMELHO}Site: {url} | ERRO: Fora do ar ou inacessível{RESET}")
            
            # Salva o log limpo no arquivo
            file.write(resultado_log)
        
        file.write("\n")

if __name__ == "__main__":
    check_endpoints()