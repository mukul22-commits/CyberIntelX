import sqlite3
import pandas as pd


def generate_alerts():

    alerts = []

    # =====================================
    # COMPLAINT ALERTS
    # =====================================

    conn = sqlite3.connect(
        "database/complaints.db"
    )

    complaints = pd.read_sql(
        "SELECT * FROM complaints",
        conn
    )

    conn.close()

    if (
        not complaints.empty
        and "risk_score" in complaints.columns
    ):

        for _, row in complaints.iterrows():

            if row["risk_score"] >= 80:

                alerts.append({

                    "type": "High Risk Complaint",

                    "severity": "Critical",

                    "details":
                    f"Case {row['id']} | "
                    f"{row['category']} | "
                    f"Risk Score {row['risk_score']}"

                })

    # =====================================
    # THREAT INTELLIGENCE ALERTS
    # =====================================

    conn = sqlite3.connect(
        "database/cybercrime.db"
    )

    intel = pd.read_sql(
        "SELECT * FROM intelligence_data",
        conn
    )

    conn.close()

    keywords = [

        "critical",
        "ransomware",
        "exploit",
        "cve",
        "phishing",
        "malware",
        "fraud",
        "botnet",
        "credential",
        "breach"

    ]

    for _, row in intel.tail(50).iterrows():

        title = str(
            row["title"]
        ).lower()

        if any(
            keyword in title
            for keyword in keywords
        ):

            alerts.append({

                "type":
                "Threat Intelligence",

                "severity":
                "High",

                "details":
                row["title"]

            })

    # =====================================
    # RETURN DATAFRAME
    # =====================================

    return pd.DataFrame(
        alerts
    )