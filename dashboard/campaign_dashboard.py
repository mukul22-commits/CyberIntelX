import streamlit as st

from processing.campaign_detector import (
    detect_campaigns
)


def campaign_dashboard():

    st.title(
        "🌐 Campaign Intelligence"
    )

    campaigns = detect_campaigns()

    if campaigns.empty:

        st.warning(
            "No campaign data."
        )

        return

    st.dataframe(
        campaigns,
        width="stretch"
    )