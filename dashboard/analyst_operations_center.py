import streamlit as st

from processing.ioc_fusion_v2 import (
    investigate_ioc
)


def analyst_operations_center():

    st.title(
        "🕵️ Analyst Operations Center"
    )

    st.markdown(
        """
Centralized Investigation Workspace

VirusTotal
WHOIS
GeoIP
IOC Reputation
IOC Fusion
"""
    )

    ioc = st.text_input(
        "Enter IOC / Domain / IP"
    )

    if st.button(
        "Investigate"
    ):

        result = investigate_ioc(
            ioc
        )

        st.markdown("---")

        c1, c2 = st.columns(2)

        with c1:

            st.subheader(
                "VirusTotal"
            )

            st.json(
                result.get(
                    "virustotal",
                    {}
                )
            )

        with c2:

            st.subheader(
                "WHOIS"
            )

            st.json(
                result.get(
                    "whois",
                    {}
                )
            )

        st.markdown("---")

        st.subheader(
            "IOC Reputation"
        )

        st.json(
            result.get(
                "reputation",
                {}
            )
        )

        if "geoip" in result:

            st.markdown("---")

            st.subheader(
                "GeoIP"
            )

            st.json(
                result["geoip"]
            )