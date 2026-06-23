import streamlit as st

from processing.case_intelligence import (
    build_case_intelligence
)


def case_intelligence_dashboard():

    st.title(
        "🧠 Case Intelligence Center"
    )

    df = build_case_intelligence()

    if df.empty:

        st.warning(
            "No complaints found."
        )

        return

    st.dataframe(
        df,
        width="stretch"
    )