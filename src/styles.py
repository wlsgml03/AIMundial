import streamlit as st

def load_css():
    st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        .stApp {
            background-color: #B9D0F3;
            color: #5B92E5;
        }

        /* Hero section with its own darker color at the top */
        .hero {
            background-color: #5B92E5;
            padding: 2.5rem 0 1.5rem 0;
            text-align: center;
            margin: -3rem -3rem 2rem -3rem;
        }
        .hero h1 {
            font-size: 3rem;
            font-weight: 800;
            letter-spacing: -1px;
            color: #ffffff;
            margin-bottom: 0.25rem;
        }
        .hero p {
            font-size: 1.1rem;
            color: #e0f0ff;
            margin-top: 0;
        }
        .hero span {
            color: #ffffff;
            font-style: italic;
        }
        .hero img {
            width: 60px;
            margin-bottom: 0.5rem;
        }

        .stTabs [data-baseweb="tab-list"] {
            gap: 0px;
            background-color: #0f1117;
            border-radius: 12px;
            padding: 6px;
            justify-content: center;
            border: 1px solid #2a2d3a;
        }
        .stTabs [data-baseweb="tab"] {
            height: 42px;
            padding: 0 28px;
            background-color: transparent;
            border-radius: 8px;
            color: #8b9ab0;
            font-weight: 500;
            font-size: 0.95rem;
            border: none;
        }
        .stTabs [aria-selected="true"] {
            background-color: #009edb !important;
            color: #ffffff !important;
        }
        .stTabs [data-baseweb="tab-highlight"] { display: none; }
        .stTabs [data-baseweb="tab-border"] { display: none; }

        [data-testid="metric-container"] {
            background-color: #0f1117;
            border: 1px solid #2a2d3a;
            border-radius: 12px;
            padding: 1rem 1.5rem;
        }
        [data-testid="stMetricLabel"] {
            color: #8b9ab0 !important;
            font-size: 0.85rem;
        }
        [data-testid="stMetricValue"] {
            color: #ffffff !important;
            font-size: 2rem !important;
            font-weight: 700 !important;
        }
        [data-testid="stMetricDelta"] {
            font-size: 0.85rem !important;
        }

        .section-title {
            font-size: 1.4rem;
            font-weight: 700;
            color: #ffffff;
            margin: 1.5rem 0 0.75rem 0;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid #009edb;
            display: inline-block;
        }

        .info-box {
            background-color: #0f1117;
            border: 1px solid #2a2d3a;
            border-left: 4px solid #009edb;
            border-radius: 8px;
            padding: 1rem 1.25rem;
            margin: 0.75rem 0;
            color: #c8d0e0;
            font-size: 0.95rem;
            line-height: 1.6;
        }

        hr {
            border: none;
            border-top: 1px solid #2a2d3a;
            margin: 1.5rem 0;
        }
    </style>
    """, unsafe_allow_html=True)