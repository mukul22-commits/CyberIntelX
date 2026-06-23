import streamlit as st
import pandas as pd
import sqlite3


def timeline_dashboard():

    st.title(
        "📅 Investigation Timeline"
    )

    conn = sqlite3.connect(
        "database/complaints.db"
    )

    complaints = pd.read_sql(
        """
        SELECT
        id,
        name,
        created_at,
        status
        FROM complaints
        """,
        conn
    )

    conn.close()

    st.dataframe(
        complaints,
        width="stretch"
    )