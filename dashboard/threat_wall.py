import streamlit as st
import sqlite3
import pandas as pd


def threat_wall():

    st.title(
        "🚨 National Threat Wall"
    )

    conn = sqlite3.connect(
        "database/cybercrime.db"
    )

    df = pd.read_sql(
        """
        SELECT
            source,
            title,
            threat_score,
            sentiment
        FROM intelligence_data
        ORDER BY threat_score DESC
        LIMIT 50
        """,
        conn
    )

    conn.close()

    critical = len(
        df[df["threat_score"] >= 80]
    )

    high = len(
        df[
            (df["threat_score"] >= 50)
            &
            (df["threat_score"] < 80)
        ]
    )

    medium = len(
        df[
            (df["threat_score"] >= 20)
            &
            (df["threat_score"] < 50)
        ]
    )

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Critical Threats",
        critical
    )

    c2.metric(
        "High Threats",
        high
    )

    c3.metric(
        "Medium Threats",
        medium
    )

    st.markdown("---")

    st.dataframe(
        df,
        width="stretch"
    )