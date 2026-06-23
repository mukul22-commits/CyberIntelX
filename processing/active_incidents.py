import sqlite3
import pandas as pd


def get_active_incidents():

    conn = sqlite3.connect(
        "database/complaints.db"
    )

    complaints = pd.read_sql(
        "SELECT * FROM complaints",
        conn
    )

    conn.close()

    if "risk_score" not in complaints.columns:

        return pd.DataFrame()

    incidents = complaints.copy()

    incidents["severity"] = "Low"

    incidents.loc[
        incidents["risk_score"] >= 80,
        "severity"
    ] = "Critical"

    incidents.loc[
        (incidents["risk_score"] >= 60) &
        (incidents["risk_score"] < 80),
        "severity"
    ] = "High"

    incidents.loc[
        (incidents["risk_score"] >= 40) &
        (incidents["risk_score"] < 60),
        "severity"
    ] = "Medium"

    return incidents