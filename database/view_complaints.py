import sqlite3
import pandas as pd

conn = sqlite3.connect(
    "database/complaints.db"
)

df = pd.read_sql(
    "SELECT * FROM complaints",
    conn
)

print(df)

conn.close()