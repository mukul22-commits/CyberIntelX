import sqlite3
import pandas as pd


def build_trend():

    conn = sqlite3.connect(
        "database/cybercrime.db"
    )

    df = pd.read_sql(
        """
        SELECT
            source,
            COUNT(*) as count
        FROM intelligence_data
        GROUP BY source
        """,
        conn
    )

    conn.close()

    return df.sort_values(
        "count",
        ascending=False
    )