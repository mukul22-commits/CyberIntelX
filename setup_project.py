import os

os.makedirs("logs", exist_ok=True)
os.makedirs("data", exist_ok=True)

from processing.create_users_db import *
from processing.create_admin import *

from processing.create_audit_db import *
from processing.create_session_db import *

from processing.create_chain_db import *
from processing.create_evidence_db import *
from processing.create_timeline_db import *

import database.complaints_db
import database.officers_db
import database.init_db

print("CyberIntelX Initialized Successfully")