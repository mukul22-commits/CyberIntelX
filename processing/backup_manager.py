import shutil
import os
from datetime import datetime


def backup_database():

    os.makedirs(
        "backup",
        exist_ok=True
    )

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    backup_file = (
        f"backup/cybercrime_{timestamp}.db"
    )

    shutil.copy(
        "database/cybercrime.db",
        backup_file
    )

    print(
        f"Backup Created: {backup_file}"
    )


if __name__ == "__main__":

    backup_database()