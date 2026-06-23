import feedparser
import sqlite3


feeds = {

    "BleepingComputer":
    "https://www.bleepingcomputer.com/feed/",

    "The Hacker News":
    "https://feeds.feedburner.com/TheHackersNews",

    "CISA":
    "https://www.cisa.gov/news.xml"
}


conn = sqlite3.connect(
    "database/threat_monitoring.db"
)

cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS threat_feed(
        source TEXT,
        title TEXT,
        link TEXT
    )
    """
)

for source, url in feeds.items():

    feed = feedparser.parse(url)

    for entry in feed.entries[:20]:

        cursor.execute(
            """
            INSERT INTO threat_feed
            VALUES(?,?,?)
            """,
            (
                source,
                entry.title,
                entry.link
            )
        )

conn.commit()
conn.close()

print(
    "Threat Feed Updated"
)