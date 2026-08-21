from coletor import buscar_acao

resultados = {}

for ativo in ['PETR4', 'VALE3', 'ITUB4']:
    valor_acao, pe = buscar_acao(ativo)
    resultados[ativo] = {'preco': valor_acao, 'pe': pe}

print("Resultados finais:", resultados)
