import sqlite3

conn = sqlite3.connect(
    "database/cybercrime.db"
)

cursor = conn.cursor()

cursor.execute("""
UPDATE intelligence_data
SET source='The Hacker News'
WHERE source='https://feeds.feedburner.com/TheHackersNews'
""")

cursor.execute("""
UPDATE intelligence_data
SET source='Bleeping Computer'
WHERE source='https://www.bleepingcomputer.com/feed/'
""")

conn.commit()
conn.close()

print("Source Names Normalized")