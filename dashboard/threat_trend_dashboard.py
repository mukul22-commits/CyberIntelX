import streamlit as st
import plotly.express as px

from processing.threat_trend_engine import (
    build_trend
)


def threat_trend_dashboard():

    st.title(
        "📈 Threat Trend Center"
    )

    df = build_trend()

    if df.empty:

        st.warning(
            "No threat intelligence data found."
        )

        return

    st.metric(
        "Total Sources",
        len(df)
    )

    st.dataframe(
        df,
        width="stretch"
    )

    fig = px.bar(
        df,
        x="source",
        y="count",
        title="Threat Feed Distribution"
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )