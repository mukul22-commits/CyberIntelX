import streamlit as st
import pandas as pd

from processing.whois_lookup import (
    get_domain_info
)


def whois_dashboard():

    st.title(
        "🌐 WHOIS Intelligence Center"
    )

    domain = st.text_input(
        "Enter Domain",
        "google.com"
    )

    if st.button(
        "Analyze Domain"
    ):

        result = get_domain_info(
            domain
        )

        # Safe variables

        domain_age = result.get(
            "domain_age_days",
            0
        )

        risk_score = result.get(
            "risk_score",
            0
        )

        risk_level = result.get(
            "risk_level",
            "Unknown"
        )

        category = result.get(
            "category",
            "Unknown"
        )

        # Top Metrics

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(
            "Domain Age",
            domain_age
        )

        c2.metric(
            "Risk Score",
            risk_score
        )

        c3.metric(
            "Risk Level",
            risk_level
        )

        c4.metric(
            "Category",
            category
        )

        st.markdown("---")

        # Summary

        st.subheader(
            "📋 Intelligence Summary"
        )

        st.info(
            f"""
Domain: {result.get('domain')}

Registrar: {result.get('registrar')}

Created: {result.get('creation_date')}

Expiry: {result.get('expiry_date')}

Age: {domain_age} Days
"""
        )

        st.markdown("---")

        # Assessment

        st.subheader(
            "🧠 Intelligence Assessment"
        )

        if risk_score >= 90:

            st.error(
                "Critical Risk Domain"
            )

        elif risk_score >= 80:

            st.warning(
                "High Risk Domain"
            )

        elif risk_score >= 60:

            st.warning(
                "Medium Risk Domain"
            )

        else:

            st.success(
                "Low Risk Domain"
            )

        st.markdown("---")

        # Raw Data

        st.subheader(
            "🔍 Technical Details"
        )

        st.dataframe(
            pd.DataFrame(
                [result]
            ),
            width="stretch"
        )