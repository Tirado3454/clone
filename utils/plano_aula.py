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

        import io
from fpdf import FPDF

# Gerar o PDF com fpdf
def gerar_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_left_margin(15)
    pdf.set_right_margin(15)
    pdf.set_top_margin(15)

    # Título do PDF
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Planejamento de Aula - Método Hipotético-Dedutivo", 0, 1, "C")
    pdf.ln(10)

    # Conteúdo do PDF
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 10, "Nome do Professor: Professor(a) X")
    pdf.multi_cell(0, 10, "Disciplina: Xadrez e Estratégias Científicas")
    pdf.multi_cell(0, 10, "Duração da Aula: 1 hora")
    pdf.multi_cell(0, 10, "Número de Alunos: 20 alunos")
    pdf.ln(5)

    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Objetivo da Aula", 0, 1)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(
        0, 10,
        "Analisar e aplicar os conceitos do Método Hipotético-Dedutivo em situações reais de partidas de xadrez, "
        "desenvolvendo o pensamento estratégico e crítico."
    )
    pdf.ln(5)

    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Etapas do Método Hipotético-Dedutivo", 0, 1)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(
        0, 10,
        "1. Observação:\n"
        "Após o lance 15... Cc4 na partida entre Gukesh e Ding Liren no Campeonato Mundial FIDE 2024, o bispo branco em e3 está sob ataque direto. "
        "A estrutura de peões na ala da dama das brancas está comprometida."
    )
    pdf.multi_cell(
        0, 10,
        "2. Formulação de Hipótese:\n"
        "A hipótese é que, recuando o bispo para f2, as brancas podem reorganizar suas peças defensivamente, mantendo o equilíbrio posicional e "
        "preservando a estrutura de peões."
    )
    pdf.multi_cell(
        0, 10,
        "3. Dedução:\n"
        "Deduzimos que, ao jogar 16. Bf2:\n"
        "- O bispo será protegido de ameaças imediatas.\n"
        "- A estrutura de peões será mantida.\n"
        "- As pretas precisarão de movimentos adicionais para criar novas ameaças."
    )
    pdf.multi_cell(
        0, 10,
        "4. Teste Experimental:\n"
        "O movimento 16. Bf2 foi jogado. As pretas pressionaram com 16... Td8, mas as brancas conseguiram tempo para reorganizar suas peças e "
        "preparar contra-ataques."
    )
    pdf.multi_cell(
        0, 10,
        "5. Conclusão:\n"
        "O movimento 16. Bf2 confirmou a hipótese inicial. A estrutura posicional foi preservada, e as brancas mantiveram o equilíbrio estratégico na partida."
    )
    pdf.ln(10)

    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Conteúdo Complementar", 0, 1)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(
        0, 10,
        "Partida:\n"
        "Campeonato Mundial FIDE 2024\n"
        "Jogadores: Gukesh (Brancas) vs. Ding Liren (Pretas)\n"
        "Resultado: 0-1\n"
        "Abertura: Defesa Francesa – Variante Clássica, Variante Steinitz"
    )
    pdf.multi_cell(
        0, 10,
        "Ferramentas do Aplicativo:\n"
        "- Editor de Tabuleiro: Para reproduzir posições críticas.\n"
        "- Banco de Frases: Para justificar hipóteses e deduções.\n"
        "- Exportação: Para registrar análises em PDFs e CSVs."
    )

    # Salvar o PDF no buffer
    buffer = io.BytesIO()
    pdf.output(buffer)
    buffer.seek(0)
    return buffer

# Adicionar botão de download no Streamlit
def planejamento_aula_function():
    st.title("Planejamento de Aula - Método Hipotético-Dedutivo")

    # Botão para gerar e baixar o PDF
    buffer = gerar_pdf()
    st.download_button(
        label="Baixar PDF",
        data=buffer,
        file_name="planejamento_aula.pdf",
        mime="application/pdf"
    )
