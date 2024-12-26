import streamlit as st
from utils.maintexto import mhd_function
from utils.tabuleiro import board_editor_function
from utils.frases import phrase_bank_function
from utils.export import generate_pdf, generate_csv
from utils.apresentacao import apresentacao_function
from utils.contextualizacao import contextualizacao_page_function

# Configuração inicial
st.set_page_config(page_title="MHD no Xadrez", layout="wide")

# Dividindo o layout em duas colunas
col1, col2 = st.columns([1, 3])

# Coluna 1 - Navegação
with col1:
    st.markdown("### Menu de Navegação")
    st.markdown("#### Textos")
    texto_selecionado = st.radio(
        "Escolha uma página:",
        ["Apresentação", "Contextualização"],
        key="text_navigation"
    )

    st.markdown("#### Funcionalidades")
    funcionalidade_selecionada = st.radio(
        "Escolha uma funcionalidade:",
        [
            "Modelo Hipotético-Dedutivo",
            "Editor de Tabuleiro",
            "Banco de Frases",
            "Exportar Dados"
        ],
        key="function_navigation"
    )

# Coluna 2 - Conteúdo
with col2:
    if texto_selecionado == "Apresentação":
        apresentacao_function()
    elif texto_selecionado == "Contextualização":
        contextualizacao_page_function()

    if funcionalidade_selecionada == "Modelo Hipotético-Dedutivo":
        mhd_function()
    elif funcionalidade_selecionada == "Editor de Tabuleiro":
        board_editor_function()
    elif funcionalidade_selecionada == "Banco de Frases":
        phrase_bank_function()
    elif funcionalidade_selecionada == "Exportar Dados":
        generate_pdf()
        generate_csv()
