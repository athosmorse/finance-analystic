import requests

response_PETR4 = requests.get("https://brapi.dev/api/quote/PETR4") # Chamada à API para obter informações sobre a ação PETR4

dados_PETR4 = response_PETR4.json() # Converte a resposta em formato JSON

print("Informações sobre a ação PETR4:")
print(dados_PETR4)

valor_acao_PETR4 = dados_PETR4['results'][0]['regularMarketPrice']

print("====================================================================================================")

print(f"Valor atual da ação PETR4: R$ {valor_acao_PETR4}")
