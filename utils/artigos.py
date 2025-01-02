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
        {
            "referencia": "CAMPITELLI, G.; GOBET, F. Adaptive Expert Decision Making: Skilled Chess Players Search More and Deeper. ICGA Journal, 2004, 27, 209-216. DOI: 10.3233/ICG-2004-27403.",
            "resumo": "Estudo que analisa como jogadores de xadrez adaptam estratégias ao buscar decisões mais profundas e eficazes."
        },
        {
            "referencia": "CHASSY, P. et al. Intuition in chess: a study with world-class players. Psychological Research, 2023, 87, 2380–2389. DOI: 10.1007/s00426-023-01823-x.",
            "resumo": "Investiga como a intuição opera em jogadores de xadrez de classe mundial, destacando sua importância para decisões rápidas."
        },
        {
            "referencia": "DEVINE, S.; OTTO, A. R. Information about task progress modulates cognitive demand avoidance. Cognition, 2022. DOI: 10.1016/j.cognition.2022.105107.",
            "resumo": "Explora como informações sobre o progresso de uma tarefa influenciam a tendência de evitar demandas cognitivas."
        },
        {
            "referencia": "GOBET, F.; SALA, G. Cognitive Training: A Field in Search of a Phenomenon. Perspectives on Psychological Science, 2023, 18(1), 125-141. DOI: 10.1177/17456916221091830.",
            "resumo": "Revisão crítica sobre a eficácia do treinamento cognitivo e seu impacto no desenvolvimento intelectual."
        },
        {
            "referencia": "KÜCHELMANN, T. et al. Expertise-dependent perceptual performance in chess tasks with varying complexity. Psychological Research, 2022. DOI: 10.1007/s00426-022-01823-x.",
            "resumo": "Examina o desempenho perceptual em tarefas de xadrez de complexidade variada com base no nível de expertise."
        },
        {
            "referencia": "MCGRATH, T. et al. Acquisition of chess knowledge in AlphaZero. PNAS, 2022, 119(47). DOI: 10.1073/pnas.2206625119.",
            "resumo": "Analisa como a inteligência artificial AlphaZero adquire conhecimento de xadrez por meio de aprendizado autônomo."
        },
        {
            "referencia": "PEREIRA, K. O Raciocínio Abdutivo no Jogo de Xadrez: A Contribuição do Conhecimento, Intuição e Consciência da Situação para o Processo Criativo. Florianópolis: UFSC, 2010.",
            "resumo": "Investiga como o raciocínio abdutivo contribui para a criatividade no xadrez."
        },
        {
            "referencia": "POSTONI, D. I.; VANDENKIEBOOM, K. K. The Effect of Chess on Standardized Test Score Gains. SAGE Open, 2019, p.1-22.",
            "resumo": "Avalia o impacto do xadrez no aumento dos resultados de testes padronizados em estudantes."
        },
        {
            "referencia": "SALA, G.; GOBET, F. Do the benefits of chess instruction transfer to academic and cognitive skills? A meta-analysis. Educational Research Review, 2016, p.46-57.",
            "resumo": "Meta-análise sobre se os benefícios do ensino de xadrez se transferem para habilidades acadêmicas e cognitivas."
        },
        {
            "referencia": "SILVA, W. Xadrez e educação: contribuições da ciência para o uso do jogo como instrumento pedagógico. Curitiba: UFPR, 2012.",
            "resumo": "Explora as contribuições do xadrez como ferramenta educacional e suas aplicações pedagógicas."
        },
        {
            "referencia": "TIRADO, A.; PILATTI, L. Integration of the scientific method in chess teaching. Main Issues of Pedagogy And Psychology, 2024, 11(2), 61–83.",
            "resumo": "Propõe a integração do método científico no ensino do xadrez, destacando benefícios pedagógicos."
        },
        {
            "referencia": "TIRADO, A.; PILATTI, L. O papel da IA no xadrez: benefícios e malefícios e implicações pedagógicas. Revista Caderno Pedagógico, 2024, 21(9), 1-22. DOI: 10.54033/cadpedv21n9-319.",
            "resumo": "Examina os benefícios e malefícios da IA no xadrez e suas implicações na educação."
        },
        {
            "referencia": "TIRADO, A. S. B.; PAGANI, R. N. Análise bibliográfica sobre xadrez e educação: utilização. Revista Mundi Engenharia, Tecnologia e Gestão, 2021, p.322-01, 322-25.",
            "resumo": "Revisão sobre a aplicação do xadrez na educação e suas contribuições acadêmicas."
        },
        {
            "referencia": "TIRADO, A. S. B.; BRUSAMOLIN, V. Análise funcional do website Lichess e a viabilidade para o ensino híbrido. Revista Mundi, 2021, 6(1), 321-01, 321-17.",
            "resumo": "Avalia o potencial do site Lichess para o ensino híbrido no contexto educacional."
        },
    ]

    for i, artigo in enumerate(artigos, 1):
        st.subheader(f"{i}.")
        st.markdown(f"**Referência:** {artigo['referencia']}")
        st.markdown(f"**Resumo:** {artigo['resumo']}")
