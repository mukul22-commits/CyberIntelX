import sqlite3

conn = sqlite3.connect(
    "database/complaints.db"
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS complaints (

id INTEGER PRIMARY KEY AUTOINCREMENT,

name TEXT,
email TEXT,
phone TEXT,
state TEXT,

category TEXT,

description TEXT,

evidence_file TEXT,

risk_score INTEGER,

created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

)
""")

conn.commit()

conn.close()

print("Complaints Database Ready")