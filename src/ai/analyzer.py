from ai.palavras import PALAVRAS_POSITIVAS, PALAVRAS_NEGATIVAS


def analisar_texto(texto):

    texto = texto.lower()

    pontos = 0

    for palavra in PALAVRAS_POSITIVAS:
        if palavra in texto:
            pontos += 1

    for palavra in PALAVRAS_NEGATIVAS:
        if palavra in texto:
            pontos -= 1

    if pontos > 0:
        sentimento = "Sentimento positivo ❤️"

    elif pontos < 0:
        sentimento = "Sentimento negativo 😞"

    else:
        sentimento = "Neutro 😐"

    return f"{sentimento} | Pontuação: {pontos}"