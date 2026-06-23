import streamlit as st
import sqlite3
import pandas as pd

from processing.national_threat_score import (
    calculate_national_threat
)

from processing.alert_engine import (
    generate_alerts
)


def cyber_fusion_center():

    st.title(
        "🛡 Cyber Fusion Center"
    )

    threat = calculate_national_threat()

    c1, c2 = st.columns(2)

    c1.metric(
        "National Threat Score",
        threat["score"]
    )

    c2.metric(
        "Threat Level",
        threat["level"]
    )

    st.markdown("---")

    # Alerts

    st.subheader(
        "🚨 Active Alerts"
    )

    alerts = generate_alerts()

    if not alerts.empty:

        st.dataframe(
            alerts.head(10),
            width="stretch"
        )

    else:

        st.success(
            "No active alerts"
        )

    st.markdown("---")

    # Latest Intelligence

    st.subheader(
        "🌍 Latest Threat Intelligence"
    )

    conn = sqlite3.connect(
        "database/cybercrime.db"
    )

    intel = pd.read_sql(
        """
        SELECT source,title
        FROM intelligence_data
        ORDER BY rowid DESC
        LIMIT 10
        """,
        conn
    )

    conn.close()

    st.dataframe(
        intel,
        width="stretch"
    )

    st.markdown("---")

    # Complaints

    st.subheader(
        "📂 Recent Complaints"
    )

    conn = sqlite3.connect(
        "database/complaints.db"
    )

    complaints = pd.read_sql(
        """
        SELECT id,
               category,
               risk_score,
               status
        FROM complaints
        ORDER BY id DESC
        LIMIT 10
        """,
        conn
    )

    conn.close()

    st.dataframe(
        complaints,
        width="stretch"
    )