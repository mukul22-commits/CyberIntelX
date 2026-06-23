import sqlite3
import pandas as pd
import re


def build_threat_actors():

    conn = sqlite3.connect(
        "database/complaints.db"
    )

    complaints = pd.read_sql(
        "SELECT * FROM complaints",
        conn
    )

    conn.close()

    actors = []

    for _, row in complaints.iterrows():

        description = str(
            row["description"]
        )

        emails = re.findall(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            description
        )

        urls = re.findall(
            r"https?://[^\s]+",
            description
        )

        upis = re.findall(
            r"\b[\w\.-]+@[a-zA-Z]+\b",
            description
        )

        actors.append(
            {
                "case_id": row["id"],
                "emails": ", ".join(emails),
                "urls": ", ".join(urls),
                "upis": ", ".join(upis),
                "risk_score": row["risk_score"]
            }
        )

    return pd.DataFrame(actors)