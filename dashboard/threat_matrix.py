import streamlit as st
import sqlite3
import pandas as pd


def threat_matrix():

    conn = sqlite3.connect(
        "database/complaints.db"
    )

    df = pd.read_sql(
        "SELECT risk_score FROM complaints",
        conn
    )

    conn.close()

    critical = len(
        df[df["risk_score"] >= 80]
    )

    high = len(
        df[
            (df["risk_score"] >= 60)
            &
            (df["risk_score"] < 80)
        ]
    )

    medium = len(
        df[
            (df["risk_score"] >= 40)
            &
            (df["risk_score"] < 60)
        ]
    )

    low = len(
        df[df["risk_score"] < 40]
    )

    st.subheader(
        "Threat Matrix"
    )

    st.progress(
        min(critical / 20, 1.0)
    )

    st.write(
        f"🔴 Critical : {critical}"
    )

    st.progress(
        min(high / 30, 1.0)
    )

    st.write(
        f"🟠 High : {high}"
    )

    st.progress(
        min(medium / 50, 1.0)
    )

    st.write(
        f"🟡 Medium : {medium}"
    )

    st.progress(
        min(low / 100, 1.0)
    )

    st.write(
        f"🟢 Low : {low}"
    )