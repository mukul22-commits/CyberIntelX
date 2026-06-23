import sqlite3
import pandas as pd
import re


def resolve_entities():

    conn = sqlite3.connect(
        "database/complaints.db"
    )

    complaints = pd.read_sql(
        "SELECT * FROM complaints",
        conn
    )

    conn.close()

    entities = {}

    for _, row in complaints.iterrows():

        description = str(
            row["description"]
        )

        emails = re.findall(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            description
        )

        upis = re.findall(
            r"\b[\w\.-]+@[a-zA-Z]+\b",
            description
        )

        values = emails + upis

        for value in values:

            if value not in entities:

                entities[value] = []

            entities[value].append(
                row["id"]
            )

    results = []

    for entity, cases in entities.items():

        results.append(
            {
                "entity": entity,
                "linked_cases": len(cases),
                "case_ids": ",".join(
                    map(str, cases)
                )
            }
        )

    return pd.DataFrame(results)