import sqlite3

from datetime import datetime


def start_session(
    username
):

    conn = sqlite3.connect(
        "database/session.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO sessions
        (
            username,
            login_time,
            status
        )
        VALUES
        (
            ?,
            ?,
            ?
        )
        """,
        (
            username,
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "ACTIVE"
        )
    )

    conn.commit()

    conn.close()


def end_session(
    username
):

    conn = sqlite3.connect(
        "database/session.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE sessions
        SET
            logout_time=?,
            status='CLOSED'
        WHERE
            username=?
            AND status='ACTIVE'
        """,
        (
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            username
        )
    )

    conn.commit()

    conn.close()