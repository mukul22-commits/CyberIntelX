import sqlite3

conn = sqlite3.connect(
    "database/users.db"
)

cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS users (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        username TEXT UNIQUE,

        password TEXT,

        role TEXT,

        full_name TEXT,

        email TEXT,

        mobile TEXT

    )
    """
)

conn.commit()

conn.close()

print(
    "Users DB Created"
)