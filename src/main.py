from coletor import buscar_acao

for ativo in ['PETR4', 'VALE3', 'ITUB4']:
    valor_acao = buscar_acao(ativo)
    print(f"O valor da ação {ativo} é R$ {valor_acao}")