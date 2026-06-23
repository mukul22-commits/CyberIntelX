import sqlite3

from processing.evidence_hash import (
    generate_hash
)

from processing.audit_logger import (
    log_action
)


def register_evidence(
    case_id,
    filepath
):

    file_hash = generate_hash(
        filepath
    )

    conn = sqlite3.connect(
        "database/evidence.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO evidence
        (
            case_id,
            filename,
            sha256_hash
        )
        VALUES
        (
            ?,
            ?,
            ?
        )
        """,
        (
            case_id,
            filepath,
            file_hash
        )
    )

    conn.commit()

    conn.close()

    log_action(
        "system",
        "Evidence Registered",
        filepath
    )

    return file_hash