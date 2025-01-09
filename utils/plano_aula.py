import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO

def planejamento_aula_function():
    st.title("Plano de Aula - Método Hipotético-Dedutivo")

    # Página 1 - Informações Básicas
    st.header("Informações Básicas")
    professor = st.text_input("Nome do Professor")
    disciplina = st.text_input("Disciplina")
    duracao = st.text_input("Duração da Aula")
    numero_alunos = st.number_input("Número de Alunos", min_value=1, step=1)
    tema = st.text_input("Tema", help="Descreva o tema central da aula.")

    st.header("Competências e Habilidades")
    competencias = st.text_area("Competências de Área", help="Liste as competências gerais a serem desenvolvidas.")
    habilidades = st.text_area("Habilidades", help="Defina as habilidades específicas para a aula.")

    st.header("Conteúdo e Recursos")
    conteudo = st.text_area("Conteúdo", help="Descreva os tópicos e conceitos que serão abordados.")
    recursos = st.text_area("Recursos", help="Liste os materiais e ferramentas necessários para a aula.")

    st.header("Organização dos Espaços")
    atividade_espaco1 = st.text_area("Espaço 1: Atividade", help="Detalhe a atividade inicial.")
    atividade_espaco2 = st.text_area("Espaço 2: Atividade", help="Detalhe a atividade intermediária.")
    atividade_espaco3 = st.text_area("Espaço 3: Atividade", help="Detalhe a atividade final.")

    st.header("Avaliação")
    avaliacao_objetivos = st.text_area("Avaliação dos Objetivos", help="Como verificar se os objetivos foram alcançados?")
    avaliacao_feedback = st.text_area("Avaliação da Aula", help="Aspectos positivos e negativos da aula.")

    # Página 2 - Etapas do MHD
    st.header("Objetivo Específico para o Método Hipotético-Dedutivo")
    objetivo_mhd = st.text_area("Defina o objetivo específico para o MHD na aula", help="Descreva como o MHD será aplicado.")

    st.header("Etapas do Método Hipotético-Dedutivo")
    observacao = st.text_area("Observação", help="O que os alunos devem observar inicialmente?")
    hipotese = st.text_area("Hipótese", help="Que hipóteses os alunos devem propor?")
    deducao = st.text_area("Dedução", help="Como as hipóteses serão analisadas?")
    teste_experimental = st.text_area("Teste Experimental", help="Explique como os alunos testarão suas hipóteses.")
    analise_consolidacao = st.text_area("Análise e Consolidação", help="Descreva como os resultados serão analisados.")

    # Registro e Reflexões
    st.header("Registro e Reflexões")
    registro_alunos = st.text_area("Registro dos Alunos", help="Como os alunos devem registrar hipóteses e resultados?")
    questionamentos = st.text_area("Questionamentos Norteadores", help="Quais perguntas podem orientar o raciocínio dos alunos?")
    reflexao_final = st.text_area("Reflexão Final", help="Descreva os aprendizados e reflexões finais da aula.")

 # Botão para salvar ou exportar o planejamento
    if st.button("Gerar e Exportar PDF"):
        buffer = BytesIO()
        c = canvas.Canvas(buffer, pagesize=letter)
        c.setFont("Helvetica", 12)

        # Adicionar título
        c.drawString(100, 750, "Planejamento de Aula - Método Hipotético-Dedutivo")

        # Adicionar informações básicas
        y = 700
        c.drawString(50, y, f"Nome do Professor: {professor}")
        y -= 20
        c.drawString(50, y, f"Disciplina: {disciplina}")
        y -= 20
        c.drawString(50, y, f"Duração da Aula: {duracao}")
        y -= 20
        c.drawString(50, y, f"Número de Alunos: {numero_alunos}")
        y -= 20
        c.drawString(50, y, f"Tema: {tema}")
        y -= 40

        # Competências e habilidades
        c.drawString(50, y, "Competências de Área:")
        y -= 20
        for line in competencias.split("\n"):
            c.drawString(70, y, line)
            y -= 20
        c.drawString(50, y, "Habilidades:")
        y -= 20
        for line in habilidades.split("\n"):
            c.drawString(70, y, line)
            y -= 20
        y -= 20

        # Conteúdo e recursos
        c.drawString(50, y, "Conteúdo:")
        y -= 20
        for line in conteudo.split("\n"):
            c.drawString(70, y, line)
            y -= 20
        c.drawString(50, y, "Recursos:")
        y -= 20
        for line in recursos.split("\n"):
            c.drawString(70, y, line)
            y -= 20
        y -= 40

        # Página 2 - MHD e Reflexões
        if y < 100:  # Adicionar nova página se o espaço for insuficiente
            c.showPage()
            y = 750

        c.drawString(50, y, "Objetivo Específico para o MHD:")
        y -= 20
        c.drawString(70, y, objetivo_mhd)
        y -= 40

        c.drawString(50, y, "Etapas do Método Hipotético-Dedutivo:")
        y -= 20
        c.drawString(70, y, "Observação:")
        y -= 20
        for line in observacao.split("\n"):
            c.drawString(90, y, line)
            y -= 20
        c.drawString(70, y, "Hipótese:")
        y -= 20
        for line in hipotese.split("\n"):
            c.drawString(90, y, line)
            y -= 20
        c.drawString(70, y, "Dedução:")
        y -= 20
        for line in deducao.split("\n"):
            c.drawString(90, y, line)
            y -= 20
        c.drawString(70, y, "Teste Experimental:")
        y -= 20
        for line in teste_experimental.split("\n"):
            c.drawString(90, y, line)
            y -= 20
        c.drawString(70, y, "Análise e Consolidação:")
        y -= 20
        for line in analise_consolidacao.split("\n"):
            c.drawString(90, y, line)
            y -= 20
        y -= 40

        c.drawString(50, y, "Registro dos Alunos:")
        y -= 20
        for line in registro_alunos.split("\n"):
            c.drawString(70, y, line)
            y -= 20
        c.drawString(50, y, "Questionamentos Norteadores:")
        y -= 20
        for line in questionamentos.split("\n"):
            c.drawString(70, y, line)
            y -= 20
        c.drawString(50, y, "Reflexão Final:")
        y -= 20
        for line in reflexao_final.split("\n"):
            c.drawString(70, y, line)
            y -= 20

        # Finalizar o PDF
        c.save()
        buffer.seek(0)

        # Botão de download
        st.download_button(
            label="Baixar PDF",
            data=buffer,
            file_name="planejamento_aula.pdf",
            mime="application/pdf"
        )
