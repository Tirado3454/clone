import streamlit as st
from utils.maintexto import mhd_function
from utils.tabuleiro import board_editor_function
from utils.frases import phrase_bank_function
from utils.export import generate_pdf, generate_csv
from utils.apresentacao import apresentacao_function  # Página de Apresentação
from utils.contextualizacao import contextualizacao_page_function  # Página de Contextualização

# Configuração inicial
st.set_page_config(page_title="MHD no Xadrez", layout="centered")

# Título Principal
st.title("MENU PRINCIPAL")

# Seção de Textos Estáticos
st.header("Informações e Introdução")
with st.container():
    st.subheader("Escolha um Tópico:")
    opcoes_textos = ["Apresentação", "Contextualização"]
    texto_escolhido = st.radio("", opcoes_textos, key="text_section")

if texto_escolhido == "Apresentação":
    apresentacao_function()
elif texto_escolhido == "Contextualização":
    contextualizacao_page_function()

# Separação visual com linha horizontal
st.markdown("---")

# Seção de Funcionalidades Interativas
st.header("Funcionalidades Interativas")
with st.container():
    st.subheader("Selecione uma Ferramenta:")
    opcoes_funcionalidades = [
        "Modelo Hipotético-Dedutivo",
        "Editor de Tabuleiro",
        "Banco de Frases",
        "Exportar Dados",
    ]
    funcionalidade_escolhida = st.radio("", opcoes_funcionalidades, key="interactive_section")

if funcionalidade_escolhida == "Modelo Hipotético-Dedutivo":
    mhd_function()
elif funcionalidade_escolhida == "Editor de Tabuleiro":
    board_editor_function()
elif funcionalidade_escolhida == "Banco de Frases":
    phrase_bank_function()
elif funcionalidade_escolhida == "Exportar Dados":
    generate_pdf()
    generate_csv()
