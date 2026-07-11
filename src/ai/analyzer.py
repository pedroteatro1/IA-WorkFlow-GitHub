def analisar_texto(texto):
    palavras_positivas = [
        "feliz",
        "ótimo",
        "excelente",
        "bom",
        "sucesso",
        "amor",
        "amo"
    ]

    palavras_negativas = [
        "ruim",
        "péssimo",
        "triste"
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
        return "Sentimento positivo ❤️"

    elif pontos < 0:
        return "Sentimento negativo 😞"

    else:
        return "Neutro 😐"