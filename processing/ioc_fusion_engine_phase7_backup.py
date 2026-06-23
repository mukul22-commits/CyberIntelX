import sqlite3
import pandas as pd
import re


def extract_iocs(text):

    text = str(text).lower()

    emails = re.findall(
        r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",
        text
    )

    urls = re.findall(
        r"https?://[^\s]+",
        text
    )

    ips = re.findall(
        r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
        text
    )

    domains = re.findall(
        r"\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b",
        text
    )

    return set(
        emails + urls + ips + domains
    )


def build_ioc_fusion():

    conn1 = sqlite3.connect(
        "database/complaints.db"
    )

    conn2 = sqlite3.connect(
        "database/cybercrime.db"
    )

    complaints = pd.read_sql(
        "SELECT * FROM complaints",
        conn1
    )

    threats = pd.read_sql(
        "SELECT * FROM intelligence_data",
        conn2
    )

    conn1.close()
    conn2.close()

    complaint_iocs = set()

    for _, row in complaints.iterrows():

        complaint_iocs.update(
            extract_iocs(
                row.get(
                    "description",
                    ""
                )
            )
        )

    results = []

    for _, row in threats.iterrows():

        threat_iocs = extract_iocs(
            row.get(
                "title",
                ""
            )
        )

        matches = complaint_iocs.intersection(
            threat_iocs
        )

        for match in matches:

            results.append({

                "ioc": match,
                "source": row["source"],
                "title": row["title"]

            })

    return pd.DataFrame(
        results
    )