import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px


def officer_performance():

    st.title("📈 Officer Performance Dashboard")

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
            "No officer data available"
        )

        return

    performance = (
        assigned.groupby(
            "officer_name"
        )
        .agg(
            Total_Cases=("id", "count"),
            Resolved_Cases=(
                "status",
                lambda x: (x == "Resolved").sum()
            )
        )
        .reset_index()
    )

    performance["Resolution_Rate"] = (
        performance["Resolved_Cases"]
        /
        performance["Total_Cases"]
        * 100
    ).round(2)

    st.dataframe(
        performance,
        width="stretch"
    )

    fig = px.bar(
        performance,
        x="officer_name",
        y="Resolution_Rate",
        title="Officer Resolution Rate (%)"
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )