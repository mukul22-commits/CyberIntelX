import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px


def officer_analytics():

    st.title("👮 Officer Analytics")

    conn = sqlite3.connect(
        "database/complaints.db"
    )

    complaints = pd.read_sql(
        "SELECT * FROM complaints",
        conn
    )

    conn.close()

    assigned = complaints[
        complaints["officer_name"].notna()
    ]

    total_officers = (
        assigned["officer_name"]
        .nunique()
    )

    total_cases = len(
        assigned
    )

    critical_cases = len(
        complaints[
            complaints["priority"] == "Critical"
        ]
    )

    resolved_cases = len(
        complaints[
            complaints["status"] == "Resolved"
        ]
    )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Officers",
        total_officers
    )

    c2.metric(
        "Assigned Cases",
        total_cases
    )

    c3.metric(
        "Critical Cases",
        critical_cases
    )

    c4.metric(
        "Resolved Cases",
        resolved_cases
    )

    st.markdown("---")

    workload = (
        assigned["officer_name"]
        .value_counts()
        .reset_index()
    )

    workload.columns = [
        "Officer",
        "Cases"
    ]

    if len(workload) > 0:

        fig = px.bar(
            workload,
            x="Officer",
            y="Cases",
            title="Officer Workload"
        )

        st.plotly_chart(
            fig,
            width="stretch"
        )

    priority_df = (
        complaints["priority"]
        .value_counts()
        .reset_index()
    )

    priority_df.columns = [
        "Priority",
        "Count"
    ]

    fig = px.pie(
        priority_df,
        names="Priority",
        values="Count",
        title="Priority Distribution"
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

    status_df = (
        complaints["status"]
        .value_counts()
        .reset_index()
    )

    status_df.columns = [
        "Status",
        "Count"
    ]

    fig = px.bar(
        status_df,
        x="Status",
        y="Count",
        title="Case Status Distribution"
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )