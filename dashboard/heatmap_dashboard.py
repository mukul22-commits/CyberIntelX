import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px


def heatmap_dashboard():

    st.title("🗺️ Cyber Crime Heatmap")

    conn = sqlite3.connect(
        "database/complaints.db"
    )

    complaints = pd.read_sql(
        "SELECT * FROM complaints",
        conn
    )

    conn.close()

    if len(complaints) == 0:

        st.warning(
            "No complaint data available"
        )

        return

    state_df = (
        complaints["state"]
        .value_counts()
        .reset_index()
    )

    state_df.columns = [
        "State",
        "Complaints"
    ]

    st.subheader(
        "State Wise Complaint Distribution"
    )

    fig = px.bar(
        state_df,
        x="State",
        y="Complaints",
        title="Cyber Crime Complaints by State"
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

    st.subheader(
        "Top Affected States"
    )

    st.dataframe(
        state_df,
        width="stretch"
    )