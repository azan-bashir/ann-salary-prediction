import pickle
from textwrap import dedent

import pandas as pd
import streamlit as st
from tensorflow import keras


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="SALARY INTELLIGENCE ",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)


# =========================================================
# HTML RENDERER
# =========================================================
# Use Streamlit's native HTML renderer for UI markup. This avoids
# Markdown interpreting HTML as a code block and displaying tags such
# as <div> / </div> as visible text.

def render_html(markup: str) -> None:
    st.html(dedent(markup).strip())


# =========================================================
# PREMIUM DARK / NEON UI
# =========================================================

render_html(
    """
    <style>
        /* ---------- GLOBAL ---------- */
        .stApp {
            background:
                radial-gradient(circle at 5% 0%, rgba(34,211,238,0.09), transparent 28%),
                radial-gradient(circle at 96% 8%, rgba(124,58,237,0.12), transparent 30%),
                linear-gradient(135deg, #030712 0%, #07111f 48%, #0a1022 100%);
        }

        .block-container {
            max-width: 1440px;
            padding: 2.0rem 2.0rem 1.5rem 2.0rem;
        }

        /* ---------- SIDEBAR ---------- */
        section[data-testid="stSidebar"] {
            background:
                linear-gradient(180deg, #020617 0%, #07101f 58%, #081225 100%);
            border-right: 1px solid rgba(56,189,248,0.12);
        }

        section[data-testid="stSidebar"] * {
            color: #dbeafe;
        }

        section[data-testid="stSidebar"] .block-container {
            padding: 1.2rem 1rem 1rem 1rem;
        }

        /* ---------- TYPOGRAPHY ---------- */
        h1, h2, h3, h4, p, label, span, div {
            font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        }

        label {
            color: #cbd5e1 !important;
            font-weight: 650 !important;
        }

        .section-kicker {
            margin-top: 0.4rem;
            margin-bottom: 0.2rem;
            color: #67e8f9;
            font-size: 0.72rem;
            font-weight: 800;
            letter-spacing: 0.18em;
            text-transform: uppercase;
        }

        .section-heading {
            margin: 0;
            color: #f8fafc;
            font-size: 1.65rem;
            font-weight: 800;
            letter-spacing: -0.03em;
        }

        .section-copy {
            margin-top: 0.35rem;
            margin-bottom: 1.15rem;
            color: #7f8ea7;
            font-size: 0.88rem;
            line-height: 1.55;
        }

        /* ---------- HERO ---------- */
        .hero-shell {
            position: relative;
            overflow: hidden;
            padding: 2.15rem 2.2rem 2rem 2.2rem;
            margin-bottom: 1.7rem;
            border: 1px solid rgba(56,189,248,0.18);
            border-radius: 26px;
            background:
                radial-gradient(circle at 87% 20%, rgba(59,130,246,0.16), transparent 25%),
                radial-gradient(circle at 10% 90%, rgba(34,211,238,0.10), transparent 25%),
                linear-gradient(135deg, rgba(7,17,31,0.97), rgba(14,22,44,0.94));
            box-shadow:
                0 26px 75px rgba(0,0,0,0.32),
                inset 0 1px 0 rgba(255,255,255,0.035);
        }

        .hero-shell::after {
            content: "";
            position: absolute;
            width: 260px;
            height: 260px;
            right: -100px;
            top: -100px;
            border-radius: 50%;
            border: 1px solid rgba(124,58,237,0.18);
            box-shadow: 0 0 80px rgba(124,58,237,0.10);
            pointer-events: none;
        }

        .hero-badges {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin-bottom: 1.0rem;
        }

        .hero-badge {
            display: inline-flex;
            align-items: center;
            padding: 0.38rem 0.72rem;
            border-radius: 999px;
            border: 1px solid rgba(56,189,248,0.22);
            background: rgba(14,165,233,0.07);
            color: #8be9f5;
            font-size: 0.68rem;
            font-weight: 800;
            letter-spacing: 0.08em;
            text-transform: uppercase;
        }

        .hero-badge.purple {
            border-color: rgba(167,139,250,0.24);
            background: rgba(124,58,237,0.08);
            color: #c4b5fd;
        }

        .hero-badge.green {
            border-color: rgba(74,222,128,0.22);
            background: rgba(34,197,94,0.07);
            color: #86efac;
        }

        .hero-title {
            margin: 0;
            color: #f8fafc;
            font-size: clamp(2.2rem, 4vw, 3.4rem);
            font-weight: 850;
            line-height: 1.03;
            letter-spacing: -0.055em;
        }

        .hero-gradient {
            background: linear-gradient(90deg, #67e8f9 0%, #60a5fa 48%, #a78bfa 100%);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
        }

        .hero-subtitle {
            max-width: 760px;
            margin-top: 0.85rem;
            color: #9aa9bf;
            font-size: 1rem;
            line-height: 1.65;
        }

        .hero-meta {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 0.8rem;
            margin-top: 1.4rem;
            max-width: 820px;
        }

        .hero-meta-item {
            padding: 0.8rem 0.9rem;
            border: 1px solid rgba(148,163,184,0.12);
            border-radius: 14px;
            background: rgba(2,6,23,0.30);
        }

        .hero-meta-label {
            color: #64748b;
            font-size: 0.67rem;
            font-weight: 750;
            letter-spacing: 0.08em;
            text-transform: uppercase;
        }

        .hero-meta-value {
            margin-top: 0.2rem;
            color: #e2e8f0;
            font-size: 0.86rem;
            font-weight: 700;
        }

        /* ---------- SIDEBAR CARDS ---------- */
        .side-brand {
            padding: 0.35rem 0.15rem 0.9rem 0.15rem;
        }

        .side-brand-title {
            color: #f8fafc;
            font-size: 1rem;
            font-weight: 800;
        }

        .side-brand-copy {
            margin-top: 0.3rem;
            color: #64748b;
            font-size: 0.7rem;
            line-height: 1.45;
        }

        .side-card {
            padding: 0.9rem;
            margin-bottom: 0.75rem;
            border: 1px solid rgba(148,163,184,0.13);
            border-radius: 16px;
            background: linear-gradient(145deg, rgba(15,23,42,0.82), rgba(8,20,35,0.72));
            box-shadow: 0 12px 30px rgba(0,0,0,0.16);
        }

        .side-card-title {
            color: #bae6fd;
            font-size: 0.7rem;
            font-weight: 850;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            margin-bottom: 0.55rem;
        }

        .side-row {
            display: flex;
            justify-content: space-between;
            gap: 0.6rem;
            padding: 0.28rem 0;
            color: #7f8ea7;
            font-size: 0.69rem;
        }

        .side-row strong {
            color: #dbeafe;
            font-weight: 750;
            text-align: right;
        }

        .status-dot {
            display: inline-block;
            width: 7px;
            height: 7px;
            margin-right: 5px;
            border-radius: 50%;
            background: #22c55e;
            box-shadow: 0 0 10px rgba(34,197,94,0.75);
            vertical-align: middle;
        }

        .side-note {
            padding-top: 0.2rem;
            color: #596981;
            font-size: 0.62rem;
            line-height: 1.55;
        }

        /* ---------- NATIVE INPUT CONTAINERS ---------- */
        div[data-testid="stVerticalBlockBorderWrapper"] {
            border: 1px solid rgba(56,189,248,0.13) !important;
            border-radius: 20px !important;
            background:
                linear-gradient(145deg, rgba(8,20,35,0.82), rgba(10,17,34,0.74)) !important;
            box-shadow:
                0 18px 45px rgba(0,0,0,0.20),
                inset 0 1px 0 rgba(255,255,255,0.025) !important;
        }

        div[data-testid="stVerticalBlockBorderWrapper"]:hover {
            border-color: rgba(56,189,248,0.25) !important;
            box-shadow:
                0 18px 48px rgba(0,0,0,0.24),
                0 0 28px rgba(34,211,238,0.05) !important;
            transition: 180ms ease;
        }

        /* ---------- STREAMLIT INPUTS ---------- */
        div[data-baseweb="select"] > div {
            background: rgba(15,23,42,0.78) !important;
            border: 1px solid rgba(100,116,139,0.24) !important;
            border-radius: 12px !important;
        }

        div[data-baseweb="select"] > div:hover {
            border-color: rgba(56,189,248,0.38) !important;
        }

        input {
            color: #f8fafc !important;
        }

        input[type="number"] {
            background: rgba(15,23,42,0.78) !important;
            border: 1px solid rgba(100,116,139,0.24) !important;
            border-radius: 12px !important;
        }

        div[data-testid="stSlider"] [role="slider"] {
            box-shadow: 0 0 0 3px rgba(34,211,238,0.08), 0 0 12px rgba(34,211,238,0.35);
        }

        div[data-testid="stSlider"] [data-baseweb="slider"] > div > div {
            border-radius: 999px;
        }

        /* ---------- CTA BUTTON ---------- */
        div.stButton {
            display: flex;
            justify-content: center;
        }

        div.stButton > button {
            width: min(100%, 720px);
            min-height: 58px;
            border: 1px solid rgba(129,140,248,0.35) !important;
            border-radius: 16px !important;
            background: linear-gradient(90deg, #2563eb 0%, #4f46e5 50%, #7c3aed 100%) !important;
            color: #ffffff !important;
            font-size: 0.96rem !important;
            font-weight: 800 !important;
            letter-spacing: 0.01em;
            box-shadow:
                0 14px 35px rgba(79,70,229,0.28),
                0 0 22px rgba(59,130,246,0.10);
            transition: transform 160ms ease, box-shadow 160ms ease, filter 160ms ease;
        }

        div.stButton > button:hover {
            transform: translateY(-2px);
            filter: brightness(1.07);
            box-shadow:
                0 18px 42px rgba(79,70,229,0.38),
                0 0 28px rgba(96,165,250,0.16);
        }

        div.stButton > button:active {
            transform: translateY(0);
        }

        /* ---------- SUMMARY ---------- */
        .summary-shell {
            padding: 1rem;
            border: 1px solid rgba(56,189,248,0.12);
            border-radius: 20px;
            background: linear-gradient(145deg, rgba(7,17,31,0.70), rgba(9,18,35,0.56));
        }

        .profile-tile {
            min-height: 78px;
            padding: 0.8rem 0.85rem;
            border: 1px solid rgba(100,116,139,0.14);
            border-radius: 14px;
            background: rgba(2,6,23,0.34);
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.02);
        }

        .profile-label {
            color: #64748b;
            font-size: 0.62rem;
            font-weight: 800;
            letter-spacing: 0.09em;
            text-transform: uppercase;
        }

        .profile-value {
            margin-top: 0.33rem;
            color: #eef2ff;
            font-size: 0.92rem;
            font-weight: 750;
        }

        .profile-icon {
            float: left;
            margin-right: 0.45rem;
            font-size: 0.85rem;
        }

        /* ---------- PREDICTION ---------- */
        .prediction-shell {
            position: relative;
            overflow: hidden;
            padding: 2.2rem 1.5rem 2rem 1.5rem;
            margin-top: 1.6rem;
            border: 1px solid rgba(103,232,249,0.22);
            border-radius: 26px;
            background:
                radial-gradient(circle at 50% 0%, rgba(34,211,238,0.12), transparent 36%),
                radial-gradient(circle at 87% 83%, rgba(124,58,237,0.15), transparent 32%),
                linear-gradient(145deg, rgba(7,19,35,0.98), rgba(10,17,36,0.94));
            text-align: center;
            box-shadow:
                0 28px 70px rgba(0,0,0,0.34),
                0 0 32px rgba(34,211,238,0.05),
                inset 0 1px 0 rgba(255,255,255,0.035);
        }

        .prediction-icon {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 66px;
            height: 66px;
            border: 1px solid rgba(103,232,249,0.20);
            border-radius: 50%;
            background: rgba(8,47,73,0.36);
            box-shadow: 0 0 30px rgba(34,211,238,0.12);
            font-size: 30px;
        }

        .prediction-eyebrow {
            margin-top: 0.9rem;
            color: #67e8f9;
            font-size: 0.72rem;
            font-weight: 850;
            letter-spacing: 0.18em;
            text-transform: uppercase;
        }

        .prediction-title {
            margin-top: 0.25rem;
            color: #e2e8f0;
            font-size: 1.05rem;
            font-weight: 700;
        }

        .prediction-value {
            margin-top: 0.35rem;
            color: #ffffff;
            font-size: clamp(2.6rem, 6vw, 4.7rem);
            font-weight: 900;
            line-height: 1;
            letter-spacing: -0.06em;
            text-shadow: 0 0 30px rgba(96,165,250,0.14);
        }

        .prediction-subtitle {
            margin-top: 0.75rem;
            color: #94a3b8;
            font-size: 0.85rem;
        }

        .prediction-description {
            max-width: 720px;
            margin: 1rem auto 0 auto;
            color: #94a3b8;
            font-size: 0.88rem;
            line-height: 1.55;
        }

        .success-badge {
            display: inline-flex;
            align-items: center;
            margin-top: 1rem;
            padding: 0.42rem 0.75rem;
            border: 1px solid rgba(74,222,128,0.18);
            border-radius: 999px;
            background: rgba(34,197,94,0.06);
            color: #86efac;
            font-size: 0.68rem;
            font-weight: 800;
        }

        /* ---------- METRICS ---------- */
        div[data-testid="stMetric"] {
            min-height: 112px;
            padding: 1rem 1.05rem !important;
            border: 1px solid rgba(148,163,184,0.13) !important;
            border-radius: 16px !important;
            background: linear-gradient(145deg, rgba(10,22,38,0.84), rgba(9,16,31,0.76)) !important;
            box-shadow: 0 14px 34px rgba(0,0,0,0.18);
        }

        div[data-testid="stMetricLabel"] p {
            color: #7f8ea7 !important;
            font-weight: 700 !important;
        }

        div[data-testid="stMetricValue"] {
            color: #f8fafc !important;
            font-weight: 850 !important;
        }

        /* ---------- FOOTER ---------- */
        .footer {
            margin-top: 1.8rem;
            padding: 1.15rem 0 0.4rem 0;
            border-top: 1px solid rgba(148,163,184,0.08);
            text-align: center;
            color: #53627a;
            font-size: 0.72rem;
            line-height: 1.6;
        }

        .footer strong {
            color: #94a3b8;
        }

        /* ---------- RESPONSIVE ---------- */
        @media (max-width: 900px) {
            .block-container {
                padding-left: 1rem;
                padding-right: 1rem;
            }

            .hero-shell {
                padding: 1.5rem;
            }

            .hero-meta {
                grid-template-columns: 1fr;
            }
        }
    </style>
    """
)


# =========================================================
# LOAD MODEL AND PREPROCESSORS — UNCHANGED
# =========================================================

@st.cache_resource
def load_resources():
    model = keras.models.load_model("salary_model.keras")

    with open("salary_gender_encoder.pkl", "rb") as f:
        gender_encoder = pickle.load(f)

    with open("salary_geography_encoder.pkl", "rb") as f:
        geography_encoder = pickle.load(f)

    with open("salary_scaler.pkl", "rb") as f:
        scaler = pickle.load(f)

    return model, gender_encoder, geography_encoder, scaler


model, gender_encoder, geography_encoder, scaler = load_resources()


# =========================================================
# ENCODE FUNCTION — UNCHANGED
# =========================================================

def encode_features(df):
    df = df.copy()

    df["Gender"] = gender_encoder.transform(
        df[["Gender"]]
    ).ravel()

    geo_array = geography_encoder.transform(
        df[["Geography"]]
    )

    geo_columns = geography_encoder.get_feature_names_out(
        ["Geography"]
    )

    geo_df = pd.DataFrame(
        geo_array,
        columns=geo_columns,
        index=df.index,
    )

    df = pd.concat(
        [
            df.drop(columns=["Geography"]),
            geo_df,
        ],
        axis=1,
    )

    return df


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:
    render_html(
        """
        <div class="side-brand">
            <div class="side-brand-title">🤖 Model Dashboard</div>
            <div class="side-brand-copy">AI Salary Prediction • Professional inference workspace</div>
        </div>
        """
    )

    render_html(
        """
        <div class="side-card">
            <div class="side-card-title">◉ Model</div>
            <div class="side-row"><span>Type</span><strong>ANN Regression</strong></div>
            <div class="side-row"><span>Status</span><strong><span class="status-dot"></span>Ready</strong></div>
            <div class="side-row"><span>Framework</span><strong>TensorFlow / Keras</strong></div>
        </div>
        """
    )

    render_html(
        """
        <div class="side-card">
            <div class="side-card-title">🧠 Architecture</div>
            <div class="side-row"><span>Layer 1</span><strong>Dense 64 → ReLU</strong></div>
            <div class="side-row"><span>Layer 2</span><strong>Dense 32 → ReLU</strong></div>
            <div class="side-row"><span>Output</span><strong>Dense 1 → Linear</strong></div>
        </div>
        """
    )

    render_html(
        """
        <div class="side-card">
            <div class="side-card-title">📊 Project</div>
            <div class="side-row"><span>Task</span><strong>Regression</strong></div>
            <div class="side-row"><span>Target</span><strong>EstimatedSalary</strong></div>
            <div class="side-row"><span>Metrics</span><strong>MAE • RMSE • R²</strong></div>
        </div>
        """
    )

    render_html(
        """
        <div class="side-note">
            Prediction interface powered by the existing trained model and preprocessing pipeline.
            UI-only redesign; model behavior remains unchanged.
        </div>
        """
    )


# =========================================================
# HERO / HEADER
# =========================================================

render_html(
    """
    <div class="hero-shell">
        <div class="hero-badges">
            <span class="hero-badge">Artificial Neural Network</span>
            <span class="hero-badge purple">Regression</span>
            <span class="hero-badge green">Live Inference</span>
        </div>

        <div class="hero-title">🧠 <span class="hero-gradient">Salary Intelligence</span></div>

        <div class="hero-subtitle">
            ⚡ ANN-Powered Salary Estimation &amp; Analytics Platform
        </div>

        <div class="hero-meta">
            <div class="hero-meta-item">
                <div class="hero-meta-label">Framework</div>
                <div class="hero-meta-value">TensorFlow / Keras</div>
            </div>
            <div class="hero-meta-item">
                <div class="hero-meta-label">Interface</div>
                <div class="hero-meta-value">Streamlit Dashboard</div>
            </div>
            <div class="hero-meta-item">
                <div class="hero-meta-label">Target</div>
                <div class="hero-meta-value">EstimatedSalary</div>
            </div>
        </div>
    </div>
    """
)


# =========================================================
# INPUT SECTION
# =========================================================

render_html(
    """
    <div class="section-kicker">Customer Profile</div>
    <div class="section-heading">Enter prediction inputs</div>
    <div class="section-copy">
        Provide the same customer features used by the trained ANN model. The selected values are passed through the existing encoder and scaler.
    </div>
    """
)

input_col1, input_col2, input_col3 = st.columns(3, gap="large")

with input_col1:
    with st.container(border=True):
        render_html(
            """
            <div style="font-weight:800;color:#e2e8f0;font-size:0.98rem;">💳 Financial Profile</div>
            <div style="color:#64748b;font-size:0.70rem;margin-top:0.2rem;margin-bottom:0.8rem;">Credit standing and account balance information.</div>
            """
        )

        credit_score = st.slider(
            "Credit Score",
            300,
            900,
            650,
            1,
            help="Customer credit score used by the existing model.",
        )

        balance = st.number_input(
            "Balance",
            min_value=0.0,
            max_value=300000.0,
            value=75000.0,
            step=1000.0,
            format="%.2f",
            help="Customer account balance.",
        )

with input_col2:
    with st.container(border=True):
        render_html(
            """
            <div style="font-weight:800;color:#e2e8f0;font-size:0.98rem;">🌍 Customer Profile</div>
            <div style="color:#64748b;font-size:0.70rem;margin-top:0.2rem;margin-bottom:0.8rem;">Demographic and location-related inputs.</div>
            """
        )

        geography = st.selectbox(
            "Geography",
            ["France", "Spain", "Germany"],
            help="Customer geography passed to the existing geography encoder.",
        )

        gender = st.radio(
            "Gender",
            ["Male", "Female"],
            horizontal=True,
            help="Customer gender passed to the existing gender encoder.",
        )

        age = st.slider(
            "Age",
            18,
            100,
            35,
            1,
            help="Customer age.",
        )

with input_col3:
    with st.container(border=True):
        render_html(
            """
            <div style="font-weight:800;color:#e2e8f0;font-size:0.98rem;">📦 Relationship & Activity</div>
            <div style="color:#64748b;font-size:0.70rem;margin-top:0.2rem;margin-bottom:0.8rem;">Tenure, product usage, card ownership and activity.</div>
            """
        )

        tenure = st.slider(
            "Tenure",
            0,
            10,
            5,
            1,
            help="Customer tenure value used by the model.",
        )

        num_products = st.selectbox(
            "Number of Products",
            [1, 2, 3, 4],
            index=1,
            help="Number of products associated with the customer.",
        )

        has_card = st.toggle(
            "Has Credit Card",
            value=True,
            help="Whether the customer has a credit card.",
        )

        active_member = st.toggle(
            "Active Member",
            value=True,
            help="Whether the customer is an active member.",
        )


# =========================================================
# INPUT SUMMARY
# =========================================================

st.write("")
render_html(
    """
    <div class="section-kicker">Input Summary</div>
    <div class="section-heading">Customer Profile Preview</div>
    <div class="section-copy">Review the exact values that will be submitted to the prediction pipeline.</div>
    """
)

with st.container(border=True):
    summary_rows = [
        ("💳", "Credit Score", f"{credit_score}"),
        ("🌍", "Geography", geography),
        ("⚥", "Gender", gender),
        ("🎂", "Age", f"{age} years"),
        ("📅", "Tenure", f"{tenure} years"),
        ("💵", "Balance", f"PKR {balance:,.2f}"),
        ("📦", "Products", f"{num_products}"),
        ("💳", "Credit Card", "Yes" if has_card else "No"),
        ("🟢", "Active Member", "Yes" if active_member else "No"),
    ]

    for row_start in range(0, len(summary_rows), 3):
        row_cols = st.columns(3, gap="small")
        for col, (icon, label, value) in zip(row_cols, summary_rows[row_start:row_start + 3]):
            with col:
                render_html(
                    f"""
                    <div class=\"profile-tile\">
                        <div class=\"profile-label\"><span class=\"profile-icon\">{icon}</span>{label}</div>
                        <div class=\"profile-value\">{value}</div>
                    </div>
                    """
                )
        if row_start + 3 < len(summary_rows):
            st.write("")


# =========================================================
# PREDICTION CTA
# =========================================================

st.write("")

predict_button = st.button(
    "🚀  Predict Estimated Salary",
    use_container_width=True,
)


# =========================================================
# PREDICTION — CALCULATION UNCHANGED
# =========================================================

if predict_button:
    # Convert boolean values to integers — unchanged
    has_card_value = int(has_card)
    active_member_value = int(active_member)

    # Create input dataframe — same feature names and order
    input_data = pd.DataFrame({
        "CreditScore": [credit_score],
        "Geography": [geography],
        "Gender": [gender],
        "Age": [age],
        "Tenure": [tenure],
        "Balance": [balance],
        "NumOfProducts": [num_products],
        "HasCrCard": [has_card_value],
        "IsActiveMember": [active_member_value],
    })

    # Encode — unchanged
    input_encoded = encode_features(input_data)

    # Scale — unchanged
    input_scaled = scaler.transform(input_encoded)

    # Prediction — unchanged
    prediction = model.predict(
        input_scaled,
        verbose=0,
    )[0][0]

    # Prevent negative salary — unchanged
    prediction = max(0, prediction)

    # =====================================================
    # PREMIUM RESULT CARD
    # =====================================================

    render_html(
        f"""
        <div class=\"prediction-shell\">
            <div class=\"prediction-icon\">💰</div>
            <div class=\"prediction-eyebrow\">Estimated Annual Salary</div>
            <div class=\"prediction-title\">AI Salary Estimate</div>
            <div class=\"prediction-value\">PKR {prediction:,.2f}</div>
            <div class=\"prediction-subtitle\">ANN Regression Prediction</div>
            <div class=\"prediction-description\">
                Based on the customer profile you entered, the trained ANN model estimates the annual salary at approximately <strong style=\"color:#e2e8f0;\">PKR {prediction:,.2f}</strong>.
            </div>
            <div class=\"success-badge\">✓ Prediction Generated Successfully</div>
        </div>
        """
    )

    # =====================================================
    # PREDICTION DETAILS
    # =====================================================

    st.write("")
    render_html(
        """
        <div class="section-kicker">Prediction Details</div>
        <div class="section-heading">Profile snapshot</div>
        <div class="section-copy">Key values associated with this prediction.</div>
        """
    )

    metric1, metric2, metric3 = st.columns(3, gap="large")

    with metric1:
        st.metric("💳 Credit Score", credit_score)

    with metric2:
        st.metric("🎂 Age", f"{age} years")

    with metric3:
        st.metric("📦 Products", num_products)


# =========================================================
# FOOTER
# =========================================================

render_html(
    """
    <div class="footer">
        <strong>🧠 Salary Intelligence</strong> · Built with Python, TensorFlow / Keras and Streamlit<br>
        Artificial Neural Network · Regression · AI Salary Estimation Platform
    </div>
    """
)
