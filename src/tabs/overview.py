import streamlit as st
from src.calculations.nofunding_total import get_unfunded_famine_countries

def render():
    st.markdown('<p class="section-title">Global Snapshot</p>', unsafe_allow_html=True)

    no_funding, unfunded_count = get_unfunded_famine_countries()

    years = list(range(2012,2023))
    selected_year = st.selectbox("Filter by Year", options=["All Years"] + list(years))

    filtered = no_funding if selected_year == "All Years" else no_funding[no_funding['year'] == selected_year]
    unfunded_count_filtered = filtered['entity'].nunique()

    st.metric(label="Countries at Famine Risk with No Funding", value=unfunded_count_filtered)