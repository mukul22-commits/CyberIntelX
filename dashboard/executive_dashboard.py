import streamlit as st

from processing.executive_metrics import (
    executive_summary
)

from processing.fraud_ring_detector import (
    detect_fraud_rings
)

from processing.campaign_detector import (
    detect_campaigns
)


def executive_dashboard():

    st.title(
        "📊 Executive Intelligence Dashboard"
    )

    summary = executive_summary()

    fraud_rings = detect_fraud_rings()

    campaigns = detect_campaigns()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Articles",
        summary["articles"]
    )

    c2.metric(
        "Critical Threats",
        summary["critical"]
    )

    c3.metric(
        "Fraud Rings",
        len(fraud_rings)
    )

    c4.metric(
        "Avg Threat Score",
        summary["avg_score"]
    )

    st.markdown("---")

    st.subheader(
        "Detected Fraud Rings"
    )

    st.dataframe(
        fraud_rings,
        width="stretch"
    )

    st.subheader(
        "Detected Campaigns"
    )

    st.dataframe(
        campaigns,
        width="stretch"
    )