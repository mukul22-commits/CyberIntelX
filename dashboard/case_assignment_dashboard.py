import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px


def case_assignment_dashboard():

    st.title("📊 Case Assignment Dashboard")

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

    assigned = assigned[
        assigned["officer_name"] != ""
    ]

    if len(assigned) == 0:

        st.warning(
            "No assigned cases found."
        )

        return

    workload = (
        assigned.groupby(
            "officer_name"
        )
        .agg(
            Total_Cases=("id", "count"),
            Critical_Cases=(
                "priority",
                lambda x: (x == "Critical").sum()
            ),
            Resolved_Cases=(
                "status",
                lambda x: (x == "Resolved").sum()
            )
        )
        .reset_index()
    )

    st.dataframe(
        workload,
        width="stretch"
    )

    fig = px.bar(
        workload,
        x="officer_name",
        y="Total_Cases",
        title="Cases Assigned Per Officer"
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )