import sqlite3

conn = sqlite3.connect(
    "database/cybercrime.db"
)

cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS intelligence_data (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        source TEXT,

        title TEXT,

        link TEXT,

        sentiment TEXT,

        threat_score INTEGER

    )
    """
)

conn.commit()

conn.close()

print(
    "Database Created Successfully"
)