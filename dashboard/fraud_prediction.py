import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px


def fraud_prediction():

    st.title("🤖 Fraud Trend Prediction")

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

    category_df = (
        complaints["category"]
        .value_counts()
        .reset_index()
    )

    category_df.columns = [
        "Category",
        "Cases"
    ]

    st.subheader(
        "Most Common Fraud Types"
    )

    fig = px.bar(
        category_df,
        x="Category",
        y="Cases"
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

    predicted = (
        category_df.iloc[0]["Category"]
    )

    st.success(
        f"Predicted Most Active Fraud Trend: {predicted}"
    )