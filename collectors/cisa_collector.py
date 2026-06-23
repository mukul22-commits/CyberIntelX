import feedparser
import sqlite3

feed = feedparser.parse(
    "https://www.cisa.gov/news.xml"
)

conn = sqlite3.connect(
    "database/cybercrime.db"
)

cursor = conn.cursor()

added = 0

for entry in feed.entries:

    try:

        cursor.execute(
            "SELECT 1 FROM intelligence_data WHERE link=?",
            (entry.link,)
        )

        if cursor.fetchone():
            continue

        cursor.execute(
            """
            INSERT INTO intelligence_data(
                source,
                title,
                link,
                threat_score,
                sentiment
            )
            VALUES(?,?,?,?,?)
            """,
            (
                "CISA",
                entry.title,
                entry.link,
                80,
                "Negative"
            )
        )

        added += 1

    except Exception as e:

        print(e)

conn.commit()
conn.close()

print(f"CISA Added: {added}")