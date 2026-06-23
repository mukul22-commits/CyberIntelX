import streamlit as st

from processing.active_incidents import (
    get_active_incidents
)


def active_incident_center():

    st.title(
        "🚨 Active Incident Center"
    )

    df = get_active_incidents()

    if df.empty:

        st.warning(
            "No incident data found."
        )

        return

    critical = len(
        df[
            df["severity"] == "Critical"
        ]
    )

    high = len(
        df[
            df["severity"] == "High"
        ]
    )

    medium = len(
        df[
            df["severity"] == "Medium"
        ]
    )

    c1, c2, c3 = st.columns(3)

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

    st.markdown("---")

    st.subheader(
        "Active Incidents"
    )

    st.dataframe(
        df,
        width="stretch"
    )