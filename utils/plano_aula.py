from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
import streamlit as st

def planejamento_aula_function():
    st.title("Planejamento de Aula - Método Hipotético-Dedutivo")

    # Formulário para os campos do planejamento
    with st.form("planejamento_form"):
        professor = st.text_input("Nome do Professor:")
        disciplina = st.text_input("Disciplina:")
        duracao = st.text_input("Duração da Aula:", "1 hora")
        numero_alunos = st.text_input("Número de Alunos:", "20")
        objetivo = st.text_area("Objetivo da Aula:", "Descreva o objetivo da aula...")
        
        observacao = st.text_area("1. Observação:", "Descreva a observação inicial...")
        hipotese = st.text_area("2. Formulação de Hipótese:", "Descreva a hipótese...")
        deducao = st.text_area("3. Dedução:", "Explique a dedução...")
        teste = st.text_area("4. Teste Experimental:", "Explique o teste realizado...")
        conclusao = st.text_area("5. Conclusão:", "Descreva as conclusões...")

        # Botão para submeter os dados
        submitted = st.form_submit_button("Gerar PDF")

    # Gerar o PDF com os dados preenchidos
    if submitted:
        buffer = BytesIO()
        c = canvas.Canvas(buffer, pagesize=letter)
        width, height = letter

        # Título do PDF
        c.setFont("Helvetica-Bold", 16)
        c.drawCentredString(width / 2, height - 50, "Planejamento de Aula - Método Hipotético-Dedutivo")

        # Conteúdo do PDF
        c.setFont("Helvetica", 12)
        c.drawString(50, height - 100, f"Nome do Professor: {professor}")
        c.drawString(50, height - 120, f"Disciplina: {disciplina}")
        c.drawString(50, height - 140, f"Duração da Aula: {duracao}")
        c.drawString(50, height - 160, f"Número de Alunos: {numero_alunos}")

        c.drawString(50, height - 200, "Objetivo da Aula:")
        c.drawString(70, height - 220, objetivo)

        # Etapas do Método Hipotético-Dedutivo
        c.drawString(50, height - 260, "Etapas do Método Hipotético-Dedutivo:")
        c.drawString(70, height - 280, "1. Observação:")
        c.drawString(90, height - 300, observacao)

        c.drawString(70, height - 320, "2. Formulação de Hipótese:")
        c.drawString(90, height - 340, hipotese)

        c.drawString(70, height - 360, "3. Dedução:")
        c.drawString(90, height - 380, deducao)

        c.drawString(70, height - 400, "4. Teste Experimental:")
        c.drawString(90, height - 420, teste)

        c.drawString(70, height - 440, "5. Conclusão:")
        c.drawString(90, height - 460, conclusao)

        # Finalizar o PDF
        c.save()
        buffer.seek(0)

        # Botão para download do PDF
        st.download_button(
            label="Baixar PDF",
            data=buffer,
            file_name="planejamento_aula.pdf",
            mime="application/pdf"
        )
