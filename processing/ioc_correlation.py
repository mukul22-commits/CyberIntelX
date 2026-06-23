import sqlite3
import pandas as pd


def correlate_iocs():

    conn = sqlite3.connect(
        "database/complaints.db"
    )

    df = pd.read_sql(
        """
        SELECT
            id,
            email,
            phone,
            description
        FROM complaints
        """,
        conn
    )

    conn.close()

    correlations = []

    for i in range(len(df)):

        for j in range(i + 1, len(df)):

            case1 = df.iloc[i]
            case2 = df.iloc[j]

            if (
                case1["email"]
                and
                case1["email"]
                == case2["email"]
            ):

                correlations.append({

                    "Case A":
                    case1["id"],

                    "Case B":
                    case2["id"],

                    "Indicator":
                    case1["email"],

                    "Type":
                    "Email"

                })

            if (
                case1["phone"]
                and
                case1["phone"]
                == case2["phone"]
            ):

                correlations.append({

                    "Case A":
                    case1["id"],

                    "Case B":
                    case2["id"],

                    "Indicator":
                    case1["phone"],

                    "Type":
                    "Phone"

                })

    return pd.DataFrame(
        correlations
    )