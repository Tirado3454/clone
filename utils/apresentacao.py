import streamlit as st

def apresentacao_function():
    """
    Função para exibir a página de Apresentação do programa.
    """
    st.title("Descubra o Método Hipotético-Dedutivo: Uma Jornada de Raciocínio e Aprendizado")

    st.header("Seção 1.1 - O que é o Método Hipotético-Dedutivo?")
    st.markdown(
        """
        O Método Hipotético-Dedutivo (MHD) é uma abordagem lógica e sistemática para resolver problemas e explorar questões complexas. 
        Utilizado amplamente nas ciências e em contextos de tomada de decisão, ele se baseia nos seguintes passos fundamentais:

        1. 🔍**Observação**: Identificação de um problema ou situação que precisa de explicação.
        2. **Formulação de Hipóteses**: Criação de suposições ou explicações provisórias para o problema.
        3. **Dedução de Consequências**: Previsão de resultados que podem ser testados com base nas hipóteses.
        4. **Teste e Experimentação**: Verificação das previsões através de experimentos ou análises.
        5. **Conclusão**: Aceitação, rejeição ou reformulação das hipóteses com base nos resultados.

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
