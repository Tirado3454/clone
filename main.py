import streamlit as st
from utils.maintexto import mhd_function
from utils.tabuleiro import board_editor_function
from utils.frases import phrase_bank_function
from utils.export import generate_pdf, generate_csv
from utils.apresentacao import apresentacao_function  # Import da página de apresentação
from utils.contextualizacao import contextualizacao_page_function  # Import da página de contextualização

# Configuração inicial da página
st.set_page_config(page_title="MHD no Xadrez", layout="centered")

# Título principal
st.title("MENU")

# Seção de introdução
st.header("Informações")
opcoes_introducao = ["Apresentação", "Contextualização"]
introducao = st.selectbox("Escolha uma opção:", opcoes_introducao)

if introducao == "Apresentação":
    apresentacao_function()
elif introducao == "Contextualização":
    contextualizacao_page_function()

# Divisão visual
st.markdown("---")

# Seção de funcionalidades
st.header("Selecione as Funcionalidades")
opcoes_funcionalidades = [
    "Modelo Hipotético-Dedutivo",
    "Editor de Tabuleiro",
    "Banco de Frases",
    "Exportar Dados",
]
funcionalidade = st.selectbox("Escolha uma funcionalidade:", opcoes_funcionalidades)

if funcionalidade == "Modelo Hipotético-Dedutivo":
    mhd_function()
elif funcionalidade == "Editor de Tabuleiro":
    board_editor_function()
elif funcionalidade == "Banco de Frases":
    phrase_bank_function()
elif funcionalidade == "Exportar Dados":
    generate_pdf()
    generate_csv()
