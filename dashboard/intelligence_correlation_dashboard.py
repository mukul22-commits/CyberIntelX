import streamlit as st

from processing.intelligence_correlation_engine import (
    correlate
)


def intelligence_correlation_dashboard():

    st.title(
        "🔗 Intelligence Correlation Center"
    )

    ioc = st.text_input(
        "IOC / Domain / IP"
    )

    if st.button(
        "Correlate"
    ):

        st.dataframe(
            correlate(ioc),
            width="stretch"
        )