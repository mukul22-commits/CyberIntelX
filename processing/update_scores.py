import sqlite3
import pandas as pd

from threat_score import calculate_score

conn = sqlite3.connect(
    "database/cybercrime.db"
)

df = pd.read_sql(
    "SELECT * FROM intelligence_data",
    conn
)

# Convert existing values safely
df["threat_score"] = (
    pd.to_numeric(
        df["threat_score"],
        errors="coerce"
    )
    .fillna(0)
    .astype(int)
)

for index, row in df.iterrows():

    score = calculate_score(
        str(row["title"])
    )

    df.loc[
        index,
        "threat_score"
    ] = score

df.to_sql(
    "intelligence_data",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print(
    "Threat scores updated"
)