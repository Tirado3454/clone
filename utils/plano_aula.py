from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
import streamlit as st

def planejamento_aula_function():
    st.title("Planejamento de Aula - Método Hipotético-Dedutivo")

    # Formulário para os campos do planejamento
    with st.form("planejamento_form"):
        # Parte 1
        professor = st.text_input("Nome do Professor:", help="Digite o nome do professor responsável pela aula.")
        disciplina = st.text_input("Disciplina:", help="Informe a disciplina para a qual a aula será planejada.")
        duracao = st.text_input("Duração da Aula:", help="Tempo total planejado para a aula.")
        numero_alunos = st.text_input("Número de Alunos:", help="Quantidade de alunos esperada na aula.")
        tema = st.text_input("Tema:", help="Especifique o tema principal da aula.")
        
        competencia = st.text_area("Competência de Área:", help="Descreva a competência relacionada à área de ensino.")
        habilidades = st.text_area("Habilidades:", help="Liste as habilidades que os alunos devem desenvolver.")
        conteudo = st.text_area("Conteúdo:", help="Detalhe o conteúdo a ser abordado na aula.")
        recursos = st.text_area("Recursos:", help="Especifique os materiais e ferramentas necessários para a aula.")

        # Organização dos espaços
        st.markdown("### Organização dos Espaços")
        espaco1_atividade = st.text_area("Espaço 1 - Atividade:", help="Descreva a atividade que será realizada neste espaço.")
        espaco1_duracao = st.text_input("Espaço 1 - Duração:", help="Informe a duração da atividade neste espaço.")
        espaco1_papel_aluno = st.text_area("Espaço 1 - Papel do Aluno:", help="Defina o papel dos alunos neste espaço.")
        espaco1_papel_professor = st.text_area("Espaço 1 - Papel do Professor:", help="Defina o papel do professor neste espaço.")

        espaco2_atividade = st.text_area("Espaço 2 - Atividade:", help="Descreva a atividade que será realizada neste espaço.")
        espaco2_duracao = st.text_input("Espaço 2 - Duração:", help="Informe a duração da atividade neste espaço.")
        espaco2_papel_aluno = st.text_area("Espaço 2 - Papel do Aluno:", help="Defina o papel dos alunos neste espaço.")
        espaco2_papel_professor = st.text_area("Espaço 2 - Papel do Professor:", help="Defina o papel do professor neste espaço.")

        espaco3_atividade = st.text_area("Espaço 3 - Atividade:", help="Descreva a atividade que será realizada neste espaço.")
        espaco3_duracao = st.text_input("Espaço 3 - Duração:", help="Informe a duração da atividade neste espaço.")
        espaco3_papel_aluno = st.text_area("Espaço 3 - Papel do Aluno:", help="Defina o papel dos alunos neste espaço.")
        espaco3_papel_professor = st.text_area("Espaço 3 - Papel do Professor:", help="Defina o papel do professor neste espaço.")

        # Parte 2
        avaliacao_objetivos = st.text_area("Avaliação dos Objetivos:", help="O que pode ser feito para observar se os objetivos foram cumpridos?")
        avaliacao_aula = st.text_area("Avaliação da Aula:", help="Como foi sua avaliação da aula? (Aspectos positivos e negativos)")

        objetivo_mhd = st.text_area("Objetivo Específico para o MHD:", help="Defina o objetivo específico do Método Hipotético-Dedutivo para a aula.")

        # Etapas do MHD
        st.markdown("### Etapas do MHD")
        observacao = st.text_area("1. Observação:", help="Descreva a observação inicial.")
        hipotese = st.text_area("2. Formulação de Hipótese:", help="Descreva a hipótese formulada.")
        deducao = st.text_area("3. Dedução:", help="Explique a dedução feita.")
        teste = st.text_area("4. Teste Experimental:", help="Explique o teste realizado.")
        analise = st.text_area("5. Análise e Consolidação:", help="Apresente a análise e os resultados consolidados.")

        # Reflexão
        registro = st.text_area("Registro dos Alunos:", help="Escreva o registro feito pelos alunos.")
        questionamentos = st.text_area("Questionamentos Norteadores:", help="Liste perguntas que guiem os alunos.")
        reflexao = st.text_area("Reflexão Final:", help="Escreva a reflexão final sobre a aula.")

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

        # Preencher os campos no PDF
        y = height - 100  # Altura inicial
        c.setFont("Helvetica", 12)
        for label, value in [
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
            ("Espaço 1 - Atividade", espaco1_atividade),
            ("Espaço 1 - Duração", espaco1_duracao),
            ("Espaço 1 - Papel do Aluno", espaco1_papel_aluno),
            ("Espaço 1 - Papel do Professor", espaco1_papel_professor),
            # Avaliação
            ("Avaliação dos Objetivos", avaliacao_objetivos),
            ("Avaliação da Aula", avaliacao_aula),
            # Reflexão Final
            ("Reflexão Final", reflexao),
        ]:
            c.drawString(50, y, f"{label}: {value}")
            y -= 20
            if y < 50:  # Nova página
                c.showPage()
                c.setFont("Helvetica", 12)
                y = height - 50

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
