import streamlit as st

from processing.case_prioritizer import (
    prioritize_cases
)


def case_prioritization_dashboard():

    st.title(
        "🎯 Case Prioritization Center"
    )

    df = prioritize_cases()

    if df.empty:

        st.warning(
            "No complaints available."
        )

        return

    st.dataframe(
        df[
            [
                "id",
                "name",
                "category",
                "risk_score",
                "priority"
            ]
        ],
        width="stretch"
    )