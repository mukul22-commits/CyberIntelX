import streamlit as st
import sqlite3
import pandas as pd

from processing.intelligence_normalizer import (
    classify_article
)


def intelligence_normalizer_dashboard():

    st.title(
        "🧠 Intelligence Normalization Center"
    )

    conn = sqlite3.connect(
        "database/cybercrime.db"
    )

    df = pd.read_sql(
        """
        SELECT source,title
        FROM intelligence_data
        ORDER BY rowid DESC
        LIMIT 50
        """,
        conn
    )

    conn.close()

    results = []

    for _, row in df.iterrows():

        intel = classify_article(
            row["title"]
        )

        results.append({

            "source": row["source"],
            "title": row["title"],
            "category": intel["category"],
            "severity": intel["severity"],
            "confidence": intel["confidence"],
    	    "mitre": intel["mitre"],
            "threat_type": intel["threat_type"]

        })

    st.dataframe(
        pd.DataFrame(results),
        width="stretch"
    )