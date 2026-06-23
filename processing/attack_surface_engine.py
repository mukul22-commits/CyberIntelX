import sqlite3
import pandas as pd


def analyze_attack_surface():

    conn = sqlite3.connect(
        "database/complaints.db"
    )

    df = pd.read_sql(
        "SELECT category,risk_score FROM complaints",
        conn
    )

    conn.close()

    if df.empty:

        return pd.DataFrame()

    attack_surface = (
        df.groupby("category")
        .agg(
            cases=("category", "count"),
            avg_risk=("risk_score", "mean")
        )
        .reset_index()
    )

    attack_surface["exposure_score"] = (
        attack_surface["cases"]
        * attack_surface["avg_risk"]
    ).round(2)

    return attack_surface.sort_values(
        "exposure_score",
        ascending=False
    )