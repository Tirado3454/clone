import streamlit as st

def tecnologias_xadrez_page_function():
    """
    Função para exibir o texto sobre o xadrez e as tecnologias, do autômato ao AlphaZero.
    """
    st.title("O Xadrez e as Tecnologias: Do Autômato ao AlphaZero")
    
    st.markdown("""
    O xadrez sempre esteve ligado à inovação tecnológica. Desde os primeiros dispositivos mecânicos do século XVIII até as avançadas inteligências artificiais do século XXI, o jogo tem sido um campo fértil para explorar a criatividade humana e o poder das máquinas. Aqui, traçamos um panorama dessa evolução.

    ### O Autômato Mecânico: O "Turco"
    O marco inicial dessa jornada tecnológica no xadrez remonta ao final do século XVIII, com a criação do **"Turco Mecânico"** (1770) por Wolfgang von Kempelen. Esse dispositivo, apresentado como um autômato capaz de jogar xadrez, era na verdade um truque engenhoso: um jogador humano escondido no interior da máquina controlava as jogadas.

    - **Impacto**: Apesar de ser uma fraude, o "Turco" capturou a imaginação do público e simbolizou o desejo de explorar as capacidades das máquinas.

    ### O Século XIX: Máquinas Reais de Cálculo
    No século XIX, Charles Babbage, criador do conceito de computadores mecânicos, especulou sobre máquinas capazes de jogar xadrez. Esse período marcou o início da busca por dispositivos que pudessem calcular jogadas reais, mas as limitações tecnológicas da época impediram grandes avanços.

    ### O Século XX: A Era dos Computadores
    Com o advento dos computadores eletrônicos no século XX, o xadrez tornou-se um dos principais campos de experimentação para a inteligência artificial.

    **Claude Shannon e Alan Turing**:
    - Em 1949, Claude Shannon publicou um artigo propondo métodos para ensinar computadores a jogar xadrez.
    - Alan Turing, considerado o pai da ciência da computação, desenvolveu o primeiro algoritmo para jogar xadrez em 1950, embora não tivesse computadores poderosos o suficiente para testá-lo.

    **Os Primeiros Programas de Xadrez**:
    - Nos anos 1950 e 1960, surgiram os primeiros programas capazes de jogar xadrez, como o **MacHack** (1966), que já podia vencer jogadores amadores.

    **Deep Blue vs. Garry Kasparov**:
    - O marco mais significativo veio em 1997, quando o supercomputador **Deep Blue**, da IBM, derrotou Garry Kasparov, então campeão mundial, em um match histórico.
    - **Impacto**: Essa vitória simbolizou o avanço das máquinas, capazes de analisar milhões de posições por segundo.

    ### O Século XXI: A Revolução da IA
    Com o avanço das tecnologias de aprendizado de máquina e redes neurais, a abordagem ao xadrez mudou radicalmente no século XXI.

    **Stockfish e os Motores Baseados em Força Bruta**:
    - Motores como o **Stockfish** dominaram o xadrez por muitos anos, baseando-se em algoritmos de força bruta combinados com refinadas funções de avaliação.
    - **Impacto**: Stockfish tornou-se uma ferramenta essencial para jogadores de todos os níveis, ajudando na análise de partidas e no treinamento.

    **AlphaZero: O Jogo Reinventado**:
    - Em 2017, a DeepMind, uma subsidiária da Alphabet (Google), introduziu o **AlphaZero**, uma IA baseada em aprendizado por reforço.
    - Diferentemente dos motores tradicionais, AlphaZero aprendeu a jogar xadrez sem conhecimento prévio humano, apenas jogando contra si mesmo.
    - **Resultado**: AlphaZero não apenas superou motores como o Stockfish, mas também revolucionou o estilo de jogo com ideias criativas e estratégias não convencionais.

    ### Impacto das Tecnologias no Xadrez
    As tecnologias não apenas mudaram a maneira como jogamos, mas também como aprendemos e entendemos o xadrez:

    - **Treinamento e Estudo**:
        Motores como Stockfish e Leela Chess Zero ajudaram jogadores a melhorar suas habilidades, oferecendo análises precisas e sugestões de jogadas.

    - **A Popularização do Jogo**:
        Plataformas online como Chess.com e Lichess utilizam motores para oferecer partidas justas, análises automáticas e conteúdo educacional.

    - **Novos Horizontes**:
        A IA continua a inspirar novas formas de abordar o xadrez, desde a geração de problemas até a criação de variantes criativas do jogo.

    ### Conclusão
    A evolução do xadrez e das tecnologias reflete a busca contínua da humanidade por superar limites. Do "Turco Mecânico" ao AlphaZero, cada avanço nos mostrou novas possibilidades, inspirando tanto jogadores quanto cientistas. O futuro do xadrez está intrinsecamente ligado à inovação, e o que aprendemos com as máquinas continuará a moldar o jogo por muitos anos.
    """)

    st.info("Para mais detalhes sobre a relação entre xadrez e tecnologia, explore os recursos disponíveis nas seções de Referências e Estudos.")
