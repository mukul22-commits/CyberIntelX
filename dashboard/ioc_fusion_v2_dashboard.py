import streamlit as st

from processing.ioc_fusion_v2 import (
    investigate_ioc
)


def ioc_fusion_v2_dashboard():

    st.title(
        "🧠 IOC Fusion Intelligence Center"
    )

    ioc = st.text_input(
        "IOC / Domain"
    )

    if st.button(
        "Investigate"
    ):

        result = investigate_ioc(
            ioc
        )

        st.json(result)