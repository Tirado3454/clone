from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
import base64
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

        # Função auxiliar para justificar texto
        def draw_justified_text(canvas, text, x, y, max_width, line_height):
            words = text.split()
            lines = []
            line = []

            # Criar as linhas
            for word in words:
                test_line = " ".join(line + [word])
                if canvas.stringWidth(test_line, "Helvetica", 12) <= max_width:
                    line.append(word)
                else:
                    lines.append(line)
                    line = [word]
            if line:
                lines.append(line)

            # Desenhar as linhas justificadas
            for line in lines[:-1]:  # Justificar todas as linhas, exceto a última
                line_text = " ".join(line)
                total_width = canvas.stringWidth(line_text, "Helvetica", 12)
                extra_space = (max_width - total_width) / (len(line) - 1) if len(line) > 1 else 0
                x_pos = x
                for word in line:
                    canvas.drawString(x_pos, y, word)
                    x_pos += canvas.stringWidth(word, "Helvetica", 12) + extra_space
                y -= line_height

            # Última linha não é justificada
            if lines:
                line_text = " ".join(lines[-1])
                canvas.drawString(x, y, line_text)
                y -= line_height

            return y

        # Escrever conteúdo no PDF na mesma ordem do formulário
        c.setFont("Helvetica", 12)
        form_sections = [
            ("Nome do Professor", professor),
            ("Disciplina", disciplina),
            ("Duração da Aula", duracao),
            ("Número de Alunos", numero_alunos),
            ("Tema", tema),
            ("Competência de Área", competencia),
            ("Habilidades", habilidades),
            ("Conteúdo", conteudo),
            ("Recursos", recursos),
            # Organização dos Espaços
            ("Espaços", None),
            *[(f"Espaço {i} - Atividade", atividade) for i, (atividade, _, _, _) in enumerate(espacos, 1)],
            *[(f"Espaço {i} - Duração", duracao) for i, (_, duracao, _, _) in enumerate(espacos, 1)],
            *[(f"Espaço {i} - Papel do Aluno", papel_aluno) for i, (_, _, papel_aluno, _) in enumerate(espacos, 1)],
            *[(f"Espaço {i} - Papel do Professor", papel_professor) for i, (_, _, _, papel_professor) in enumerate(espacos, 1)],
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

        for label, value in form_sections:
            if value is None:  # Título de seção
                c.setFont("Helvetica-Bold", 12)
                c.drawString(margin_x, y, label)
                c.setFont("Helvetica", 12)
            else:  # Campo de texto
                c.drawString(margin_x, y, f"{label}:")
                y -= 20
                y = draw_justified_text(c, value, margin_x + 20, y, width - 2 * margin_x, 15)
            y -= 20
            if y < margin_y:
                c.showPage()
                y = height - margin_y
                c.setFont("Helvetica", 12)

        # Finalizar o PDF
        c.save()
        buffer.seek(0)

        # Obter os dados do PDF
        pdf_data = buffer.getvalue()

        # Codificar para base64 para visualização
        pdf_base64 = base64.b64encode(pdf_data).decode("utf-8")

        # Visualizar no navegador
        st.markdown("### Visualização do PDF")
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
