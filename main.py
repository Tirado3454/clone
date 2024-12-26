import streamlit as st
from utils.maintexto import mhd_function
from utils.tabuleiro import board_editor_function
from utils.frases import phrase_bank_function
from utils.export import generate_pdf, generate_csv
from utils.apresentacao import apresentacao_function
from utils.contextualizacao import contextualizacao_page_function

# Configuração inicial
st.set_page_config(page_title="MHD no Xadrez", layout="wide")

# Inicializar estado de navegação
if "active_tab" not in st.session_state:
    st.session_state["active_tab"] = "Apresentação"

# Função para alterar o estado ativo
def set_active_tab(tab_name):
    st.session_state["active_tab"] = tab_name

# Dividindo o layout em duas colunas
col1, col2 = st.columns([1, 3])

# Coluna 1 - Navegação
with col1:
    st.markdown("### Textos Explicativos")
    if st.button("Apresentação", key="btn_apresentacao"):
        set_active_tab("Apresentação")
    if st.button("Contextualização", key="btn_contextualizacao"):
        set_active_tab("Contextualização")

    st.markdown("### Funcionalidades")
    if st.button("Modelo Hipotético-Dedutivo", key="btn_mhd"):
        set_active_tab("Modelo Hipotético-Dedutivo")
    if st.button("Editor de Tabuleiro", key="btn_tabuleiro"):
        set_active_tab("Editor de Tabuleiro")
    if st.button("Banco de Frases", key="btn_frases"):
        set_active_tab("Banco de Frases")
    if st.button("Exportar Dados", key="btn_exportar"):
        set_active_tab("Exportar Dados")

# Coluna 2 - Conteúdo
with col2:
    if st.session_state["active_tab"] == "Apresentação":
        apresentacao_function()
    elif st.session_state["active_tab"] == "Contextualização":
        contextualizacao_page_function()
    elif st.session_state["active_tab"] == "Modelo Hipotético-Dedutivo":
        mhd_function()
    elif st.session_state["active_tab"] == "Editor de Tabuleiro":
        board_editor_function()
    elif st.session_state["active_tab"] == "Banco de Frases":
        phrase_bank_function()
    elif st.session_state["active_tab"] == "Exportar Dados":
        generate_pdf()
        generate_csv()
