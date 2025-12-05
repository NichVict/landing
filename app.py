import streamlit as st
from pathlib import Path
import base64

# ----------------------------
# CONFIG
# ----------------------------
st.set_page_config(
    page_title="Phoenix Strategy – O algoritmo genial",
    page_icon="🔥",
    layout="wide"
)

# ----------------------------
# CSS
# ----------------------------
CSS = """
<style>
body, .stApp {
    background-color: #030303;
    color: #eaeaea;
    font-family: "Inter", sans-serif;
}

/* Container central */
.main-block {
    max-width: 1000px;
    margin: auto;
}

/* Títulos */
h1, h2, h3 {
    color: #00ff9a;
    font-weight: 700;
}

/* Tag laranja */
.orange-tag {
    color: #ff7a1a;
    font-size: 0.9rem;
    text-transform: uppercase;
    letter-spacing: 0.12em;
}

/* Divisor */
.section-divider {
    margin: 3rem 0;
    border-bottom: 1px solid rgba(255,255,255,0.08);
}

/* Card dos Gênios */
.genius-card {
    background: radial-gradient(circle at top, rgba(255,120,20,0.35), rgba(0,0,0,0.85));
    border: 1px solid rgba(0,255,154,0.25);
    border-radius: 18px;
    padding: 1.4rem 1rem;
    text-align: center;
    transition: .25s ease-in-out;
}
.genius-card:hover {
    transform: translateY(-4px);
    border-color: #00ff9a;
    box-shadow: 0 0 18px rgba(0,255,154,0.6);
}

/* Foto circular neon */
.genius-img-container {
    width: 105px;
    height: 105px;
    border-radius: 50%;
    overflow: hidden;
    border: 3px solid #00ff9a;
    margin: 0 auto 0.7rem auto;
    box-shadow: 0 0 12px rgba(0,255,154,0.7);
}
.genius-img-container img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    filter: grayscale(100%);
}

/* Nome */
.genius-name {
    color: #00ff9a;
    font-size: 1.0rem;
    font-weight: 700;
    margin-bottom: .2rem;
    letter-spacing: 0.08em;
}

/* Subtítulo */
.genius-role {
    color: #ff7a1a;
    font-size: 0.9rem;
    margin-bottom: 0.5rem;
}

/* Texto */
.genius-text {
    color: #dcdcdc;
    font-size: .95rem;
    line-height: 1.45;
}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)


# ----------------------------
# Função imagem circular
# ----------------------------
def circular_image_html(path):
    if not Path(path).exists():
        return ""
    img_bytes = Path(path).read_bytes()
    img_b64 = base64.b64encode(img_bytes).decode()

    return f"""
    <div class="genius-img-container">
        <img src="data:image/png;base64,{img_b64}">
    </div>
    """


# ----------------------------
# LOGO
# ----------------------------
st.markdown("<div class='logo-container' style='text-align:center;'>", unsafe_allow_html=True)
if Path("Phoenix_logo.png").exists():
    st.image("Phoenix_logo.png", width=260)
st.markdown("</div>", unsafe_allow_html=True)


# ----------------------------
# MAIN BLOCK
# ----------------------------
st.markdown("<div class='main-block'>", unsafe_allow_html=True)

# ----------------------------
# SECTION 1 – HERO
# ----------------------------
st.markdown("<div class='orange-tag'>PLATAFORMA QUANT</div>", unsafe_allow_html=True)
st.markdown("## PHOENIX STRATEGY")
st.markdown("### O algoritmo genial.")

st.markdown("""
Um novo padrão nasceu.  
A fusão perfeita entre a genialidade humana e a precisão algorítmica.  
O poder de análise que antes era privilégio de poucos — agora renascido em tecnologia.
""")

st.markdown(
    "<a href='https://phoenix-master.onrender.com/dashboard_geral' "
    "style='display:inline-block;margin-top:10px;padding:10px 22px;"
    "background:linear-gradient(90deg,#00ff9a,#ff7a1a);color:#000;border-radius:50px;"
    "font-weight:700;text-decoration:none;'>ACESSAR PLATAFORMA</a>",
    unsafe_allow_html=True
)

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# ----------------------------
# SECTION 3 – GÊNIOS
# ----------------------------
st.markdown("## A genialidade dos gênios, ressignificada em algoritmo")

html_grid = f"""
<div style="display:grid;
            grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
            gap:22px; margin-top:25px;">

    <div class="genius-card">
        {circular_image_html("charles_dow_bw.png")}
        <div class="genius-name">CHARLES DOW</div>
        <div class="genius-role">Pai da tendência moderna</div>
        <div class="genius-text">
            Criou princípios estruturais de tendência, fases e comportamento direcional.
        </div>
    </div>

    <div class="genius-card">
        {circular_image_html("richard_wyckoff_bw.png")}
        <div class="genius-name">RICHARD WYCKOFF</div>
        <div class="genius-role">Arquitetura do fluxo</div>
        <div class="genius-text">
            Decodificou oferta e demanda, fases institucionais e acumulação/distribuição.
        </div>
    </div>

    <div class="genius-card">
        {circular_image_html("welles_wilder_bw.png")}
        <div class="genius-name">WELLES WILDER</div>
        <div class="genius-role">O mestre dos indicadores</div>
        <div class="genius-text">
            Criou RSI, ATR, ADX e Parabolic SAR — base matemática da análise técnica moderna.
        </div>
    </div>

    <div class="genius-card">
        {circular_image_html("al_brooks_bw.png")}
        <div class="genius-name">AL BROOKS</div>
        <div class="genius-role">Price action refinado</div>
        <div class="genius-text">
            Transformou candles em linguagem microestrutural e direcional.
        </div>
    </div>

    <div class="genius-card">
        {circular_image_html("black_scholes_bw.png")}
        <div class="genius-name">BLACK & SCHOLES</div>
        <div class="genius-role">Gênios das opções</div>
        <div class="genius-text">
            Criaram o modelo das Gregas, a volatilidade implícita e a base da precificação moderna.
        </div>
    </div>

</div>
"""

st.markdown(html_grid, unsafe_allow_html=True)

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# ----------------------------
# COPY FINAL (mantido)
# ----------------------------
st.markdown("""
Os pilares da análise técnica nasceram das mentes de gigantes.  
Hoje, suas genialidades renascem em forma algorítmica.  
A Phoenix Strategy honra esses gênios — e os leva além do que era possível.
""")

st.markdown("</div>", unsafe_allow_html=True)  # Fecha main-block



# -------------------------------------
# TEXTO COMPLEMENTAR DA SEÇÃO
# -------------------------------------
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

st.markdown(
    """
O coração da plataforma.

Um sistema projetado para:

- Detectar padrões invisíveis ao olho humano  
- Analisar dezenas de variáveis simultaneamente  
- Traduzir movimentos do preço
    em decisões claras  
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
