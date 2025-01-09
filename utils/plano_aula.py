import streamlit as st
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def planejamento_aula_function():
    st.title("Planejamento de Aula - Método Hipotético-Dedutivo")

    # Introdução
    st.markdown("""
    Bem-vindo ao planejamento de aula! Aqui você poderá estruturar uma aula completa com base no Método Hipotético-Dedutivo, 
    integrando o xadrez ao ensino de ciência e tecnologia.
    """)

    # Formulário para informações básicas
    st.header("Informações Básicas")
    professor = st.text_input("Nome do Professor")
    disciplina = st.text_input("Disciplina")
    duracao = st.text_input("Duração da Aula")
    numero_alunos = st.number_input("Número de Alunos", min_value=1, step=1)
    tema = st.text_input("Tema", help="Deve refletir a integração entre o MHD e o xadrez, por exemplo: "Aplicação do Método Hipotético-Dedutivo no Xadrez Estratégico")

    # Competências e habilidades
    st.header("Competências e Habilidades")
    competencias = st.text_area("Competências de Área", help="Liste as competências gerais a serem desenvolvidas.")
    habilidades = st.text_area("Habilidades", help="Defina as habilidades específicas para a aula.")

    # Conteúdo e recursos
    st.header("Conteúdo e Recursos")
    conteudo = st.text_area("Conteúdo", help="Descreva os tópicos e conceitos que serão abordados.")
    recursos = st.text_area("Recursos", help="Liste os materiais e ferramentas necessários para a aula.")

    # Organização dos espaços
    st.header("Organização dos Espaços")
    atividade_espaco1 = st.text_area("Espaço 1: Atividade", help="Detalhe a atividade inicial.")
    atividade_espaco2 = st.text_area("Espaço 2: Atividade", help="Detalhe a atividade intermediária.")
    atividade_espaco3 = st.text_area("Espaço 3: Atividade", help="Detalhe a atividade final.")

    # Avaliação
    st.header("Avaliação")
    avaliacao_objetivos = st.text_area("Avaliação dos Objetivos", help="Como verificar se os objetivos foram alcançados?")
    avaliacao_feedback = st.text_area("Avaliação da Aula", help="Aspectos positivos e negativos da aula.")

    # Botão para gerar o planejamento em PDF
    if st.button("Gerar e Exportar PDF"):
        buffer = BytesIO()
        c = canvas.Canvas(buffer, pagesize=letter)
        c.setFont("Helvetica", 12)
        c.drawString(100, 750, "Planejamento de Aula - Método Hipotético-Dedutivo")
        
        # Adicionar informações ao PDF
        y = 700
        c.drawString(50, y, f"Nome do Professor: {professor}")
        y -= 20
        c.drawString(50, y, f"Disciplina: {disciplina}")
        y -= 20
        c.drawString(50, y, f"Duração da Aula: {duracao}")
        y -= 20
        c.drawString(50, y, f"Número de Alunos: {numero_alunos}")
        y -= 40
        c.drawString(50, y, f"Tema: {tema}")
        y -= 40
        c.drawString(50, y, "Competências de Área:")
        y -= 20
        for line in competencias.split("\n"):
            c.drawString(70, y, line)
            y -= 20
        y -= 20
        c.drawString(50, y, "Habilidades:")
        y -= 20
        for line in habilidades.split("\n"):
            c.drawString(70, y, line)
            y -= 20
        y -= 20
        c.drawString(50, y, "Conteúdo:")
        y -= 20
        for line in conteudo.split("\n"):
            c.drawString(70, y, line)
            y -= 20
        y -= 20
        c.drawString(50, y, "Recursos:")
        y -= 20
        for line in recursos.split("\n"):
            c.drawString(70, y, line)
            y -= 20
        y -= 20
        c.drawString(50, y, "Espaço 1: Atividade:")
        y -= 20
        for line in atividade_espaco1.split("\n"):
            c.drawString(70, y, line)
            y -= 20
        y -= 20
        c.drawString(50, y, "Espaço 2: Atividade:")
        y -= 20
        for line in atividade_espaco2.split("\n"):
            c.drawString(70, y, line)
            y -= 20
        y -= 20
        c.drawString(50, y, "Espaço 3: Atividade:")
        y -= 20
        for line in atividade_espaco3.split("\n"):
            c.drawString(70, y, line)
            y -= 20
        y -= 20
        c.drawString(50, y, "Avaliação dos Objetivos:")
        y -= 20
        for line in avaliacao_objetivos.split("\n"):
            c.drawString(70, y, line)
            y -= 20
        y -= 20
        c.drawString(50, y, "Avaliação da Aula:")
        y -= 20
        for line in avaliacao_feedback.split("\n"):
            c.drawString(70, y, line)
            y -= 20

        # Finalizar o PDF
        c.save()
        buffer.seek(0)
        st.download_button(
            label="Baixar PDF",
            data=buffer,
            file_name="planejamento_aula.pdf",
            mime="application/pdf"
        )
