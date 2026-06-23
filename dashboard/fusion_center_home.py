import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

from streamlit_autorefresh import st_autorefresh

from threat_ticker import threat_ticker

from threat_matrix import threat_matrix

from live_threat_feed import live_threat_feed

from navigation_hub import navigation_hub

from executive_brief import (
    executive_brief
)

from incident_board import (
    incident_board
)

from officer_workload_dashboard import (
    officer_workload_dashboard
)



def fusion_center_home():

    st_autorefresh(
        interval=30000,
        key="fusion_center_refresh"
    )


    st.title(
        "🛡️ CYBER CRIME FUSION CENTER"
    )


    st.caption(
        "National Cyber Intelligence & Investigation Command Center"
    )


    threat_ticker()


    st.markdown("---")


    navigation_hub()


    st.markdown("---")



    # =====================================
    # DATABASE CONNECTION
    # =====================================

    conn = sqlite3.connect(
        "database/complaints.db"
    )


    complaints = pd.read_sql(
        "SELECT * FROM complaints",
        conn
    )


    conn.close()



    # =====================================
    # KPI CALCULATIONS
    # =====================================

    total_cases = len(complaints)


    critical_cases = len(
        complaints[
            complaints["risk_score"] >= 80
        ]
    )


    high_risk_cases = len(
        complaints[
            complaints["risk_score"] >= 60
        ]
    )


    pending_cases = len(
        complaints[
            complaints["status"] == "Pending"
        ]
    )


    resolved_cases = len(
        complaints[
            complaints["status"] == "Resolved"
        ]
    )


    active_incidents = len(
        complaints[
            complaints["status"] != "Resolved"
        ]
    )



    # =====================================
    # NATIONAL THREAT LEVEL
    # =====================================

    st.subheader(
        "🚨 National Threat Level"
    )


    if critical_cases >= 20:

        st.error(
            "🔴 CRITICAL"
        )


    elif critical_cases >= 10:

        st.warning(
            "🟠 HIGH"
        )


    elif critical_cases >= 5:

        st.info(
            "🟡 ELEVATED"
        )


    else:

        st.success(
            "🟢 NORMAL"
        )


    st.markdown("---")



    # =====================================
    # KPI CARDS
    # =====================================

    c1, c2, c3, c4, c5, c6 = st.columns(6)


    c1.metric(
        "Cases",
        total_cases
    )


    c2.metric(
        "Critical",
        critical_cases
    )


    c3.metric(
        "High Risk",
        high_risk_cases
    )


    c4.metric(
        "Pending",
        pending_cases
    )


    c5.metric(
        "Resolved",
        resolved_cases
    )


    c6.metric(
        "Active",
        active_incidents
    )


    st.markdown("---")

    # =====================================
    # CASE STATUS DISTRIBUTION
    # =====================================

    if "status" in complaints.columns:

        st.subheader(
            "📈 Case Status Distribution"
        )


        status_df = (
            complaints["status"]
            .value_counts()
            .reset_index()
        )


        status_df.columns = [
            "Status",
            "Cases"
        ]


        fig = px.pie(
            status_df,
            names="Status",
            values="Cases"
        )


        st.plotly_chart(
            fig,
            width="stretch"
        )


    st.markdown("---")



    # =====================================
    # COMMAND CENTER
    # =====================================

    left, right = st.columns(
        [2, 1]
    )


    with left:

        st.subheader(
            "🔥 Highest Risk Cases"
        )


        risk_columns = [
            col
            for col in [
                "id",
                "name",
                "category",
                "state",
                "risk_score",
                "status",
                "officer_name"
            ]
            if col in complaints.columns
        ]


        high_risk = complaints.sort_values(
            by="risk_score",
            ascending=False
        )


        st.dataframe(
            high_risk[
                risk_columns
            ].head(10),
            width="stretch"
        )



    with right:

        threat_matrix()



    st.markdown("---")



    # =====================================
    # EXECUTIVE OVERVIEW
    # =====================================

    left, right = st.columns(
        [1, 1]
    )


    with left:

        st.subheader(
            "📊 Quick Statistics"
        )


        st.info(
            f"""
Total Cases: {total_cases}

Critical Cases: {critical_cases}

High Risk Cases: {high_risk_cases}

Pending Cases: {pending_cases}

Resolved Cases: {resolved_cases}

Active Incidents: {active_incidents}
"""
        )



    with right:

        if "category" in complaints.columns:

            st.subheader(
                "🎯 Top Crime Categories"
            )


            category_df = (
                complaints["category"]
                .value_counts()
                .reset_index()
            )


            category_df.columns = [
                "Category",
                "Cases"
            ]


            fig = px.pie(
                category_df.head(5),
                names="Category",
                values="Cases"
            )


            st.plotly_chart(
                fig,
                width="stretch"
            )



    st.markdown("---")



    # =====================================
    # STATE ANALYSIS
    # =====================================

    if "state" in complaints.columns:

        st.subheader(
            "🌍 Top Affected States"
        )


        state_df = (
            complaints["state"]
            .value_counts()
            .reset_index()
        )


        state_df.columns = [
            "State",
            "Cases"
        ]


        fig = px.bar(
            state_df.head(10),
            x="State",
            y="Cases"
        )


        st.plotly_chart(
            fig,
            width="stretch"
        )



    st.markdown("---")

    # =====================================
    # CRITICAL COMMAND BOARD
    # =====================================

    st.subheader(
        "🚨 Critical Cases Command Board"
    )


    critical_df = complaints[
        complaints["risk_score"] >= 80
    ]


    critical_columns = [
        col
        for col in [
            "id",
            "name",
            "category",
            "state",
            "risk_score",
            "status",
            "officer_name"
        ]
        if col in critical_df.columns
    ]


    st.dataframe(
        critical_df[
            critical_columns
        ].head(20),
        width="stretch"
    )


    st.markdown("---")



    # =====================================
    # RECENT INCIDENT QUEUE
    # =====================================

    st.subheader(
        "📂 Recent Incident Queue"
    )


    recent_columns = [
        col
        for col in [
            "id",
            "name",
            "category",
            "state",
            "risk_score",
            "status"
        ]
        if col in complaints.columns
    ]


    st.dataframe(
        complaints.sort_values(
            by="id",
            ascending=False
        )[
            recent_columns
        ].head(15),
        width="stretch"
    )


    st.markdown("---")



    # =====================================
    # EXECUTIVE INTELLIGENCE SUMMARY
    # =====================================

    st.subheader(
        "🧠 Executive Intelligence Summary"
    )


    st.info(
        f"""
Total Cases: {total_cases}

Critical Cases: {critical_cases}

High Risk Cases: {high_risk_cases}

Pending Cases: {pending_cases}

Resolved Cases: {resolved_cases}

Active Incidents: {active_incidents}
"""
    )


    st.markdown("---")



    # =====================================
    # LIVE THREAT FEED
    # =====================================

    live_threat_feed()

    st.markdown("---")

    left, right = st.columns(
        [2, 1]
    )

    with left:

        incident_board()

    with right:

        executive_brief()

    st.markdown("---")