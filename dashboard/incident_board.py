import streamlit as st
import sqlite3
import pandas as pd


def incident_board():

    conn = sqlite3.connect(
        "database/complaints.db"
    )

    df = pd.read_sql(
        """
        SELECT *
        FROM complaints
        ORDER BY risk_score DESC
        LIMIT 15
        """,
        conn
    )

    conn.close()

    st.subheader(
        "🚨 Active Incident Board"
    )

    st.dataframe(
        df,
        width="stretch"
    )