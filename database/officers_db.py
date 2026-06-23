import sqlite3

conn = sqlite3.connect(
    "database/officers.db" 
)

cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS officers(

        officer_id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT,

        rank TEXT,

        department TEXT,

        phone TEXT,

        email TEXT,

        specialization TEXT,

        status TEXT
    )
    """
)

conn.commit()
conn.close()

print(
    "Officer Database Ready"
)