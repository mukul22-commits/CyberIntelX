import sqlite3

conn = sqlite3.connect(
    "database/complaints.db"
)

cursor = conn.cursor()

try:

    cursor.execute("""
    ALTER TABLE complaints
    ADD COLUMN officer_name TEXT
    """)

except:
    pass

try:

    cursor.execute("""
    ALTER TABLE complaints
    ADD COLUMN priority TEXT
    """)

except:
    pass

try:

    cursor.execute("""
    ALTER TABLE complaints
    ADD COLUMN investigation_notes TEXT
    """)

except:
    pass

conn.commit()
conn.close()

print("Case fields added")