import sqlite3
import pandas as pd


def generate_intelligence_report():

    conn = sqlite3.connect(
        "database/complaints.db"
    )

    complaints = pd.read_sql(
        "SELECT * FROM complaints",
        conn
    )

    conn.close()

    report = f"""

Total Complaints:
{len(complaints)}

High Risk Cases:
{len(
complaints[
complaints["risk_score"] >= 70
]
)}

Categories:

{
complaints["category"]
.value_counts()
.to_string()
}
"""

    return report