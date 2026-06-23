import streamlit as st
import pandas as pd
import sqlite3


def alert_center():

    st.title("🚨 Alert Center")

    conn = sqlite3.connect(
        "database/complaints.db"
    )

    complaints = pd.read_sql(
        "SELECT * FROM complaints",
        conn
    )

    conn.close()

    critical = complaints[
        complaints["priority"] == "Critical"
    ]

    high_risk = complaints[
        complaints["risk_score"] >= 80
    ]

    st.metric(
        "Critical Cases",
        len(critical)
    )

    st.metric(
        "High Risk Cases",
        len(high_risk)
    )

    st.markdown("---")

    st.subheader(
        "Critical Alerts"
    )

    if len(critical) == 0:

        st.success(
            "No critical alerts"
        )

    else:

        st.dataframe(
            critical[
                [
                    "id",
                    "name",
                    "category",
                    "risk_score",
                    "priority",
                    "status"
                ]
            ],
            width="stretch"
        )