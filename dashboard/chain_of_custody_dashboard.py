import streamlit as st
import pandas as pd
import sqlite3


def chain_of_custody_dashboard():

    st.title(
        "🔒 Chain Of Custody"
    )

    conn = sqlite3.connect(
        "database/chain_of_custody.db"
    )

    try:

        df = pd.read_sql(
            """
            SELECT
                case_id,
                action,
                officer,
                timestamp
            FROM custody_log
            ORDER BY id DESC
            """,
            conn
        )

        if len(df) == 0:

            st.warning(
                "No custody records found"
            )

        else:

            st.dataframe(
                df,
                width="stretch"
            )

    except Exception as e:

        st.error(str(e))

    conn.close()