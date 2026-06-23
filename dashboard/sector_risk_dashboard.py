import streamlit as st
import plotly.express as px

from processing.sector_risk_engine import (
    calculate_sector_risk
)


def sector_risk_dashboard():

    st.title(
        "🏦 Sector Risk Center"
    )

    df = calculate_sector_risk()

    if df.empty:

        st.warning(
            "No complaint data available."
        )

        return

    st.dataframe(
        df,
        width="stretch"
    )

    fig = px.bar(
        df,
        x="sector",
        y="average_risk",
        title="Sector Risk Analysis"
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )