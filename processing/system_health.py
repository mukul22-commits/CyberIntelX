import os
import sqlite3
import pandas as pd


def system_health():

    status = []

    status.append({

        "component": "complaints.db",
        "status":
        os.path.exists(
            "database/complaints.db"
        )

    })

    status.append({

        "component": "cybercrime.db",
        "status":
        os.path.exists(
            "database/cybercrime.db"
        )

    })

    try:

        conn = sqlite3.connect(
            "database/cybercrime.db"
        )

        count = pd.read_sql(
            "SELECT COUNT(*) c FROM intelligence_data",
            conn
        )

        conn.close()

        status.append({

            "component": "Threat Feed",
            "status":
            count["c"][0] > 0

        })

    except:

        status.append({

            "component": "Threat Feed",
            "status": False

        })

    return pd.DataFrame(status)