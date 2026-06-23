import streamlit as st
import pandas as pd
import sqlite3


def officer_kpi_dashboard():

    st.title(
        "📊 Officer KPI Dashboard"
    )

    conn = sqlite3.connect(
        "database/complaints.db"
    )

    df = pd.read_sql(
        """
        SELECT *
        FROM complaints
        """,
        conn
    )

    conn.close()

    total = len(df)

    resolved = len(
        df[
            df["status"] == "Resolved"
        ]
    )

    closed = len(
        df[
            df["status"] == "Closed"
        ]
    )

    active = total - resolved - closed

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Total Cases",
        total
    )

    c2.metric(
        "Active Cases",
        active
    )

    c3.metric(
        "Resolved",
        resolved
    )

    c4.metric(
        "Closed",
        closed
    )