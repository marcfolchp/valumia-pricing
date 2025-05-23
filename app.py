import streamlit as st

st.set_page_config(page_title="Pricing", page_icon=":money_with_wings:", layout="wide")

# --- Modern Professional CSS ---
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    html, body, .stApp {
        background: linear-gradient(135deg, #e8f6ef 0%, #34bc7a 100%) !important;
        font-family: 'Inter', sans-serif !important;
    }
    .pricing-title {
        text-align: center;
        font-size: 4rem;
        font-weight: 800;
        color: #1a3c34;
        margin-bottom: 1.5rem;
        letter-spacing: 1px;
    }
    .centered-input-row {
        display: flex;
        justify-content: center;
        align-items: flex-end;
        gap: 2.5rem;
        margin-bottom: 2.5rem;
    }
    .input-label {
        font-size: 1.2rem;
        color: #1a3c34;
        font-weight: 600;
        margin-bottom: 0.5rem;
        display: block;
        text-align: center;
        letter-spacing: 0.5px;
    }
    .stNumberInput > div > input {
        font-size: 1.5rem !important;
        height: 2.8rem !important;
        width: 7rem !important;
        text-align: center;
        border-radius: 10px !important;
        border: 1.5px solid #34bc7a !important;
        background: #f8fdfb !important;
        box-shadow: 0 2px 8px rgba(52,188,122,0.08);
        margin-bottom: 0.5rem;
    }
    .pricing-card {
        background: linear-gradient(135deg, #ffffff 60%, #e8f6ef 100%);
        border-radius: 22px;
        padding: 2.2rem 2rem 2rem 2rem;
        color: #1a3c34;
        min-width: 270px;
        text-align: center;
        border: 1.5px solid #e0e0e0;
        box-shadow: 0 6px 32px 0 rgba(52,188,122,0.10), 0 1.5px 6px 0 rgba(0,0,0,0.03);
        margin-bottom: 1.5rem;
        transition: box-shadow 0.2s;
        position: relative;
    }
    .pricing-card:hover {
        box-shadow: 0 12px 40px 0 rgba(52,188,122,0.18), 0 2px 8px 0 rgba(0,0,0,0.06);
        border-color: #34bc7a;
    }
    .company-title {
        font-size: 2rem;
        font-weight: 800;
        margin-bottom: 1.2rem;
        letter-spacing: 1px;
        color: #34bc7a;
    }
    .static-price {
        font-size: 2.5rem;
        font-weight: 800;
        margin-bottom: 0.3rem;
        color: #1a3c34;
    }
    .per-request {
        font-size: 1.05rem;
        margin-bottom: 2.2rem;
        color: #4e6e5d;
    }
    .dynamic-price {
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 0.3rem;
        color: #217150;
    }
    .dynamic-label {
        font-size: 1.05rem;
        color: #4e6e5d;
        margin-bottom: 0.2rem;
    }
    .divider {
        width: 100%;
        height: 2px;
        background: linear-gradient(90deg, #34bc7a 0%, #e8f6ef 100%);
        margin: 2.5rem 0 2rem 0;
        border-radius: 2px;
        opacity: 0.25;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Title ---
st.markdown('<div class="pricing-title">API Pricing</div>', unsafe_allow_html=True)

# --- Centered, larger input boxes for suppliers (s) and keywords (k) ---
st.markdown('<div class="centered-input-row">', unsafe_allow_html=True)
col1, col2 = st.columns([1,1], gap="large")
with col1:
    st.markdown('<span class="input-label">Suppliers</span>', unsafe_allow_html=True)
    s = st.number_input(" ", min_value=1, value=100, step=10, key="suppliers")
with col2:
    st.markdown('<span class="input-label">Keywords</span>', unsafe_allow_html=True)
    k = st.number_input("  ", min_value=1, value=80, step=10, key="keywords")
st.markdown('</div>', unsafe_allow_html=True)

# --- Divider ---
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# --- Pricing Data ---
companies = [
    {
        "name": "EXA",
        "static_price": 2.5,
        "pro": "accuracy",
    },
    {
        "name": "GOOGLE",
        "static_price": 5.0,
        "pro": "compliance",
    },
    {
        "name": "RAPIDAPI",
        "static_price": 0.2,
        "pro": "price",
    },
]

# --- Cards Layout: 3 columns ---
col_exa, col_google = st.columns(2)
for col, company in zip([col_exa, col_google], companies):
    dynamic_price = ( company["static_price"] * k * s ) / 1000
    with col:
        st.markdown(f'''
        <div class="pricing-card">
            <div class="company-title">{company["name"]}</div>
            <div class="static-price">{company["static_price"]}€</div>
            <div class="per-request">per 1,000 requests</div>
            <div class="dynamic-price">{dynamic_price:.2f}€ / report</div>
            <div class="dynamic-label">for {k} keywords × {s} suppliers</div>
        </div>
        <div style="display:flex; justify-content:center; margin-top:0.7rem;">
            <div style="background:rgba(255,255,255,0.92); border-radius:12px; padding:0.3rem 1.1rem; font-size:1.05rem; color:#34bc7a; font-weight:600; letter-spacing:0.5px; box-shadow:0 1px 6px 0 rgba(52,188,122,0.07);">
                PRO: <span style=\"color:#217150; font-weight:700; text-transform:capitalize;\">{company['pro']}</span>
            </div>
        </div>
        ''', unsafe_allow_html=True)
