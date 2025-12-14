import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Carteiras Individuais – Phoenix Strategy",
    layout="wide"
)

# ================================================================
# CABEÇALHO DA PÁGINA (STREAMLIT)
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

st.markdown("<div class='planos-wrapper'>", unsafe_allow_html=True)
st.markdown("<h2 class='titulo'>Carteiras Individuais</h2>", unsafe_allow_html=True)
st.markdown("""
<p class='subtexto'>
Planos individuais para quem deseja focar apenas em uma estratégia específica de ações ou derivativos.
</p>
""", unsafe_allow_html=True)

# ================================================================
# HTML DOS CARDS (CAMINHO B – SEM MARKDOWN)
# ================================================================
html_cards = '''
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<style>

.grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 22px;
}

@media(max-width: 1100px) {
    .grid { grid-template-columns: repeat(2, 1fr); }
}

@media(max-width: 700px) {
    .grid { grid-template-columns: 1fr; }
}

.card {
    background: rgba(255,255,255,0.03);
    border-radius: 18px;
    padding: 1.5rem;
    border: 1px solid rgba(0,255,154,0.25);
    box-shadow: 0 0 18px rgba(0,255,154,0.35);
    color: white;
    font-family: Arial, Helvetica, sans-serif;
}

.badge-green {
    background: #00ff9a;
    padding: 4px 10px;
    border-radius: 50px;
    font-size: 0.75rem;
    font-weight: 700;
    color: #000;
    display: inline-block;
}

.badge-orange {
    background: #ff7a1a;
    padding: 4px 10px;
    border-radius: 50px;
    font-size: 0.75rem;
    font-weight: 700;
    color: #000;
    display: inline-block;
}

h3 {
    margin-top: 0.8rem;
    margin-bottom: 0.4rem;
}

.desc {
    color: #d7d7d7;
    font-size: 0.95rem;
}

.price {
    margin-top: 1rem;
    font-size: 1.3rem;
    font-weight: 700;
    color: #00ff9a;
}

.price-sub {
    font-size: 0.8rem;
    color: #bfbfbf;
    margin-top: 4px;
}

.btn {
    margin-top: 1.2rem;
    display: flex;
    justify-content: center;
}

.btn a {
    border: 2px solid #00ff9a;
    padding: 0.5rem 2rem;
    border-radius: 50px;
    color: #00ff9a;
    text-decoration: none;
    font-weight: 700;
}

.btn a:hover {
    background: #00ff9a;
    color: #000;
}

</style>
</head>

<body>

<div class="grid">

<div class="card">
    <span class="badge-green">Essencial</span>
    <h3>Carteira IBOV</h3>
    <p class="desc">Ações líderes do Ibovespa com foco em consistência e proteção de capital.</p>
    <div class="price">R$ 148/mês</div>
    <div class="price-sub">Cobrado anualmente · 3 meses grátis<br>Mensal R$ 197 · Trimestral R$ 173</div>
    <div class="btn"><a href="https://wa.me/351915323219" target="_blank">Assinar</a></div>
</div>

<div class="card">
    <span class="badge-orange">Alta Performance</span>
    <h3>Small Caps</h3>
    <p class="desc">Empresas em crescimento acelerado com maior potencial de valorização.</p>
    <div class="price">R$ 164/mês</div>
    <div class="price-sub">Cobrado anualmente · 3 meses grátis<br>Mensal R$ 219 · Trimestral R$ 193</div>
    <div class="btn"><a href="https://wa.me/351915323219" target="_blank">Assinar</a></div>
</div>

<div class="card">
    <span class="badge-green">Internacional</span>
    <h3>Carteira BDR</h3>
    <p class="desc">Exposição a empresas globais com diversificação cambial.</p>
    <div class="price">R$ 164/mês</div>
    <div class="price-sub">Cobrado anualmente · 3 meses grátis<br>Mensal R$ 219 · Trimestral R$ 193</div>
    <div class="btn"><a href="https://wa.me/351915323219" target="_blank">Assinar</a></div>
</div>

<div class="card">
    <span class="badge-orange">Agressivo</span>
    <h3>Carteira de Opções</h3>
    <p class="desc">Estratégias com opções focadas em assimetria e volatilidade.</p>
    <div class="price">R$ 223/mês</div>
    <div class="price-sub">Cobrado anualmente · 3 meses grátis<br>Mensal R$ 297 · Trimestral R$ 261</div>
    <div class="btn"><a href="https://wa.me/351915323219" target="_blank">Assinar</a></div>
</div>

</div>

</body>
</html>
'''

components.html(
    html_cards,
    height=520,
    scrolling=False
)

st.markdown("</div>", unsafe_allow_html=True)
