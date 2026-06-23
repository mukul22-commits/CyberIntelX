import streamlit as st

from processing.national_threat_score import (
    calculate_national_threat
)


def national_threat_center():

    st.title(
        "🛡 National Cyber Threat Center"
    )

    threat = calculate_national_threat()

    st.metric(
        "National Threat Score",
        threat["score"]
    )

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Active Alerts",
        threat["alerts"]
    )

    c2.metric(
        "Critical CVEs",
        threat["cves"]
    )

    c3.metric(
        "Threat Sources",
        threat["sources"]
    )

    st.metric(
        "Threat Level",
        threat["level"]
    )

    if threat["level"] == "CRITICAL":

        st.error(
            "🔴 National Threat Level: CRITICAL"
        )

    elif threat["level"] == "HIGH":

        st.warning(
            "🟠 National Threat Level: HIGH"
        )

    elif threat["level"] == "ELEVATED":

        st.info(
            "🟡 National Threat Level: ELEVATED"
        )

    else:

        st.success(
            "🟢 National Threat Level: GUARDED"
        )