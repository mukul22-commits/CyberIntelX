import sqlite3

from processing.auth_manager import (
    hash_password
)
conn = sqlite3.connect(
    "database/users.db"
)

cursor = conn.cursor()

password = hash_password(
    "Admin123"
)

cursor.execute(
    """
    INSERT OR IGNORE INTO users
    (
        username,
        password,
        role
    )
    VALUES
    (
        ?,
        ?,
        ?
    )
    """,
    (
        "admin",
        password,
        "Admin"
    )
)

conn.commit()

conn.close()

print(
    "Admin Created"
)