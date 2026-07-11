from ai.analyzer import analisar_texto


def test_sentimento_positivo():
    resultado = analisar_texto("Eu amo programação")
    assert resultado == "Sentimento positivo ❤️"


def test_sentimento_negativo():
    resultado = analisar_texto("Esse projeto está ruim")
    assert resultado == "Sentimento negativo 😞"


def test_sentimento_neutro():
    resultado = analisar_texto("Hoje está um dia comum")
    assert resultado == "Neutro 😐"