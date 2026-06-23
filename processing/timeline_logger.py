import sqlite3


def log_action(
    complaint_id,
    action
):

    conn = sqlite3.connect(
        "database/complaints.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO case_timeline(
        complaint_id,
        action
        )
        VALUES(
        ?,?
        )
        """,
        (
            complaint_id,
            action
        )
    )

    conn.commit()
    conn.close()