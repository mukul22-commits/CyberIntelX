import sqlite3
import pandas as pd


def forecast_threats():

    conn = sqlite3.connect(
        "database/cybercrime.db"
    )

    df = pd.read_sql(
        """
        SELECT source,
               COUNT(*) as incidents
        FROM intelligence_data
        GROUP BY source
        """,
        conn
    )

    conn.close()

    if df.empty:

        return pd.DataFrame()

    df["forecast_next_week"] = (
        df["incidents"] * 1.15
    ).round().astype(int)

    return df.sort_values(
        "forecast_next_week",
        ascending=False
    )