import sqlite3


def feed_health():

    conn = sqlite3.connect(
        "database/cybercrime.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT source,
               COUNT(*)
        FROM intelligence_data
        GROUP BY source
        """
    )

    data = cursor.fetchall()

    print(
        "\n=== FEED HEALTH STATUS ===\n"
    )

    for source, count in data:

        if count < 10:

            status = "LOW DATA"

        elif count < 50:

            status = "STABLE"

        else:

            status = "ACTIVE"

        print(
            f"{source}: {count} → {status}"
        )

    conn.close()


if __name__ == "__main__":

    feed_health()