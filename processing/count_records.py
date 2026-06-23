import sqlite3

conn = sqlite3.connect(
    "database/cybercrime.db"
)

cursor = conn.cursor()

cursor.execute(
    "SELECT COUNT(*) FROM intelligence_data"
)

print(
    "Total Records:",
    cursor.fetchone()[0]
)

conn.close()