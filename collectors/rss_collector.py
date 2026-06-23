import feedparser
import sqlite3
from datetime import datetime

feeds = [
    (
        "The Hacker News",
        "https://feeds.feedburner.com/TheHackersNews"
    ),
    (
        "Bleeping Computer",
        "https://www.bleepingcomputer.com/feed/"
    )
]

conn = sqlite3.connect(
    "database/cybercrime.db"
)

cursor = conn.cursor()

added = 0

for source_name, url in feeds:

    feed = feedparser.parse(url)

    for entry in feed.entries[:20]:

        try:

            cursor.execute(
                """
                INSERT OR IGNORE INTO intelligence_data(
                    source,
                    title,
                    link,
                    threat_score,
                    sentiment,
                    collected_at
                )
                VALUES(?,?,?,?,?,?)
                """,
                (
                    source_name,
                    entry.title,
                    entry.link,
                    0,
                    "Neutral",
                    datetime.now().strftime(
                        "%Y-%m-%d %H:%M:%S"
                    )
                )
            )

            if cursor.rowcount > 0:
                added += 1

        except Exception as e:

            with open(
                "logs/feed_errors.log",
                "a"
            ) as log:

                log.write(
                    f"RSS Error: {e}\n"
                )

conn.commit()
conn.close()

print(
    f"RSS Added: {added}"
)