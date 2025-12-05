import streamlit as st
from pathlib import Path
import base64

# -----------------------------
# CONFIGURAÇÃO INICIAL DA PÁGINA
# -----------------------------
st.set_page_config(
    page_title="Phoenix Strategy – O algoritmo genial",
    page_icon="🔥",
    layout="wide"
)

# -----------------------------
# FUNÇÃO PARA IMAGEM CIRCULAR COM NEON
# -----------------------------
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

</style>
"""

# -----------------------------
# LOGO NO TOPO – VERSÃO CORRETA
# -----------------------------
from PIL import Image

logo_path = "Phoenix_logo.png"

try:
    logo = Image.open(logo_path)
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


st.markdown(CUSTOM_CSS, unsafe_allow_html=True)




# -----------------------------
# INÍCIO DO BLOCO PRINCIPAL
# -----------------------------
st.markdown("<div class='main-block'>", unsafe_allow_html=True)

# -----------------------------
# SEÇÃO 1 — HERO
# -----------------------------
col1, col2 = st.columns([1.3, 1])

with col1:
    st.markdown("<div class='orange-tag'>PLATAFORMA QUANT</div>", unsafe_allow_html=True)
    st.markdown("## PHOENIX STRATEGY")
    st.markdown("### O algoritmo genial.")
    st.markdown("<p class='hero-subtitle'>Um novo padrão nasceu. A fusão perfeita entre a genialidade humana e a precisão algorítmica.</p>", unsafe_allow_html=True)
    st.markdown("<p>O poder de análise que antes era privilégio de poucos — agora renascido em tecnologia.</p>", unsafe_allow_html=True)

    if st.button("ACESSAR PLATAFORMA"):
        st.toast("Em breve: acesso à plataforma Phoenix Strategy. 🚀")

with col2:
    st.empty()

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# -----------------------------
# SEÇÃO 2 — O QUE É O PHOENIX STRATEGY?
# -----------------------------
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

# -----------------------------
# SEÇÃO 3 — OS GÊNIOS (AGORA COM IMAGENS!)
# -----------------------------
st.markdown("### A genialidade dos mestres, ressignificada em algoritmo")

# CHARLES DOW
st.markdown(circular_image("charles_dow_bw.png"), unsafe_allow_html=True)
st.markdown("#### **Charles Dow** – Pai da tendência moderna")
st.markdown("Criou os princípios estruturais de tendência, fases e comportamento direcional do mercado.")

# WYCKOFF
st.markdown(circular_image("richard_wyckoff_bw.png"), unsafe_allow_html=True)
st.markdown("#### **Richard Wyckoff** – Arquitetura do fluxo")
st.markdown("Decodificou oferta e demanda, atuação institucional e fases de acumulação/distribuição.")

# WELLES WILDER
st.markdown(circular_image("welles_wilder_bw.png"), unsafe_allow_html=True)
st.markdown("#### **Welles Wilder** – O mestre dos indicadores")
st.markdown("Criou RSI, ATR, ADX e Parabolic SAR — a base matemática moderna da análise técnica.")

# AL BROOKS
st.markdown(circular_image("al_brooks_bw.png"), unsafe_allow_html=True)
st.markdown("#### **Al Brooks** – Price action refinado")
st.markdown("Transformou candles em linguagem microestrutural e direcional.")

# BLACK & SCHOLES
st.markdown(circular_image("black_scholes_bw.png"), unsafe_allow_html=True)
st.markdown("#### **Black & Scholes** – Gênios das opções")
st.markdown("Criaram o modelo das Gregas, volatilidade implícita e a base da precificação moderna de opções.")

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# -----------------------------
# CONTINUAÇÃO DAS SUAS SEÇÕES (SEM ALTERAR)
# -----------------------------
# ... (restante igual)


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
