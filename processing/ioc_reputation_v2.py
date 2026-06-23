import sqlite3
import pandas as pd


def investigate_ioc(ioc_value):

    conn = sqlite3.connect(
        "database/complaints.db"
    )

    complaints = pd.read_sql(
        "SELECT * FROM complaints",
        conn
    )

    conn.close()

    matches = 0
    linked_cases = []

    for _, row in complaints.iterrows():

        description = str(
            row.get(
                "description",
                ""
            )
        )

        if str(ioc_value).lower() in description.lower():

            matches += 1

            linked_cases.append(
                row["id"]
            )

    score = matches * 25

    if matches >= 3:

        risk = "Critical"

    elif matches >= 2:

        risk = "High"

    elif matches >= 1:

        risk = "Medium"

    else:

        risk = "Low"

    if risk == "Critical":

        recommendation = (
            "Immediate Escalation"
        )

    elif risk == "High":

        recommendation = (
            "Priority Investigation"
        )

    elif risk == "Medium":

        recommendation = (
            "Monitor Closely"
        )

    else:

        recommendation = (
            "No Action Required"
        )

    return {

        "ioc": ioc_value,
        "risk": risk,
        "score": score,
        "linked_cases": linked_cases,
        "recommendation": recommendation

    }