import streamlit as st
import sqlite3
import pandas as pd


def assigned_cases():

    st.subheader(
        "Assigned Cases"
    )

    username = st.session_state.get(
        "username"
    )

    officer_name = username.split("_")[0]

    conn = sqlite3.connect(
        "database/complaints.db"
    )

    df = pd.read_sql(
        """
        SELECT
            id,
            victim_username,
            category,
            risk_score,
            priority,
            status,
            created_at
        FROM complaints
        WHERE lower(officer_name)
        LIKE ?
        ORDER BY risk_score DESC
        """,
        conn,
        params=(
            f"%{officer_name.lower()}%",
        )
    )

    conn.close()

    if len(df) == 0:

        st.info(
            "No assigned cases."
        )

    else:

        st.dataframe(
            df,
            width="stretch"
        )