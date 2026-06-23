import streamlit as st
import sqlite3
import pandas as pd

from processing.case_prioritizer import prioritize_cases
from processing.case_intelligence import build_case_intelligence
from processing.fraud_ring_detector import detect_fraud_rings
from processing.campaign_detector import detect_campaigns

def investigator_workspace():

    st.title("🕵️ Investigator Workspace")

    cases = prioritize_cases()

    st.subheader("Priority Cases")

    st.dataframe(
        cases[
            [
                "id",
                "name",
                "category",
                "risk_score",
                "priority"
            ]
        ]
    )

    st.subheader("Case Intelligence")

    st.dataframe(
        build_case_intelligence()
    )

    st.subheader("Fraud Ring Detection")

    st.dataframe(
        detect_fraud_rings()
    )

    st.subheader("Campaign Detection")

    st.dataframe(
        detect_campaigns()
    )