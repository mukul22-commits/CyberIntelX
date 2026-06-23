import sqlite3
import pandas as pd
import re


def extract_iocs(text):

    text = str(text).lower()

    emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)

    urls = re.findall(r"https?://[^\s]+", text)

    phones = re.findall(r"\b\d{10}\b", text)

    return emails, urls, phones


def correlate_intelligence():

    conn1 = sqlite3.connect("database/complaints.db")
    conn2 = sqlite3.connect("database/cybercrime.db")

    complaints = pd.read_sql("SELECT * FROM complaints", conn1)
    threats = pd.read_sql("SELECT * FROM intelligence_data", conn2)

    conn1.close()
    conn2.close()

    results = []

    for _, c in complaints.iterrows():

        c_text = str(c.get("description", "")).lower()

        c_emails, c_urls, c_phones = extract_iocs(c_text)

        for _, t in threats.iterrows():

            t_text = str(t.get("title", "")).lower()

            t_emails, t_urls, t_phones = extract_iocs(t_text)

            # EMAIL MATCH
            for e in c_emails:
                if any(e in x for x in t_emails):
                    results.append({
                        "case_id": c["id"],
                        "ioc_type": "EMAIL",
                        "ioc": e,
                        "threat_source": t["source"],
                        "threat_title": t["title"]
                    })

            # URL MATCH
            for u in c_urls:
                if any(u in x for x in t_urls):
                    results.append({
                        "case_id": c["id"],
                        "ioc_type": "URL",
                        "ioc": u,
                        "threat_source": t["source"],
                        "threat_title": t["title"]
                    })

            # PHONE MATCH
            for p in c_phones:
                if p in t_text:
                    results.append({
                        "case_id": c["id"],
                        "ioc_type": "PHONE",
                        "ioc": p,
                        "threat_source": t["source"],
                        "threat_title": t["title"]
                    })

    return pd.DataFrame(results)