import streamlit as st

from processing.threat_score_v2 import (
    calculate_threat_scores
)


def threat_score_dashboard():

    st.title(
        "🎯 Threat Score Center"
    )

    df = calculate_threat_scores()

    if df.empty:

        st.warning(
            "No threat data available."
        )

        return

    critical = len(
        df[
            df["risk"] == "Critical"
        ]
    )

    high = len(
        df[
            df["risk"] == "High"
        ]
    )

    c1, c2 = st.columns(2)

    c1.metric(
        "Critical Threats",
        critical
    )

    c2.metric(
        "High Threats",
        high
    )

    st.dataframe(
        df,
        width="stretch"
    )