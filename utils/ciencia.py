import streamlit as st

def historia_ciencia_page_function():
    """
    Função para exibir a página de História da Ciência.
    """
    # Título principal
    st.title("A Evolução da Ciência ao Longo da História")
    
    # Subtítulo introdutório
    st.subheader("Uma Jornada pelo Desenvolvimento do Conhecimento Científico")
    
    # Antiguidade
    st.header("Antiguidade: Ciência como Contemplação")
    st.markdown("""
    Na Grécia Antiga, a ciência (*episteme*) era vista como um conhecimento contemplativo, distinto da prática ou do saber empírico. Filósofos como **Platão** e **Aristóteles** defendiam que o objetivo da ciência era alcançar a verdade universal por meio da razão.
    
    **Exemplo**: Aristóteles estudou o movimento dos corpos celestes e desenvolveu a teoria dos "quatro elementos" (terra, água, fogo e ar), que influenciaria o pensamento científico por séculos.
    """)

    # Idade Média
    st.header("Idade Média: Ciência e Fé")
    st.markdown("""
    Durante a Idade Média, a ciência foi fortemente influenciada pela religião. A busca pelo conhecimento era vista como um meio de compreender a obra divina. **Tomás de Aquino**, por exemplo, integrou o pensamento aristotélico com o cristianismo, enfatizando que a razão e a fé eram compatíveis.
    
    **Exemplo**: A astronomia de **Ptolomeu**, preservada e estudada por estudiosos medievais, reforçou a visão geocêntrica do universo, compatível com a visão teológica da época.
    """)

    # Renascimento
    st.header("Renascimento: O Nascimento da Ciência Moderna")
    st.markdown("""
    Com o Renascimento (séculos XV e XVI), houve uma ruptura com as concepções medievais. O humanismo colocou o ser humano no centro do conhecimento, e o método experimental começou a ganhar destaque. **Galileu Galilei** é considerado o pai da ciência moderna por enfatizar a observação empírica e o uso da matemática para descrever fenômenos naturais.
    
    **Exemplo**: Galileu utilizou telescópios para observar luas orbitando Júpiter, o que desafiava o modelo geocêntrico e apoiava a teoria heliocêntrica de Copérnico.
    """)

    # Século XVII
    st.header("Século XVII: A Revolução Científica")
    st.markdown("""
    O século XVII trouxe grandes avanços com a chamada Revolução Científica. **Francis Bacon** propôs o **método indutivo**, baseado na observação e na experimentação, enquanto **René Descartes** enfatizou o **método dedutivo**, fundado na lógica e no raciocínio matemático. **Isaac Newton**, por sua vez, unificou essas abordagens ao formular as leis do movimento e da gravitação universal.
    
    **Exemplo**: O trabalho de Isaac Newton na publicação de **"Principia Mathematica"** (1687) estabeleceu as leis da gravitação universal, revolucionando a física e a astronomia.
    """)

    # Séculos XVIII e XIX
    st.header("Séculos XVIII e XIX: A Ciência como Progresso")
    st.markdown("""
    Durante o Iluminismo (século XVIII), a ciência foi exaltada como motor do progresso humano. O positivismo, defendido por **Auguste Comte**, estabeleceu que a ciência deveria ser baseada em fatos observáveis e mensuráveis, rejeitando especulações metafísicas. No século XIX, teorias como a **evolução de Darwin** e a **termodinâmica** reforçaram a ideia de que a ciência poderia desvendar as leis fundamentais da natureza.
    
    **Exemplo**: A teoria da evolução por seleção natural, proposta por **Charles Darwin** em seu livro **"A Origem das Espécies"** (1859), transformou profundamente a biologia e a visão sobre a vida na Terra.
    """)

    # Século XX
    st.header("Século XX: Questionamentos e a Nova Concepção de Ciência")
    st.markdown("""
    O século XX foi marcado por mudanças profundas na compreensão da ciência. O **falsificacionismo** de **Karl Popper** redefiniu o método científico, argumentando que uma teoria científica só é válida se puder ser falsificada por experimentos. Por outro lado, pensadores como **Thomas Kuhn** introduziram a ideia de que a ciência avança por meio de "revoluções científicas", com mudanças de paradigmas que desafiam o conhecimento estabelecido.
    
    **Exemplo**: A teoria da relatividade geral de **Albert Einstein** (1915) desafiou as ideias newtonianas, revolucionando a física ao descrever o espaço-tempo e a gravidade de forma inédita.
    """)

    # Ciência Atual
    st.header("O que é Ciência Hoje?")
    st.markdown("""
    Atualmente, a ciência é entendida como um processo dinâmico e coletivo, fundamentado em:
    - **Observação e experimentação**: Coleta sistemática de dados para entender fenômenos.
    - **Formulação de hipóteses**: Propostas explicativas que podem ser testadas.
    - **Falsificabilidade**: A capacidade de uma teoria ser refutada é essencial.
    - **Revisão por pares**: O conhecimento científico é validado por especialistas antes de ser aceito.
    - **Interdisciplinaridade**: A ciência atual é colaborativa, integrando diferentes áreas do saber.

    **Exemplo**: O Projeto Genoma Humano (1990-2003), que envolveu cientistas de várias disciplinas e países, exemplifica a ciência moderna como um esforço colaborativo e interdisciplinar.
    """)

    st.info("A ciência é um processo em constante evolução, que busca não apenas entender o mundo, mas também melhorar a vida humana e enfrentar desafios globais.")

