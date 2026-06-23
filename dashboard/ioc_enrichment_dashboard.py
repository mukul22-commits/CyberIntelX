import streamlit as st

from processing.ioc_enrichment import enrich_ioc


def ioc_enrichment_dashboard():

    st.title("IOC Enrichment Center")

    ioc = st.text_input(
        "Enter IP, Domain or URL"
    )

    if st.button("Enrich IOC"):

        result = enrich_ioc(ioc)

        if result.empty:

            st.warning(
                "No intelligence found."
            )
            return

        st.dataframe(
            result,
            width="stretch"
        )

        row = result.iloc[0]

        cols = st.columns(3)

        if "type" in row:

            cols[0].metric(
                "IOC Type",
                row["type"]
            )

        if "reputation" in row:

            cols[1].metric(
                "Reputation",
                row["reputation"]
            )

        if "malicious" in row:

            cols[2].metric(
                "Malicious",
                row["malicious"]
            )