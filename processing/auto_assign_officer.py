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

    risk_score = int(row[0])

    if risk_score >= 80:

        assigned_username = "rahulkumar_101"
        officer_name = "Rahul Kumar"
        priority = "Critical"

    elif risk_score >= 60:

        assigned_username = "rahulkumar_101"
        officer_name = "Rahul Kumar"
        priority = "High"

    elif risk_score >= 40:

        assigned_username = "amitsharma_102"
        officer_name = "Amit Sharma"
        priority = "Medium"

    else:

        assigned_username = "amitsharma_102"
        officer_name = "Amit Sharma"
        priority = "Low"

    cursor.execute(
        """
        UPDATE complaints
        SET
            assigned_username=?,
            officer_name=?,
            priority=?,
            status='Assigned'
        WHERE id=?
        """,
        (
            assigned_username,
            officer_name,
            priority,
            case_id
        )
    )

    conn.commit()
    conn.close()

    return {
        "assigned_username": assigned_username,
        "officer_name": officer_name,
        "priority": priority
    }