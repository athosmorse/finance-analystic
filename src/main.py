from coletor import buscar_acao

resultados = {}

for ativo in ['PETR4', 'VALE3', 'ITUB4']:
    valor_acao, pe = buscar_acao(ativo)
    resultados[ativo] = {'preco': valor_acao, 'pe': pe}
print("Resultados finais:", resultados)

melhor_ativo = 'PETR4'
melhor_pe = resultados['PETR4']['pe']

for ativo, dados in resultados.items():
    if dados['pe'] < melhor_pe:
        melhor_pe = dados['pe']
        melhor_ativo = ativo
        
print(f'Melhor ativo: {melhor_ativo} com o P/E de {melhor_pe:.2f}')
