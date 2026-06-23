import sqlite3
import pandas as pd


def executive_summary():

    conn = sqlite3.connect(
        "database/cybercrime.db"
    )

    df = pd.read_sql(
        "SELECT * FROM intelligence_data",
        conn
    )

    conn.close()

    if len(df) == 0:

        return {

            "articles": 0,
            "critical": 0,
            "avg_score": 0.0

        }

    return {

        "articles": int(
            len(df)
        ),

        "critical": int(
            len(
                df[
                    df["threat_score"] >= 80
                ]
            )
        ),

        "avg_score": float(
            round(
                df["threat_score"].mean(),
                2
            )
        )
    }