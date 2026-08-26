import requests

def buscar_acao(simbolo): # 'Simbolo' é definido no main.py como 'ativo'
    response = requests.get(f"https://brapi.dev/api/quote/{simbolo}")   # Faz uma requisição GET para a API com o símbolo da ação
    dados = response.json() # Converte a resposta em formato JSON
    valor_acao = dados['results'][0]['regularMarketPrice']  # Obtém o preço de mercado regular da ação
    pe = dados['results'][0]['priceEarnings']  # Obtém o P/E da ação
    valor_2WH = dados['results'][0]['fiftyTwoWeekHigh']  # Obtém o preço máximo das últimas 52 semanas
    valor_2WL = dados['results'][0]['fiftyTwoWeekLow']  # Obtém o preço mínimo das últimas 52 semanas

    return valor_acao, pe, valor_2WH, valor_2WL