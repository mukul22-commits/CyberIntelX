import streamlit as st

from processing.intelligence_correlator_v2 import (
    correlate_intelligence
)


def advanced_correlation_dashboard():

    st.title(
        "🔗 Advanced Correlation Engine"
    )

    df = correlate_intelligence()

    if df.empty:

        st.warning(
            "No correlations found."
        )

        return

    st.metric(
        "Total Correlations",
        len(df)
    )

    st.dataframe(
        df,
        width="stretch"
    )