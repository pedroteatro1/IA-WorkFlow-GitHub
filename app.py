import streamlit as st
from ai.analyzer import analisar_texto


st.set_page_config(
    page_title="IA WorkFlow - Analisador de Sentimentos",
    page_icon="🤖"
)


st.title("🤖 IA WorkFlow")
st.subheader("Analisador de Sentimentos com Inteligência Artificial")


st.write(
    """
Digite uma frase e a IA irá analisar se o sentimento é:
- ❤️ Positivo
- 😞 Negativo
- 😐 Neutro
"""
)


texto = st.text_area(
    "Digite seu texto:",
    placeholder="Exemplo: Eu amo programação Python!"
)


if st.button("🔍 Analisar sentimento"):

    if texto.strip() == "":
        st.warning("Digite algum texto para analisar.")

    else:
        resultado = analisar_texto(texto)

        st.divider()

        st.subheader("Resultado da análise:")

        if "positivo" in resultado.lower():
            st.success(resultado)

        elif "negativo" in resultado.lower():
            st.error(resultado)

        else:
            st.info(resultado)


        quantidade_palavras = len(texto.split())

        st.divider()

        st.metric(
            label="Quantidade de palavras",
            value=quantidade_palavras
        )