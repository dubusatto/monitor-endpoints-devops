"""Testes unitários para a API de monitoramento de endpoints."""

from unittest.mock import patch
import requests
from fastapi.testclient import TestClient

# Importa a instância do FastAPI 'app' do seu arquivo na pasta src
from src.monitor_api import app

# Cria um cliente de testes que simula requisições para a nossa API
client = TestClient(app)

def test_estrutura_da_resposta():
    """
    Testa se a API responde com status 200 e se o JSON 
    tem as chaves exatas que o front-end ou o webhook esperam.
    """
    response = client.get("/api/monitorar")
    
    # Valida o status HTTP do FastAPI
    assert response.status_code == 200
    
    # Extrai o corpo da resposta
    json_data = response.json()
    
    # Valida as chaves principais
    assert "mensagem_inicio" in json_data
    assert "resultados" in json_data
    assert isinstance(json_data["resultados"], list)
    
    # Valida se trouxe os 3 sites da lista original
    assert len(json_data["resultados"]) == 3 

@patch("src.monitor_api.requests.get")
def test_sites_todos_online(mock_get):
    """
    Testa o comportamento da API quando todos os sites retornam sucesso.
    Usa o @patch para interceptar o 'requests.get' e forçar um status 200.
    """
    # Configura o mock para devolver um objeto com status_code = 200
    mock_get.return_value.status_code = 200
    
    response = client.get("/api/monitorar")
    json_data = response.json()
    
    # Verifica se a lógica de classificação de 'online: True' funcionou
    for resultado in json_data["resultados"]:
        assert resultado["status"] == 200
        assert resultado["online"] is True

@patch("src.monitor_api.requests.get")
def test_sites_todos_offline(mock_get):
    """
    Testa o comportamento da API quando ocorre erro de rede (Timeout/Offline).
    Força o mock a disparar a exceção RequestException.
    """
    # Configura o mock para simular um erro de conexão
    mock_get.side_effect = requests.exceptions.RequestException("Erro simulado")
    
    response = client.get("/api/monitorar")
    json_data = response.json()
    
    # Verifica se a API lidou com o erro graciosamente sem quebrar
    for resultado in json_data["resultados"]:
        assert resultado["status"] == "Fora do ar ou inacessível"
        assert resultado["online"] is False