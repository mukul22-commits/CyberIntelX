import streamlit as st

from processing.investigation_confidence import (
    calculate_confidence
)


def investigation_confidence_dashboard():

    st.title(
        "🎯 Investigation Confidence Engine"
    )

    risk_score = st.slider(
        "Risk Score",
        0,
        100,
        50
    )

    fraud_ring = st.checkbox(
        "Fraud Ring Match"
    )

    campaign = st.checkbox(
        "Campaign Match"
    )

    verification_matches = st.slider(
        "Verification Matches",
        0,
        5,
        0
    )

    if st.button(
        "Calculate Confidence"
    ):

        result = calculate_confidence(
            risk_score,
            fraud_ring,
            campaign,
            verification_matches
        )

        st.dataframe(
            result,
            width="stretch"
        )