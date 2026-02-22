import streamlit as st
import plotly.graph_objects as go

def render_roc():
    fpr = [0.00, 0.00, 0.08, 0.08, 0.38, 0.38, 0.40, 0.40, 1.00]
    tpr = [0.00, 0.18, 0.18, 0.38, 0.38, 0.80, 0.80, 1.00, 1.00]

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=fpr, y=tpr,
        mode="lines",
        fill="tozeroy",
        fillcolor="rgba(91,146,229,0.18)",
        line=dict(color="#5B92E5", width=2.5),
        name="ROC Curve",
        hovertemplate="FPR: %{x:.2f}<br>TPR: %{y:.2f}<extra></extra>",
    ))
    fig.add_trace(go.Scatter(
        x=[0, 1], y=[0, 1],
        mode="lines",
        line=dict(color="#94a3b8", width=1.5, dash="dash"),
        name="Random Classifier",
        hoverinfo="skip",
    ))
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=60, r=20, t=20, b=60),
        height=340,
        xaxis=dict(
            title=dict(text="False Positive Rate", font=dict(color="#94a3b8", size=13)),
            range=[0, 1], tickvals=[0, 0.2, 0.4, 0.6, 0.8, 1.0],
            tickfont=dict(color="#64748b", size=11),
            gridcolor="rgba(255,255,255,0.05)", zeroline=False,
        ),
        yaxis=dict(
            title=dict(text="True Positive Rate", font=dict(color="#94a3b8", size=13)),
            range=[0, 1], tickvals=[0, 0.2, 0.4, 0.6, 0.8, 1.0],
            tickfont=dict(color="#64748b", size=11),
            gridcolor="rgba(255,255,255,0.05)", zeroline=False,
        ),
        legend=dict(
            orientation="h", yanchor="bottom", y=1.04, xanchor="left", x=0,
            font=dict(color="#94a3b8", size=12), bgcolor="rgba(0,0,0,0)",
        ),
    )

    st.markdown('<p class="section-title">Model Performance</p>', unsafe_allow_html=True)
    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("AUC Score", "0.71")
    with col2:
        st.metric("Max TPR", "1.00")
    with col3:
        st.metric("Lift", "+42%")

def render():
    col_left, col_center, col_right = st.columns([1, 2, 1])
    with col_center:
        render_roc()