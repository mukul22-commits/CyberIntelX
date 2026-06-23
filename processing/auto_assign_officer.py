import sqlite3


def auto_assign_officer(case_id):

    conn = sqlite3.connect(
        "database/complaints.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT risk_score
        FROM complaints
        WHERE id=?
        """,
        (case_id,)
    )

    row = cursor.fetchone()

    if not row:

        conn.close()

        return None

    risk_score = row[0]

    if risk_score >= 80:

        assigned_username = (
            "rahulkumar_101"
        )

        officer_name = (
            "Rahul Kumar"
        )

    elif risk_score >= 50:

        assigned_username = (
            "amitsharma_102"
        )

        officer_name = (
            "Amit Sharma"
        )

    else:

        assigned_username = (
            "amitsharma_102"
        )

        officer_name = (
            "Amit Sharma"
        )

    cursor.execute(
        """
        UPDATE complaints
        SET
            assigned_username=?,
            officer_name=?
        WHERE id=?
        """,
        (
            assigned_username,
            officer_name,
            case_id
        )
    )

    conn.commit()

    conn.close()

    return {
        "officer_name":
        officer_name,

        "assigned_username":
        assigned_username
    }