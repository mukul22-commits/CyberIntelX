import sqlite3
import pandas as pd

from entity_extractor import extract_entities

conn = sqlite3.connect(
    "database/cybercrime.db"
)

df = pd.read_sql(
    "SELECT title FROM intelligence_data",
    conn
)

all_entities = []

allowed_labels = [
    "ORG",
    "GPE",
    "PRODUCT"
]

for title in df["title"]:

    entities = extract_entities(
        str(title)
    )

    for e in entities:

        if e["label"] in allowed_labels:

            all_entities.append(
                [
                    e["text"],
                    e["label"]
                ]
            )

entity_df = pd.DataFrame(
    all_entities,
    columns=[
        "entity",
        "type"
    ]
)

entity_df.to_csv(
    "data/entities.csv",
    index=False
)

print(
    f"Extracted {len(entity_df)} entities"
)

conn.close()