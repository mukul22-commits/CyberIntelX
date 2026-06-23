import streamlit as st

from processing.ai_report_generator import (
    generate_report
)


def ai_report_dashboard():

    st.title(
        "📄 AI Intelligence Report"
    )

    if st.button(
        "Generate Report"
    ):

        report = generate_report()

        st.code(
            report
        )