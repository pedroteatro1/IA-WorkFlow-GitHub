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

    for palavra in palavras_positivas:
        if palavra in texto:
            return "Sentimento positivo ❤️"

    for palavra in palavras_negativas:
        if palavra in texto:
            return "Sentimento negativo 😞"

    return "Neutro 😐"