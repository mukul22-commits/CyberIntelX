import streamlit as st
import pandas as pd

from processing.geoip_lookup import (
    get_ip_info
)


def geoip_dashboard():

    st.title(
        "🌍 Geo-IP Intelligence Center"
    )

    ip = st.text_input(
        "Enter IP Address",
        "8.8.8.8"
    )

    if st.button(
        "Analyze IP"
    ):

        result = get_ip_info(ip)

        # -------------------
        # Status
        # -------------------

        if result["lookup_status"] == "Success":

            st.success(
                "Geo-IP Lookup Successful"
            )

        else:

            st.warning(
                result["lookup_status"]
            )

        # -------------------
        # IP CLASSIFICATION
        # -------------------

        ip_type = "Public IP"
        environment = "Internet"
        routable = "Yes"
        threat_note = "Publicly reachable"
        risk_classification = result["risk_level"]

        if ip.startswith("100."):

            ip_type = (
                "Carrier Grade NAT (CGNAT)"
            )

            environment = (
                "ISP Internal Network"
            )

            routable = "No"

            threat_note = (
                "Reserved CGNAT Range"
            )

            risk_classification = (
                "LOW (CGNAT)"
            )

        elif ip.startswith("10."):

            ip_type = "Private Network"

            environment = (
                "Corporate/Home LAN"
            )

            routable = "No"

            threat_note = (
                "Internal private network"
            )

            risk_classification = (
                "LOW (Private Network)"
            )

        elif ip.startswith("192.168."):

            ip_type = "Private Network"

            environment = "Home LAN"

            routable = "No"

            threat_note = (
                "Local router network"
            )

            risk_classification = (
                "LOW (Private Network)"
            )

        elif ip.startswith("172."):

            try:

                second = int(
                    ip.split(".")[1]
                )

                if 16 <= second <= 31:

                    ip_type = (
                        "Private Network"
                    )

                    environment = (
                        "Private Subnet"
                    )

                    routable = "No"

                    threat_note = (
                        "Private enterprise network"
                    )

                    risk_classification = (
                        "LOW (Private Network)"
                    )

            except:
                pass

        elif ip.startswith("127."):

            ip_type = "Loopback"

            environment = (
                "Local Device"
            )

            routable = "No"

            threat_note = (
                "Self communication"
            )

            risk_classification = (
                "NONE (Loopback)"
            )

        # -------------------
        # TOP CARDS
        # -------------------

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(
            "Country",
            result["country"]
        )

        c2.metric(
            "City",
            result["city"]
        )

        c3.metric(
            "Provider",
            result["org"]
        )

        c4.metric(
            "Risk Level",
            risk_classification
        )

        st.markdown("---")

        # -------------------
        # INTELLIGENCE SUMMARY
        # -------------------

        st.subheader(
            "📋 Intelligence Summary"
        )

        st.info(
            f"""
IP Address: {result['ip']}

Country: {result['country']}

Region: {result['region']}

City: {result['city']}

Provider / ISP: {result['org']}

ASN: {result['asn']}

Latitude: {result['latitude']}

Longitude: {result['longitude']}

Lookup Status: {result['lookup_status']}
"""
        )

        # -------------------
        # NETWORK CLASSIFICATION
        # -------------------

        st.markdown("---")

        st.subheader(
            "🏷 Network Classification"
        )

        st.info(
            f"""
IP Type: {ip_type}

Environment: {environment}

Routable: {routable}

Threat Note: {threat_note}
"""
        )

        # -------------------
        # INTELLIGENCE ASSESSMENT
        # -------------------

        st.subheader(
            "🧠 Intelligence Assessment"
        )

        org = str(
            result["org"]
        ).lower()

        if "google" in org:

            final_risk = (
                "LOW (Trusted Infrastructure)"
            )

        elif "cloudflare" in org:

            final_risk = (
                "LOW (Trusted Infrastructure)"
            )

        elif "amazon" in org:

            final_risk = (
                "MEDIUM (Cloud Provider)"
            )

        elif "microsoft" in org:

            final_risk = (
                "MEDIUM (Cloud Provider)"
            )

        elif result["country"] in [
            "Russia",
            "China",
            "North Korea",
            "Iran"
        ]:

            final_risk = (
                "HIGH (Watchlist Country)"
            )

        else:

            final_risk = (
                risk_classification
            )

        st.info(
            f"""
Risk Classification:
{final_risk}
"""
        )

        st.success(
            f"""
This IP belongs to:

{result['org']}

Location:

{result['city']},
{result['region']},
{result['country']}

ASN:

{result['asn']}

Coordinates:

({result['latitude']},
{result['longitude']})

Status:

{result['lookup_status']}
"""
        )

        # -------------------
        # TECHNICAL DETAILS
        # -------------------

        st.subheader(
            "🔍 Technical Details"
        )

        st.dataframe(
            pd.DataFrame(
                [result]
            ),
            width="stretch"
        )

        # -------------------
        # MAP
        # -------------------

        if result["latitude"] is not None:

            map_df = pd.DataFrame(
                {
                    "lat": [
                        result["latitude"]
                    ],
                    "lon": [
                        result["longitude"]
                    ]
                }
            )

            st.markdown("---")

            st.subheader(
                "🗺 Geographic Location"
            )

            st.map(map_df)

        else:

            st.warning(
                "Location coordinates unavailable."
            )