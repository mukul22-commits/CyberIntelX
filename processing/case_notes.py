import sqlite3


def update_notes(
    case_id,
    notes
):

    conn = sqlite3.connect(
        "database/complaints.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE complaints
        SET investigation_notes=?
        WHERE id=?
        """,
        (
            notes,
            case_id
        )
    )

    conn.commit()

    conn.close()

    return True