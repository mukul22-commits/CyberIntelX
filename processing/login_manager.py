import sqlite3

from processing.auth_manager import (
    verify_password
)

from processing.audit_logger import (
    log_action
)

from processing.session_manager import (
    start_session
)


def login_user(
    username,
    password
):

    conn = sqlite3.connect(
        "database/users.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT password,
               role
        FROM users
        WHERE username=?
        """,
        (username,)
    )

    row = cursor.fetchone()

    conn.close()

    if not row:

        log_action(
            username,
            "Login Failed",
            "User not found"
        )

        return None

    stored_hash = row[0]

    role = row[1]

    if verify_password(
        password,
        stored_hash
    ):

        start_session(
            username
        )

        log_action(
            username,
            "Login Success",
            role
        )

        return role

    log_action(
        username,
        "Login Failed",
        "Invalid Password"
    )

    return None