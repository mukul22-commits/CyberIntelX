import sqlite3
import pandas as pd
import re


def generate_ai_brief(case_id):

    conn = sqlite3.connect(
        "database/complaints.db"
    )

    query = f"""
    SELECT *
    FROM complaints
    WHERE id = {case_id}
    """

    df = pd.read_sql(
        query,
        conn
    )

    conn.close()

    if len(df) == 0:

        return "Case not found."

    case = df.iloc[0]

    description = str(
        case["description"]
    )

    emails = re.findall(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        description
    )

    urls = re.findall(
        r"https?://[^\s]+",
        description
    )

    upi = re.findall(
        r"\b[\w\.-]+@[a-zA-Z]+\b",
        description
    )

    brief = f"""
CASE SUMMARY

Complaint ID: {case['id']}

Victim: {case['name']}

Category: {case['category']}

Risk Score: {case['risk_score']}

Status: {case['status']}

DETECTED IOCs

Emails:
{emails}

URLs:
{urls}

UPI IDs:
{upi}

RECOMMENDED ACTIONS

• Review linked complaints

• Preserve evidence

• Notify relevant financial institution

• Escalate if risk score > 70
"""

    return brief