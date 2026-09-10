def analisar_acao(valor_2WH, valor_2WL):
    amplitude = ((valor_2WH - valor_2WL) / valor_2WL) * 100 
    # Calcula a amplitude percentual do ativo
    if amplitude > 500:  # limite de sanidade — acima disso, o dado é suspeito
        return None
    
    return amplitude