import sqlite3
import pandas as pd


def build_case_intelligence():

    conn = sqlite3.connect(
        "database/complaints.db"
    )

    df = pd.read_sql(
        "SELECT * FROM complaints",
        conn
    )

    conn.close()

    if df.empty:

        return pd.DataFrame()

    intelligence = []

    for _, row in df.iterrows():

        risk = row.get(
            "risk_score",
            0
        )

        confidence = min(
            100,
            risk + 20
        )

        recommendation = (
            "Immediate Investigation"
            if confidence >= 80
            else "Monitor"
        )

        intelligence.append({

            "case_id": row["id"],
            "category": row["category"],
            "risk_score": risk,
            "confidence": confidence,
            "recommendation": recommendation

        })

    return pd.DataFrame(
        intelligence
    )