import streamlit as st
from utils.maintexto import mhd_function
from utils.tabuleiro import board_editor_function
from utils.frases import phrase_bank_function
from utils.export import generate_pdf, generate_csv
from utils.apresentacao import apresentacao_function
from utils.contextualizacao import contextualizacao_page_function

# Configuração inicial
st.set_page_config(page_title="Modelo Hipotético-Dedutivo no Xadrez", layout="wide")

# Definição de abas principais
menu_itens = ["Apresentação", "Contextualização"]
funcionalidades = ["Modelo Hipotético-Dedutivo", "Editor de Tabuleiro", "Banco de Frases", "Exportar Dados"]

# Sessões para controle de abas
if "active_text_tab" not in st.session_state:
    st.session_state["active_text_tab"] = menu_itens[0]

if "active_func_tab" not in st.session_state:
    st.session_state["active_func_tab"] = funcionalidades[0]

# Barra lateral
st.sidebar.title("Menu")
st.sidebar.markdown("### Textos")
for item in menu_itens:
    if st.sidebar.button(item, key=f"text_{item}"):
        st.session_state["active_text_tab"] = item
        st.session_state["active_func_tab"] = None

st.sidebar.markdown("### Funcionalidades")
for func in funcionalidades:
    if st.sidebar.button(func, key=f"func_{func}"):
        st.session_state["active_func_tab"] = func
        st.session_state["active_text_tab"] = None

# Apresentação das abas
if st.session_state["active_text_tab"] == "Apresentação":
    apresentacao_function()

elif st.session_state["active_text_tab"] == "Contextualização":
    contextualizacao_page_function()

elif st.session_state["active_func_tab"] == "Modelo Hipotético-Dedutivo":
    mhd_function()

elif st.session_state["active_func_tab"] == "Editor de Tabuleiro":
    board_editor_function()

elif st.session_state["active_func_tab"] == "Banco de Frases":
    phrase_bank_function()

elif st.session_state["active_func_tab"] == "Exportar Dados":
    st.markdown("### Exportar Dados")
    st.write("Baixe os dados gerados durante a interação com o programa.")

    if "mhd_data" in st.session_state and not st.session_state.mhd_data.empty:
        col_download1, col_download2 = st.columns(2)
        with col_download1:
            st.download_button(
                label="Baixar PDF",
                data=generate_pdf(st.session_state.mhd_data),
                file_name="mhd_xadrez.pdf",
                mime="application/pdf"
            )
        with col_download2:
            st.download_button(
                label="Baixar CSV",
                data=generate_csv(st.session_state.mhd_data),
                file_name="mhd_xadrez.csv",
                mime="text/csv"
            )
    else:
        st.info("Nenhum dado disponível para exportação.")
