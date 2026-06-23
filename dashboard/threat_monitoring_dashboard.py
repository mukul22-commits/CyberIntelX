import streamlit as st
import sqlite3
import pandas as pd


def threat_monitoring_dashboard():

    st.title(
        "🌍 National Cyber Threat Monitoring Center"
    )

    conn = sqlite3.connect(
        "database/threat_monitoring.db"
    )

    try:

        df = pd.read_sql(
            "SELECT * FROM threat_feed",
            conn
        )

    except:

        st.warning(
            "No threat feed collected yet."
        )

        return

    conn.close()

    st.metric(
        "Threat Articles",
        len(df)
    )

    st.dataframe(
        df,
        width="stretch"
    )