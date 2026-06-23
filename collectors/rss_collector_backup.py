import feedparser
import sqlite3

feeds = [
    ("The Hacker News", "https://feeds.feedburner.com/TheHackersNews"),
    ("Bleeping Computer", "https://www.bleepingcomputer.com/feed/")
]

conn = sqlite3.connect(
    "database/cybercrime.db"
)

cursor = conn.cursor()

for source_name, url in feeds:

    feed = feedparser.parse(url)

    for entry in feed.entries[:20]:

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
                source_name,
                entry.title,
                entry.link,
                0,
                "Neutral"
            )
        )

conn.commit()
conn.close()

print("Feed Updated Successfully")