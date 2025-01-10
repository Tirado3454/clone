from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase.pdfmetrics import stringWidth
from io import BytesIO
import streamlit as st

def planejamento_aula_function():
    st.title("Planejamento de Aula - Método Hipotético-Dedutivo")

    # Formulário para os campos do planejamento
    with st.form("planejamento_form"):
        # Parte 1 - Informações Gerais
        st.subheader("Informações Gerais")
        professor = st.text_input("Nome do Professor:")
        disciplina = st.text_input("Disciplina:")
        duracao = st.text_input("Duração da Aula:", "1 hora")
        numero_alunos = st.text_input("Número de Alunos:", "20")
        tema = st.text_input("Tema:")

        # Parte 2 - Competências, Conteúdo e Recursos
        st.subheader("Competências, Conteúdo e Recursos")
        competencia = st.text_area("Competência de Área:")
        habilidades = st.text_area("Habilidades:")
        conteudo = st.text_area("Conteúdo:")
        recursos = st.text_area("Recursos:")

        # Parte 3 - Organização dos Espaços
        st.subheader("Organização dos Espaços")
        espacos = []
        for i in range(1, 4):
            st.markdown(f"**Espaço {i}**")
            atividade = st.text_area(f"Espaço {i} - Atividade:")
            duracao_espaco = st.text_input(f"Espaço {i} - Duração:")
            papel_aluno = st.text_area(f"Espaço {i} - Papel do Aluno:")
            papel_professor = st.text_area(f"Espaço {i} - Papel do Professor:")
            espacos.append((atividade, duracao_espaco, papel_aluno, papel_professor))

        # Parte 4 - Avaliação
        st.subheader("Avaliação")
        avaliacao_objetivos = st.text_area("Avaliação dos Objetivos:")
        avaliacao_aula = st.text_area("Avaliação da Aula:")

        # Parte 5 - Etapas do Método Hipotético-Dedutivo
        st.subheader("Etapas do Método Hipotético-Dedutivo")
        observacao = st.text_area("Observação:")
        hipotese = st.text_area("Hipótese:")
        deducao = st.text_area("Dedução:")
        teste = st.text_area("Teste Experimental:")
        analise = st.text_area("Análise e Consolidação:")

        # Parte 6 - Reflexão e Registros
        st.subheader("Reflexão e Registros")
        registro = st.text_area("Registro dos Alunos:")
        questionamentos = st.text_area("Questionamentos Norteadores:")
        reflexao = st.text_area("Reflexão Final:")

        submitted = st.form_submit_button("Gerar PDF")

    if submitted:
        # Geração do PDF
        buffer = BytesIO()
        c = canvas.Canvas(buffer, pagesize=letter)
        width, height = letter
        margin_x = 50
        margin_y = 50
        y = height - margin_y

        # Função auxiliar para quebrar texto
        def draw_wrapped_text(canvas, text, x, y, max_width, line_height):
            words = text.split()
            line = ""
            for word in words:
                if stringWidth(line + word, "Helvetica", 12) < max_width:
                    line += word + " "
                else:
                    canvas.drawString(x, y, line.strip())
                    y -= line_height
                    line = word + " "
            if line:
                canvas.drawString(x, y, line.strip())
                y -= line_height
            return y

        # Escrever conteúdo no PDF
        c.setFont("Helvetica", 12)
        sections = [
            ("Nome do Professor", professor),
            ("Disciplina", disciplina),
            ("Duração da Aula", duracao),
            ("Número de Alunos", numero_alunos),
            ("Tema", tema),
            ("Competência de Área", competencia),
            ("Habilidades", habilidades),
            ("Conteúdo", conteudo),
            ("Recursos", recursos),
            ("Avaliação dos Objetivos", avaliacao_objetivos),
            ("Avaliação da Aula", avaliacao_aula),
            ("Observação", observacao),
            ("Hipótese", hipotese),
            ("Dedução", deducao),
            ("Teste Experimental", teste),
            ("Análise e Consolidação", analise),
            ("Registro dos Alunos", registro),
            ("Questionamentos Norteadores", questionamentos),
            ("Reflexão Final", reflexao),
        ]

        for label, value in sections:
            c.drawString(margin_x, y, f"{label}:")
            y -= 20
            y = draw_wrapped_text(c, value, margin_x + 20, y, width - 2 * margin_x, 15)
            if y < margin_y:
                c.showPage()
                y = height - margin_y

        # Espaços
        for i, (atividade, duracao_espaco, papel_aluno, papel_professor) in enumerate(espacos, start=1):
            c.drawString(margin_x, y, f"Espaço {i}:")
            y -= 20
            y = draw_wrapped_text(c, f"Atividade: {atividade}", margin_x + 20, y, width - 2 * margin_x, 15)
            y = draw_wrapped_text(c, f"Duração: {duracao_espaco}", margin_x + 20, y, width - 2 * margin_x, 15)
            y = draw_wrapped_text(c, f"Papel do Aluno: {papel_aluno}", margin_x + 20, y, width - 2 * margin_x, 15)
            y = draw_wrapped_text(c, f"Papel do Professor: {papel_professor}", margin_x + 20, y, width - 2 * margin_x, 15)
            if y < margin_y:
                c.showPage()
                y = height - margin_y

        # Finalizar o PDF
        c.save()
        buffer.seek(0)

        # Visualizar no navegador
        st.markdown("### Visualização do PDF")
        pdf_data = buffer.getvalue()
        pdf_base64 = base64.b64encode(pdf_data).decode("utf-8")
        st.markdown(
            f'<iframe src="data:application/pdf;base64,{pdf_base64}" width="700" height="500"></iframe>',
            unsafe_allow_html=True,
        )

        # Botão para download
        st.download_button(
            label="Baixar PDF",
            data=pdf_data,
            file_name="planejamento_aula.pdf",
            mime="application/pdf",
        )
