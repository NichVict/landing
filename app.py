import streamlit as st
from pathlib import Path
import base64
from PIL import Image

# ============================================================
# 1. CONFIGURAÇÃO DA PÁGINA
# ============================================================
st.set_page_config(
    page_title="Phoenix Strategy – O algoritmo genial",
    page_icon="🔥",
    layout="wide"
)

# ============================================================
# 2. CSS — DEIXE SEMPRE ANTES DE TUDO SER RENDERIZADO
# ============================================================
CUSTOM_CSS = """
<style>

/* Fundo geral */
body, .stApp {
    background-color: #050608;
    color: #f2f2f2;
    font-family: -apple-system, BlinkMacSystemFont, system-ui, sans-serif;
}

/* Títulos */
h1, h2, h3, h4 {
    color: #00ff9a;
    font-weight: 700;
}

/* Texto padrão */
p, li {
    font-size: 1.02rem;
    line-height: 1.6;
}

/* Container central */
.main-block {
    max-width: 900px;
    margin: 0 auto;
}

/* Divisores */
.section-divider {
    border-bottom: 1px solid rgba(255,255,255,0.08);
    margin: 3rem 0 2rem 0;
}

/* ================================
   BOTÃO DE LINK (st.link_button)
================================ */
a[kind="secondary"], a[kind="primary"] {
    display: inline-block;
    border: 2px solid #00ff9a;
    color: #ff7a1a !important;
    background: transparent !important;
    padding: 0.55rem 1.7rem;
    border-radius: 999px;
    font-weight: 700;
    font-size: 1rem;
    text-decoration: none !important;
    cursor: pointer;
    transition: 0.18s ease-in-out;
}

a[kind="secondary"]:hover,
a[kind="primary"]:hover {
    box-shadow: 0 0 12px #00ff9a;
    transform: translateY(-2px);
}

/* Botões normais (se forem usados em outros locais) */
.stButton>button {
    background: linear-gradient(90deg, #00ff9a, #ff7a1a);
    color: #050608 !important;
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

/* SUBTÍTULOS */
.hero-subtitle {
    font-size: 1.1rem;
    color: #d7d7d7;
    margin-bottom: 0.4rem;
}

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

# ============================================================
# 3. FUNÇÃO DE IMAGEM CIRCULAR COM NEON
# ============================================================
def circular_image(path, size=120):
    if not Path(path).exists():
        return ""

    img_bytes = Path(path).read_bytes()
    img_b64 = base64.b64encode(img_bytes).decode()

    return f"""
    <div style="
        width:{size}px;
        height:{size}px;
        border-radius:50%;
        overflow:hidden;
        margin:12px 0 18px 0;
        border:3px solid #00ff9a;
        box-shadow:0 0 15px rgba(0,255,154,0.8);
    ">
        <img src="data:image/png;base64,{img_b64}"
             style="width:100%;height:100%;object-fit:cover;filter:grayscale(100%);">
    </div>
    """

# ============================================================
# 4. LOGO DA PHOENIX (CORRETO E ALINHADO À ESQUERDA)
# ============================================================
try:
    logo = Image.open("Phoenix_logo.png")
    st.markdown(
        """
        <div style="display:flex; align-items:center; justify-content:flex-start; margin:10px 0 25px 0;">
        """,
        unsafe_allow_html=True
    )
    st.image(logo, width=200)
    st.markdown("</div>", unsafe_allow_html=True)
except:
    st.warning("⚠️ Logo não encontrado: coloque Phoenix_logo.png na mesma pasta do app.py")


# ============================================================
# 5. INÍCIO DO BLOCO PRINCIPAL
# ============================================================
st.markdown("<div class='main-block'>", unsafe_allow_html=True)

# ============================================================
# 6. HERO
# ============================================================
col1, col2 = st.columns([1.3, 1])

with col1:
    st.markdown("<div class='orange-tag'>PLATAFORMA QUANT</div>", unsafe_allow_html=True)
    st.markdown("## PHOENIX STRATEGY")
    st.markdown("### O algoritmo genial.")
    st.markdown("<p class='hero-subtitle'>Um novo padrão nasceu. A fusão perfeita entre a genialidade humana e a precisão algorítmica.</p>", unsafe_allow_html=True)
    st.markdown("<p>O poder de análise que antes era privilégio de poucos — agora renascido em tecnologia.</p>", unsafe_allow_html=True)

    st.link_button(
        "ACESSAR PLATAFORMA",
        "https://phoenix-master.onrender.com/dashboard_geral"
    )

with col2:
    st.empty()

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# ============================================================
# 7. O QUE É O PHOENIX STRATEGY?
# ============================================================
st.markdown("### O que é a Phoenix Strategy?")
st.markdown("""
A **Phoenix Strategy** é a evolução da análise técnica:  
um sistema capaz de monitorar mais de **300 ativos a cada 5 minutos**, encontrar padrões, 
identificar movimentos, antecipar riscos e entregar **o momento exato de entrada e saída** — tudo em tempo real.
""")

st.markdown("""
O que seria humanamente impossível, mesmo reunindo os **maiores gênios da história**, 
agora acontece em **segundos**.

Porque quando a genialidade se transforma em algoritmo,  
**nasce precisão absoluta.**
""")

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# ============================================================
# 8. SEÇÃO DOS GÊNIOS — TEXTO PREMIUM + IMAGENS
# ============================================================
st.markdown("### A genialidade dos mestres, ressignificada em algoritmo")


# ====== CHARLES DOW ======
col1, col2 = st.columns([0.35, 1])
with col1: st.markdown(circular_image("charles_dow_bw.png"), unsafe_allow_html=True)
with col2:
    st.markdown("#### 🟩 **Charles Dow — O arquiteto da tendência moderna**")
    st.markdown("""
Charles Dow organizou o mercado em **tendências, fases e ciclos**, decifrando sua estrutura.

**No Phoenix Strategy:**  
Suas leis foram traduzidas em lógica algorítmica, identificando automaticamente  
tendências primárias, secundárias e microtendências.
""")

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)


# ====== WYCKOFF ======
col1, col2 = st.columns([0.35, 1])
with col1: st.markdown(circular_image("richard_wyckoff_bw.png"), unsafe_allow_html=True)
with col2:
    st.markdown("#### 🟩 **Richard Wyckoff — A mente que enxergou o fluxo**")
    st.markdown("""
Wyckoff revelou a atuação institucional: acumulação, manipulação, distribuição e volume como linguagem.

**No Phoenix Strategy:**  
Esses ciclos se tornam **variáveis matemáticas detectáveis em tempo real**.
""")

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)


# ====== WELLES WILDER ======
col1, col2 = st.columns([0.35, 1])
with col1: st.markdown(circular_image("welles_wilder_bw.png"), unsafe_allow_html=True)
with col2:
    st.markdown("#### 🟩 **Welles Wilder — O engenheiro da matemática aplicada ao mercado**")
    st.markdown("""
Criador de RSI, ATR, ADX e Parabolic SAR — a base dos indicadores modernos.

**No Phoenix Strategy:**  
Essas fórmulas são recalculadas milhares de vezes ao dia, combinadas em leitura **probabilística antecipativa**.
""")

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)


# ====== AL BROOKS ======
col1, col2 = st.columns([0.35, 1])
with col1: st.markdown(circular_image("al_brooks_bw.png"), unsafe_allow_html=True)
with col2:
    st.markdown("#### 🟩 **Al Brooks — O cirurgião do price action**")
    st.markdown("""
Transformou candles em **linguagem microestrutural**.

**No Phoenix Strategy:**  
A subjetividade virou código: padrões, rejeições e micro-movimentos se tornam lógica computacional.
""")

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)


# ====== BLACK & SCHOLES ======
col1, col2 = st.columns([0.35, 1])
with col1: st.markdown(circular_image("black_scholes_bw.png"), unsafe_allow_html=True)
with col2:
    st.markdown("#### 🟩 **Black & Scholes — Gênios das opções e do risco matemático**")
    st.markdown("""
Criadores das Gregas e da volatilidade implícita.

**No Phoenix Strategy:**  
Delta, gama, vega, IV e risco são recalculados em ciclos de segundos para decisão tática.
""")

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# ============================================================
# 9. ALGORITMO GENIAL™
# ============================================================
st.markdown("### O algoritmo genial™")
st.markdown("""
Enquanto humanos analisam…  
**o algoritmo já concluiu.**

Enquanto humanos hesitam…  
**o algoritmo já executou.**
""")

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# ============================================================
# 10. CHAMADA FINAL
# ============================================================
st.markdown("### Pronto para ver o algoritmo genial em ação?")
st.markdown("## PHOENIX STRATEGY")
st.markdown("### O algoritmo genial.")

st.link_button(
    "ACESSAR AGORA",
    "https://phoenix-master.onrender.com/dashboard_geral"
)

st.markdown("</div>", unsafe_allow_html=True)
