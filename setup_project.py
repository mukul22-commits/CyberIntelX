import os

os.makedirs("logs", exist_ok=True)
os.makedirs("data", exist_ok=True)
os.makedirs("reports", exist_ok=True)

import processing.create_users_db
import processing.create_admin

import processing.create_audit_db
import processing.create_session_db

import processing.create_chain_db
import processing.create_evidence_db
import processing.create_timeline_db

import database.complaints_db
import database.officers_db
import database.init_db

print(
    "CyberIntelX Initialized Successfully"
)