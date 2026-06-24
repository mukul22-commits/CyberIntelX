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

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    status TEXT DEFAULT 'Pending',

    officer_name TEXT,

    priority TEXT,

    investigation_notes TEXT,

    victim_username TEXT,

    assigned_username TEXT

)
""")

conn.commit()

conn.close()

print(
    "Complaints Database Ready"
)