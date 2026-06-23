import streamlit as st
import plotly.express as px

from processing.threat_forecast_engine import (
    forecast_threats
)


def threat_forecast_dashboard():

    st.title(
        "🔮 Threat Forecast Center"
    )

    df = forecast_threats()

    if df.empty:

        st.warning(
            "No threat data available."
        )

        return

    st.dataframe(
        df,
        width="stretch"
    )

    fig = px.bar(
        df,
        x="source",
        y="forecast_next_week",
        title="Forecasted Threat Volume"
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )