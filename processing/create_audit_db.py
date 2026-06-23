import sqlite3

conn = sqlite3.connect(
    "database/audit.db"
)

cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS audit_logs(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        timestamp TEXT,

        username TEXT,

        action TEXT,

        details TEXT

    )
    """
)

conn.commit()

conn.close()

print(
    "Audit DB Created"
)