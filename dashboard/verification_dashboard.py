import streamlit as st

from processing.verification_engine import (
    verify_ioc
)


def verification_dashboard():

    st.title(
        "✅ Intelligence Verification Center"
    )

    ioc = st.text_input(
        "Enter IOC / Domain / Email / Hash"
    )

    if st.button(
        "Verify"
    ):

        result = verify_ioc(
            ioc
        )

        st.dataframe(
            result,
            width="stretch"
        )