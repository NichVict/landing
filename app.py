import streamlit as st

# -----------------------------
# CONFIGURAÇÃO INICIAL DA PÁGINA
# -----------------------------
st.set_page_config(
    page_title="Phoenix Strategy – O algoritmo genial",
    page_icon="🔥",
    layout="wide"
)

# -----------------------------
# ESTILO CUSTOMIZADO (CSS)
# -----------------------------
CUSTOM_CSS = """
<style>
/* Fundo geral e fonte */
body, .stApp {
    background-color: #050608;
    color: #f2f2f2;
    font-family: -apple-system, BlinkMacSystemFont, system-ui, sans-serif;
}

/* Títulos */
h1, h2, h3, h4 {
    color: #00ff9a; /* neon verde */
    font-weight: 700;
}

/* Texto principal */
p, li {
    font-size: 1.02rem;
    line-height: 1.6;
}

/* Contêiner centralizado */
.main-block {
    max-width: 900px;
    margin: 0 auto;
}

/* Linha divisória customizada */
.section-divider {
    border-bottom: 1px solid rgba(255,255,255,0.08);
    margin: 3rem 0 2rem 0;
}

/* Botão principal */
.stButton>button {
    background: linear-gradient(90deg, #00ff9a, #ff7a1a);
    color: #050608;
    border-radius: 999px;
    border: none;
    padding: 0.6rem 1.8rem;
    font-weight: 700;
    font-size: 1rem;
    cursor: pointer;
    transition: 0.2s ease-in-out;
}

.stButton>button:hover {
    filter: brightness(1.1);
    transform: translateY(-1px);
}

/* Subtítulo hero */
.hero-subtitle {
    font-size: 1.1rem;
    color: #d7d7d7;
    margin-bottom: 0.4rem;
}

/* Slogan */
.hero-slogan {
    font-size: 0.95rem;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #ff7a1a;
    margin-bottom: 1.7rem;
}

/* Caixa levemente destacada */
.highlight-box {
    border-radius: 18px;
    border: 1px solid rgba(0,255,154,0.3);
    background: radial-gradient(circle at top left, rgba(0,255,154,0.12), rgba(5,6,8,0.95));
    padding: 1.5rem 1.6rem;
    margin-top: 1.5rem;
}

/* Bullets customizados */
ul {
    list-style-position: outside;
    padding-left: 1.2rem;
}

/* Pequeno texto em destaque */
.muted {
    color: #b0b0b0;
    font-size: 0.92rem;
}

/* Título menor laranja */
.orange-tag {
    color: #ff7a1a;
    text-transform: uppercase;
    font-size: 0.9rem;
    letter-spacing: 0.12em;
    margin-bottom: 0.2rem;
}
</style>
"""

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# -----------------------------
# LOGO (OPCIONAL)
# -----------------------------
# Se você tiver o arquivo do logo na pasta (ex: "phoenix_logo.png"),
# descomente a linha abaixo e ajuste o nome do arquivo:
#
# st.image("phoenix_logo.png", width=140)


# -----------------------------
# SEÇÃO 1 — HERO (CAPA)
# -----------------------------
st.markdown("<div class='main-block'>", unsafe_allow_html=True)

col1, col2 = st.columns([1.3, 1])

with col1:
    st.markdown("<div class='orange-tag'>PLATAFORMA QUANT</div>", unsafe_allow_html=True)
    st.markdown("## PHOENIX STRATEGY")
    st.markdown("### O algoritmo genial.")

    st.markdown(
        "<p class='hero-subtitle'>"
        "Um novo padrão nasceu. A fusão perfeita entre a genialidade humana e a precisão algorítmica."
        "</p>",
        unsafe_allow_html=True,
    )

    st.markdown(
        "<p>O poder de análise que antes era privilégio de poucos — agora renascido em tecnologia.</p>",
        unsafe_allow_html=True,
    )

    if st.button("ACESSAR PLATAFORMA"):
        # Aqui no futuro você pode redirecionar para um link real
        st.toast("Em breve: acesso à plataforma Phoenix Strategy. 🚀")

with col2:
    # Espaço reservado para o logo grande ou uma imagem do dashboard
    st.empty()
    # Exemplo: st.image("phoenix_dashboard_mock.png", use_column_width=True)

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# -----------------------------
# SEÇÃO 2 — O QUE É O PHOENIX STRATEGY?
# -----------------------------
st.markdown("### O que é a Phoenix Strategy?")

st.markdown(
    """
A **Phoenix Strategy** é a evolução da análise técnica:  
um sistema capaz de monitorar mais de **300 ativos a cada 5 minutos**, encontrar padrões, 
identificar movimentos, antecipar riscos e entregar **o momento exato de entrada e saída** — tudo em tempo real.
"""
)

st.markdown(
    """
O que seria humanamente impossível, mesmo reunindo os **maiores gênios da história**, 
agora acontece em **segundos**.

Porque quando a genialidade se transforma em algoritmo,  
**nasce precisão absoluta.**
"""
)

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# -----------------------------
# SEÇÃO 3 — A GENIALIDADE DOS GÊNIOS
# -----------------------------
st.markdown("### A genialidade dos gênios, ressignificada em algoritmo")

st.markdown(
    """
Os pilares da análise técnica nasceram das mentes de gigantes:

- **Charles Dow**, o visionário da tendência.  
- **Richard Wyckoff**, o decodificador do fluxo.  
- **Welles Wilder**, o engenheiro que criou revoluções matemáticas.  
- **Al Brooks**, a leitura mais refinada do price action moderno.
"""
)

st.markdown(
    """
Cada um deles alterou para sempre a forma como entendemos o mercado.  
Hoje, suas genialidades renascem em forma algorítmica.

A **Phoenix Strategy** honra esses gênios —  
e os leva além do que era possível.
"""
)

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# -----------------------------
# SEÇÃO 4 — O ALGORITMO GENIAL™
# -----------------------------
st.markdown("### O algoritmo genial™")

st.markdown("O coração da plataforma.")

st.markdown(
    """
Um sistema projetado para:

- Detectar padrões invisíveis ao olho humano  
- Analisar dezenas de variáveis simultaneamente  
- Traduzir movimentos do preço em decisões claras  
- Criar probabilidades reais de vantagem  
- Atualizar-se constantemente com novos dados  
"""
)

st.markdown(
    """
Enquanto humanos analisam…  
**o algoritmo já concluiu.**

Enquanto humanos hesitam…  
**o algoritmo já executou.**

Isso é **precisão**.  
Isso é **velocidade**.  
Isso é **genialidade aplicada.**
"""
)

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# -----------------------------
# SEÇÃO 5 — VELOCIDADE QUE HUMANOS NÃO ALCANÇAM
# -----------------------------
st.markdown("### Velocidade que humanos não alcançam")

st.markdown(
    """
Enquanto um analista experiente consegue acompanhar **3, talvez 5 ativos**…  
o **algoritmo genial** monitora **300+ ao mesmo tempo**, sem erro, sem atraso, sem cansaço.
"""
)

st.markdown(
    """
Ele não pisca.  
Ele não esquece.  
Ele não se contradiz.

Ele apenas **calcula, compara, detecta, decide.**
"""
)

st.markdown(
    """
É assim que a genialidade se perpetua.  
É assim que nasce o futuro.
"""
)

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# -----------------------------
# SEÇÃO 6 — RESULTADOS EM TEMPO REAL
# -----------------------------
st.markdown("### Resultados em tempo real")

st.markdown(
    """
A **Phoenix Strategy** entrega:

- Sinais de entrada e saída com precisão  
- Monitoramento contínuo  
- Leitura de fluxo simplificada  
- Insights algorítmicos  
- Interpretação automatizada de price action  
- Probabilidade estatística a favor do trader  
"""
)

st.markdown(
    """
Tudo isso com a mesma lógica que guiou os gênios —  
mas com a **rapidez que eles nunca tiveram**.
"""
)

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# -----------------------------
# SEÇÃO 7 — O RENASCIMENTO DA ANÁLISE TÉCNICA
# -----------------------------
st.markdown("### O renascimento da análise técnica")

st.markdown(
    """
A **Phoenix Strategy** não substitui os gênios.  
Ela **honra, amplifica e perpetua** sua genialidade.
"""
)

st.markdown(
    """
O que eles imaginaram,  
**nós transformamos em algoritmo.**

O que eles definiram,  
**nós levamos ao extremo.**

O que era teoria,  
**agora é execução instantânea.**
"""
)

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# -----------------------------
# SEÇÃO 8 — CHAMADA FINAL
# -----------------------------
st.markdown("### Pronto para ver o algoritmo genial em ação?")

st.markdown(
    """
A genialidade humana nos trouxe até aqui.  
A precisão algorítmica nos levará além.
"""
)

st.markdown("## PHOENIX STRATEGY")
st.markdown("### O algoritmo genial.")

st.button("ACESSAR AGORA")

st.markdown("</div>", unsafe_allow_html=True)
