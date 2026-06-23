import streamlit as st

from processing.ioc_correlation import (
    correlate_iocs
)


def ioc_correlation_dashboard():

    st.title(
        "🔗 IOC Correlation Center"
    )

    df = correlate_iocs()

    if len(df) == 0:

        st.warning(
            "No Correlations Found"
        )

        return

    st.dataframe(
        df,
        width="stretch"
    )