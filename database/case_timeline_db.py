import sqlite3

conn = sqlite3.connect(
    "database/complaints.db"
)

cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS case_timeline(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        complaint_id INTEGER,

        action TEXT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """
)

conn.commit()
conn.close()

print(
    "Timeline Table Ready"
)