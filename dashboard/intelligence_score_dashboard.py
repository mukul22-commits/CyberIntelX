import streamlit as st
import sqlite3
import pandas as pd

from processing.intelligence_score import (
    calculate_intelligence_score
)


def intelligence_score_dashboard():

    st.title(
        "🧠 Intelligence Scoring Center"
    )

    conn = sqlite3.connect(
        "database/complaints.db"
    )

    complaints = pd.read_sql(
        "SELECT * FROM complaints",
        conn
    )

    conn.close()

    rows = []

    for _, row in complaints.iterrows():

        score, level = (
            calculate_intelligence_score(
                row["risk_score"],
                1
            )
        )

        rows.append(
            {
                "Case ID": row["id"],
                "Category":
                row["category"],
                "Risk Score":
                row["risk_score"],
                "Intelligence Score":
                score,
                "Level":
                level
            }
        )

    st.dataframe(
        pd.DataFrame(rows),
        width="stretch"
    )