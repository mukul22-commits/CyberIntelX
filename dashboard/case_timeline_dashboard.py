import streamlit as st
import sqlite3
import pandas as pd


def case_timeline_dashboard():

    st.title("📜 Case Timeline")

    case_id = st.number_input(
        "Complaint ID",
        min_value=1
    )

    if st.button("Load Timeline"):

        conn = sqlite3.connect(
            "database/timeline.db"
        )

        df = pd.read_sql(
            """
            SELECT
                action,
                username,
                timestamp
            FROM timeline
            WHERE complaint_id=?
            ORDER BY id
            """,
            conn,
            params=(case_id,)
        )

        conn.close()

        if len(df) == 0:

            st.warning(
                "No timeline found"
            )

        else:

            st.dataframe(
                df,
                width="stretch"
            )