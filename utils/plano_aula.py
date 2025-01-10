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

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
import streamlit as st

def planejamento_aula_function():
    st.title("Planejamento de Aula - Método Hipotético-Dedutivo")

    # Gerar o PDF
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    # Título
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(width / 2, height - 50, "Planejamento de Aula - Método Hipotético-Dedutivo")

    # Conteúdo
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 100, "Nome do Professor: Professor(a) X")
    c.drawString(50, height - 120, "Disciplina: Xadrez e Estratégias Científicas")
    c.drawString(50, height - 140, "Duração da Aula: 1 hora")
    c.drawString(50, height - 160, "Número de Alunos: 20 alunos")

    c.drawString(50, height - 200, "Objetivo da Aula:")
    c.drawString(70, height - 220, "Analisar e aplicar os conceitos do Método Hipotético-Dedutivo em situações reais de partidas de xadrez,")
    c.drawString(70, height - 240, "desenvolvendo o pensamento estratégico e crítico.")

    # Etapas do Método Hipotético-Dedutivo
    c.drawString(50, height - 280, "Etapas do Método Hipotético-Dedutivo:")
    c.drawString(70, height - 300, "1. Observação:")
    c.drawString(90, height - 320, "Após o lance 15... Cc4 na partida entre Gukesh e Ding Liren no Campeonato Mundial FIDE 2024,")
    c.drawString(90, height - 340, "o bispo branco em e3 está sob ataque direto. A estrutura de peões na ala da dama das brancas está comprometida.")

    c.drawString(70, height - 360, "2. Formulação de Hipótese:")
    c.drawString(90, height - 380, "A hipótese é que, recuando o bispo para f2, as brancas podem reorganizar suas peças defensivamente,")
    c.drawString(90, height - 400, "mantendo o equilíbrio posicional e preservando a estrutura de peões.")

    c.drawString(70, height - 420, "3. Dedução:")
    c.drawString(90, height - 440, "Deduzimos que, ao jogar 16. Bf2:")
    c.drawString(110, height - 460, "- O bispo será protegido de ameaças imediatas.")
    c.drawString(110, height - 480, "- A estrutura de peões será mantida.")
    c.drawString(110, height - 500, "- As pretas precisarão de movimentos adicionais para criar novas ameaças.")

    c.drawString(70, height - 520, "4. Teste Experimental:")
    c.drawString(90, height - 540, "O movimento 16. Bf2 foi jogado. As pretas pressionaram com 16... Td8,")
    c.drawString(90, height - 560, "mas as brancas conseguiram tempo para reorganizar suas peças e preparar contra-ataques.")

    c.drawString(70, height - 580, "5. Conclusão:")
    c.drawString(90, height - 600, "O movimento 16. Bf2 confirmou a hipótese inicial. A estrutura posicional foi preservada,")
    c.drawString(90, height - 620, "e as brancas mantiveram o equilíbrio estratégico na partida.")

    # Finalizar o PDF
    c.save()
    buffer.seek(0)

    # Botão de download no Streamlit
    st.download_button(
        label="Baixar PDF",
        data=buffer,
        file_name="planejamento_aula.pdf",
        mime="application/pdf"
    )
