import streamlit as st

from processing.threat_cluster_engine import (
    build_clusters
)


def threat_cluster_dashboard():

    st.title(
        "🧩 Threat Cluster Center"
    )

    df = build_clusters()

    if df.empty:

        st.warning(
            "No clusters found."
        )

        return

    st.metric(
        "Clusters Detected",
        len(df)
    )

    st.dataframe(
        df,
        width="stretch"
    )