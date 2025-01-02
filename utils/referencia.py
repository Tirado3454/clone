import streamlit as st

def referencia_page_function():
    """
    Função para exibir sugestões de referências organizadas por temas.
    """
    st.title("Sugestões de Referências")
    
    st.markdown("""
    Aqui você encontrará sugestões de leituras organizadas por temas relevantes para o estudo da ciência, metodologia científica e xadrez.
    """)

    # Referências de Ciência
    st.header("Ciência")
    st.markdown("""
    - **BRAGA, Marco; GUERRA, Andreia; REIS, José Claúdio.** Breve história da ciência moderna. Rio de Janeiro: Zahar, 2003.  
    - **CALADO, Jorge.** Haja luz! Uma história da química através de tudo. Lisboa: IST Press, 2012.  
    - **CAMPBELL, M.; HOANE JR, A. J.; HSU, F..** Deep Blue. Artificial Intelligence, 2002. Disponível em: [https://doi.org/10.1016/S0004-3702(01)00129-1](https://doi.org/10.1016/S0004-3702(01)00129-1).  
    - **KUHN, Thomas S.** A estrutura das revoluções científicas. São Paulo: Ed. Perspectiva, 1970.  
    - **POPPER, Karl.** A lógica da pesquisa científica. São Paulo: Cultrix, 1972.  
    - **FEYERABEND, Paul.** Contra o método. Rio de Janeiro: Francisco Alves, 1977.  
    """)

    # Referências de Metodologia Científica
    st.header("Metodologia Científica")
    st.markdown("""
    - **KUHN, Thomas S.** A estrutura das revoluções científicas. São Paulo: Ed. Perspectiva, 1970.  
    - **LAKATOS, Imre.** La metodologia de los programas de investigación científica. Madrid: Alianza, 1989.  
    - **POPPER, Karl.** A lógica da pesquisa científica. São Paulo: Cultrix, 1972.  
    - **FEYERABEND, Paul.** Contra o método. Rio de Janeiro: Francisco Alves, 1977.  
    """)

    # Referências de Xadrez
    st.header("Xadrez")
    st.markdown("""
    - **ALEKHINE, A.** Alekhine - Mis mejores partidas 1908-1923. Madrid: Editorial la casa del ajedrez, 2001a.  
    - **BECKER, I.** Manual de xadrez. São Paulo: Nobel, 2002.  
    - **BOTVINNIK, Mikhail.** Secretos de estrategia magistral en ajedrez. Buenos Aires: Grabo, 1942.  
    - **CAPABLANCA, J. R.** Chess Fundamentals. New York: Haarcourt, Brace and Company, 1934.  
    - **KARPOV, A.** Mis mejores partidas. Barcelona: Editorial Hispano Europea, S. A., 2009.  
    - **KASPAROV, Garry.** Meus grandes predecessores 1: uma história moderna sobre o desenvolvimento do jogo de xadrez. Santana de Parnaíba: Solis, 2016.  
    - **NIMZOWITSCH, A.** Mi sistema. Madrid: La Casa del Ajedrez, 2006.  
    """)
