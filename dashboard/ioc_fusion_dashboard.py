import streamlit as st

from processing.ioc_fusion_engine import (
    build_ioc_fusion
)


def ioc_fusion_dashboard():

    st.title(
        "🔗 IOC Fusion Center"
    )

    df = build_ioc_fusion()

    if df.empty:

        st.warning(
            "No IOC correlations found."
        )

        return

    st.metric(
        "IOC Matches",
        len(df)
    )

    st.dataframe(
        df,
        width="stretch"
    )