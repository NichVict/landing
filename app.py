import streamlit as st
from pathlib import Path
import base64
# -------------------------------------
# CONFIG DA PÁGINA
# -------------------------------------
st.set_page_config(
    page_title="Phoenix Strategy – O algoritmo genial",
    page_icon="🔥",
    layout="wide"
)

# -------------------------------------
# CSS – TEMA PHOENIX (PRETO + NEON + CARDS)
# -------------------------------------
CSS = """
<style>
body, .stApp {
    background-color: #030303;
    color: #e2e2e2;
    font-family: "Inter", -apple-system, BlinkMacSystemFont, system-ui, sans-serif;
}

/* CENTRALIZA BLOCO PRINCIPAL */
.main-block {
    max-width: 960px;
    margin: 0 auto;
}

/* LOGO */
.logo-container {
    text-align: center;
    margin: 1.5rem 0 2.5rem 0;
}

/* TÍTULOS */
h1, h2, h3 {
    color: #00ff9a;
    font-weight: 700;
}

/* TAG LARANJA */
.orange-tag {
    color: #ff7a1a;
    text-transform: uppercase;
    font-size: 0.9rem;
    letter-spacing: 0.14em;
    margin-bottom: 0.2rem;
}

/* DIVISOR */
.section-divider {
    border-bottom: 1px solid rgba(255,255,255,0.10);
    margin: 3rem 0 2.2rem 0;
}

/* BOTÕES */
.stButton>button {
    background: linear-gradient(90deg, #00ff9a, #ff7a1a);
    color: #050608;
    border-radius: 999px;
    padding: 0.7rem 2.1rem;
    border: none;
    font-weight: 700;
    font-size: 0.98rem;
    cursor: pointer;
    transition: 0.22s ease-in-out;
}
.stButton>button:hover {
    transform: translateY(-2px) scale(1.02);
    filter: brightness(1.15);
}

/* TEXTO */
p, li {
    font-size: 1.02rem;
    line-height: 1.6;
}

/* SEÇÃO GÊNIOS – GRID */
.genius-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 1.5rem;
    margin: 1.5rem 0 1.0rem 0;
}

/* CARD VERTICAL DOS GÊNIOS */
.genius-card {
    background: radial-gradient(circle at top, rgba(255,122,26,0.40), rgba(0,0,0,0.92));
    border-radius: 20px;
    border: 1px solid rgba(0,255,154,0.30);
    padding: 1.3rem 1.2rem 1.4rem 1.2rem;
    text-align: center;
    transition: 0.25s ease-in-out;
}
.genius-card:hover {
    transform: translateY(-4px) scale(1.02);
    box-shadow: 0 0 20px rgba(255,122,26,0.65);
    border-color: rgba(0,255,154,0.70);
}

/* IMAGEM CIRCULAR P&B COM CONTORNO NEON */
.genius-img {
    width: 90px;
    height: 90px;
    border-radius: 50%;
    object-fit: cover;
    filter: grayscale(100%);
    border: 2px solid #00ff9a;
    box-shadow: 0 0 12px rgba(0,255,154,0.6);
    margin-bottom: 0.7rem;
}

/* NOME DO GÊNIO */
.genius-name {
    font-weight: 700;
    color: #00ff9a;
    font-size: 1.0rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 0.1rem;
}

/* SUBTÍTULO LARANJA NO CARD */
.genius-role {
    color: #ff7a1a;
    font-size: 0.9rem;
    margin-bottom: 0.5rem;
}

/* PARÁGRAFO MENOR DENTRO DO CARD */
.genius-text {
    font-size: 0.95rem;
    color: #d7d7d7;
}

/* UL */
ul {
    padding-left: 1.3rem;
}

/* HERO SUB */
.hero-sub {
    font-size: 1.05rem;
    color: #d0d0d0;
}

</style>
"""

st.markdown(CSS, unsafe_allow_html=True)

# -------------------------------------
# LOGO PHOENIX (TOPO)
# -------------------------------------
st.markdown("<div class='logo-container'>", unsafe_allow_html=True)
if Path("Phoenix_logo.png").exists():
    st.image("Phoenix_logo.png", width=260)
st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------------
# INÍCIO BLOCO PRINCIPAL
# -------------------------------------
st.markdown("<div class='main-block'>", unsafe_allow_html=True)

# =====================================
# SECTION 1 — HERO (CAPA)
# =====================================
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

# =====================================
# SECTION 2 — O QUE É O PHOENIX STRATEGY?
# =====================================
st.markdown("## O que é o Phoenix Strategy?")

st.markdown(
    """
A Phoenix Strategy é a evolução da análise técnica:  
um sistema capaz de monitorar mais de **300 ativos a cada 5 minutos**, encontrar padrões, 
identificar movimentos, antecipar riscos e entregar **o momento exato de entrada e saída** — tudo em tempo real.
"""
)

st.markdown(
    """
O que seria humanamente impossível, mesmo reunindo os maiores gênios da história,  
agora acontece em **segundos**.

Porque quando a genialidade se transforma em algoritmo,  
**nasce precisão absoluta.**
"""
)

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# =====================================
# SECTION 3 — A GENIALIDADE DOS GÊNIOS (CARDS + TEXTO ORIGINAL)
# =====================================
st.markdown("## A genialidade dos gênios, ressignificada em algoritmo")

# ---- GRID DE GÊNIOS (CARDS VERTICAIS) ----
st.markdown("<div class='genius-grid'>", unsafe_allow_html=True)


st.markdown("<div class='genius-grid'>", unsafe_allow_html=True)

import base64

def circular_image(image_path, size=110):
    if Path(image_path).exists():
        with open(image_path, "rb") as img_file:
            img_bytes = img_file.read()
            img_b64 = base64.b64encode(img_bytes).decode()
    else:
        return ""

    html = f"""
    <div style="
        width: {size}px;
        height: {size}px;
        border-radius: 50%;
        overflow: hidden;
        border: 3px solid #00ff9a;
        box-shadow: 0 0 10px rgba(0,255,154,0.7);
        margin: 0 auto 0.6rem auto;
    ">
        <img src="data:image/png;base64,{img_b64}" 
             style="
                width: 100%;
                height: 100%;
                object-fit: cover;
                filter: grayscale(100%);
             ">
    </div>
    """
    return html


# -------------------------------
# RENDERIZAÇÃO DOS CARDS
# -------------------------------

def render_genius_card(image_path, name, role, text):
    st.markdown("<div class='genius-card'>", unsafe_allow_html=True)

    # FOTO CIRCULAR NEON
    st.markdown(circular_image(image_path), unsafe_allow_html=True)

    # TITULOS
    st.markdown(f"<div class='genius-name'>{name}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='genius-role'>{role}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='genius-text'>{text}</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)


# LINHA 1
col1, col2, col3 = st.columns(3)

with col1:
    render_genius_card(
        "charles_dow_bw.png",
        "CHARLES DOW",
        "Pai da tendência moderna",
        "Criou os princípios estruturais de tendência, fases e comportamento direcional do mercado."
    )

with col2:
    render_genius_card(
        "richard_wyckoff_bw.png",
        "RICHARD WYCKOFF",
        "Arquitetura do fluxo",
        "Decodificou oferta e demanda, atuação institucional e fases de acumulação e distribuição."
    )

with col3:
    render_genius_card(
        "welles_wilder_bw.png",
        "WELLES WILDER",
        "O mestre dos indicadores",
        "Criou RSI, ATR, ADX e Parabolic SAR — a espinha dorsal matemática da análise técnica moderna."
    )

# LINHA 2
col4, col5, col6 = st.columns(3)

with col4:
    render_genius_card(
        "al_brooks_bw.png",
        "AL BROOKS",
        "Price action refinado",
        "Transformou candles em linguagem, com leitura microestrutural e direcional do preço."
    )

with col5:
    render_genius_card(
        "black_scholes_bw.png",
        "BLACK & SCHOLES",
        "Gênios das opções",
        "Criadores do modelo que originou as Gregas, a volatilidade implícita e a base da precificação moderna de opções."
    )

with col6:
    render_genius_card(
        "Phoenix_logo.png",
        "PHOENIX STRATEGY",
        "O renascimento em algoritmo",
        "A fusão da genialidade desses nomes em um único sistema capaz de monitorar 300+ ativos em tempo real."
    )


# ---- TEXTO ORIGINAL DA SECTION 3 (COPY INTACTA) ----
st.markdown(
    """
Os pilares da análise técnica nasceram das mentes de gigantes:

- **Charles Dow**, o visionário da tendência.  
- **Richard Wyckoff**, o decodificador do fluxo.  
- **Welles Wilder**, o engenheiro que criou revoluções matemáticas.  
- **Al Brooks**, a leitura mais refinada do price action moderno.  

Cada um deles alterou para sempre a forma como entendemos o mercado.  
Hoje, suas genialidades renascem em forma algorítmica.

A Phoenix Strategy honra esses gênios —  
e os leva além do que era possível.
"""
)

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# =====================================
# SECTION 4 — O ALGORITMO GENIAL™
# =====================================
st.markdown("## O algoritmo genial™")

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
o algoritmo já concluiu.

Enquanto humanos hesitam…  
o algoritmo já executou.

Isso é precisão. Isso é velocidade. Isso é genialidade aplicada.
"""
)

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# =====================================
# SECTION 5 — VELOCIDADE QUE HUMANOS NÃO ALCANÇAM
# =====================================
st.markdown("## Velocidade que humanos não alcançam")

st.markdown(
    """
Enquanto um analista experiente consegue acompanhar 3, talvez 5 ativos…  
o algoritmo genial monitora 300+ ao mesmo tempo, sem erro, sem atraso, sem cansaço.
"""
)

st.markdown(
    """
Ele não pisca.  
Ele não esquece.  
Ele não se contradiz.

Ele apenas calcula, compara, detecta, decide.

É assim que a genialidade se perpetua.  
É assim que nasce o futuro.
"""
)

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# =====================================
# SECTION 6 — RESULTADOS EM TEMPO REAL
# =====================================
st.markdown("## Resultados em tempo real")

st.markdown(
    """
A Phoenix Strategy entrega:

- Sinais de entrada e saída com precisão  
- Monitoramento contínuo  
- Leitura de fluxo simplificada  
- Insights algorítmicos  
- Interpretação automatizada de price action  
- Probabilidade estatística a favor do trader  

Tudo isso com a mesma lógica que guiou os gênios —  
mas com a rapidez que eles nunca tiveram.
"""
)

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# =====================================
# SECTION 7 — O RENASCIMENTO DA ANÁLISE TÉCNICA
# =====================================
st.markdown("## O renascimento da análise técnica")

st.markdown(
    """
A Phoenix Strategy não substitui os gênios.  
Ela honra, amplifica e perpetua sua genialidade.
"""
)

st.markdown(
    """
O que eles imaginaram,  
nós transformamos em algoritmo.

O que eles definiram,  
nós levamos ao extremo.

O que era teoria,  
agora é execução instantânea.
"""
)

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# =====================================
# SECTION 8 — CHAMADA FINAL
# =====================================
st.markdown("## A genialidade humana nos trouxe até aqui.")
st.markdown("### A precisão algorítmica nos levará além.")

st.markdown("## PHOENIX STRATEGY")
st.markdown("### O algoritmo genial.")

st.button("ACESSAR AGORA")

st.markdown("</div>", unsafe_allow_html=True)
