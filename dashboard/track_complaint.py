import streamlit as st
import pandas as pd
import sqlite3


def track_complaint():

    st.title(
        "📋 My Complaints"
    )

    username = st.session_state.get(
        "username",
        ""
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
            "No complaints found"
        )

        return

    st.dataframe(
        complaints,
        width="stretch"
    )

    st.markdown("---")

    complaint_id = st.selectbox(
        "View Complaint Details",
        complaints["id"]
    )

    conn = sqlite3.connect(
        "database/complaints.db"
    )

    details = pd.read_sql(
        """
        SELECT *
        FROM complaints
        WHERE id=?
        """,
        conn,
        params=(complaint_id,)
    )

    conn.close()

    st.subheader(
        f"Case #{complaint_id}"
    )

    st.write(
        "Status:",
        details.iloc[0]["status"]
    )

    st.write(
        "Assigned Officer:",
        details.iloc[0]["officer_name"]
    )

    st.write(
        "Investigation Notes:"
    )

    st.info(
        str(
            details.iloc[0][
                "investigation_notes"
            ]
        )
    )