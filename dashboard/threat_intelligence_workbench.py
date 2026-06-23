import streamlit as st

from processing.virustotal_lookup import (
    lookup_ip,
    lookup_domain,
    lookup_url
)

from processing.whois_lookup import (
    lookup_whois
)

from processing.geoip_lookup import (
    lookup_geoip
)


def threat_intelligence_workbench():

    st.title(
        "🛰️ Cyber Threat Intelligence Workbench"
    )

    st.markdown(
        """
        Analyze domains, IPs and URLs from a single screen.
        """
    )

    st.markdown("---")

    ioc_type = st.selectbox(
        "IOC Type",
        [
            "Domain",
            "IP Address",
            "URL"
        ]
    )

    ioc_value = st.text_input(
        "IOC Value"
    )

    if st.button(
        "Analyze IOC"
    ):

        if not ioc_value:

            st.error(
                "Enter IOC"
            )

            return

        # ==========================
        # VIRUSTOTAL
        # ==========================

        try:

            if ioc_type == "Domain":

                vt = lookup_domain(
                    ioc_value
                )

            elif ioc_type == "IP Address":

                vt = lookup_ip(
                    ioc_value
                )

            else:

                vt = lookup_url(
                    ioc_value
                )

            if "data" in vt:

                attrs = vt[
                    "data"
                ][
                    "attributes"
                ]

                stats = attrs.get(
                    "last_analysis_stats",
                    {}
                )

                c1, c2, c3, c4 = st.columns(4)

                c1.metric(
                    "Malicious",
                    stats.get(
                        "malicious",
                        0
                    )
                )

                c2.metric(
                    "Suspicious",
                    stats.get(
                        "suspicious",
                        0
                    )
                )

                c3.metric(
                    "Harmless",
                    stats.get(
                        "harmless",
                        0
                    )
                )

                c4.metric(
                    "Undetected",
                    stats.get(
                        "undetected",
                        0
                    )
                )

        except Exception as e:

            st.error(
                f"VT Error: {e}"
            )

        st.markdown("---")

        # ==========================
        # WHOIS
        # ==========================

        if ioc_type == "Domain":

            try:

                st.subheader(
                    "WHOIS Intelligence"
                )

                whois_data = lookup_whois(
                    ioc_value
                )

                st.json(
                    whois_data
                )

            except Exception as e:

                st.warning(
                    f"WHOIS Error: {e}"
                )

        # ==========================
        # GEOIP
        # ==========================

        if ioc_type == "IP Address":

            try:

                st.subheader(
                    "GeoIP Intelligence"
                )

                geo = lookup_geoip(
                    ioc_value
                )

                st.json(
                    geo
                )

            except Exception as e:

                st.warning(
                    f"GeoIP Error: {e}"
                )

        st.markdown("---")

        st.subheader(
            "VirusTotal Details"
        )

        st.json(vt)