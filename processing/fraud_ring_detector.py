import sqlite3
import pandas as pd

def detect_fraud_rings():

    conn = sqlite3.connect(
        "database/complaints.db"
    )

    df = pd.read_sql(
        "SELECT * FROM complaints",
        conn
    )

    conn.close()

    if len(df) == 0:
        return pd.DataFrame()

    rings = []

    email_counts = (
        df.groupby("email")
        .size()
        .reset_index(name="count")
    )

    for _, row in email_counts.iterrows():

        if row["count"] > 1:

            rings.append({

                "indicator": row["email"],
                "type": "Email",
                "cases": row["count"]

            })

    return pd.DataFrame(rings)