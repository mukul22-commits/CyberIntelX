import streamlit as st

from processing.hash_intelligence import (
    analyze_hash
)


def hash_intelligence_dashboard():

    st.title(
        "🦠 Hash Intelligence Center"
    )

    file_hash = st.text_input(
        "Enter MD5/SHA1/SHA256"
    )

    if st.button(
        "Analyze Hash"
    ):

        results = analyze_hash(
            file_hash
        )

        st.dataframe(
            results,
            width="stretch"
        )