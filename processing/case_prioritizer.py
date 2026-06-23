import sqlite3
import pandas as pd


def prioritize_cases():

    conn = sqlite3.connect(
        "database/complaints.db"
    )

    complaints = pd.read_sql(
        "SELECT * FROM complaints",
        conn
    )

    conn.close()

    if complaints.empty:
        return complaints

    complaints["priority"] = complaints[
        "risk_score"
    ].apply(
        lambda x:
        "Critical"
        if x >= 80
        else "High"
        if x >= 60
        else "Medium"
        if x >= 40
        else "Low"
    )

    return complaints.sort_values(
        "risk_score",
        ascending=False
    )