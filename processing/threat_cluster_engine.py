import sqlite3
import pandas as pd
import re


def build_clusters():

    conn = sqlite3.connect(
        "database/complaints.db"
    )

    complaints = pd.read_sql(
        "SELECT * FROM complaints",
        conn
    )

    conn.close()

    clusters = {}

    for _, row in complaints.iterrows():

        desc = str(
            row["description"]
        ).lower()

        words = re.findall(
            r"\b[a-z]{5,}\b",
            desc
        )

        for word in words:

            if word not in clusters:

                clusters[word] = []

            clusters[word].append(
                row["id"]
            )

    results = []

    cluster_id = 1

    for keyword, cases in clusters.items():

        if len(cases) >= 2:

            results.append({

                "cluster_id": cluster_id,
                "keyword": keyword,
                "related_cases": len(cases),
                "case_ids": ",".join(
                    map(str, cases)
                )

            })

            cluster_id += 1

    return pd.DataFrame(
        results
    )