import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Carteiras Individuais – Phoenix Strategy",
    layout="wide"
)

# ================================================================
# ESTILO GLOBAL (NEON THEME)
# ================================================================
st.markdown("""
<style>
    .planos-wrapper {
        max-width: 1100px;
        margin: 0 auto;
        margin-top: 2rem;
    }

    .titulo {
        color: #00ff9a;
        text-align: center;
        font-size: 2rem;
        margin-bottom: 0.3rem;
    }

    .subtexto {
        text-align: center;
        font-size: 1rem;
        color: #d7d7d7;
        margin-bottom: 2.5rem;
    }
</style>
""", unsafe_allow_html=True)

# ================================================================
# CONTEÚDO DA PÁGINA (STREAMLIT PURO)
# ================================================================
st.markdown("<div class='planos-wrapper'>", unsafe_allow_html=True)

st.markdown("<h2 class='titulo'>Carteiras Individuais</h2>", unsafe_allow_html=True)

st.markdown("""
<p class='subtexto'>
Planos individuais para quem deseja focar apenas em uma estratégia específica de ações ou derivativos.
</p>
""", unsafe_allow_html=True)

# ================================================================
# HTML PURO DOS CARDS (CAMINHO B)
# ================================================================
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">

<style>
.grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 28px;
}

@media(max-width: 900px) {
    .grid {
        grid-template-columns: 1fr;
    }
}

.card {
    background: rgba(255,255,255,0.03);
    border-radius: 18px;
    padding: 1.8rem;
    border: 1px solid rgba(0,255,154,0.25);
    box-shadow: 0 0 20px rgba(0,255,154,0.35);
    color: #ffffff;
    font-family: Arial, Helvetica, sans-serif;
}

.badge-green {
    background: #00ff9a;
    padding: 4px 12px;
    border-radius: 50px;
    font-size: 0.75rem;
    font-weight: 700;
    color: #000;
    display: inline-block;
}

.badge-orange {
    background: #ff7a1a;
    padding: 4px 12px;
    border-radius: 50px;
    font-size: 0.75rem;
    font-weight: 700;
    color: #000;
    display: inline-block;
}

h3 {
    margin-top: 0.8rem;
    margin-bottom: 0.6rem;
}

.desc {
    color: #d7d7d7;
    font-size: 0.95rem;
    line-height: 1.5;
}

.features {
    margin-top: 0.8rem;
    font-size: 0.9rem;
    color: #d7d7d7;
}

.features div {
    margin-bottom: 4px;
}

.price {
    margin-top: 1.2rem;
    font-size: 1.4rem;
    font-weight: 700;
    color: #00ff9a;
}

.price-sub {
    font-size: 0.85rem;
    color: #bfbfbf;
    margin-top: 4px;
}

.highlight {
    color: #00ff9a;
}

.btn {
    margin-top: 1.4rem;
    display: flex;
    justify-content: center;
}

.btn a {
    border: 2px solid #00ff9a;
    padding: 0.6rem 2.4rem;
    border-radius: 50px;
    color:#00ff9a;
    text-decoration:none;
    font-weight:700;
}

.btn a:hover {
    background:#00ff9a;
    color:#000;
}
</style>
</head>

<body>

<div class="grid">

<!-- IBOV -->
<div class="card">
    <span class="badge-green">Essencial</span>
    <h3>Carteira IBOV</h3>

    <p class="desc">
    Ações líderes do Ibovespa com foco em consistência, diversificação e proteção de capital.
    </p>

    <div class="features">
        <div>• Principais ações do mercado brasileiro</div>
        <div>• Algoritmo proprietário com sinais objetivos</div>
        <div>• Alertas automáticos por Telegram e e-mail</div>
        <div>• Plataforma exclusiva com relatórios em tempo real</div>
    </div>

    <div class="price">R$ 148/mês</div>
    <div class="price-sub">
        Cobrado anualmente · <span class="highlight">3 meses grátis</span><br>
        Mensal R$ 197 · Trimestral R$ 173
    </div>

    <div class="btn">
        <a href="https://wa.me/351915323219" target="_blank">Assinar IBOV</a>
    </div>
</div>

<!-- SMALL CAPS -->
<div class="card">
    <span class="badge-orange">Alta Performance</span>
    <h3>Small Caps</h3>

    <p class="desc">
    Empresas em crescimento acelerado com alto potencial de valorização e maior volatilidade.
    </p>

    <div class="features">
        <div>• Foco em assimetria e oportunidades táticas</div>
        <div>• Algoritmo proprietário de monitoramento contínuo</div>
        <div>• Alertas automáticos por Telegram e e-mail</div>
        <div>• Plataforma exclusiva com histórico e relatórios</div>
    </div>

    <div class="price">R$ 164/mês</div>
    <div class="price-sub">
        Cobrado anualmente · <span class="highlight">Economize 3 meses</span><br>
        Mensal R$ 219 · Trimestral R$ 193
    </div>

    <div class="btn">
        <a href="https://wa.me/351915323219" target="_blank">Assinar Small Caps</a>
    </div>
</div>

<!-- BDR -->
<div class="card">
    <span class="badge-green">Internacional</span>
    <h3>Carteira BDR</h3>

    <p class="desc">
    Exposição a empresas globais com diversificação geográfica e cambial.
    </p>

    <div class="features">
        <div>• BDRs de grandes empresas internacionais</div>
        <div>• Diversificação fora do Brasil</div>
        <div>• Alertas automáticos por Telegram e e-mail</div>
        <div>• Plataforma exclusiva com dados e relatórios</div>
    </div>

    <div class="price">R$ 164/mês</div>
    <div class="price-sub">
        Cobrado anualmente · <span class="highlight">3 meses grátis</span><br>
        Mensal R$ 219 · Trimestral R$ 193
    </div>

    <div class="btn">
        <a href="https://wa.me/351915323219" target="_blank">Assinar BDR</a>
    </div>
</div>

<!-- OPÇÕES -->
<div class="card">
    <span class="badge-orange">Agressivo</span>
    <h3>Carteira de Opções</h3>

    <p class="desc">
    Estratégias com opções focadas em assimetria, volatilidade e proteção de carteira.
    </p>

    <div class="features">
        <div>• Estratégias estruturadas com derivativos</div>
        <div>• Exploração de volatilidade e distorções de preço</div>
        <div>• Alertas automáticos por Telegram e e-mail</div>
        <div>• Plataforma exclusiva com operações em tempo real</div>
    </div>

    <div class="price">R$ 223/mês</div>
    <div class="price-sub">
        Cobrado anualmente · <span class="highlight">3 meses grátis</span><br>
        Mensal R$ 297 · Trimestral R$ 261
    </div>

    <div class="btn">
        <a href="https://wa.me/351915323219" target="_blank">Assinar Opções</a>
    </div>
</div>

</div>

</body>
</html>


components.html(
    html_cards_detalhado,
    height=1200,
    scrolling=False
)

st.markdown("</div>", unsafe_allow_html=True)

