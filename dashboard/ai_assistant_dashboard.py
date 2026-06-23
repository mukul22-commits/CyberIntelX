import streamlit as st
import sqlite3
import pandas as pd

from processing.ai_assistant import (
    generate_ai_brief
)


def ai_assistant_dashboard():

    st.title(
        "🤖 AI Investigation Assistant"
    )

    conn = sqlite3.connect(
        "database/complaints.db"
    )

    complaints = pd.read_sql(
        """
        SELECT
            id,
            name,
            category,
            risk_score
        FROM complaints
        """,
        conn
    )

    conn.close()

    if len(complaints) == 0:

        st.warning(
            "No complaints available."
        )

        return

    selected_case = st.selectbox(
        "Select Complaint ID",
        complaints["id"]
    )

    if st.button(
        "Generate AI Brief"
    ):

        brief = generate_ai_brief(
            selected_case
        )

        st.text_area(
            "AI Investigation Brief",
            brief,
            height=400
        )