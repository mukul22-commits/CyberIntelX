import streamlit as st
import pandas as pd
import sqlite3


def officer_assignment_dashboard():

    st.title(
        "👮 Officer Assignment Center"
    )

    conn = sqlite3.connect(
        "database/complaints.db"
    )

    complaints = pd.read_sql(
        """
        SELECT
            id,
            name,
            category,
            risk_score,
            officer_name
        FROM complaints
        ORDER BY risk_score DESC
        """,
        conn
    )

    st.dataframe(
        complaints,
        width="stretch"
    )

    conn.close()