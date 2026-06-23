import sqlite3
import pandas as pd

from processing.national_threat_score import (
    calculate_national_threat
)


def build_executive_report():

    threat = calculate_national_threat()

    conn = sqlite3.connect(
        "database/cybercrime.db"
    )

    intel = pd.read_sql(
        """
        SELECT source,
               COUNT(*) total
        FROM intelligence_data
        GROUP BY source
        ORDER BY total DESC
        """,
        conn
    )

    conn.close()

    return {
        "threat": threat,
        "sources": intel
    }