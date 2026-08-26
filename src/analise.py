from coletor import buscar_acao

def analisar_acao(simbolo):
    _, _, valor_2WH, valor_2WL = buscar_acao(simbolo)
    amplitude = ((valor_2WH - valor_2WL) / valor_2WL) * 100 
    # Calcula a amplitude percentual do ativo
    
    return amplitude