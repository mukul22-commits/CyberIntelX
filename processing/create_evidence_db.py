import sqlite3

conn = sqlite3.connect(
    "database/evidence.db"
)

cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS evidence(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        case_id INTEGER,

        filename TEXT,

        sha256_hash TEXT

    )
    """
)

conn.commit()

conn.close()

print(
    "Evidence DB Created"
)