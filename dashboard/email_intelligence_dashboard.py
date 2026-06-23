import streamlit as st

from processing.email_intelligence import (
    analyze_email
)


def email_intelligence_dashboard():

    st.title(
        "📧 Email Intelligence Center"
    )

    email = st.text_input(
        "Enter Email Address"
    )

    if st.button(
        "Analyze Email"
    ):

        results = analyze_email(
            email
        )

        st.dataframe(
            results,
            width="stretch"
        )