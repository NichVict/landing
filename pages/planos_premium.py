import streamlit as st

st.set_page_config(page_title="Planos Premium – Phoenix Strategy", layout="wide")

# ================================================================
# ESTILO PREMIUM NEON
# ================================================================
st.markdown("""
<style>

    .premium-wrapper {
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

    /* GRID – Premium fica lado a lado, e em 1 coluna no mobile */
    .grid-premium {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 28px;
    }

    @media(max-width: 900px) {
        .grid-premium {
            grid-template-columns: repeat(1, 1fr);
        }
    }

    /* CARD PREMIUM */
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

st.markdown("<h2 class='titulo'>Planos Premium</h2>", unsafe_allow_html=True)
st.markdown("""
<p class='subtexto'>
Os melhores planos custo-benefício para quem quer operar ações ou unir todas as carteiras em um único pacote.
</p>
""", unsafe_allow_html=True)


st.markdown("<div class='grid-premium'>", unsafe_allow_html=True)

# ---------------------- PHOENIX EQUITY ----------------------
st.markdown("""
<div class='plan-card-wrapper'>
    <div class='plan-card'>
        <span class='badge'>Mais Vendido</span>
        <h3>Phoenix Equity</h3>
        <p>Inclui IBOV + Small Caps + BDR. O melhor custo-benefício para quem opera ações.</p>
        <div class='price'>R$ 247/mês</div>
    </div>
    <div class='assinatura-btn'>
        <a href='https://wa.me/351915323219' target='_blank'>Assinar Phoenix Equity</a>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------------- PHOENIX FULL ----------------------
st.markdown("""
<div class='plan-card-wrapper'>
    <div class='plan-card'>
        <span class='badge'>Recomendado</span>
        <h3>Phoenix Full</h3>
        <p>Todas as 4 carteiras: IBOV, Small Caps, BDR e Opções em um único plano.</p>
        <div class='price'>R$ 397/mês</div>
    </div>
    <div class='assinatura-btn'>
        <a href='https://wa.me/351915323219' target='_blank'>Assinar Phoenix Full</a>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)  # fecha grid
st.markdown("</div>", unsafe_allow_html=True)  # fecha wrapper
