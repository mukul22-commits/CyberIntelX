import sqlite3
import pandas as pd

from sentiment_analysis import (
    get_sentiment
)

conn = sqlite3.connect(
    "database/cybercrime.db"
)

df = pd.read_sql(
    "SELECT * FROM intelligence_data",
    conn
)

if "sentiment" not in df.columns:
    df["sentiment"] = ""

for index, row in df.iterrows():

    sentiment = get_sentiment(
        str(row["title"])
    )

    df.loc[
        index,
        "sentiment"
    ] = sentiment

df.to_sql(
    "intelligence_data",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print(
    "Sentiment Updated"
)