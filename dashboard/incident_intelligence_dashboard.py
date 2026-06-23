import streamlit as st

from processing.incident_intelligence import (
    build_incident_intelligence
)


def incident_intelligence_dashboard():

    st.title(
        "🧠 Incident Intelligence Center"
    )

    df = build_incident_intelligence()

    if df.empty:

        st.warning(
            "No incidents found."
        )

        return

    critical = len(
        df[
            df["priority"] == "Critical"
        ]
    )

    high = len(
        df[
            df["priority"] == "High"
        ]
    )

    medium = len(
        df[
            df["priority"] == "Medium"
        ]
    )

    low = len(
        df[
            df["priority"] == "Low"
        ]
    )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Critical",
        critical
    )

    c2.metric(
        "High",
        high
    )

    c3.metric(
        "Medium",
        medium
    )

    c4.metric(
        "Low",
        low
    )

    st.markdown("---")

    st.dataframe(
        df,
        width="stretch"
    )