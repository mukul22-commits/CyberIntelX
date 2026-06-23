import streamlit as st
import pandas as pd
import sqlite3


def threat_heatmap():

    st.title(
        "🌎 Threat Heat Map"
    )

    conn = sqlite3.connect(
        "database/complaints.db"
    )

    df = pd.read_sql(
        """
        SELECT
            state,
            COUNT(*) as cases
        FROM complaints
        GROUP BY state
        ORDER BY cases DESC
        """,
        conn
    )

    conn.close()

    if len(df) == 0:

        st.warning(
            "No Data Found"
        )

        return

    st.subheader(
        "State-wise Complaints"
    )

    st.dataframe(
        df,
        width="stretch"
    )

    st.bar_chart(
        df.set_index("state")
    )