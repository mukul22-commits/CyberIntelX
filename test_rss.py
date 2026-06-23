import feedparser

feed = feedparser.parse(
    "https://feeds.feedburner.com/TheHackersNews"
)

print("Entries:", len(feed.entries))

for item in feed.entries[:5]:
    print(item.title)