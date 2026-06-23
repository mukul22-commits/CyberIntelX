import streamlit as st

from processing.alert_engine import (
    generate_alerts
)


def alert_engine_dashboard():

    st.title(
        "🚨 Alert Center"
    )

    alerts = generate_alerts()

    if alerts.empty:

        st.success(
            "No active alerts."
        )

        return

    st.metric(
        "Active Alerts",
        len(alerts)
    )

    st.dataframe(
        alerts,
        width="stretch"
    )

    critical = alerts[
        alerts["severity"] == "Critical"
    ]

    if not critical.empty:

        st.error(
            f"{len(critical)} Critical Alerts"
        )