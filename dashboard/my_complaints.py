import streamlit as st
import sqlite3
import pandas as pd


def my_complaints():

    st.subheader(
        "My Complaints"
    )

    username = st.session_state.get(
        "username"
    )

    conn = sqlite3.connect(
        "database/complaints.db"
    )

    df = pd.read_sql(
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

    if len(df) == 0:

        st.info(
            "No complaints found."
        )

    else:

        st.dataframe(
            df,
            width="stretch"
        )