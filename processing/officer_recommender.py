import sqlite3
import pandas as pd


def recommend_officer(category):

    mapping = {
        "UPI Fraud": "Financial Fraud",
        "Investment Scam": "Financial Fraud",
        "Phishing": "Phishing",
        "Identity Theft": "Digital Forensics",
        "Cyber Bullying": "Cyber Crime",
        "Other": "Cyber Crime"
    }

    specialization = mapping.get(
        category,
        "Cyber Crime"
    )

    conn = sqlite3.connect(
        "database/officers.db" 
    )

    query = f"""
    SELECT *
    FROM officers
    WHERE specialization='{specialization}'
    """

    officers = pd.read_sql(
        query,
        conn
    )

    conn.close()

    if len(officers) == 0:
        return None

    return officers.iloc[0]["name"]