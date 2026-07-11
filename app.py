import streamlit as st

from ai.analyzer import analisar_texto


st.set_page_config(
    page_title="Analisador de Sentimentos IA",
    page_icon="🤖"
)


st.title("🤖 Analisador de Sentimentos IA")

st.write(
    "Digite uma frase e descubra o sentimento identificado pelo modelo."
)


texto = st.text_area(
    "Digite seu texto:"
)


if st.button("Analisar"):

    if texto.strip():

        resultado = analisar_texto(texto)

        st.success(resultado)

    else:
        st.warning("Digite um texto antes de analisar.")