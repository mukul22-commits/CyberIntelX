import streamlit as st

from processing.domain_intelligence import (
    analyze_domain
)


def domain_intelligence_dashboard():

    st.title(
        "🌐 Domain Intelligence Center"
    )

    domain = st.text_input(
        "Enter Domain"
    )

    if st.button(
        "Analyze Domain"
    ):

        results = analyze_domain(
            domain
        )

        st.dataframe(
            results,
            width="stretch"
        )