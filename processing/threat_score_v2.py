import sqlite3
import pandas as pd


def calculate_threat_scores():

    conn = sqlite3.connect(
        "database/cybercrime.db"
    )

    df = pd.read_sql(
        "SELECT * FROM intelligence_data",
        conn
    )

    conn.close()

    if df.empty:
        return df

    scores = []

    for _, row in df.iterrows():

        score = 0

        title = str(
            row.get(
                "title",
                ""
            )
        ).lower()

        source = str(
            row.get(
                "source",
                ""
            )
        )

        if "malware" in title:
            score += 20

        if "ransomware" in title:
            score += 30

        if "phishing" in title:
            score += 25

        if "data breach" in title:
            score += 30

        if source == "CISA":
            score += 20

        if source == "NVD-CVE":
            score += 15

        if score >= 70:
            risk = "Critical"

        elif score >= 50:
            risk = "High"

        elif score >= 25:
            risk = "Medium"

        else:
            risk = "Low"

        scores.append({

            "title": row["title"],
            "source": source,
            "score": score,
            "risk": risk

        })

    return pd.DataFrame(scores)