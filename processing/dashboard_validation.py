import sqlite3
import pandas as pd


def validate_dashboard():

    try:

        conn = sqlite3.connect(
            "database/cybercrime.db"
        )

        df = pd.read_sql(
            "SELECT * FROM intelligence_data",
            conn
        )

        print(
            "\n=== DASHBOARD VALIDATION ===\n"
        )

        print(
            "Total Records:",
            len(df)
        )

        print(
            "Columns:",
            list(df.columns)
        )

        if "threat_score" in df.columns:

            print(
                "High Risk Articles:",
                len(
                    df[
                        df["threat_score"] >= 30
                    ]
                )
            )

            print(
                "Average Threat Score:",
                round(
                    df["threat_score"].mean(),
                    2
                )
            )

        if "sentiment" in df.columns:

            print(
                "\nSentiment Distribution:"
            )

            print(
                df[
                    "sentiment"
                ].value_counts()
            )

        conn.close()

        print(
            "\nValidation Successful"
        )

    except Exception as e:

        print(
            f"\nValidation Failed: {e}"
        )


if __name__ == "__main__":

    validate_dashboard()