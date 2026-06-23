import streamlit as st
import sqlite3
import pandas as pd


def cyber_fusion_v2():

    st.markdown(
        """
        <style>

        .fusion-card{
            background:rgba(255,255,255,0.05);
            backdrop-filter: blur(20px);
            border-radius:20px;
            padding:20px;
            box-shadow:0 8px 32px rgba(0,0,0,0.3);
            margin-bottom:15px;
        }

        .fusion-title{
            font-size:22px;
            font-weight:bold;
            color:white;
        }

        .fusion-number{
            font-size:40px;
            color:#00ffcc;
            font-weight:bold;
        }

        </style>
        """,
        unsafe_allow_html=True
    )

    st.title(
        "🛰 Cyber Fusion Command Center"
    )

    conn = sqlite3.connect(
        "database/complaints.db"
    )

    complaints = pd.read_sql(
        "SELECT * FROM complaints",
        conn
    )

    conn.close()

    total_cases = len(complaints)

    active_cases = len(
        complaints[
            complaints["status"]
            != "Closed"
        ]
    )

    high_risk = len(
        complaints[
            complaints["risk_score"] >= 70
        ]
    )

    resolved = len(
        complaints[
            complaints["status"]
            == "Resolved"
        ]
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(
            f"""
            <div class="fusion-card">
            <div class="fusion-title">
            Total Cases
            </div>
            <div class="fusion-number">
            {total_cases}
            </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            f"""
            <div class="fusion-card">
            <div class="fusion-title">
            Active Cases
            </div>
            <div class="fusion-number">
            {active_cases}
            </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c3:
        st.markdown(
            f"""
            <div class="fusion-card">
            <div class="fusion-title">
            High Risk
            </div>
            <div class="fusion-number">
            {high_risk}
            </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c4:
        st.markdown(
            f"""
            <div class="fusion-card">
            <div class="fusion-title">
            Resolved
            </div>
            <div class="fusion-number">
            {resolved}
            </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")

    st.subheader(
        "🚨 Live Incident Board"
    )

    st.dataframe(
        complaints[
            [
                "id",
                "category",
                "risk_score",
                "status",
                "officer_name"
            ]
        ],
        width="stretch"
    )