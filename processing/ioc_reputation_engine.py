import sqlite3
import pandas as pd
import re
from collections import defaultdict


def extract_iocs(text):

    text = str(text).lower()

    emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
    urls = re.findall(r"https?://[^\s]+", text)
    phones = re.findall(r"\b\d{10}\b", text)

    return emails + urls + phones


def calculate_reputation():

    conn = sqlite3.connect("database/cybercrime.db")

    df = pd.read_sql(
        "SELECT source, title FROM intelligence_data",
        conn
    )

    conn.close()

    ioc_map = defaultdict(lambda: {
        "count": 0,
        "sources": set(),
        "titles": []
    })

    # STEP 1: Extract IOC from threat feed
    for _, row in df.iterrows():

        text = str(row["title"]).lower()
        iocs = extract_iocs(text)

        for ioc in iocs:

            ioc_map[ioc]["count"] += 1
            ioc_map[ioc]["sources"].add(row["source"])
            ioc_map[ioc]["titles"].append(row["title"])

    # STEP 2: Build reputation score
    results = []

    for ioc, data in ioc_map.items():

        count = data["count"]
        source_count = len(data["sources"])

        score = min(100, (count * 10) + (source_count * 15))

        if score >= 80:
            risk = "CRITICAL"
        elif score >= 60:
            risk = "HIGH"
        elif score >= 30:
            risk = "MEDIUM"
        else:
            risk = "LOW"

        results.append({

            "ioc": ioc,
            "occurrences": count,
            "sources": source_count,
            "reputation_score": score,
            "risk_level": risk

        })

    return pd.DataFrame(results)