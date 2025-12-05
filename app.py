import streamlit as st

# -------------------------------------
# CONFIGURAÇÃO DA PÁGINA
# -------------------------------------
st.set_page_config(
    page_title="Phoenix Strategy – O Algoritmo Genial",
    page_icon="🔥",
    layout="wide"
)

# -------------------------------------
# CSS CUSTOMIZADO (NEON + CARDS GRADIENTE)
# -------------------------------------
Phoenix_CSS = """
<style>

body, .stApp {
    background-color: #030303;
    color: #D7D7D7;
    font-family: "Inter", -apple-system, BlinkMacSystemFont, sans-serif;
}

/* TITULOS NEON */
h1, h2, h3 {
    color: #00FF7F;
    font-weight: 700;
}

/* SUBTÍTULOS LARANJA */
.orange-tag {
    color: #FF7A1A;
    text-transform: uppercase;
    font-size: 0.9rem;
    letter-spacing: 0.12em;
}

/* BLOCO CENTRAL */
.main-block {
    max-width: 950px;
    margin: 0 auto;
}

/* DIVISOR */
.section-divider {
    border-bottom: 1px solid rgba(255,255,255,0.08);
    margin: 3rem 0 2rem 0;
}

/* BOTÃO NEON */
.stButton>button {
    background: linear-gradient(90deg, #00FF7F, #FF7A1A);
    color: black;
    border-radius: 999px;
    padding: 0.7rem 2rem;
    border: none;
    font-weight: 700;
    cursor: pointer;
    transition: 0.25s ease-in-out;
}
.stButton>button:hover {
    transform: scale(1.03);
    filter: brightness(1.2);
}

/* IMG LOGO CENTRALIZADA */
.logo-container {
    text-align: center;
    margin-bottom: 2rem;
}

/* CARDS ESTILO B (gradiente Phoenix) */
.phoenix-card {
    padding: 1.5rem;
    border-radius: 18px;
    background: radial-gradient(circle at top left, rgba(255,120,20,0.40), rgba(0,255,140,0.07));
    border: 1px solid rgba(0,255,120,0.25);
    transition: 0.25s ease-in-out;
}
.phoenix-card:hover {
    transform: translateY(-4px) scale(1.02);
    box-shadow: 0 0 18px rgba(255,100,20,0.7);
    border: 1px solid rgba(0,255,120,0.55);
}

/* LISTAS */
ul {
    padding-left: 1.3rem;
}

</style>
"""
st.markdown(Phoenix_CSS, unsafe_allow_html=True)

# -------------------------------------
# LOGO
# -------------------------------------
st.markdown("<div class='logo-container'>", unsafe_allow_html=True)
st.image("Phoenix_logo.png", width=240)
st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------------
# HERO SECTION
# -------------------------------------
st.markdown("<div class='main-block'>", unsafe_allow_html=True)

st.markdown("<div class='orange-tag'>PLATAFORMA QUANT</div>", unsafe_allow_html=True)
st.markdown("## PHOENIX STRATEGY")
st.markdown("### O algoritmo genial.")

st.markdown(
    """
Um novo padrão nasceu.  
A fusão perfeita entre a genialidade humana e a precisão algorítmica.  
O poder de análise que antes era privilégio de poucos — agora renascido em tecnologia.
"""
)

if st.button("ACESSAR PLATAFORMA"):
    st.markdown(
        "<meta http-equiv='refresh' content='0; url=https://phoenix-master.onrender.com/dashboard_geral'/>",
        unsafe_allow_html=True
    )

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# -------------------------------------
# SEÇÃO: O QUE É A PHOENIX STRATEGY
# -------------------------------------
st.markdown("## O que é a Phoenix Strategy?")

st.markdown(
    """
A **Phoenix Strategy** é a evolução da análise técnica:  
um sistema capaz de monitorar **300+ ativos a cada 5 minutos**, identificar padrões,  
prever movimentos e entregar **o momento exato de entrada e saída** — em tempo real.
"""
)

st.markdown(
    """
O que seria humanamente impossível, mesmo reunindo os maiores **gênios** da história,  
agora acontece em **segundos**.

Porque quando a genialidade se transforma em algoritmo,  
**nasce precisão absoluta.**
"""
)

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# -------------------------------------
# SEÇÃO 3 — OS GÊNIOS
# -------------------------------------
st.markdown("## A genialidade dos mestres, ressignificada em algoritmo")

cols = st.columns(2)

with cols[0]:
    st.markdown(
        """
        - **Charles Dow**, o visionário da tendência  
        - **Richard Wyckoff**, o decodificador do fluxo  
        - **Welles Wilder**, o engenheiro matemático da volatilidade  
        """
    )

with cols[1]:
    st.markdown(
        """
        - **Al Brooks**, o refinamento máximo do price action  
        - **Gênios que mudaram tudo**  
        - E que agora renascem em forma algorítmica  
        """
    )

st.markdown(
    """
A **Phoenix Strategy** honra esses gênios — e os leva além do possível.
"""
)

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# -------------------------------------
# SEÇÃO 4 — O ALGORITMO GENIAL (CARDS)
# -------------------------------------
st.markdown("## O algoritmo genial™")

cards = st.columns(3)

with cards[0]:
    st.markdown("<div class='phoenix-card'>", unsafe_allow_html=True)
    st.markdown("### Precisão")
    st.markdown("Detecta padrões invisíveis ao olho humano.")
    st.markdown("</div>", unsafe_allow_html=True)

with cards[1]:
    st.markdown("<div class='phoenix-card'>", unsafe_allow_html=True)
    st.markdown("### Velocidade")
    st.markdown("Analisa dezenas de variáveis em segundos.")
    st.markdown("</div>", unsafe_allow_html=True)

with cards[2]:
    st.markdown("<div class='phoenix-card'>", unsafe_allow_html=True)
    st.markdown("### Inteligência")
    st.markdown("Atualiza e aprimora decisões a cada novo dado.")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# -------------------------------------
# SEÇÃO 5 — VELOCIDADE
# -------------------------------------
st.markdown("## Velocidade que humanos não alcançam")

st.markdown(
    """
Enquanto um analista acompanha **3 a 5 ativos**,  
o algoritmo monitora **300+ simultaneamente** — sem cansaço, sem erro.
"""
)

st.markdown(
    """
Ele não pisca.  
Ele não hesita.  
Ele não esquece.

Ele apenas calcula, compara, detecta, decide.
"""
)

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# -------------------------------------
# SEÇÃO 6 — RESULTADOS
# -------------------------------------
st.markdown("## Resultados em tempo real")

st.markdown(
    """
A Phoenix Strategy entrega:

- Sinais instantâneos  
- Análises contínuas  
- Insights algorítmicos  
- Fluxo decodificado  
- Probabilidade a favor  
"""
)

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# -------------------------------------
# FINAL SECTION
# -------------------------------------
st.markdown("## Pronto para ver o algoritmo genial em ação?")
st.markdown("### PHOENIX STRATEGY · O algoritmo genial.")

st.button("ACESSAR A PLATAFORMA")
st.markdown("</div>", unsafe_allow_html=True)
