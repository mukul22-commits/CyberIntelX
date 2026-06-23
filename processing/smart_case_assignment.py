import sqlite3
import pandas as pd


def recommend_assignment():

    conn = sqlite3.connect(
        "database/complaints.db"
    )

    df = pd.read_sql(
        "SELECT * FROM complaints",
        conn
    )

    conn.close()

    recommendations = []

    for _, row in df.iterrows():

        risk = row["risk_score"]

        if risk >= 80:

            team = "Senior Investigation Unit"

        elif risk >= 60:

            team = "Fraud Investigation Unit"

        else:

            team = "General Investigation Unit"

        recommendations.append({

            "case_id": row["id"],
            "risk_score": risk,
            "recommended_team": team

        })

    return pd.DataFrame(
        recommendations
    )