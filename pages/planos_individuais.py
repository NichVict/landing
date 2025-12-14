


import streamlit as st

st.set_page_config(page_title="Carteiras Individuais – Phoenix Strategy", layout="wide")

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

    /* GRID RESPONSIVO */
    .grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 22px;
    }

    @media(max-width: 1100px) {
        .grid {
            grid-template-columns: repeat(2, 1fr);
        }
    }

    @media(max-width: 700px) {
        .grid {
            grid-template-columns: repeat(1, 1fr);
        }
    }

    /* CARDS */
    .plan-card-wrapper {
        background: rgba(255,255,255,0.03);
        border-radius: 18px;
        padding: 1.5rem;
        border: 1px solid rgba(0,255,154,0.25);
        box-shadow: 0 0 15px rgba(0,255,154,0.25);
        transition: 0.25s;
    }

    .plan-card-wrapper:hover {
        transform: translateY(-3px);
        box-shadow: 0 0 25px rgba(0,255,154,0.45);
    }

    .badge-green {
        background: #00ff9a;
        padding: 4px 10px;
        border-radius: 50px;
        font-size: 0.75rem;
        font-weight: 700;
        color: #000;
    }

    .badge {
        background: #ff7a1a;
        padding: 4px 10px;
        border-radius: 50px;
        font-size: 0.75rem;
        font-weight: 700;
        color: #000;
    }

    h3 {
        margin-top: 0.8rem;
        color: #fff;
    }

    .price {
        margin-top: 1rem;
        font-size: 1.3rem;
        font-weight: 700;
        color: #00ff9a;
    }

    .assinatura-btn {
        margin-top: 1rem;
        display: flex;
        justify-content: center;
    }

    .assinatura-btn a {
        background: transparent;
        border: 2px solid #00ff9a;
        color: #00ff9a !important;
        padding: 0.5rem 2rem;
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
# CONTEÚDO DA PÁGINA
# ================================================================
st.markdown("<div class='planos-wrapper'>", unsafe_allow_html=True)

st.markdown("<h2 class='titulo'>Carteiras Individuais</h2>", unsafe_allow_html=True)
st.markdown("""
<p class='subtexto'>
Planos individuais para quem deseja focar apenas em uma estratégia específica de ações ou derivativos.
</p>
""", unsafe_allow_html=True)

st.markdown("<div class='grid'>", unsafe_allow_html=True)

# ----------------------------- CARD 1
st.markdown("""
<div class='plan-card-wrapper'>
    <span class='badge-green'>Essencial</span>
    <h3>Carteira IBOV</h3>

    <p>
    Ações líderes do Ibovespa com foco em consistência e proteção de capital.
    </p>

    <p style='font-size:0.9rem; color:#d7d7d7;'>
    • Sinais claros de entrada e saída<br>
    • Operações baseadas em tendência<br>
    • Ideal para investidores que buscam previsibilidade
    </p>

    <div class='price'>R$ 197/mês</div>

    <p style='font-size:0.85rem; color:#bfbfbf;'>
        Trimestral: <b>R$ 173/mês</b> ·
        Anual: <b>R$ 148/mês</b><br>
        <span style='color:#00ff9a;'>3 meses grátis no plano anual</span>
    </p>

    <div class='assinatura-btn'>
        <a href='https://wa.me/351915323219' target='_blank'>Assinar IBOV</a>
    </div>
</div>
""", unsafe_allow_html=True)


# ----------------------------- CARD 2
st.markdown("""
<div class='plan-card-wrapper'>
    <span class='badge'>Alta Performance</span>
    <h3>Small Caps</h3>
    <p>Oportunidades agressivas com forte potencial de valorização.</p>
    <div class='price'>R$ 219/mês</div>
    <div class='assinatura-btn'>
        <a href='https://wa.me/351915323219' target='_blank'>Assinar</a>
    </div>
</div>
""", unsafe_allow_html=True)

# ----------------------------- CARD 3
st.markdown("""
<div class='plan-card-wrapper'>
    <span class='badge-green'>Internacional</span>
    <h3>Carteira BDR</h3>
    <p>Exposição global com simplicidade total.</p>
    <div class='price'>R$ 219/mês</div>
    <div class='assinatura-btn'>
        <a href='https://wa.me/351915323219' target='_blank'>Assinar</a>
    </div>
</div>
""", unsafe_allow_html=True)

# ----------------------------- CARD 4
st.markdown("""
<div class='plan-card-wrapper'>
    <span class='badge'>Agressivo</span>
    <h3>Carteira de Opções</h3>
    <p>Estratégias assimétricas com potencial explosivo.</p>
    <div class='price'>R$ 297/mês</div>
    <div class='assinatura-btn'>
        <a href='https://wa.me/351915323219' target='_blank'>Assinar</a>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)  # fecha grid
st.markdown("</div>", unsafe_allow_html=True)  # fecha wrapper
