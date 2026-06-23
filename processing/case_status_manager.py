import sqlite3


def update_case_status(
    case_id,
    status
):

    conn = sqlite3.connect(
        "database/complaints.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE complaints
        SET status=?
        WHERE id=?
        """,
        (
            status,
            case_id
        )
    )

    conn.commit()

    conn.close()

    return True