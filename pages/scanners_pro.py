import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Linha PRO – Scanners Profissionais | Phoenix Strategy",
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
st.markdown("<h2 class='titulo'>Linha PRO — Scanners Profissionais</h2>", unsafe_allow_html=True)
st.markdown(
    "<p class='subtexto'>Ferramentas avançadas para traders profissionais que buscam autonomia, precisão e leitura profunda do mercado.</p>",
    unsafe_allow_html=True
)

# ================================================================
# HTML ISOLADO — SCANNERS PRO
# ================================================================
html_scanners = '''
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

<!-- SCANNER AÇÕES -->
<div class="card">
    <span class="badge-orange">Uso Profissional</span>
    <h3>Phoenix Scanner Ações</h3>

    <p class="desc">
        Motor analítico de ações. Autonomia total para leitura técnica e tomada de decisão.
    </p>

    <div class="price">R$ 298/mês no plano anual</div>
    <div class="price-sub">
        Economia de <strong>25%</strong>
        <span class="highlight">(equivalente a 3 meses grátis)</span>
    </div>

    <div class="price-sub" style="margin-top:8px;">
        <strong>Plano trimestral:</strong> R$ 349/mês<br>
        Economia de <strong>12%</strong> · pagamento a cada 3 meses
    </div>

    <div class="price-sub" style="margin-top:6px;">
        <strong>Plano mensal:</strong> R$ 397/mês
    </div>

    <div class="btn">
        <a href="https://loja.infinitepay.io/aurinvest/yhz4317-scanner-acoes-ibov" target="_blank">Assinar Scanner Ações</a>
    </div>
</div>

<!-- SCANNER OPÇÕES -->
<div class="card">
    <span class="badge-orange">Traders Avançados</span>
    <h3>Phoenix Scanner Opções</h3>

    <p class="desc">
        Leitura avançada de volatilidade, assimetrias e distorções de prêmio no mercado de opções.
    </p>

    <div class="price">R$ 298/mês no plano anual</div>
    <div class="price-sub">
        Economia de <strong>25%</strong>
        <span class="highlight">(equivalente a 3 meses grátis)</span>
    </div>

    <div class="price-sub" style="margin-top:8px;">
        <strong>Plano trimestral:</strong> R$ 349/mês<br>
        Economia de <strong>12%</strong> · pagamento a cada 3 meses
    </div>

    <div class="price-sub" style="margin-top:6px;">
        <strong>Plano mensal:</strong> R$ 397/mês
    </div>

    <div class="btn">
        <a href="https://loja.infinitepay.io/aurinvest/imf0541-scanner-opcoes-de-acoes-ibov" target="_blank">Assinar Scanner Opções</a>
    </div>
</div>

<!-- SCANNER PRO -->
<div class="card">
    <span class="badge-green">Completo</span>
    <h3>Phoenix Scanner PRO</h3>

    <p class="desc">
        Ações + Opções. A experiência definitiva para profissionais que exigem leitura total do mercado.
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
        <a href="https://wa.me/351915323219" target="_blank">Assinar Scanner PRO</a>
    </div>
</div>

</div>

<!-- DESCRIÇÃO -->
<div class="section-title">O que cada Scanner entrega</div>

<div class="features">
    <div><strong>Scanner Ações:</strong> leitura técnica automatizada, filtros proprietários e identificação de oportunidades em tempo real.</div>
    <div><strong>Scanner Opções:</strong> análise profunda de volatilidade implícita, skew, assimetrias e distorções de prêmio.</div>
    <div><strong>Scanner PRO:</strong> combinação completa de ações + opções para leitura total do mercado.</div>
    <div>✔️ Plataforma profissional em tempo real</div>
    <div>✔️ Ferramenta de apoio à decisão (não são sinais)</div>
    <div>✔️ Autonomia total para traders avançados</div>
</div>

</body>
</html>
'''

components.html(
    html_scanners,
    height=1550,
    scrolling=False
)

st.markdown("</div>", unsafe_allow_html=True)
