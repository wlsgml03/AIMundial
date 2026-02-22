import streamlit as st
from src.styles import load_css
from src.tabs import overview
from src.tabs import model_performance

st.set_page_config(
    page_title="AIMundial",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

load_css()

# --- Hero Header ---
st.markdown("""
<div class="hero">
    <h1>🌍 AIM<span>Mundial</span></h1>
    <p>AI-powered famine risk detection & aid allocation analysis</p>
</div>
""", unsafe_allow_html=True)

# --- Tabs ---
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊  Overview",
    "📈 Model Performance",
    "🗺️  Funding Gap",
    "📉  Aid Utilization",
    "🔍  Root Causes"
])
with tab1:
    overview.render()
with tab2:
    model_performance.render()