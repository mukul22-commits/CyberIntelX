import streamlit as st
import pandas as pd
import sqlite3


def victim_dashboard():

    st.title("👤 Victim Dashboard")

    username = st.session_state.get(
        "username"
    )

    conn = sqlite3.connect(
        "database/complaints.db"
    )

    complaints = pd.read_sql(
        """
        SELECT
            id,
            category,
            risk_score,
            status,
            officer_name,
            priority,
            created_at
        FROM complaints
        WHERE victim_username=?
        ORDER BY id DESC
        """,
        conn,
        params=(username,)
    )

    conn.close()

    if len(complaints) == 0:

        st.warning(
            "No complaints submitted yet"
        )

        return

    st.subheader(
        "My Complaints"
    )

    st.dataframe(
        complaints,
        width="stretch"
    )

    st.markdown("---")

    complaint_id = st.selectbox(
        "View Complaint",
        complaints["id"]
    )

    selected = complaints[
        complaints["id"] == complaint_id
    ].iloc[0]

    st.info(
        f"""
Case ID: {selected['id']}

Status: {selected['status']}

Assigned Officer: {selected['officer_name']}

Priority: {selected['priority']}

Risk Score: {selected['risk_score']}
"""
    )