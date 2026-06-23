import sqlite3
import pandas as pd

from processing.alert_engine import (
    generate_alerts
)


def calculate_national_threat():

    score = 0

    # ------------------
    # Complaints
    # ------------------

    conn = sqlite3.connect(
        "database/complaints.db"
    )

    complaints = pd.read_sql(
        "SELECT * FROM complaints",
        conn
    )

    conn.close()

    total_cases = len(
        complaints
    )

    score += min(
        total_cases,
        20
    )

    # ------------------
    # High Risk Cases
    # ------------------

    if "risk_score" in complaints.columns:

        high_risk = len(

            complaints[
                complaints["risk_score"] >= 70
            ]

        )

        score += min(
            high_risk * 2,
            20
        )

    # ------------------
    # Threat Intelligence
    # ------------------

    conn = sqlite3.connect(
        "database/cybercrime.db"
    )

    intel = pd.read_sql(
        "SELECT * FROM intelligence_data",
        conn
    )

    conn.close()

    score += min(
        len(intel) // 10,
        20
    )

    # ------------------
    # Source Diversity
    # ------------------

    sources = len(
        intel["source"].unique()
    )

    score += min(
        sources * 2,
        10
    )

    # ------------------
    # Critical CVEs
    # ------------------

    cves = intel[
        intel["source"] == "NVD-CVE"
    ]

    score += min(
        len(cves),
        15
    )

    # ------------------
    # Active Alerts
    # ------------------

    alerts = generate_alerts()

    score += min(
        len(alerts),
        15
    )

    # ------------------
    # Final Score
    # ------------------

    score = min(
        score,
        100
    )

    if score >= 80:

        level = "CRITICAL"

    elif score >= 60:

        level = "HIGH"

    elif score >= 40:

        level = "ELEVATED"

    else:

        level = "GUARDED"

    return {

        "score": score,
        "level": level,

        "complaints": total_cases,

        "high_risk_cases":
        high_risk if "risk_score"
        in complaints.columns else 0,

        "sources": sources,

        "cves": len(cves),

        "alerts": len(alerts)

    }