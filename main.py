import streamlit as st
from utils.maintexto import mhd_function
from utils.tabuleiro import board_editor_function
from utils.frases import phrase_bank_function
from utils.export import generate_pdf, generate_csv
from utils.apresentacao import apresentacao_function
from utils.contextualizacao import contextualizacao_page_function
from utils.ciencia import ciencia_page_function
from utils.metodos_cientificos import metodos_cientificos_page_function
from utils.metodologia_cientifica import metodologia_cientifica_page_function
from utils.steinitz import steinitz_page_function
from utils.escola_sovietica import escola_sovietica_page_function
from utils.tecnologias_xadrez import tecnologias_xadrez_page_function
from utils.rating_xadrez import rating_xadrez_page_function
from utils.tecnologia_no_treinamento import tecnologia_no_treinamento_page_function
from utils.campeonatos_mundiais import campeonatos_mundiais_page_function
from utils.referencia import referencia_page_function
from utils.artigos import artigos_page_function  # Import da página de artigos
from utils.plano_aula import planejamento_aula_function

# Configuração inicial da página
st.set_page_config(page_title="Ensino de Ciência e Xadrez", layout="wide")

# Inicializar estados globais, se necessário
if "mhd_data" not in st.session_state:
    st.session_state["mhd_data"] = {}
if "board_data" not in st.session_state:
    st.session_state["board_data"] = ""
if "phrases_selected" not in st.session_state:
    st.session_state["phrases_selected"] = []

# Divisão do menu
menu_type = st.sidebar.radio("Selecione o tipo de conteúdo:", ["Textos", "Funcionalidades", "Planejamento"])

# Menu de textos
if menu_type == "Textos":
    text_option = st.sidebar.radio(
        "Escolha uma opção:",
        ["Apresentação", "Contextualização", "Ciência", "Métodos Científicos", "Metodologia Científica", "Steinitz e o Xadrez Moderno", "Escola Soviética de Xadrez", "Xadrez e Tecnologias", "O Rating no Xadrez", "Tecnologia no Treinamento", "Campeonatos Mundiais", "Referências", "Artigos"]
    )
    if text_option == "Apresentação":
        apresentacao_function()
    elif text_option == "Contextualização":
        contextualizacao_page_function()
    elif text_option == "Ciência":
        ciencia_page_function()
    elif text_option == "Métodos Científicos":
        metodos_cientificos_page_function()
    elif text_option == "Metodologia Científica":
        metodologia_cientifica_page_function()
    elif text_option == "Steinitz e o Xadrez Moderno":
        steinitz_page_function()
    elif text_option == "Escola Soviética de Xadrez":
        escola_sovietica_page_function()
    elif text_option == "Xadrez e Tecnologias":
        tecnologias_xadrez_page_function()
    elif text_option == "O Rating no Xadrez":
        rating_xadrez_page_function()
    elif text_option == "Tecnologia no Treinamento":
        tecnologia_no_treinamento_page_function()
    elif text_option == "Campeonatos Mundiais":
        campeonatos_mundiais_page_function()
    elif text_option == "Referências":
        referencia_page_function()
    elif text_option == "Artigos":
        artigos_page_function()
        
# Menu de funcionalidades
elif menu_type == "Funcionalidades":
    menu_option = st.sidebar.radio(
        "Escolha uma funcionalidade:",
        ["Modelo Hipotético-Dedutivo", "Editor de Tabuleiro", "Banco de Frases", "Exportar Dados"]
    )
    if menu_option == "Modelo Hipotético-Dedutivo":
        mhd_function()
    elif menu_option == "Editor de Tabuleiro":
        board_editor_function()
    elif menu_option == "Banco de Frases":
        phrase_bank_function()
    elif menu_option == "Exportar Dados":
        st.title("Exportar Dados Consolidados")
        
        # Exibir dados disponíveis
        st.markdown("### Dados do Modelo Hipotético-Dedutivo")
        if st.session_state.get("mhd_data"):
            st.write(st.session_state["mhd_data"])
        else:
            st.warning("Nenhum dado do Modelo Hipotético-Dedutivo disponível.")

        st.markdown("### Configuração do Tabuleiro")
        if st.session_state.get("board_data"):
            st.write(st.session_state["board_data"])
        else:
            st.warning("Nenhuma configuração de tabuleiro disponível.")

        st.markdown("### Frases Selecionadas")
        if st.session_state.get("phrases_selected"):
            st.write(st.session_state["phrases_selected"])
        else:
            st.warning("Nenhuma frase selecionada.")

        # Escolher formato de exportação
        export_format = st.radio("Escolha o formato de exportação:", ["PDF", "CSV"])

        # Botão de exportação
        if st.button("Exportar"):
            if export_format == "PDF":
                pdf_data = generate_pdf(
                    st.session_state.get("mhd_data", {}),
                    st.session_state.get("board_data", ""),
                    st.session_state.get("phrases_selected", [])
                )
                st.download_button(
                    label="Baixar PDF",
                    data=pdf_data,
                    file_name="dados_consolidados.pdf",
                    mime="application/pdf"
                )
            elif export_format == "CSV":
                csv_data = generate_csv(
                    st.session_state.get("mhd_data", {}),
                    st.session_state.get("board_data", ""),
                    st.session_state.get("phrases_selected", [])
                )
                st.download_button(
                    label="Baixar CSV",
                    data=csv_data,
                    file_name="dados_consolidados.csv",
                    mime="text/csv"
                )
# Menu de planejamento
elif menu_type == "Planejamento":
    planning_option = st.sidebar.radio(
        "Escolha uma opção:",
        ["Plano de Aula", "Acessar PDFs"]
    )

    # Opção de Plano de Aula
    if planning_option == "Plano de Aula":
        planejamento_aula_function()  # Chama a função existente

    # Opção de Acessar PDFs
    elif planning_option == "Acessar PDFs":
        st.title("Repositório de PDFs")
        st.markdown("### PDFs Disponíveis para Download")
        # Exemplo de links para PDFs existentes
        pdfs = {
            "Planejamento Aula 1": "https://exemplo.com/planejamento_aula1.pdf",
            "Planejamento Aula 2": "https://exemplo.com/planejamento_aula2.pdf",
            "Planejamento Aula 3": "https://exemplo.com/planejamento_aula3.pdf",
        }
        for nome, link in pdfs.items():
            st.markdown(f"- [{nome}]({link})")
