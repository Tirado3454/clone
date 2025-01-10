from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
import base64
import streamlit as st

def planejamento_aula_function():
    st.title("Planejamento de Aula - Método Hipotético-Dedutivo")

    # Formulário para os campos do planejamento
    with st.form("planejamento_form"):
        professor = st.text_input("Nome do Professor:", help="Digite o nome do professor responsável pela aula.")
        disciplina = st.text_input("Disciplina:", help="Informe a disciplina para a qual a aula será planejada.")
        duracao = st.text_input("Duração da Aula:", "1 hora", help="Tempo total planejado para a aula.")
        numero_alunos = st.text_input("Número de Alunos:", "20", help="Quantidade de alunos esperada na aula.")
        tema = st.text_input("Tema:", help="Especifique o tema principal da aula.")
        
        conteudo = st.text_area("Conteúdo:", help="Detalhe o conteúdo a ser abordado na aula.")
        reflexao = st.text_area("Reflexão Final:", help="Escreva a reflexão final sobre a aula.")
        
        submitted = st.form_submit_button("Gerar PDF")

    if submitted:
        # Geração do PDF
        buffer = BytesIO()
        c = canvas.Canvas(buffer, pagesize=letter)
        width, height = letter

        # Ajustar margens
        margin_x = 50
        margin_y = 50
        y = height - margin_y

        # Título
        c.setFont("Helvetica-Bold", 16)
        c.drawCentredString(width / 2, y, "Planejamento de Aula - Método Hipotético-Dedutivo")
        y -= 40

        # Conteúdo
        c.setFont("Helvetica", 12)
        for label, value in [
            ("Nome do Professor", professor),
            ("Disciplina", disciplina),
            ("Duração da Aula", duracao),
            ("Número de Alunos", numero_alunos),
            ("Tema", tema),
            ("Conteúdo", conteudo),
            ("Reflexão Final", reflexao),
        ]:
            text = f"{label}: {value}"
            c.drawString(margin_x, y, text)
            y -= 20
            if y < margin_y:  # Adiciona uma nova página se ultrapassar os limites
                c.showPage()
                y = height - margin_y
                c.setFont("Helvetica", 12)

        # Finalizar o PDF
        c.save()
        buffer.seek(0)

        # Converter o PDF em base64 para exibição no navegador
        pdf_data = buffer.getvalue()
        pdf_base64 = base64.b64encode(pdf_data).decode('utf-8')

        # Visualização no Streamlit
        st.markdown("### Visualização do PDF")
        st.markdown(
            f'<iframe src="data:application/pdf;base64,{pdf_base64}" width="700" height="500"></iframe>',
            unsafe_allow_html=True
        )

        # Botão para download do PDF
        st.download_button(
            label="Baixar PDF",
            data=pdf_data,
            file_name="planejamento_aula.pdf",
            mime="application/pdf"
        )
