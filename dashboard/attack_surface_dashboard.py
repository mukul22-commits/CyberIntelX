import streamlit as st
import plotly.express as px

from processing.attack_surface_engine import (
    analyze_attack_surface
)


def attack_surface_dashboard():

    st.title(
        "⚔️ Attack Surface Center"
    )

    df = analyze_attack_surface()

    if df.empty:

        st.warning(
            "No attack surface data available."
        )

        return

    st.dataframe(
        df,
        width="stretch"
    )

    fig = px.bar(
        df,
        x="category",
        y="exposure_score",
        title="Attack Surface Exposure"
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )