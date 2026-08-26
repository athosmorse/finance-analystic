from coletor import buscar_acao
from analise import analisar_acao

resultados = {} #Biblioteca para armazenar os resultados das ações

for ativo in ['PETR4', 'VALE3', 'ITUB4']:
    valor_acao, pe, valor_2WH, valor_2WL = buscar_acao(ativo)
    amplitude = analisar_acao(valor_2WH, valor_2WL)
    resultados[ativo] = {'preco': valor_acao, 'pe': pe, 'amplitude': amplitude}
print("Resultados finais:", resultados)

for ativo, dados in resultados.items():
    print(f"{ativo} - Amplitude: {dados['amplitude']:.2f}%")

# Aqui, defini de forma estática o melhor ativo como PETR4

melhor_ativo = 'PETR4'
melhor_pe = resultados['PETR4']['pe']

for ativo, dados in resultados.items():
# Essa lógica ira servir para comparar o P/E de cada ativo com o melhor P/E que definimos.
    if dados['pe'] < melhor_pe:
        melhor_pe = dados['pe']
        melhor_ativo = ativo
# Se o código encontrar um ativo com P/E menor que o melhor P/E atual, ele atualiza o melhor P/E e o melhor ativo.
print(f'Melhor ativo: {melhor_ativo} com o P/E de {melhor_pe:.2f}')