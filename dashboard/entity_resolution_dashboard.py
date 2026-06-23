import streamlit as st

from processing.entity_resolution import (
    resolve_entities
)


def entity_resolution_dashboard():

    st.title(
        "🧠 Entity Resolution Center"
    )

    df = resolve_entities()

    if df.empty:

        st.warning(
            "No linked entities found."
        )

        return

    c1, c2 = st.columns(2)

    c1.metric(
        "Unique Entities",
        len(df)
    )

    c2.metric(
        "Most Linked Cases",
        df["linked_cases"].max()
    )

    st.markdown("---")

    st.subheader(
        "Linked Entities"
    )

    st.dataframe(
        df.sort_values(
            "linked_cases",
            ascending=False
        ),
        width="stretch"
    )

    st.markdown("---")

    st.subheader(
        "Potential Fraud Rings"
    )

    fraud_rings = df[
        df["linked_cases"] >= 2
    ]

    st.dataframe(
        fraud_rings,
        width="stretch"
    )

    if len(fraud_rings) > 0:

        st.error(
            f"{len(fraud_rings)} suspicious entities detected."
        )