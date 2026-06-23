import streamlit as st

from processing.daily_brief_generator import (
    generate_daily_brief
)


def daily_brief_dashboard():

    st.title(
        "📋 Daily Intelligence Brief"
    )

    report = generate_daily_brief()

    st.text_area(
        "Report",
        report,
        height=500
    )