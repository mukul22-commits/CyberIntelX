import sqlite3
import pandas as pd


def build_incident_intelligence():

    conn = sqlite3.connect(
        "database/complaints.db"
    )

    df = pd.read_sql(
        "SELECT * FROM complaints",
        conn
    )

    conn.close()

    results = []

    for _, row in df.iterrows():

        risk = row.get(
            "risk_score",
            0
        )

        try:
            risk = float(risk)
        except:
            risk = 0

        if risk >= 80:

            priority = "Critical"

            action = (
                "Immediate Escalation"
            )

        elif risk >= 60:

            priority = "High"

            action = (
                "Priority Investigation"
            )

        elif risk >= 40:

            priority = "Medium"

            action = (
                "Investigate"
            )

        else:

            priority = "Low"

            action = (
                "Monitor"
            )

        results.append({

            "case_id":
            row["id"],

            "risk_score":
            risk,

            "priority":
            priority,

            "recommended_action":
            action

        })

    return pd.DataFrame(
        results
    )