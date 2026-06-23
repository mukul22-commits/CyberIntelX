import streamlit as st
import sqlite3
import pandas as pd


def live_threat_feed():

    st.subheader(
        "🌍 Live Threat Intelligence Feed"
    )

    try:

        conn = sqlite3.connect(
            "database/cybercrime.db"
        )

        df = pd.read_sql(
            """
            SELECT
                source,
                title,
                threat_score
            FROM intelligence_data
            ORDER BY rowid DESC
            LIMIT 10
            """,
            conn
        )

        conn.close()

        st.dataframe(
            df,
            width="stretch"
        )

    except Exception:

        st.warning(
            "No intelligence feed available."
        )