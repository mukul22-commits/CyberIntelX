import sqlite3
import pandas as pd

conn = sqlite3.connect(
    "database/cybercrime.db"
)

df = pd.read_sql(
    """
    SELECT title,
           sentiment,
           threat_score
    FROM intelligence_data
    LIMIT 20
    """,
    conn
)

print(df)

conn.close()