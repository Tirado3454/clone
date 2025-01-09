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
        # Código de exportação (mantido como está)

# Menu de planejamento
elif menu_type == "Planejamento":
    st.title("Planejamento de Aula com o Método Hipotético-Dedutivo")
    # Insira aqui o formulário de planejamento de aula
    professor = st.text_input("Nome do Professor")
    disciplina = st.text_input("Disciplina")
    duracao = st.text_input("Duração da Aula")
    numero_alunos = st.number_input("Número de Alunos", min_value=1, step=1)
    tema = st.text_input("Tema", help="Descreva o tema central da aula.")
    
    st.header("Competências e Habilidades")
    competencias = st.text_area("Competências de Área", help="Liste as competências gerais.")
    habilidades = st.text_area("Habilidades", help="Defina as habilidades específicas.")

    st.header("Conteúdo e Recursos")
    conteudo = st.text_area("Conteúdo", help="Detalhe os conteúdos abordados.")
    recursos = st.text_area("Recursos", help="Liste os materiais necessários.")

    st.header("Objetivo Específico para o Método Hipotético-Dedutivo")
    objetivo_mhd = st.text_area("Defina o objetivo específico", help="Explique como o MHD será aplicado.")

    st.header("Etapas do Método Hipotético-Dedutivo")
    observacao = st.text_area("Observação", help="O que os alunos devem observar?")
    hipotese = st.text_area("Hipótese", help="Que hipóteses devem ser formuladas?")
    deducao = st.text_area("Dedução", help="Como as hipóteses serão analisadas?")
    teste_experimental = st.text_area("Teste Experimental", help="Como as hipóteses serão testadas?")
    analise_consolidacao = st.text_area("Análise e Consolidação", help="Como os resultados serão analisados?")
    
    st.header("Organização dos Espaços")
    atividade_espaco1 = st.text_area("Espaço 1: Atividade", help="Atividade inicial da aula.")
    atividade_espaco2 = st.text_area("Espaço 2: Atividade", help="Atividade intermediária.")
    atividade_espaco3 = st.text_area("Espaço 3: Atividade", help="Atividade final.")

    st.header("Avaliação")
    avaliacao_objetivos = st.text_area("Avaliação dos Objetivos", help="Como verificar se os objetivos foram cumpridos?")
    avaliacao_feedback = st.text_area("Avaliação da Aula", help="Aspectos positivos e negativos.")

    if st.button("Salvar Planejamento"):
        st.success("Planejamento salvo com sucesso!")
