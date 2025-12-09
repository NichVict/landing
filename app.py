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



EXTRA_CSS = """
<style>

.plan-card-wrapper {
    display: block;
    width: 100%;
    margin-bottom: 2rem;
}

.plan-card {
    background: #0b0d10;
    border: 1px solid rgba(0,255,154,0.25);
    border-radius: 16px;
    padding: 1.4rem;
    overflow: hidden;
    width: 100% !important;
    box-shadow: 0 0 12px rgba(0,255,154,0.18);
    transition: transform .25s ease-in-out, box-shadow .25s ease-in-out;
}

.plan-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 0 25px rgba(0,255,154,0.55);
    border-color: #00ff9a;
}

/* Correção crítica: remove highlight fantasma do container do Streamlit */
[data-testid="column"] {
    background: transparent !important;
    border: none !important;
    padding: 0 !important;
}
[data-testid="column"] > div {
    padding: 0 !important;
}

/* BADGES */
.badge, .badge-green {
    display: inline-block;
    padding: 4px 10px;
    border-radius: 999px;
    font-weight: 700;
    font-size: 0.75rem;
    margin-bottom: 12px;
}

.badge {
    background: linear-gradient(90deg, #ff7a1a, #ff5a1a);
    color: #050608;
}

.badge-green {
    background: linear-gradient(90deg, #00ff9a, #00d97a);
    color: #050608;
}

/* TEXTO DO PREÇO */
.price {
    color: #00ff9a;
    font-weight: 700;
    font-size: 1.6rem;
    margin-top: 0.7rem;
}

/* TÍTULOS CENTRAIS */
.section-title-center {
    text-align: center;
    font-size: 2rem;
    font-weight: 700;
    margin-bottom: 1rem;
    color: #00ff9a;
}

.subtle-center {
    text-align: center;
    color: #d7d7d7;
    margin-bottom: 2rem;
}

/* DIVISOR */
.divider-neon {
    border-bottom: 1px solid rgba(0,255,154,0.35);
    margin: 2.2rem 0;
}

</style>
"""
st.markdown(EXTRA_CSS, unsafe_allow_html=True)


CTA_BANNER_CSS = """
<style>
.top-cta-banner {
    position: sticky;
    top: 0;
    z-index: 999;
    width: 100%;
    background: rgba(5, 6, 8, 0.96);
    border-bottom: 1px solid rgba(0,255,154,0.35);
    padding: 0.5rem 1.5rem;
    backdrop-filter: blur(10px);
}

.top-cta-inner {
    max-width: 1100px;
    margin: 0 auto;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 0.8rem;
    font-size: 0.95rem;
}

.top-cta-text {
    color: #f2f2f2;
}

.top-cta-text span {
    color: #00ff9a;
    font-weight: 600;
}

.top-cta-btn {
    border: 1px solid #00ff9a;
    border-radius: 999px;
    padding: 0.3rem 1.1rem;
    font-size: 0.9rem;
    font-weight: 600;
    text-decoration: none;
    color: #050608;
    background: linear-gradient(90deg, #00ff9a, #ff7a1a);
}
.top-cta-btn:hover {
    filter: brightness(1.05);
}
@media (max-width: 768px){
    .top-cta-inner {
        flex-direction: column;
        align-items: flex-start;
    }
}
</style>
"""
st.markdown(CTA_BANNER_CSS, unsafe_allow_html=True)

st.markdown(
    """
    <div class="top-cta-banner">
        <div class="top-cta-inner">
            <div class="top-cta-text">
                Pronto para operar com o <span>Phoenix Strategy</span>?
            </div>
            <a class="top-cta-btn" href="https://wa.me/351915323219" target="_blank">
                Falar com o estrategista no WhatsApp
            </a>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


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

    # ---------------------------
    # BOTÕES LADO A LADO
    # ---------------------------
    b1, b2 = st.columns([1, 1])

    with b1:
        st.link_button(
            "ACESSAR PLATAFORMA",
            "https://phoenix-strategy.onrender.com/dashboard_geral"
        )

    with b2:
        st.link_button(
            "ASSINAR AGORA",
            "https://linknabio.gg/aurinvest"
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
st.markdown(
    "<h4 style='color:#00ff9a; font-weight:700;'>Quem está por trás do Phoenix Strategy\u2122?</h4>",
    unsafe_allow_html=True
)


col1, col2 = st.columns([0.35, 1])

with col1:
    # mesma moldura neon dos gênios, usando sua foto eu.png
    st.markdown(circular_image("eu.png", size=130), unsafe_allow_html=True)

with col2:
    st.markdown(
        """
Sou estrategista financeiro, certificado no Brasil e formado em programação e inteligência artificial na Europa.  
Estudei com analistas CNPIs e especialistas em derivativos, e dedico minha carreira a integrar tecnologia avançada com tomada de decisão no mercado financeiro.  
O Phoenix Strategy é o resultado dessa jornada: a união entre análise técnica clássica, matemática moderna e automação inteligente para entregar precisão, velocidade e simplicidade a todos os investidores.
"""
    )

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# -----------------------------
# EXPANDER — JORNADA COMPLETA
# -----------------------------
# -----------------------------
# EXPANDER — JORNADA COMPLETA
# -----------------------------
with st.expander("Ler a jornada completa por trás do Phoenix Strategy™"):
    st.markdown(
        """
O Phoenix Strategy™ não nasceu de um insight momentâneo — ele é o resultado direto de uma trajetória inteira dedicada à tecnologia, ao estudo da inteligência artificial e à precisão das análises financeiras.

A semente do projeto começou a ser plantada ainda na Europa, durante meus estudos em programação, linguagens modernas como Python e cursos avançados de Inteligência Artificial. A combinação entre tecnologia, matemática aplicada e mercado financeiro sempre esteve presente no meu dia a dia. Ao retornar ao Brasil, após conquistar certificações relevantes, como a ANBIMA, intensifiquei meu trabalho como estrategista financeiro e aprofundei minha especialização em análise técnica, derivativos e comportamento de mercado.

Foi durante minha última mentoria — talvez a mais transformadora de todas — ao lado de mestres, analistas CNPIs e especialistas em derivativos, que a percepção se tornou inevitável:  
**mesmo com tanto conhecimento, o mercado sofre com um problema estrutural.**

Profissionais e investidores usam quatro, cinco ou até mais plataformas para localizar dados, comparar informações, avaliar risco, analisar fluxo, volatilidade, tendências e possíveis entradas.  
Esse processo é lento, fragmentado e, acima de tudo, vulnerável ao maior inimigo dos traders:

### A emoção!


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
"""
    )

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)


# -----------------------------
# SEÇÃO — WHITEPAPER TÉCNICO (PDF)
# -----------------------------
# -----------------------------
# SEÇÃO — WHITEPAPER TÉCNICO (PDF)
# -----------------------------
st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# Título em verde neon
st.markdown(
    "<h3 style='color:#00ff9a; font-weight:700;'>Whitepaper Técnico – Phoenix Strategy™</h3>",
    unsafe_allow_html=True
)

st.markdown(
    """
Para profissionais, analistas, engenheiros quantitativos e investidores que desejam compreender a 
estrutura lógica, matemática e computacional do Phoenix Strategy™, disponibilizamos o 
**Whitepaper Oficial** — um documento técnico que descreve a arquitetura, os modelos estatísticos, 
os módulos analíticos e a filosofia que orienta todo o sistema.
"""
)

# Download real do PDF
with open("Whitepaper_Phoenix.pdf", "rb") as pdf_file:
    st.download_button(
        label="📥 Baixar Whitepaper Técnico (PDF)",
        data=pdf_file,
        file_name="Whitepaper_Phoenix.pdf",
        mime="application/pdf",
        key="download_whitepaper"
    )

# ==============================
# EXPANDER — WHITEPAPER
# ==============================
# ==============================
# EXPANDER — WHITEPAPER
# ==============================

exp = st.expander("O que você encontrará no Whitepaper?", expanded=False)

with exp:
    # Título estilizado dentro do expander (aqui pode HTML)
    st.markdown(
        "<h4 style='color:#00ff9a; font-weight:700; margin-top:0;'>O que você encontrará no Whitepaper?</h4>",
        unsafe_allow_html=True
    )

    st.markdown(
        """
O Whitepaper apresenta uma visão aprofundada da tecnologia:

- Arquitetura central do algoritmo  
- Formulações matemáticas e bases estatísticas  
- Mecanismos de monitoramento de ativos  
- Sistemas de priorização e pesos dinâmicos  
- Modelos de volatilidade, risco e simulação  
- Fundamentos que inspiraram o Phoenix Strategy™  

Um material desenvolvido para **profissionais que precisam de precisão, transparência e entendimento técnico real**
do mecanismo interno da plataforma.
        """
    )

# ============================================================
# SEÇÃO — DEPOIMENTOS / CONFIANÇA
# ============================================================
st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

st.markdown(
    "<h3 style='color:#00ff9a; font-weight:700; text-align:center;'>Por que profissionais confiam na Phoenix Strategy?</h3>",
    unsafe_allow_html=True
)

col_t1, col_t2, col_t3 = st.columns(3)

with col_t1:
    st.markdown(
        """
        <div class='plan-card'>
            <p style='font-size:0.9rem; color:#d7d7d7;'>
            “A ideia de consolidar leitura de fluxo, tendência e volatilidade em um único motor analítico
            resolve exatamente os gargalos que vejo no dia a dia.”
            </p>
            <p style='font-size:0.85rem; opacity:0.8; margin-top:0.8rem;'>
            — Estrategista em Renda Variável
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col_t2:
    st.markdown(
        """
        <div class='plan-card'>
            <p style='font-size:0.9rem; color:#d7d7d7;'>
            “Ter sinais claros, com lógica explicável e relatórios rastreáveis, é o tipo de ferramenta
            que eu gostaria de ter quando comecei.”
            </p>
            <p style='font-size:0.85rem; opacity:0.8; margin-top:0.8rem;'>
            — Analista técnico e educador
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col_t3:
    st.markdown(
        """
        <div class='plan-card'>
            <p style='font-size:0.9rem; color:#d7d7d7;'>
            “A separação entre carteiras prontas e scanners profissionais deixa muito claro para quem o
            produto foi feito em cada nível. Isso é raro no mercado.”
            </p>
            <p style='font-size:0.85rem; opacity:0.8; margin-top:0.8rem;'>
            — Consultor independente
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

# ============================================================
# DEPOIMENTOS — PERFIS INICIANTES E INTERMEDIÁRIOS
# ============================================================

col_t4, col_t5, col_t6 = st.columns(3)

with col_t4:
    st.markdown(
        """
        <div class='plan-card'>
            <p style='font-size:0.9rem; color:#d7d7d7;'>
            “Eu não tinha experiência nenhuma. Sempre achei que precisava ficar o dia inteiro olhando gráfico.
            Com os alertas da Phoenix, eu só sigo as entradas e saídas. Simples, direto e seguro.”
            </p>
            <p style='font-size:0.85rem; opacity:0.8; margin-top:0.8rem;'>
            — Investidor Iniciante (1º mês operando)
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col_t5:
    st.markdown(
        """
        <div class='plan-card'>
            <p style='font-size:0.9rem; color:#d7d7d7;'>
            “Trabalho o dia todo e não tenho tempo para acompanhar mercado. Os alertas chegam prontos,
            com instrução clara. É só executar. Finalmente consegui consistência sem viver na frente da tela.”
            </p>
            <p style='font-size:0.85rem; opacity:0.8; margin-top:0.8rem;'>
            — Trader Intermediário, sem tempo para acompanhar mercado
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col_t6:
    st.markdown(
        """
        <div class='plan-card'>
            <p style='font-size:0.9rem; color:#d7d7d7;'>
            “Sempre tive dificuldade com análise gráfica. A Phoenix me tirou esse peso das costas.
            Os alertas são objetivos e o relatório em tempo real mostra exatamente o que o algoritmo está lendo.”
            </p>
            <p style='font-size:0.85rem; opacity:0.8; margin-top:0.8rem;'>
            — Investidor que não gosta de análise técnica
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )



st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)



# ============================================================
# SEÇÃO — COMO FUNCIONA NA PRÁTICA (3 PASSOS)
# ============================================================
st.markdown("<div class='divider-neon'></div>", unsafe_allow_html=True)

st.markdown(
    "<h2 class='section-title-center'>Como funciona na prática</h2>",
    unsafe_allow_html=True
)

st.markdown(
    "<p class='subtle-center'>Da análise ao resultado, tudo acontece em três passos simples.</p>",
    unsafe_allow_html=True
)

# 3 COLUNAS — PASSO 1, PASSO 2, PASSO 3
step1, step2, step3 = st.columns(3)

with step1:
    st.markdown(
        """
        <div class="plan-card" style="text-align:center;">
            <h3 style="color:#00ff9a;">1. O algoritmo monitora</h3>
            <p style="font-size:0.9rem; color:#d7d7d7;">
                O Phoenix Strategy varre mais de <strong>300 ativos</strong> em tempo real,
                analisando tendência, fluxo, volatilidade, assimetrias e padrões invisíveis ao olho humano.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with step2:
    st.markdown(
        """
        <div class="plan-card" style="text-align:center;">
            <h3 style="color:#00ff9a;">2. Você recebe o alerta</h3>
            <p style="font-size:0.9rem; color:#d7d7d7;">
                Quando uma oportunidade é confirmada, você recebe um <strong>alerta imediato</strong>
                no Telegram e no e-mail, com ponto de entrada, alvo e stop pré-calculados.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with step3:
    st.markdown(
        """
<div class="plan-card" style="text-align:center;">
    <h3 style="color:#00ff9a;">3. Execute com clareza</h3>
    <p style="font-size:0.9rem; color:#d7d7d7;">
        Recebeu o alerta? Execute na sua corretora.<br>
        <strong>Sem análise gráfica.<br>
        Sem necessidade de monitorar.</strong><br>
        A plataforma cuida do resto em tempo real.
    </p>
</div>
        """,
        unsafe_allow_html=True
    )





st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)
st.markdown("""
<h2 style='color:#00ff9a; text-align:center; margin-bottom:0.3rem;'>Entendendo o ROI da Phoenix Strategy</h2>
<p style='text-align:center; color:#d7d7d7; font-size:1.05rem;'>
A Phoenix Strategy opera em ciclos curtos, com média de <strong>15 dias entre entrada e saída</strong>, permitindo que o cliente 
opere duas vezes o próprio capital por mês.  
Os resultados abaixo são <strong>simulações educacionais</strong> baseadas em premissas conservadoras e na filosofia da estratégia.
</p>
""", unsafe_allow_html=True)

st.markdown("""
<div style='text-align:center; margin-top:1rem; margin-bottom:1rem;'>
    <span style='color:#ff7a1a; font-weight:700; font-size:1.1rem;'>
        Dois Cenários. Total Transparência. Total Segurança.
    </span>
    <p style='color:#d7d7d7; font-size:0.95rem; margin-top:0.4rem;'>
        • <strong>Cenário Conservador:</strong> Premissas reduzidas de 4% (Ações) e 12% (Opções).<br>
        • <strong>Premissas da Estratégia:</strong> Faixas históricas da metodologia (5%–8% Ações | 25% Opções).<br>
        Estes valores NÃO representam promessa de rentabilidade futura.
    </p>
</div>
""", unsafe_allow_html=True)

perfis = [
    {"nome": "Investidor Iniciante", "capital": 5000},
    {"nome": "Investidor Intermediário", "capital": 30000},
    {"nome": "Investidor Avançado", "capital": 100000},
]

import math

cols = st.columns(3)

for idx, p in enumerate(perfis):
    with cols[idx]:
        capital = p["capital"]

        conservador_acoes = capital * 0.04
        conservador_opcoes = capital * 0.12

        estrategico_acoes = capital * 0.06
        estrategico_opcoes = capital * 0.25

        html_card = f"""
<div style="
    border: 1px solid rgba(0,255,154,0.3);
    padding: 1.3rem;
    border-radius: 12px;
    box-shadow: 0 0 12px rgba(0,255,154,0.25);
    margin-bottom: 1.2rem;
    background: rgba(255,255,255,0.02);
">

    <h3 style='color:#00ff9a; text-align:center;'>{p["nome"]}</h3>

    <p style='text-align:center; color:#d7d7d7; font-size:1.05rem;'>
        Capital: <strong>R$ {capital:,.0f}</strong>
    </p>

    <hr style='border: 1px solid rgba(255,255,255,0.1); margin: 1rem 0;'>

    <h4 style='color:#ff7a1a; text-align:center; margin-bottom:0.3rem;'>Cenário Conservador</h4>
    <p style='font-size:0.9rem; color:#d7d7d7;'>
        Ações (4%): <strong>R$ {conservador_acoes:,.0f}</strong><br>
        Opções (12%): <strong>R$ {conservador_opcoes:,.0f}</strong>
    </p>

    <h4 style='color:#00ff9a; text-align:center; margin-top:1rem; margin-bottom:0.3rem;'>Premissas da Estratégia</h4>
    <p style='font-size:0.9rem; color:#d7d7d7;'>
        Ações (≈6%): <strong>R$ {estrategico_acoes:,.0f}</strong><br>
        Opções (25%): <strong>R$ {estrategico_opcoes:,.0f}</strong>
    </p>

</div>
"""

        st.markdown(html_card, unsafe_allow_html=True)



st.markdown("""
<p style='color:#888; font-size:0.8rem; text-align:center; margin-top:1rem;'>
As simulações acima são meramente educacionais. Não constituem garantia, promessa ou sugestão 
de rentabilidade futura. Rentabilidade passada — quando existente — não garante resultados futuros.  
A Phoenix Strategy é uma ferramenta de apoio à decisão, e o investidor permanece responsável pelas próprias operações.
</p>
""", unsafe_allow_html=True)

st.markdown("""
<div style='text-align:center; margin-top:1.5rem;'>
    <a href="https://wa.me/351915323219" target="_blank"
       style="
           display:inline-block;
           background:linear-gradient(90deg, #00ff9a, #ff7a1a);
           padding:1rem 2.5rem;
           border-radius:50px;
           color:#050608 !important;
           font-weight:700;
           font-size:1.15rem;
           text-decoration:none;
           box-shadow:0 0 15px rgba(0,255,154,0.45);
       ">
       🔥 Quero entender meu ROI com o Phoenix Strategy
    </a>
</div>
""", unsafe_allow_html=True)












# ============================================================
# NOVA SEÇÃO — PLANOS PHOENIX STRATEGY (VERSÃO PREMIUM CORRIGIDA)
# ============================================================
st.markdown("<div class='divider-neon'></div>", unsafe_allow_html=True)

st.markdown("<h2 class='section-title-center'>Planos Phoenix Strategy</h2>", unsafe_allow_html=True)
st.markdown("<p class='subtle-center'>Escolha o nível de autonomia e profundidade.</p>", unsafe_allow_html=True)

# ===================================================================
# 1) CARTEIRAS INDIVIDUAIS
# ===================================================================
st.markdown("<h3 style='color:#00ff9a;'>Carteiras Individuais</h3>", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class='plan-card-wrapper'>
        <div class='plan-card'>
            <span class='badge-green'>Essencial</span>
            <h3>Carteira IBOV</h3>
            <p>Ações sólidas do Ibovespa, com sinais automatizados.</p>
            <div class='price'>R$ 49/mês</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Assinar", "https://wa.me/351915323219")

with c2:
    st.markdown("""
    <div class='plan-card-wrapper'>
        <div class='plan-card'>
            <span class='badge'>Alta Performance</span>
            <h3>Small Caps</h3>
            <p>Oportunidades agressivas com forte potencial de valorização.</p>
            <div class='price'>R$ 69/mês</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Assinar", "https://wa.me/351915323219")

with c3:
    st.markdown("""
    <div class='plan-card-wrapper'>
        <div class='plan-card'>
            <span class='badge-green'>Internacional</span>
            <h3>Carteira BDR</h3>
            <p>Exposição global com simplicidade total.</p>
            <div class='price'>R$ 49/mês</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Assinar", "https://wa.me/351915323219")

with c4:
    st.markdown("""
    <div class='plan-card-wrapper'>
        <div class='plan-card'>
            <span class='badge'>Agressivo</span>
            <h3>Carteira de Opções</h3>
            <p>Estratégias assimétricas com potencial explosivo.</p>
            <div class='price'>R$ 97/mês</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Assinar", "https://wa.me/351915323219")

st.markdown("<div class='divider-neon'></div>", unsafe_allow_html=True)

# ===================================================================
# 2) PLANOS PREMIUM
# ===================================================================
st.markdown("<h3 style='color:#00ff9a;'>Planos Premium</h3>", unsafe_allow_html=True)

p1, p2 = st.columns(2)

with p1:
    st.markdown("""
    <div class='plan-card-wrapper'>
        <div class='plan-card'>
            <span class='badge'>Mais Vendido</span>
            <h3>Phoenix Equity</h3>
            <p>Inclui IBOV + Small Caps + BDR. O melhor custo-benefício para quem opera ações.</p>
            <div class='price'>R$ 97/mês</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Assinar Phoenix Equity", "https://wa.me/351915323219")

with p2:
    st.markdown("""
    <div class='plan-card-wrapper'>
        <div class='plan-card'>
            <span class='badge'>Recomendado</span>
            <h3>Phoenix Full</h3>
            <p>Todas as 4 carteiras: IBOV, Small Caps, BDR e Opções em um único plano.</p>
            <div class='price'>R$ 147/mês</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Assinar Phoenix Full", "https://wa.me/351915323219")

st.markdown("<div class='divider-neon'></div>", unsafe_allow_html=True)

# ===================================================================
# 3) SCANNERS — LINHA PRO
# ===================================================================
st.markdown("<h3 style='color:#00ff9a;'>Linha PRO — Scanners Profissionais</h3>", unsafe_allow_html=True)

s1, s2, s3 = st.columns(3)

with s1:
    st.markdown("""
    <div class='plan-card-wrapper'>
        <div class='plan-card'>
            <h3>Phoenix Quant Scanner</h3>
            <p>O motor analítico de ações. Autonomia total para traders avançados.</p>
            <div class='price'>R$ 147/mês</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Assinar Quant Scanner", "https://wa.me/351915323219")

with s2:
    st.markdown("""
    <div class='plan-card-wrapper'>
        <div class='plan-card'>
            <span class='badge'>Profissional</span>
            <h3>Phoenix Volatility Scanner</h3>
            <p>Leitura avançada de volatilidade, assimetrias e distorções de prêmio.</p>
            <div class='price'>R$ 197/mês</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Assinar Volatility Scanner", "https://wa.me/351915323219")

with s3:
    st.markdown("""
    <div class='plan-card-wrapper'>
        <div class='plan-card'>
            <span class='badge'>Completo</span>
            <h3>Phoenix Scanner PRO</h3>
            <p>Quant + Volatility. A experiência definitiva para profissionais.</p>
            <div class='price'>R$ 247/mês</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Assinar Scanner PRO", "https://wa.me/351915323219")

st.markdown("<div class='divider-neon'></div>", unsafe_allow_html=True)

# ===================================================================
# 4) SEÇÃO — QUAL PLANO ESCOLHER?
# ===================================================================
st.markdown("<h3 style='color:#00ff9a; text-align:center;'>Qual plano escolher?</h3>", unsafe_allow_html=True)

st.markdown("""
- **Sou iniciante e quero sinais claros** → Carteira IBOV ou BDR  
- **Quero agressividade, mas sem complexidade** → Small Caps  
- **Quero assimetria explosiva** → Carteira de Opções  
- **Quero todas as ações com melhor valor** → Phoenix Equity  
- **Quero tudo em um único plano** → Phoenix Full  
- **Quero autonomia total e operar como profissional** → Scanners  
- **Quero o melhor do melhor** → Phoenix Scanner PRO  
""")

st.markdown("<div class='divider-neon'></div>", unsafe_allow_html=True)


# ============================================================
# SEÇÃO — FAQ PHOENIX STRATEGY
# ============================================================
st.markdown("<div class='divider-neon'></div>", unsafe_allow_html=True)
st.markdown(
    "<h3 style='color:#00ff9a; font-weight:700; text-align:center;'>Perguntas Frequentes</h3>",
    unsafe_allow_html=True
)

faq_expander_1 = st.expander("Preciso saber análise técnica para usar a Phoenix Strategy?")
with faq_expander_1:
    st.markdown("""
Não.  
Se você optar pelas **carteiras**, você recebe sinais prontos de entrada e saída, com explicação simples do racional.

Se você já é avançado, pode usar os **Scanners** para montar suas próprias estratégias, com total autonomia.
""")

faq_expander_2 = st.expander("Qual o capital mínimo recomendado para começar?")
with faq_expander_2:
    st.markdown("""
Depende do plano:

- A partir de **R$ 3.000** você já consegue seguir parte das carteiras.  
- Entre **R$ 10.000 e R$ 40.000** é a faixa ideal para aproveitar bem o Phoenix Equity ou o Phoenix Full.  
- Acima de **R$ 50.000** os Scanners passam a ter ainda mais impacto.
""")

faq_expander_3 = st.expander("Posso cancelar quando quiser?")
with faq_expander_3:
    st.markdown("""
Sim.  
Os planos são recorrentes, mas você pode cancelar a qualquer momento, sem multa de fidelidade.
""")

faq_expander_4 = st.expander("Qual a diferença entre carteiras e Scanners?")
with faq_expander_4:
    st.markdown("""
- **Carteiras** → você segue sinais prontos de entrada e saída.  
- **Scanners** → você recebe o motor analítico bruto, com rankings e filtros, para montar suas próprias operações.

Um não substitui o outro — são níveis diferentes de autonomia.
""")

faq_expander_5 = st.expander("A Phoenix Strategy garante resultado?")
with faq_expander_5:
    st.markdown("""
Nenhuma estratégia séria pode prometer resultados garantidos.  
O que a Phoenix Strategy entrega é **processo**, **método**, **disciplina** e **inteligência de análise**, 
aumentando a clareza e a qualidade das suas decisões.
""")

st.markdown("<div class='divider-neon'></div>", unsafe_allow_html=True)



# ==============================
# SEÇÃO 8 — CHAMADA FINAL
# ==============================
st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

st.markdown("### Pronto para ver o algoritmo genial em ação?")


st.link_button(
    "ASSINAR A PHOENIX STRATEGY",
    "https://linknabio.gg/aurinvest"
)


st.markdown("</div>", unsafe_allow_html=True)
