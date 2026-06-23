from processing.evidence_hash import (
    generate_hash
)


def verify_evidence(
    filepath,
    original_hash
):

    current_hash = generate_hash(
        filepath
    )

    if current_hash == original_hash:

        return {

            "status": "VALID",

            "tampered": False

        }

    return {

        "status": "TAMPERED",

        "tampered": True

    }