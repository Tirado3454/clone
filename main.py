import streamlit as st
import pandas as pd  # Certifique-se de importar pandas
from utils.maintexto import mhd_function
from utils.tabuleiro import board_editor_function
from utils.frases import phrase_bank_function
from utils.export import generate_pdf, generate_csv
from utils.apresentacao import apresentacao_function
from utils.contextualizacao import contextualizacao_page_function

# Inicializar o estado do programa
if "mhd_data" not in st.session_state or not isinstance(st.session_state.mhd_data, pd.DataFrame):
    st.session_state.mhd_data = pd.DataFrame(columns=["Etapa", "Descrição", "FEN"])

# Certificar-se de que mhd_data é tratado como DataFrame antes de usar
if not st.session_state.mhd_data.empty:
    # Código relacionado ao DataFrame `mhd_data`
    st.write("Tabela de dados existente:")
    st.dataframe(st.session_state.mhd_data)

# Restante do programa
menu = st.sidebar.radio("Escolha uma funcionalidade:", ["Apresentação", "Contextualização", "MHD", "Editor de Tabuleiro", "Banco de Frases", "Exportar Dados"])

if menu == "Apresentação":
    apresentacao_function()
elif menu == "Contextualização":
    contextualizacao_page_function()
elif menu == "MHD":
    mhd_function()
elif menu == "Editor de Tabuleiro":
    board_editor_function()
elif menu == "Banco de Frases":
    phrase_bank_function()
elif menu == "Exportar Dados":
    generate_pdf()
    generate_csv()
