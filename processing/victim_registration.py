import sqlite3

from processing.auth_manager import (
    hash_password
)


def register_victim(
    username,
    password,
    full_name,
    email,
    mobile
):

    conn = sqlite3.connect(
        "database/users.db"
    )

    cursor = conn.cursor()

    try:

        cursor.execute(
            """
            INSERT INTO users
            (
                username,
                password,
                role,
                full_name,
                email,
                mobile
            )
            VALUES
            (
                ?, ?, ?, ?, ?, ?
            )
            """,
            (
                username,
                hash_password(password),
                "Victim",
                full_name,
                email,
                mobile
            )
        )

        conn.commit()

    except Exception:

        conn.close()

        return {
            "error":
            "User already exists"
        }

    conn.close()

    return {
        "success": True
    }