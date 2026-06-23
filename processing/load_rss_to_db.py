import pandas as pd
import sqlite3

df = pd.read_csv(
    "data/rss_feed.csv"
)

df["threat_score"] = 0
df["sentiment"] = ""

conn = sqlite3.connect(
    "database/cybercrime.db"
)

df.to_sql(
    "intelligence_data",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print(
    f"{len(df)} records inserted"
)