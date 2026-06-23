import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px


def officer_workload_dashboard():

    st.title(
        "👮 Officer Workload Dashboard"
    )

    conn = sqlite3.connect(
        "database/complaints.db"
    )

    df = pd.read_sql(
        """
        SELECT
            officer_name,
            COUNT(*) as total_cases,
            AVG(risk_score) as avg_risk
        FROM complaints
        WHERE officer_name IS NOT NULL
        GROUP BY officer_name
        """,
        conn
    )

    conn.close()

    if len(df) == 0:

        st.warning(
            "No Officer Data"
        )

        return

    st.dataframe(
        df,
        width="stretch"
    )

    fig = px.bar(
        df,
        x="officer_name",
        y="total_cases",
        color="avg_risk"
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )