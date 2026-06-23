import streamlit as st
import pandas as pd
import sqlite3


def notification_center():

    st.subheader(
        "🔔 Notification Center"
    )

    try:

        conn = sqlite3.connect(
            "database/complaints.db"
        )

        complaints = pd.read_sql(
            "SELECT * FROM complaints",
            conn
        )

        conn.close()

        critical = complaints[
            complaints["risk_score"] >= 90
        ]

        if len(critical) > 0:

            st.error(
                f"🔴 {len(critical)} Critical Complaint(s) Need Immediate Attention"
            )

        pending = complaints[
            complaints["status"] == "Pending"
        ]

        if len(pending) > 0:

            st.warning(
                f"🟡 {len(pending)} Complaint(s) Awaiting Investigation"
            )

        resolved = complaints[
            complaints["status"] == "Resolved"
        ]

        if len(resolved) > 0:

            st.success(
                f"🟢 {len(resolved)} Complaint(s) Resolved"
            )

    except Exception as e:

        st.error(
            f"Notification Error: {e}"
        )