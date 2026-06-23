import streamlit as st

from processing.ioc_reputation import (
    evaluate_ioc
)


def ioc_reputation_dashboard():

    st.title(
        "🛡 IOC Reputation Center"
    )

    ioc = st.text_input(
        "Enter IOC"
    )

    if st.button(
        "Analyze IOC"
    ):

        result = evaluate_ioc(ioc)

        st.metric(
            "Risk Score",
            result["score"]
        )

        st.metric(
            "Risk Level",
            result["risk"]
        )

        st.write(
            result["reasons"]
        )