import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px


def executive_situation_room():

    st.title(
        "🌐 Executive Situation Room"
    )

    conn = sqlite3.connect(
        "database/complaints.db"
    )

    df = pd.read_sql(
        "SELECT * FROM complaints",
        conn
    )

    conn.close()

    total_cases = len(df)

    high_risk = len(
        df[df["risk_score"] >= 70]
    )

    resolved = len(
        df[df["status"] == "Resolved"]
    )

    pending = len(
        df[df["status"] == "Pending"]
    )

    avg_risk = round(
        df["risk_score"].mean(),
        2
    ) if len(df) else 0

    c1, c2, c3, c4, c5 = st.columns(5)

    c1.metric(
        "Total Cases",
        total_cases
    )

    c2.metric(
        "High Risk",
        high_risk
    )

    c3.metric(
        "Resolved",
        resolved
    )

    c4.metric(
        "Pending",
        pending
    )

    c5.metric(
        "Avg Risk",
        avg_risk
    )

    st.markdown("---")

    left, right = st.columns(2)

    with left:

        st.subheader(
            "Cases by Category"
        )

        category_df = (
            df["category"]
            .value_counts()
            .reset_index()
        )

        category_df.columns = [
            "Category",
            "Count"
        ]

        fig = px.pie(
            category_df,
            names="Category",
            values="Count"
        )

        st.plotly_chart(
            fig,
            width="stretch"
        )

    with right:

        st.subheader(
            "Cases by State"
        )

        state_df = (
            df["state"]
            .value_counts()
            .reset_index()
        )

        state_df.columns = [
            "State",
            "Count"
        ]

        fig = px.bar(
            state_df,
            x="State",
            y="Count"
        )

        st.plotly_chart(
            fig,
            width="stretch"
        )

    st.markdown("---")

    st.subheader(
        "Latest Cases"
    )

    st.dataframe(
        df.sort_values(
            "id",
            ascending=False
        ).head(20),
        width="stretch"
    )