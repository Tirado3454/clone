import streamlit as st

def artigos_page_function():
    st.title("Explorando o Impacto do Xadrez no Desenvolvimento Cognitivo, Educacional e Estratégico")

    artigos = [
        {
            "referencia": "ACIEGO, R.; GARCIA, L.; BETANCORT, M. Efectos del método de entrenamiento en ajedrez, entrenamiento táctico versus formación integral, en las competencias cognitivas y sociopersonales de los escolares. Universitas Psychologica, 2016, 15(1), 165-176. DOI: 10.11144/Javeriana.upsy15-1.emea.",
            "resumo": "O estudo compara os efeitos do treinamento tático de xadrez com uma formação integral nas competências cognitivas e sociopessoais dos escolares."
        },
        {
            "referencia": "BART, W. M. On the effect of chess training on scholastic achievement. Frontiers in Psychology, 2014, v.5, p.1-3. DOI: 10.3389/fpsyg.2014.00762.",
            "resumo": "Analisa o impacto do treinamento de xadrez no desempenho acadêmico, sugerindo que ele contribui para habilidades cognitivas e escolares."
        },
        {
            "referencia": "BILALIĆ, M.; MCLEOD, P.; GOBET, F. Why good thoughts block better ones: the mechanism of the pernicious Einstellung (set) effect. Cognition, 2008.",
            "resumo": "Explora o efeito Einstellung, que descreve como ideias boas podem bloquear soluções melhores durante a tomada de decisão."
        },
        # Continue listando os outros artigos...
    ]

    for i, artigo in enumerate(artigos, 1):
        st.subheader(f"{i}.")
        st.markdown(f"**Referência:** {artigo['referencia']}")
        st.markdown(f"**Resumo:** {artigo['resumo']}")
