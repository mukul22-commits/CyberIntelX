import streamlit as st

from processing.fraud_ring_detector import (
    detect_fraud_rings
)


def fraud_ring_dashboard():

    st.title(
        "🚨 Fraud Ring Intelligence"
    )

    rings = detect_fraud_rings()

    if rings.empty:

        st.success(
            "No fraud rings detected."
        )

        return

    st.metric(
        "Detected Fraud Rings",
        len(rings)
    )

    st.dataframe(
        rings,
        width="stretch"
    )