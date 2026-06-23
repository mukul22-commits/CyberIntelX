import sqlite3
import pandas as pd
import re

from processing.ioc_enrichment import enrich_ioc


def extract_iocs(text):

    text = str(text)

    emails = re.findall(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        text
    )

    urls = re.findall(
        r"https?://[^\s]+",
        text
    )

    ips = re.findall(
        r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
        text
    )

    domains = re.findall(
        r"\b(?:[A-Za-z0-9-]+\.)+[A-Za-z]{2,}\b",
        text
    )

    return set(
        emails + urls + ips + domains
    )


def build_ioc_fusion():

    conn1 = sqlite3.connect(
        "database/complaints.db"
    )

    conn2 = sqlite3.connect(
        "database/cybercrime.db"
    )

    complaints = pd.read_sql(
        "SELECT * FROM complaints",
        conn1
    )

    threats = pd.read_sql(
        "SELECT * FROM intelligence_data",
        conn2
    )

    conn1.close()
    conn2.close()

    complaint_counter = {}

    for _, row in complaints.iterrows():

        iocs = extract_iocs(
            row.get(
                "description",
                ""
            )
        )

        for ioc in iocs:

            complaint_counter[ioc] = (
                complaint_counter.get(
                    ioc,
                    0
                ) + 1
            )

    threat_counter = {}

    for _, row in threats.iterrows():

        title = str(
            row.get(
                "title",
                ""
            )
        )

        iocs = extract_iocs(title)

        for ioc in iocs:

            threat_counter[ioc] = (
                threat_counter.get(
                    ioc,
                    0
                ) + 1
            )

    all_iocs = set(
        list(complaint_counter.keys())
        + list(threat_counter.keys())
    )

    results = []

    for ioc in all_iocs:

        complaint_hits = complaint_counter.get(
            ioc,
            0
        )

        threat_hits = threat_counter.get(
            ioc,
            0
        )

        vt_reputation = 0
        malicious = 0
        suspicious = 0

        try:

            vt = enrich_ioc(ioc)

            if not vt.empty:

                if "reputation" in vt.columns:
                    vt_reputation = int(
                        vt.iloc[0]["reputation"]
                    )

                if "malicious" in vt.columns:
                    malicious = int(
                        vt.iloc[0]["malicious"]
                    )

                if "suspicious" in vt.columns:
                    suspicious = int(
                        vt.iloc[0]["suspicious"]
                    )

        except Exception:
            pass

        risk_score = min(
            100,
            (
                complaint_hits * 40
                + threat_hits * 25
                + malicious * 10
                + suspicious * 5
                + (vt_reputation // 10)
            )
        )

        if risk_score >= 80:

            risk_level = "CRITICAL"

        elif risk_score >= 60:

            risk_level = "HIGH"

        elif risk_score >= 40:

            risk_level = "MEDIUM"

        else:

            risk_level = "LOW"

        results.append({

            "ioc": ioc,

            "complaint_hits":
            complaint_hits,

            "threat_hits":
            threat_hits,

            "vt_reputation":
            vt_reputation,

            "malicious":
            malicious,

            "suspicious":
            suspicious,

            "risk_score":
            risk_score,

            "risk_level":
            risk_level

        })

    fusion = pd.DataFrame(
        results
    )

    if fusion.empty:

        return fusion

    return fusion.sort_values(
        by="risk_score",
        ascending=False
    )