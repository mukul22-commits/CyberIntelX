import sqlite3
import pandas as pd


def build_incidents():

    conn = sqlite3.connect(
        "database/complaints.db"
    )

    complaints = pd.read_sql(
        "SELECT * FROM complaints",
        conn
    )

    conn.close()

    if complaints.empty:

        return pd.DataFrame()

    incidents = []

    for _, row in complaints.iterrows():

        risk = row.get(
            "risk_score",
            0
        )

        if risk >= 80:

            priority = "CRITICAL"

        elif risk >= 60:

            priority = "HIGH"

        elif risk >= 40:

            priority = "MEDIUM"

        else:

            priority = "LOW"

        recommendation = (
            "Immediate Investigation"
            if risk >= 80
            else "Monitor Activity"
        )

        incidents.append({

            "incident_id":
            f"INC-{row['id']}",

            "case_id":
            row["id"],

            "category":
            row.get(
                "category",
                "Unknown"
            ),

            "risk_score":
            risk,

            "priority":
            priority,

            "status":
            row.get(
                "status",
                "Open"
            ),

            "recommendation":
            recommendation

        })

    return pd.DataFrame(
        incidents
    )