import sqlite3

conn = sqlite3.connect(
    "database/complaints.db"
)

cursor = conn.cursor()

try:

    cursor.execute(
        """
        ALTER TABLE complaints
        ADD COLUMN assigned_username TEXT
        """
    )

    conn.commit()

    print(
        "assigned_username column added"
    )

except Exception as e:

    print(e)

conn.close()