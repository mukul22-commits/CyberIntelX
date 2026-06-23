import sqlite3

conn = sqlite3.connect(
    "database/complaints.db"
)

cursor = conn.cursor()

try:

    cursor.execute("""
    ALTER TABLE complaints
    ADD COLUMN status TEXT
    DEFAULT 'Pending'
    """)

    print("Status Column Added")

except:

    print("Already Exists")

conn.commit()
conn.close()