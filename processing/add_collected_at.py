import sqlite3

conn = sqlite3.connect(
    "database/cybercrime.db"
)

cursor = conn.cursor()

try:

    cursor.execute("""
    ALTER TABLE intelligence_data
    ADD COLUMN collected_at TEXT
    """)

    print("Column Added")

except Exception as e:

    print(e)

conn.commit()
conn.close()