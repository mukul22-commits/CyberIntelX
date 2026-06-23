import sqlite3

conn = sqlite3.connect(
    "database/session.db"
)

cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS sessions(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        username TEXT,

        login_time TEXT,

        logout_time TEXT,

        status TEXT

    )
    """
)

conn.commit()

conn.close()

print(
    "Session DB Created"
)