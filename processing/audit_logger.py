import sqlite3
from datetime import datetime


def log_action(
    username,
    action,
    details=""
):

    conn = sqlite3.connect(
        "database/audit.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO audit_logs
        (
            timestamp,
            username,
            action,
            details
        )
        VALUES
        (
            ?,
            ?,
            ?,
            ?
        )
        """,
        (
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            username,
            action,
            details
        )
    )

    conn.commit()

    conn.close()