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
    opcoes = [
        "Apresentação",
        "Contextualização",
        "Modelo Hipotético-Dedutivo",
        "Editor de Tabuleiro",
        "Banco de Frases",
        "Exportar Dados"
    ]
    selecao = st.radio("Escolha uma opção:", opcoes, key="main_navigation")

# Coluna 2 - Conteúdo
with col2:
    if selecao == "Apresentação":
        apresentacao_function()
    elif selecao == "Contextualização":
        contextualizacao_page_function()
    elif selecao == "Modelo Hipotético-Dedutivo":
        mhd_function()
    elif selecao == "Editor de Tabuleiro":
        board_editor_function()
    elif selecao == "Banco de Frases":
        phrase_bank_function()
    elif selecao == "Exportar Dados":
        generate_pdf()
        generate_csv()
