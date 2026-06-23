import sqlite3

conn = sqlite3.connect(
    "database/complaints.db"
)

cursor = conn.cursor()

try:

    cursor.execute(
        """
        ALTER TABLE complaints
        ADD COLUMN victim_username TEXT
        """
    )

    conn.commit()

    print(
        "victim_username column added"
    )

except Exception as e:

    print(
        "Already exists"
    )

conn.close()