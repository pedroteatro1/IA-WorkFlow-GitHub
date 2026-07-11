def analisar_texto(texto):
    """
    Função simples de análise de sentimento.
    Futuramente será substituída por um modelo de IA real.
    """

    palavras_positivas = [
        "feliz",
        "ótimo",
        "excelente",
        "bom",
        "sucesso",
        "amor"
    ]

    palavras_negativas = [
        "ruim",
        "péssimo",
        "triste",
        "erro",
        "problema"
    ]

    texto = texto.lower()

    pontos = 0

    for palavra in palavras_positivas:
        if palavra in texto:
            pontos += 1

    for palavra in palavras_negativas:
        if palavra in texto:
            pontos -= 1

    if pontos > 0:
        return "Positivo 😀"

    elif pontos < 0:
        return "Negativo 😞"

    else:
        return "Neutro 😐"