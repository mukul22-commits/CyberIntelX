import sqlite3

conn = sqlite3.connect(
    "database/timeline.db"
)

cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS timeline(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        complaint_id INTEGER,
        action TEXT,
        username TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """
)

conn.commit()
conn.close()

print(
    "Timeline DB Created"
)