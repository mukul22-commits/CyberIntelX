import streamlit as st
import sqlite3
import pandas as pd


def threat_ticker():

    conn = sqlite3.connect(
        "database/cybercrime.db"
    )

    try:

        df = pd.read_sql(
            """
            SELECT title
            FROM intelligence_data
            ORDER BY rowid DESC
            LIMIT 10
            """,
            conn
        )

        text = " | ".join(
            df["title"].tolist()
        )

        st.markdown(
            f"""
<marquee>
🚨 {text}
</marquee>
""",
            unsafe_allow_html=True
        )

    except:

        pass

    conn.close()