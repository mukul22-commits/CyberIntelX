import pandas as pd
import sqlite3


def export_complaints():

    conn = sqlite3.connect(
        "database/complaints.db"
    )

    df = pd.read_sql(
        "SELECT * FROM complaints",
        conn
    )

    conn.close()

    filename = (
        "reports/complaints_export.csv"
    )

    df.to_csv(
        filename,
        index=False
    )

    return filename