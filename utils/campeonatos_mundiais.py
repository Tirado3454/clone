import streamlit as st

def campeonatos_mundiais_page_function():
    """
    Função para exibir o texto sobre a evolução do desempenho nos Campeonatos Mundiais de Xadrez.
    """
    st.title("Campeonatos Mundiais: Evolução do Desempenho e Precisão")
    
    st.markdown("""
    Os Campeonatos Mundiais de Xadrez, desde 1886 até os dias atuais, refletem não apenas o talento dos jogadores, mas também a evolução das técnicas de treinamento, preparação e, mais recentemente, o impacto das tecnologias. Uma análise das partidas ao longo dos anos mostra um aumento constante na precisão dos jogadores, medido em comparação com motores modernos como Stockfish.

    ### Os Primeiros Campeonatos (1886-1930)
    No início, os campeonatos mundiais foram dominados por lendas como **Wilhelm Steinitz**, **Emanuel Lasker** e **José Raúl Capablanca**. Durante esse período:
    - **Precisão Média**: Geralmente variava entre 85% e 93%, conforme analisado por motores modernos.
    - **Estilo de Jogo**: Os jogadores priorizavam o controle posicional e estratégias intuitivas, mas sem a profundidade analítica dos dias atuais.
    - **Impacto do Conhecimento Limitado**: Sem motores ou bases de dados extensas, o conhecimento vinha exclusivamente de livros e análises humanas.

    **Exemplo**:
    - **Steinitz x Zukertort (1886)**: Precisão de 88,2% para Steinitz, um marco inicial para o jogo científico, mas ainda longe dos padrões modernos.

    ### A Era dos Soviéticos (1948-1972)
    Com o domínio da Escola Soviética, jogadores como **Botvinnik**, **Smyslov** e **Petrosian** elevaram o padrão técnico:
    - **Precisão Média**: Subiu para 91%-94%.
    - **Contribuições**: O estudo sistemático das aberturas e finais tornou-se uma prática essencial.
    - **Preparação Coletiva**: Jogadores soviéticos contavam com equipes de analistas, aumentando a profundidade de suas preparações.

    **Exemplo**:
    - **Petrosian x Spassky (1969)**: Petrosian alcançou uma precisão de 94,4%, refletindo a ênfase em estratégias defensivas e posicionais.

    ### A Revolução de Fischer (1972)
    O título mundial de Bobby Fischer contra Boris Spassky marcou um novo paradigma:
    - **Precisão de Fischer**: 93,6%, combinando criatividade tática e precisão técnica.
    - **Impacto**: Fischer revolucionou a preparação individual e destacou a importância de bases de dados de partidas.

    ### A Era Karpov-Kasparov (1975-2000)
    A rivalidade entre **Anatoly Karpov** e **Garry Kasparov** definiu uma nova era no xadrez:
    - **Precisão Média**: Atingiu 94%-95%, refletindo o uso crescente de computadores na preparação.
    - **Estilo de Jogo**:
      - Karpov: Controle posicional e sutileza estratégica.
      - Kasparov: Combinação de agressividade tática e preparo tecnológico.
    - **Exemplo**:
      - **Kasparov x Anand (1995)**: Kasparov obteve 94,8% de precisão, destacando o impacto dos primeiros motores de análise.

    ### A Era da Inteligência Artificial (2000-presente)
    Com o advento de motores como **Stockfish** e **Leela Chess Zero**, o nível técnico dos jogadores atingiu novos patamares:
    - **Precisão Média**: Alcançou 96% ou mais nos matches mais recentes.
    - **Estilo de Jogo**:
      - Os jogadores atuais são altamente influenciados pelas análises dos motores, levando a um jogo mais técnico e calculado.
      - Partidas com menos erros críticos e maior ênfase em estratégias equilibradas.

    **Curiosidade**:
    Até hoje, apenas **duas partidas de Campeonatos Mundiais** registraram uma precisão perfeita (100%) de um jogador:
    1. **Carlsen x Nepomniachtchi** (2021, 7ª partida): Carlsen atingiu 100% de precisão, enquanto Nepomniachtchi alcançou impressionantes 99%.
    2. **Ding Liren x Nepomniachtchi** (2023, 11ª partida): Ding Liren também obteve 100% de precisão, com Nepomniachtchi novamente em 99%.

    ### A Influência das Tecnologias
    O uso de motores no treinamento tornou-se indispensável:
    - **Preparação de Aberturas**: Jogadores utilizam motores para encontrar linhas ideais e explorar novidades teóricas.
    - **Treinamento Técnico**: Análise de partidas com motores ajuda os jogadores a minimizar erros e otimizar sua tomada de decisão.
    - **Estilo Atual**: A proximidade com as análises de motores tornou os jogos mais precisos, mas, segundo alguns, menos criativos.

    ### Conclusão
    A evolução do desempenho nos Campeonatos Mundiais reflete não apenas o talento dos jogadores, mas também o avanço das ferramentas disponíveis. Se no início os jogadores dependiam exclusivamente de sua intuição e estudo manual, hoje eles contam com o apoio de motores e IA para elevar o nível de suas partidas. O resultado é um xadrez cada vez mais preciso e competitivo, que continua a encantar gerações.
    """)

    st.info("Para explorar mais sobre Campeonatos Mundiais, consulte as seções de Referências e análises detalhadas.")
