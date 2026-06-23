import feedparser

feed = feedparser.parse(
    "https://nvd.nist.gov/feeds/xml/cve/misc/nvd-rss.xml"
)

print("Entries:", len(feed.entries))

if len(feed.entries) > 0:

    print(feed.entries[0].title)

else:

    print("No entries returned")