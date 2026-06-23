import sqlite3

from processing.auth_manager import (
    hash_password
)

from processing.officer_account_generator import (
    generate_officer_credentials
)

from processing.audit_logger import (
    log_action
)


def register_officer(
    officer_name,
    case_id
):

    creds = generate_officer_credentials(
        officer_name,
        case_id
    )

    conn = sqlite3.connect(
        "database/users.db"
    )

    cursor = conn.cursor()

    hashed = hash_password(
        creds["password"]
    )

    try:

        cursor.execute(
            """
            INSERT INTO users
            (
                username,
                password,
                role
            )
            VALUES
            (
                ?,
                ?,
                ?
            )
            """,
            (
                creds["username"],
                hashed,
                "Officer"
            )
        )

        conn.commit()

        log_action(
            "admin",
            "Officer Created",
            creds["username"]
        )

    except Exception:

        conn.close()

        return {
            "error":
            "Officer already exists"
        }

    conn.close()

    return creds