"""API para consultar a disponibilidade de endpoints web."""

from datetime import datetime
import requests
from fastapi import FastAPI

app = FastAPI()

URLS = ["https://google.com", "https://github.com", "https://site-que-nao-existe.com"]

@app.get("/api/monitorar")
def check_endpoints():
    """
    Percorre a lista de URLs, faz a requisição GET,
    e retorna os resultados em formato JSON estruturado.
    """
    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    resultados = []

    for url in URLS:
        try:
            response = requests.get(url, timeout=5)
            resultados.append({
                "site": url,
                "status": response.status_code,
                "online": True
            })
        except requests.exceptions.RequestException:
            resultados.append({
                "site": url,
                "status": "Fora do ar ou inacessível",
                "online": False
            })

    # O FastAPI converte automaticamente esse dicionário para JSON
    return {
        "mensagem_inicio": f"Monitoramento realizado em: {agora}",
        "resultados": resultados
    }