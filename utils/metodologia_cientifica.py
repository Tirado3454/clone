import streamlit as st

def metodologia_cientifica_page_function():
    """
    Função para exibir a página sobre os mitos de Bacon, Popper e outros pensadores.
    """
    st.title("Metodologia Científica: Dos Mitos de Bacon ao Falsificacionismo")
    
    st.markdown("""
    Neste texto, exploramos as contribuições de grandes pensadores para a metodologia científica, incluindo os mitos de Bacon, o falsificacionismo de Popper e outros conceitos significativos.
    """)

    # Seção sobre Francis Bacon
    st.header("Francis Bacon e os Ídolos da Mente")
    st.markdown("""
    **Francis Bacon** identificou quatro tipos de preconceitos que distorcem a busca pelo conhecimento científico:

    - **Ídolos da Tribo**: Tendências naturais humanas, como confiar cegamente nos sentidos.  
      **Exemplo**: Acreditar que o Sol gira ao redor da Terra apenas pela observação visual.

    - **Ídolos da Caverna**: Preconceitos pessoais baseados em experiências individuais.  
      **Exemplo**: Um cientista que rejeita evidências contraditórias às suas crenças anteriores.

    - **Ídolos do Mercado**: Problemas causados pela linguagem imprecisa.  
      **Exemplo**: Uso incorreto de termos científicos no debate público.

    - **Ídolos do Teatro**: Aceitação de dogmas tradicionais sem questionamento.  
      **Exemplo**: A manutenção do modelo geocêntrico por séculos devido à autoridade da Igreja.
    """)

    # Seção sobre Karl Popper
    st.header("Karl Popper e o Falsificacionismo")
    st.markdown("""
    **Karl Popper** argumentou que uma teoria científica deve ser testável e falsificável. Ele destacou a importância de refutar teorias, em vez de apenas confirmá-las.

    - **Exemplo**: A teoria da relatividade de Einstein foi testada durante um eclipse solar em 1919. Embora confirmada, ela permanece aberta a refutações por novos dados.

    - **Crítica ao Indutivismo**: Popper rejeitou a ideia de que a ciência avança apenas por observação, afirmando que todas as observações são influenciadas por teorias prévias.
    """)

    # Seção sobre Thomas Kuhn
    st.header("Thomas Kuhn e as Revoluções Científicas")
    st.markdown("""
    **Thomas Kuhn** introduziu o conceito de paradigmas, que são modelos amplamente aceitos por comunidades científicas. Quando um paradigma não explica novas evidências, ocorre uma revolução científica.

    - **Exemplo**: A transição do modelo geocêntrico para o heliocêntrico representou uma mudança de paradigma na astronomia.
    """)

    # Conclusão
    st.header("Conclusão")
    st.markdown("""
    A ciência é um empreendimento dinâmico, constantemente influenciado por ideias inovadoras e críticas construtivas. De Bacon a Feyerabend, a história do pensamento científico nos ensina que questionar, testar e adaptar são fundamentais para o progresso do conhecimento.
    """)
