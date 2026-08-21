import requests

def buscar_acao(simbolo):
    response = requests.get(f"https://brapi.dev/api/quote/{simbolo}")
    dados = response.json() # Converte a resposta em formato JSON
    valor_acao = dados['results'][0]['regularMarketPrice']
    
    pe = dados['results'][0]['priceEarnings']
    
    return valor_acao, pe