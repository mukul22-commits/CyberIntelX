import sqlite3
import pandas as pd


def calculate_sector_risk():

    conn = sqlite3.connect(
        "database/complaints.db"
    )

    complaints = pd.read_sql(
        "SELECT category,risk_score FROM complaints",
        conn
    )

    conn.close()

    if complaints.empty:

        return pd.DataFrame()

    risk = complaints.groupby(
        "category"
    )["risk_score"].mean().reset_index()

    risk.columns = [
        "sector",
        "average_risk"
    ]

    risk = risk.sort_values(
        "average_risk",
        ascending=False
    )

    return risk