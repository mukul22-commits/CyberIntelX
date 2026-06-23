import sqlite3


def assign_case(
    complaint_id,
    officer_name,
    username
):

    conn = sqlite3.connect(
        "database/complaints.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE complaints
        SET
            officer_name=?,
            assigned_username=?
        WHERE id=?
        """,
        (
            officer_name,
            username,
            complaint_id
        )
    )

    conn.commit()

    conn.close()

    return True