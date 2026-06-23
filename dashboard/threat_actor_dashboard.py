import streamlit as st
import pandas as pd
import sqlite3

from processing.threat_actor_engine import (
    identify_threat_actor
)


def threat_actor_dashboard():

    st.title(
        "👤 Threat Actor Intelligence"
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

    results = []

    for _, row in df.iterrows():

        actors = identify_threat_actor(
            str(row["description"])
        )

        for actor, campaign in actors:

            results.append({

                "Case ID":
                row["id"],

                "Category":
                row["category"],

                "Threat Actor":
                actor,

                "Campaign":
                campaign

            })

    if len(results) == 0:

        st.warning(
            "No Threat Actors Found"
        )

        return

    result_df = pd.DataFrame(
        results
    )

    st.dataframe(
        result_df,
        width="stretch"
    )