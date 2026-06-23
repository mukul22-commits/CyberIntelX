import streamlit as st

def navigation_menu():

    section = st.sidebar.selectbox(
        "Operations Center",
        [
            "Fusion Center",
            "Case Management",
            "Intelligence",
            "Threat Monitoring",
            "Administration"
        ]
    )

    if section == "Fusion Center":

        return st.sidebar.radio(
            "Module",
            [
                "Fusion Center Home",
                "Case Command Center",
                "Executive Situation Room",
                "National Threat Wall"
            ]
        )

    elif section == "Case Management":

        return st.sidebar.radio(
            "Module",
            [
                "Complaint Analytics",
                "Investigation Panel",
                "Case Timeline",
                "Chain Of Custody",
                "Officer Assignment Center",
                "Officer Workload"
            ]
        )

    elif section == "Intelligence":

        return st.sidebar.radio(
            "Module",
            [
                "Analyst Operations Center",
                "Threat Intelligence Workbench",
                "IOC Fusion Intelligence",
                "IOC Enrichment Center",
                "WHOIS Intelligence",
                "Geo-IP Intelligence",
                "VirusTotal Intelligence"
            ]
        )

    elif section == "Threat Monitoring":

        return st.sidebar.radio(
            "Module",
            [
                "Cyber Crime Heatmap",
                "Threat Trend Center",
                "Threat Forecast Center",
                "Sector Risk Center",
                "National Threat Center"
            ]
        )

    else:

        return st.sidebar.radio(
            "Module",
            [
                "Officer Management",
                "Executive Intelligence Dashboard",
                "Investigation Report Center"
            ]
        )