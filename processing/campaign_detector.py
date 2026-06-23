import sqlite3
import pandas as pd

def detect_campaigns():

    conn = sqlite3.connect(
        "database/complaints.db"
    )

    df = pd.read_sql(
        "SELECT * FROM complaints",
        conn
    )

    conn.close()

    campaigns = (
        df.groupby("category")
        .size()
        .reset_index(name="count")
    )

    campaigns = campaigns[
        campaigns["count"] >= 2
    ]

    return campaigns