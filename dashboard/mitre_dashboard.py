import streamlit as st
import sqlite3
import pandas as pd

from processing.mitre_mapper import (
    map_to_mitre
)


def mitre_dashboard():

    st.title(
        "🎯 MITRE ATT&CK Intelligence"
    )

    conn = sqlite3.connect(
        "database/complaints.db"
    )

    df = pd.read_sql(
        """
        SELECT
            id,
            category,
            description
        FROM complaints
        """,
        conn
    )

    conn.close()

    if len(df) == 0:

        st.warning(
            "No complaints available"
        )

        return

    results = []

    for _, row in df.iterrows():

        techniques = map_to_mitre(
            str(row["description"])
        )

        for tid, name in techniques:

            results.append(
                {
                    "Case ID":
                    row["id"],

                    "Category":
                    row["category"],

                    "Technique ID":
                    tid,

                    "Technique":
                    name
                }
            )

    if len(results) == 0:

        st.warning(
            "No ATT&CK mappings found"
        )

        return

    result_df = pd.DataFrame(
        results
    )

    st.dataframe(
        result_df,
        width="stretch"
    )