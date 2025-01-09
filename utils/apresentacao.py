import streamlit as st

def apresentacao_function():
    """
    Função para exibir a página de Apresentação do programa.
    """
    # Logotipos no topo
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("images/capes.png", width=120, caption="CAPES")  # Logo da CAPES
    with col2:
        st.image("images/ppgect.png", width=120, caption="PPGECT")  # Logo do PPGECT
    with col3:
        st.image("images/utfpr.png", width=120, caption="UTFPR")  # Logo da UTFPR

    # Título principal abaixo dos logotipos
    st.markdown(
        """
        <h1 style="text-align: center; color: #4CAF50;">Ensino de Ciência e Xadrez</h1>
        <p style="text-align: center; color: #555;">Uma abordagem inovadora que conecta raciocínio lógico e método científico</p>
        """,
        unsafe_allow_html=True
    )

    # Introdução
    st.markdown(
        """
        <h2 style="text-align: center; color: #4CAF50;">Apresentação</h2>
        <p style="text-align: justify; color: #555;">
        Este material foi desenvolvido como parte de uma pesquisa de doutorado conduzida no 
        <b>Programa de Pós-Graduação em Ensino de Ciência e Tecnologia (PPGECT)</b> da 
        <b>Universidade Tecnológica Federal do Paraná (UTFPR)</b>, Campus Ponta Grossa. A pesquisa abordou a interseção entre educação, ciência e xadrez, enfatizando o papel dos professores como mediadores no processo de aprendizagem.
        </p>
        <p style="text-align: justify; color: #555;">
        O xadrez, aqui apresentado, é explorado como uma ferramenta pedagógica poderosa, 
        capaz de desenvolver o pensamento crítico, a alfabetização científica e o raciocínio lógico dos estudantes. Este material propõe uma abordagem prática e inovadora que conecta o método científico ao raciocínio enxadrístico, permitindo que temas específicos sejam explorados de forma lúdica e significativa.
        </p>
        <p style="text-align: justify; color: #555;">
        Por exemplo, o <b>método hipotético-dedutivo</b> é aplicado ao jogo de xadrez: cada movimento no tabuleiro é tratado como uma hipótese que deve ser testada e ajustada conforme as reações do adversário.
        </p>
        <p style="text-align: justify; color: #555;">
        Este eBook foi especialmente pensado para professores, oferecendo ferramentas e estratégias práticas que integram o xadrez ao ensino de conceitos científicos e estratégicos. O objetivo é proporcionar uma experiência interativa que conecte os estudantes ao método científico, promovendo o desenvolvimento de habilidades fundamentais para a vida acadêmica e além.
        </p>
        <p style="text-align: justify; color: #555;">
        Gostaríamos de expressar nosso especial agradecimento ao <b>Professor Doutor Luiz Pilatti</b>, pela orientação e valiosas contribuições ao longo do desenvolvimento deste trabalho.
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")  # Divisor para separar a introdução das seções principais

    st.header("Seção 1.1 - O que é o Método Hipotético-Dedutivo?")
    st.markdown(
        """
        O Método Hipotético-Dedutivo (MHD) é uma abordagem lógica e sistemática para resolver problemas e explorar questões complexas. 
        Utilizado amplamente nas ciências e em contextos de tomada de decisão, ele se baseia nos seguintes passos fundamentais:

        1. 🔍**Observação**: Identificação de um problema ou situação que precisa de explicação.
        2. 💡**Formulação de Hipóteses**: Criação de suposições ou explicações provisórias para o problema.
        3. 🧪**Dedução de Consequências**: Previsão de resultados que podem ser testados com base nas hipóteses.
        4. 📊**Teste e Experimentação**: Verificação das previsões através de experimentos ou análises.
        5. 📘**Conclusão**: Aceitação, rejeição ou reformulação das hipóteses com base nos resultados.

        **Exemplo Prático:**
        Imagine que você está jogando xadrez e quer prever o resultado de um movimento estratégico. Usando o MHD:

        - **Observação**: "Meu oponente está posicionando suas peças em uma linha defensiva."
        - **Hipótese**: "Se eu atacar pelo flanco direito, posso quebrar essa defesa."
        - **Dedução**: "Ao mover minha torre e bispo, vou forçar o rei adversário a sair de sua posição."
        - **Teste**: Faça o movimento e avalie a resposta do oponente.
        - **Conclusão**: Refine sua estratégia com base no resultado do teste.
        """
    )

    st.header("Seção 1.2 - Objetivos do Programa")
    st.markdown(
        """
        Nosso programa foi desenvolvido para:

        - Guiar você na aplicação prática do Método Hipotético-Dedutivo, seja na resolução de problemas científicos ou no contexto do xadrez.
        - Promover o desenvolvimento de habilidades de pensamento crítico e lógico.
        - Fornecer ferramentas interativas, como um editor de tabuleiro e banco de frases, para facilitar sua análise e organização de ideias.
        - Permitir que você registre, organize e exporte suas descobertas e análises.
        """
    )

    st.header("Seção 1.3 - Público-Alvo")
    st.markdown(
        """
        Este programa é ideal para:

        - **Educadores e estudantes**: Que desejam explorar o método em contextos educacionais.
        - **Pesquisadores e profissionais**: Que aplicam o raciocínio hipotético-dedutivo em sua rotina.
        - **Jogadores de xadrez**: Interessados em aprofundar a análise estratégica por meio de uma abordagem lógica e sistemática.
        - **Curiosos e entusiastas do raciocínio lógico**: Que buscam aprimorar suas habilidades analíticas.
        """
    )

    st.header("Seção 1.4 - Benefícios do Método Hipotético-Dedutivo")
    st.markdown(
        """
        **Lista de Benefícios:**

        - Desenvolvimento de pensamento estruturado.
        - Melhor capacidade de prever e testar cenários complexos.
        - Maior compreensão e organização de ideias.
        - Aplicação prática em diversas áreas, da ciência ao xadrez.
        """
    )

if __name__ == "__main__":
    apresentacao()
