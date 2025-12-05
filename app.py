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
    logo = Image.open("Logo_phoenix.png")
    st.markdown(
        """
        <div style="display:flex; align-items:center; justify-content:flex-start; margin:10px 0 25px 0;">
        """,
        unsafe_allow_html=True
    )
    st.image(logo, width=300)
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
    #st.markdown("<div class='orange-tag'>PLATAFORMA QUANT</div>", unsafe_allow_html=True)
    st.markdown("<h2 style='color:#00ff9a;'>PHOENIX STRATEGY</h2>", unsafe_allow_html=True)    
    st.markdown(
        "<div style='color:#ff5a1f; font-size:1.45rem; font-weight:400; letter-spacing:0.06em; text-transform:uppercase;'>O ALGORITMO GENIAL</div>",
        unsafe_allow_html=True
    )
    # LINHA DIVISÓRIA
    st.markdown(
        """
        <div style='
            border-bottom:1px solid rgba(255,255,255,0.08);
            margin: 1.5rem 0 2rem 0;
        '></div>
        """,
        unsafe_allow_html=True
    )

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
    st.markdown("#### 🧠 **Charles Dow — O arquiteto da tendência moderna**")
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
    st.markdown("#### 🧠 **Richard Wyckoff — A mente que enxergou o fluxo**")
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
    st.markdown("#### 🧠 **Welles Wilder — O engenheiro da matemática aplicada ao mercado**")
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
    st.markdown("#### 🧠 **Al Brooks — O cirurgião do price action**")
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
    st.markdown("#### 🧠 **Black & Scholes — Gênios das opções e do risco matemático**")
    st.markdown("""
Criadores das Gregas e da volatilidade implícita.

**No Phoenix Strategy:**  
Delta, gama, vega, IV e risco são recalculados em ciclos de segundos para decisão tática.
""")

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# ============================================================
# 9. ALGORITMO GENIAL™
# ============================================================
# 9. O ALGORITMO GENIAL™ (VERSÃO COMPLETA)
# ============================================================
st.markdown(
    "<h3 style='color:#00ff9a; font-weight:700;'>O algoritmo genial™</h3>",
    unsafe_allow_html=True
)

st.markdown("""
O cérebro digital da plataforma.

Um sistema projetado para:

- Detectar padrões invisíveis ao olho humano  
- Analisar dezenas de variáveis simultaneamente  
- Traduzir movimentos do preço em decisões claras  
- Criar probabilidades reais de vantagem  
- Atualizar-se constantemente com novos dados  

Enquanto humanos analisam…  
**o algoritmo já concluiu.**

Enquanto humanos hesitam…  
**o algoritmo já executou.**

Isso é **precisão**.  
Isso é **velocidade**.  
Isso é **genialidade aplicada.**
""")

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)


# ============================================================
# 10. VELOCIDADE QUE HUMANOS NÃO ALCANÇAM (VERSÃO COMPLETA)
# ============================================================
st.markdown(
    "<h3 style='color:#00ff9a; font-weight:700;'>Velocidade que humanos não alcançam</h3>",
    unsafe_allow_html=True
)

st.markdown("""
Enquanto um analista experiente consegue acompanhar **3, talvez 5 ativos**…  
o **algoritmo genial** monitora **300+ ao mesmo tempo**, sem erro, sem atraso, sem cansaço.

Ele não pisca.  
Ele não esquece.  
Ele não se contradiz.  
Ele não se emociona.

Ele apenas **calcula, compara, detecta, decide**.

É assim que a genialidade se perpetua.  
É assim que nasce o futuro.
""")

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)


# ============================================================
# 11. RESULTADOS EM TEMPO REAL (VERSÃO COMPLETA)
# ============================================================
st.markdown(
    "<h3 style='color:#00ff9a; font-weight:700;'>Resultados em tempo real</h3>",
    unsafe_allow_html=True
)

st.markdown(
    """
A **Phoenix Strategy™ entrega:**

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
mas com a **rapidez que nunca tiveram**.
"""
)


st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)


# ============================================================
# 12. O RENASCIMENTO DA ANÁLISE TÉCNICA (VERSÃO COMPLETA)
# ============================================================
st.markdown(
    "<h3 style='color:#00ff9a; font-weight:700;'>O renascimento da análise técnica</h3>",
    unsafe_allow_html=True
)

st.markdown("""
A **Phoenix Strategy** não substitui os gênios.  
Ela **honra, amplifica e perpetua** sua genialidade.
""")

st.markdown("""
O que eles imaginaram,  
**nós transformamos em algoritmo.**

O que eles definiram,  
**nós levamos ao extremo.**

O que era teoria,  
**agora é execução instantânea.**
""")

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# -----------------------------
# NOVA SEÇÃO — SOBRE O CRIADOR
# -----------------------------
st.markdown("### Quem está por trás do Phoenix Strategy™?")

col1, col2 = st.columns([0.35, 1])

with col1:
    # mesma moldura neon dos gênios, usando sua foto eu.png
    st.markdown(circular_image("eu.png", size=130), unsafe_allow_html=True)

with col2:
    st.markdown(
        """
Sou estrategista financeiro, certificado no Brasil e formado em programação e inteligência artificial na Europa.  
Estudei com analistas CNPIs e especialistas em derivativos, e dediquei minha carreira a integrar tecnologia avançada com tomada de decisão no mercado financeiro.  
O Phoenix Strategy é o resultado dessa jornada: a união entre análise técnica clássica, matemática moderna e automação inteligente para entregar precisão, velocidade e simplicidade a todos os investidores.
"""
    )

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# -----------------------------
# EXPANDER — JORNADA COMPLETA
# -----------------------------
with st.expander(
    "<span style='color:#00ff9a; font-weight:700;'>Ler a jornada completa por trás do Phoenix Strategy\u2122</span>",
    expanded=False
):
    st.markdown(
        """
O Phoenix Strategy™ não nasceu de um insight momentâneo — ele é o resultado direto de uma trajetória inteira dedicada à tecnologia, ao estudo da inteligência artificial e à precisão das análises financeiras.

A semente do projeto começou a ser plantada ainda na Europa, durante meus estudos em programação, linguagens modernas como Python e cursos avançados de Inteligência Artificial. A combinação entre tecnologia, matemática aplicada e mercado financeiro sempre esteve presente no meu dia a dia. Ao retornar ao Brasil, após conquistar certificações relevantes, como a ANBIMA, intensifiquei meu trabalho como estrategista financeiro e aprofundei minha especialização em análise técnica, derivativos e comportamento de mercado.

Foi durante minha última mentoria — talvez a mais transformadora de todas — ao lado de mestres, analistas CNPIs e especialistas em derivativos, que a percepção se tornou inevitável:  
**mesmo com tanto conhecimento, o mercado sofre com um problema estrutural.**

Profissionais e investidores usam quatro, cinco ou até mais plataformas para localizar dados, comparar informações, avaliar risco, analisar fluxo, volatilidade, tendências e possíveis entradas.  
Esse processo é lento, fragmentado e, acima de tudo, vulnerável ao maior inimigo dos traders:

### A emoção.

O fator emocional atrapalha decisões, distorce leituras, antecipa saídas e atrasa entradas.  
Já a complexidade operacional leva investidores — até os avançados — a perder oportunidades valiosas simplesmente porque **ninguém consegue analisar dezenas de ativos simultaneamente em tempo real**.

Foi então que a ideia deixou de ser uma visão e se tornou uma necessidade:  
criar um sistema capaz de integrar tudo isso.  
Rápido. Preciso. Impessoal.  
E baseado na genialidade dos mestres que criaram os pilares da análise moderna.

Assim nasceu o **Projeto Fênix**:  
um algoritmo proprietário que sintetiza os princípios de Charles Dow, Wyckoff, Welles Wilder, Al Brooks, Black & Scholes e outros gigantes — traduzidos em lógica computacional, monitoramento contínuo e análise automatizada de centenas de ativos simultaneamente.

Um algoritmo que não pisca.  
Não esquece.  
Não se contradiz.  
E nunca age por emoção.

Mas o Phoenix Strategy™ não é apenas uma ferramenta de trade — ele é uma plataforma completa, criada para todos os níveis de investidores e profissionais:

- **Leigos** que desejam entrar no mercado sem dominar análise gráfica ou indicadores complexos.  
- **Intermediários** que já investem, mas não têm tempo para analisar gráficos diariamente.  
- **Investidores avançados** que dominam análise técnica, mas não conseguem acompanhar centenas de ativos ao mesmo tempo.  
- **Analistas CNPI, gestores e profissionais** que precisam de ferramentas sérias, auditáveis e com relatórios formais — incluindo relatórios consolidados, motores de busca de ações e opções, e documentação adequada para órgãos reguladores como CVM e APIMEC.

O Phoenix Strategy™ transforma minutos em segundos, incerteza em precisão e subjetividade em cálculo.  
Ele não substitui o analista — **ele o potencializa**.  
Ele não remove os princípios — **ele os leva à perfeição matemática**.  
Ele não elimina o trader — **ele devolve a ele vantagem estatística, precisão e clareza operacional.**

O projeto Fênix é o renascimento da análise técnica em sua forma mais evoluída:  
um sistema que honra a genialidade humana ao mesmo tempo em que elimina suas limitações.

O futuro do trade não é humano ou algorítmico.  
É **a união perfeita dos dois.**  
E esse futuro começa agora.
""",
        unsafe_allow_html=True
    )

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)


# SEÇÃO 8 — CHAMADA FINAL
st.markdown("### Pronto para ver o algoritmo genial em ação?")

st.link_button(
    "ACESSAR AGORA",
    "https://phoenix-master.onrender.com/dashboard_geral"
)

st.markdown("</div>", unsafe_allow_html=True)
