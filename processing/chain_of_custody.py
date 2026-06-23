import sqlite3
from datetime import datetime


def log_custody(
    case_id,
    action,
    officer
):

    conn = sqlite3.connect(
        "database/chain_of_custody.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS custody_log(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            case_id INTEGER,
            action TEXT,
            officer TEXT,
            timestamp TEXT
        )
        """
    )

    cursor.execute(
        """
        INSERT INTO custody_log(
            case_id,
            action,
            officer,
            timestamp
        )
        VALUES(
            ?,?,?,?
        )
        """,
        (
            case_id,
            action,
            officer,
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        )
    )

    conn.commit()

    conn.close()