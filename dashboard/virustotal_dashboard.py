import streamlit as st

from processing.virustotal_lookup import (
    lookup_ip,
    lookup_domain,
    lookup_url
)


def virustotal_dashboard():

    st.title("🦠 VirusTotal Intelligence Center")

    lookup_type = st.selectbox(
        "IOC Type",
        [
            "Domain",
            "IP Address",
            "URL"
        ]
    )

    ioc_value = st.text_input(
        "Enter IOC"
    )

    if st.button(
        "Analyze IOC"
    ):

        if not ioc_value:

            st.error(
                "Please enter an IOC"
            )

            return

        with st.spinner(
            "Querying VirusTotal..."
        ):

            try:

                if lookup_type == "Domain":

                    result = lookup_domain(
                        ioc_value
                    )

                elif lookup_type == "IP Address":

                    result = lookup_ip(
                        ioc_value
                    )

                else:

                    result = lookup_url(
                        ioc_value
                    )

                if "error" in result:

                    st.error(
                        result["error"]
                    )

                    return

                data = result["data"]

                attributes = data[
                    "attributes"
                ]

                stats = attributes.get(
                    "last_analysis_stats",
                    {}
                )

                malicious = stats.get(
                    "malicious",
                    0
                )

                suspicious = stats.get(
                    "suspicious",
                    0
                )

                harmless = stats.get(
                    "harmless",
                    0
                )

                undetected = stats.get(
                    "undetected",
                    0
                )

                c1, c2, c3, c4 = st.columns(4)

                c1.metric(
                    "Malicious",
                    malicious
                )

                c2.metric(
                    "Suspicious",
                    suspicious
                )

                c3.metric(
                    "Harmless",
                    harmless
                )

                c4.metric(
                    "Undetected",
                    undetected
                )

                st.markdown("---")

                st.subheader(
                    "Raw VirusTotal Data"
                )

                st.json(
                    attributes
                )

            except Exception as e:

                st.error(
                    str(e)
                )