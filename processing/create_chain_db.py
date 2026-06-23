import sqlite3

conn = sqlite3.connect(
    "database/chain_of_custody.db"
)

cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS custody(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        complaint_id INTEGER,
        evidence_file TEXT,
        sha256_hash TEXT,
        collected_by TEXT,
        verified_by TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """
)

conn.commit()
conn.close()

print(
    "Chain Of Custody DB Created"
)