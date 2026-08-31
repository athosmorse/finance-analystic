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

# Neste momento irei pegar o segundo elemento da tupla que criei no FOR em cima
# Estou extraindo o valor que o sorted vai me retornar, e vou comparar com o valor do P/E que denifi como melhor.

# Criando o campo 'score' no JSON zerado
for ativo in resultados:
    resultados[ativo]['score'] = 0


# Criando o Ranking P/E - soma dos pontos no score
# A lógica aqui consiste em pegar o elemento da tupla, e retornar o valor para comparação ⬇
ranking_pe = sorted(resultados.items(), key=lambda item: item[1]['pe'])
for posicao, (ativo, dados) in enumerate(ranking_pe):
    # posicao vale 0, 1, 3... ativo vale 'PETR4', 'ITUB4'... e dados vale o dicionário interno
    pontos = len(ranking_pe) - posicao
    resultados[ativo]['score'] += pontos

# Criando o Ranking Amplitude - soma dos pontos no score
ranking_amplitude = sorted(resultados.items(), key=lambda item: item[1]['amplitude'])
for posicao, (ativo, dados) in enumerate(ranking_amplitude):
    pontos = len(ranking_amplitude) - posicao
    resultados[ativo]['score'] += pontos

melhor_ativo = 'PETR4'
melhor_score = resultados['PETR4']['score']

for ativo, dados in resultados.items():
# Essa lógica ira servir para comparar o socre de cada ativo com o melhorscore que definimos.
    if dados['score'] > melhor_score:
        melhor_score = dados['score']
        melhor_ativo = ativo
   
print(f'Melhor ativo: {melhor_ativo} com o Socre de {melhor_score:.2f}')    
    
print("=======================================================================================================================")
print(resultados)
    