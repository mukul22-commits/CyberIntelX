import sqlite3
from datetime import datetime


def log_timeline(
    complaint_id,
    action,
    username
):

    conn = sqlite3.connect(
        "database/timeline.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS timeline(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            complaint_id INTEGER,
            action TEXT,
            username TEXT,
            timestamp TEXT
        )
        """
    )

    cursor.execute(
        """
        INSERT INTO timeline(
            complaint_id,
            action,
            username,
            timestamp
        )
        VALUES(
            ?,?,?,?
        )
        """,
        (
            complaint_id,
            action,
            username,
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        )
    )

    conn.commit()
    conn.close()