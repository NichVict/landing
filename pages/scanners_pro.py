import streamlit as st

st.set_page_config(page_title="Linha PRO — Scanners Profissionais", layout="wide")

# ================================================================
# ESTILO PREMIUM NEON
# ================================================================
st.markdown("""
<style>

    .premium-wrapper {
        max-width: 1200px;
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

    /* GRID – 3 colunas no desktop, 1 no mobile */
    .grid-pro {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 28px;
    }

    @media(max-width: 900px) {
        .grid-pro {
            grid-template-columns: repeat(1, 1fr);
        }
    }

    /* CARD PRO */
    .plan-card-wrapper {
        background: rgba(255,255,255,0.03);
        border-radius: 22px;
        padding: 2rem;
        border: 1px solid rgba(0,255,154,0.28);
        box-shadow: 0 0 18px rgba(0,255,154,0.30);
        transition: 0.25s;
    }

    .plan-card-wrapper:hover {
        transform: translateY(-4px);
        box-shadow: 0 0 30px rgba(0,255,154,0.55);
    }

    .badge {
        background: #ff7a1a;
        padding: 6px 12px;
        border-radius: 50px;
        font-size: 0.78rem;
        font-weight: 700;
        color: #000;
    }

    .badge-green {
        background: #00ff9a;
        padding: 6px 12px;
        border-radius: 50px;
        font-size: 0.78rem;
        font-weight: 700;
        color: #000;
    }

    h3 {
        margin-top: 1rem;
        margin-bottom: 0.6rem;
        color: #fff;
        font-size: 1.55rem;
    }

    .plan-card {
        margin-bottom: 1.2rem;
    }

    .price {
        margin-top: 1rem;
        font-size: 1.45rem;
        font-weight: 700;
        color: #00ff9a;
    }

    .assinatura-btn {
        margin-top: 1.2rem;
        display: flex;
        justify-content: center;
    }

    .assinatura-btn a {
        background: transparent;
        border: 2px solid #00ff9a;
        color: #00ff9a !important;
        padding: 0.55rem 2.2rem;
        border-radius: 50px;
        font-weight: 700;
        text-decoration: none;
        transition: 0.25s;
    }

    .assinatura-btn a:hover {
        background: #00ff9a;
        color: #000 !important;
        box-shadow: 0 0 18px rgba(0,255,154,0.45);
    }

</style>
""", unsafe_allow_html=True)

# ================================================================
# CONTEÚDO
# ================================================================
st.markdown("<div class='premium-wrapper'>", unsafe_allow_html=True)

st.markdown("<h2 class='titulo'>Linha PRO — Scanners Profissionais</h2>", unsafe_allow_html=True)
st.markdown("""
<p class='subtexto'>
Ferramentas avançadas para traders profissionais que buscam autonomia, precisão e leitura profunda do mercado.
</p>
""", unsafe_allow_html=True)


st.markdown("<div class='grid-pro'>", unsafe_allow_html=True)

# ---------------------- SCANNER AÇÕES ----------------------
st.markdown("""
<div class='plan-card-wrapper'>
    <div class='plan-card'>
        <span class='badge'>Profissional</span>    
        <h3>Phoenix Scanner Ações</h3>
        <p>O motor analítico de ações. Autonomia total para traders avançados.</p>
        <div class='price'>R$ 397/mês</div>
    </div>
    <div class='assinatura-btn'>
        <a href='https://wa.me/351915323219' target='_blank'>Assinar Scanner Ações</a>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------------- SCANNER OPÇÕES ----------------------
st.markdown("""
<div class='plan-card-wrapper'>
    <div class='plan-card'>
        <span class='badge'>Profissional</span>
        <h3>Phoenix Scanner Opções</h3>
        <p>Leitura avançada de volatilidade, assimetrias e distorções de prêmio.</p>
        <div class='price'>R$ 397/mês</div>
    </div>
    <div class='assinatura-btn'>
        <a href='https://wa.me/351915323219' target='_blank'>Assinar Volatility Scanner</a>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------------- SCANNER PRO ----------------------
st.markdown("""
<div class='plan-card-wrapper'>
    <div class='plan-card'>
        <span class='badge-green'>Completo</span>
        <h3>Phoenix Scanner PRO</h3>
        <p>Ações + Opções. A experiência definitiva para profissionais.</p>
        <div class='price'>R$ 597/mês</div>
    </div>
    <div class='assinatura-btn'>
        <a href='https://wa.me/351915323219' target='_blank'>Assinar Scanner PRO</a>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)  # fecha grid
st.markdown("</div>", unsafe_allow_html=True)  # fecha wrapper
