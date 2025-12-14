import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Planos Premium – Phoenix Strategy",
    layout="wide"
)

# ================================================================
# CABEÇALHO
# ================================================================
st.markdown("""
<style>
.wrapper {
    max-width: 1100px;
    margin: 0 auto;
    margin-top: 2rem;
}

.titulo {
    color: #ffffff;
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

st.markdown("<div class='wrapper'>", unsafe_allow_html=True)
st.markdown("<h2 class='titulo'>Planos Premium</h2>", unsafe_allow_html=True)
st.markdown(
    "<p class='subtexto'>Os melhores planos custo-benefício para quem quer operar ações ou unificar todas as carteiras em um único pacote.</p>",
    unsafe_allow_html=True
)

# ================================================================
# HTML DOS PLANOS PREMIUM (ISOLADO)
# ================================================================
html_premium = '''
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<style>

.grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 28px;
}

.card {
    background: rgba(255,255,255,0.03);
    border-radius: 18px;
    padding: 2rem;
    border: 1px solid rgba(0,255,154,0.35);
    box-shadow: 0 0 25px rgba(0,255,154,0.4);
    color: white;
    font-family: Arial, Helvetica, sans-serif;
}

.badge-orange {
    background: #ff7a1a;
    padding: 5px 14px;
    border-radius: 50px;
    font-size: 0.75rem;
    font-weight: 700;
    color: #000;
    display: inline-block;
}

.badge-green {
    background: #00ff9a;
    padding: 5px 14px;
    border-radius: 50px;
    font-size: 0.75rem;
    font-weight: 700;
    color: #000;
    display: inline-block;
}

h3 {
    margin-top: 0.8rem;
    margin-bottom: 0.5rem;
}

.desc {
    color: #d7d7d7;
    font-size: 0.95rem;
}

.price {
    margin-top: 1.2rem;
    font-size: 1.5rem;
    font-weight: 700;
    color: #00ff9a;
}

.price-sub {
    font-size: 0.9rem;
    color: #bfbfbf;
    margin-top: 6px;
    line-height: 1.4;
}

.highlight {
    color: #00ff9a;
}

.btn {
    margin-top: 1.6rem;
    display: flex;
    justify-content: center;
}

.btn a {
    border: 2px solid #00ff9a;
    padding: 0.6rem 2.8rem;
    border-radius: 50px;
    color: #00ff9a;
    text-decoration: none;
    font-weight: 700;
}

.btn a:hover {
    background: #00ff9a;
    color: #000;
}

.section-title {
    margin-top: 3rem;
    margin-bottom: 1rem;
    font-size: 1.4rem;
    color: #ffffff;
}

.features {
    color: #d7d7d7;
    font-size: 0.95rem;
    line-height: 1.6;
}

.features div {
    margin-bottom: 6px;
}

</style>
</head>

<body>

<div class="grid">

<!-- PHOENIX EQUITY -->
<div class="card">
    <span class="badge-orange">Mais vendido</span>
    <h3>Phoenix Equity</h3>

    <p class="desc">
        Inclui IBOV, Small Caps e BDR. O melhor custo-benefício para quem opera ações.
    </p>

    <div class="price">R$ 335/mês no plano anual</div>
    <div class="price-sub">
        Economia de <strong>25%</strong>
        <span class="highlight">(equivalente a 3 meses grátis)</span>
    </div>

    <div class="price-sub" style="margin-top:8px;">
        <strong>Plano trimestral:</strong> R$ 393/mês<br>
        Economia de <strong>12%</strong> · pagamento a cada 3 meses
    </div>

    <div class="price-sub" style="margin-top:6px;">
        <strong>Plano mensal:</strong> R$ 447/mês
    </div>

    <div class="btn">
        <a href="https://wa.me/351915323219" target="_blank">Assinar Phoenix Equity</a>
    </div>
</div>

<!-- PHOENIX FULL -->
<div class="card">
    <span class="badge-green">Recomendado</span>
    <h3>Phoenix Full</h3>

    <p class="desc">
        Todas as carteiras em um único plano: IBOV, Small Caps, BDR e Opções.
    </p>

    <div class="price">R$ 448/mês no plano anual</div>
    <div class="price-sub">
        Economia de <strong>25%</strong>
        <span class="highlight">(equivalente a 3 meses grátis)</span>
    </div>

    <div class="price-sub" style="margin-top:8px;">
        <strong>Plano trimestral:</strong> R$ 525/mês<br>
        Economia de <strong>12%</strong> · pagamento a cada 3 meses
    </div>

    <div class="price-sub" style="margin-top:6px;">
        <strong>Plano mensal:</strong> R$ 597/mês
    </div>

    <div class="btn">
        <a href="https://wa.me/351915323219" target="_blank">Assinar Phoenix Full</a>
    </div>
</div>

</div>

<!-- DESCRIÇÃO ABAIXO -->
<div class="section-title">O que está incluído em cada plano</div>

<div class="features">
    <div><strong>IBOV:</strong> ações líderes do Ibovespa com foco em consistência e proteção de capital.</div>
    <div><strong>Small Caps:</strong> empresas em crescimento acelerado com alto potencial de valorização.</div>
    <div><strong>BDR:</strong> exposição a empresas globais com diversificação geográfica e cambial.</div>
    <div><strong>Opções:</strong> estratégias com derivativos focadas em assimetria, volatilidade e proteção.</div>
    <div>✔️ Alertas automáticos por Telegram e e-mail</div>
    <div>✔️ Plataforma exclusiva com operações e relatórios em tempo real</div>
</div>

</body>
</html>
'''

components.html(
    html_premium,
    height=1150,
    scrolling=False
)

st.markdown("</div>", unsafe_allow_html=True)
