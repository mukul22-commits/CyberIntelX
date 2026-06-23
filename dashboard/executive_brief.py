import streamlit as st
import sqlite3
import pandas as pd


def executive_brief():

    conn = sqlite3.connect(
        "database/complaints.db"
    )

    df = pd.read_sql(
        "SELECT * FROM complaints",
        conn
    )

    conn.close()

    total = len(df)

    critical = len(
        df[df["risk_score"] >= 80]
    )

    pending = len(
        df[df["status"] == "Pending"]
    )

    resolved = len(
        df[df["status"] == "Resolved"]
    )

    st.subheader(
        "🧠 Executive Intelligence Brief"
    )

    st.info(
        f"""
Total Cases: {total}

Critical Cases: {critical}

Pending Cases: {pending}

Resolved Cases: {resolved}

National Cyber Threat Status:
{'CRITICAL' if critical > 10 else 'ELEVATED'}
"""
    )