import streamlit as st
import sqlite3
import pandas as pd


def case_command_center():

    st.title("🎯 Case Command Center")

    conn = sqlite3.connect(
        "database/complaints.db"
    )

    df = pd.read_sql(
        "SELECT * FROM complaints",
        conn
    )

    conn.close()

    total_cases = len(df)

    critical_cases = len(
        df[df["risk_score"] >= 80]
    )

    pending_cases = len(
        df[df["status"] == "Pending"]
    )

    resolved_cases = len(
        df[df["status"] == "Resolved"]
    )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Total Cases",
        total_cases
    )

    c2.metric(
        "Critical Cases",
        critical_cases
    )

    c3.metric(
        "Pending",
        pending_cases
    )

    c4.metric(
        "Resolved",
        resolved_cases
    )

    st.markdown("---")

    st.subheader(
        "Highest Risk Cases"
    )

    high_risk = df.sort_values(
        by="risk_score",
        ascending=False
    )

    st.dataframe(
        high_risk.head(20),
        width="stretch"
    )