from ai.analyzer import analisar_texto


def main():

    texto = input("Digite um texto para análise: ")

    resultado = analisar_texto(texto)

    print("\nResultado da análise:")
    print(resultado)


if __name__ == "__main__":
    main()