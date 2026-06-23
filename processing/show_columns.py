import sqlite3

conn = sqlite3.connect(
    "database/cybercrime.db"
)

cursor = conn.cursor()

cursor.execute(
    "PRAGMA table_info(intelligence_data)"
)

for row in cursor.fetchall():
    print(row)

conn.close()