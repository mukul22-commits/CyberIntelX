import sqlite3
import pandas as pd
import re


def correlate_intelligence():

    conn = sqlite3.connect(
        "database/complaints.db"
    )

    complaints = pd.read_sql(
        "SELECT * FROM complaints",
        conn
    )

    conn.close()

    correlations = []

    for i in range(len(complaints)):

        desc1 = str(
            complaints.iloc[i]["description"]
        )

        emails1 = set(
            re.findall(
                r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
                desc1
            )
        )

        urls1 = set(
            re.findall(
                r"https?://[^\s]+",
                desc1
            )
        )

        domains1 = set(
            re.findall(
                r"(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}",
                desc1
            )
        )

        ips1 = set(
            re.findall(
                r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
                desc1
            )
        )

        phones1 = set(
            re.findall(
                r"\b[6-9]\d{9}\b",
                desc1
            )
        )

        upis1 = set(
            re.findall(
                r"[A-Za-z0-9.\-_]{2,}@[A-Za-z]{2,}",
                desc1
            )
        )

        hashes1 = set(
            re.findall(
                r"\b[a-fA-F0-9]{32,64}\b",
                desc1
            )
        )

        for j in range(i + 1, len(complaints)):

            desc2 = str(
                complaints.iloc[j]["description"]
            )

            emails2 = set(
                re.findall(
                    r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
                    desc2
                )
            )

            urls2 = set(
                re.findall(
                    r"https?://[^\s]+",
                    desc2
                )
            )

            domains2 = set(
                re.findall(
                    r"(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}",
                    desc2
                )
            )

            ips2 = set(
                re.findall(
                    r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
                    desc2
                )
            )

            phones2 = set(
                re.findall(
                    r"\b[6-9]\d{9}\b",
                    desc2
                )
            )

            upis2 = set(
                re.findall(
                    r"[A-Za-z0-9.\-_]{2,}@[A-Za-z]{2,}",
                    desc2
                )
            )

            hashes2 = set(
                re.findall(
                    r"\b[a-fA-F0-9]{32,64}\b",
                    desc2
                )
            )

            checks = [

                ("Email",
                 emails1.intersection(emails2)),

                ("URL",
                 urls1.intersection(urls2)),

                ("Domain",
                 domains1.intersection(domains2)),

                ("IP",
                 ips1.intersection(ips2)),

                ("Phone",
                 phones1.intersection(phones2)),

                ("UPI",
                 upis1.intersection(upis2)),

                ("Hash",
                 hashes1.intersection(hashes2))

            ]

            for ioc_type, values in checks:

                if values:

                    correlations.append(
                        {
                            "case_1":
                            complaints.iloc[i]["id"],

                            "case_2":
                            complaints.iloc[j]["id"],

                            "ioc_type":
                            ioc_type,

                            "value":
                            list(values)[0]
                        }
                    )

    return pd.DataFrame(
        correlations
    )