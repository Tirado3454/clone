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
    st.markdown("### Textos Explicativos")
    texto_opcoes = ["Apresentação", "Contextualização"]
    texto_selecao = st.radio("Selecione:", texto_opcoes, key="text_navigation")

    st.markdown("### Funcionalidades")
    func_opcoes = [
        "Modelo Hipotético-Dedutivo",
        "Editor de Tabuleiro",
        "Banco de Frases",
        "Exportar Dados"
    ]
    func_selecao = st.radio("Escolha uma funcionalidade:", func_opcoes, key="func_navigation")

# Coluna 2 - Conteúdo
with col2:
    # Verificar se um texto ou uma funcionalidade foi selecionado
    if texto_selecao == "Apresentação":
        apresentacao_function()
    elif texto_selecao == "Contextualização":
        contextualizacao_page_function()
    elif func_selecao == "Modelo Hipotético-Dedutivo":
        mhd_function()
    elif func_selecao == "Editor de Tabuleiro":
        board_editor_function()
    elif func_selecao == "Banco de Frases":
        phrase_bank_function()
    elif func_selecao == "Exportar Dados":
        generate_pdf()
        generate_csv()
