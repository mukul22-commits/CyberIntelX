import requests
import sqlite3
import time

URL = (
    "https://services.nvd.nist.gov/rest/json/cves/2.0"
    "?resultsPerPage=20"
)

success = False

for attempt in range(5):

    try:

        print(
            f"Attempt {attempt+1}"
        )

        response = requests.get(
            URL,
            timeout=60,
            headers={
                "User-Agent":
                "Mozilla/5.0"
            }
        )

        if response.status_code == 200:

            success = True
            break

        print(
            f"Status: {response.status_code}"
        )

    except Exception as e:

        print(
            "Error:",
            e
        )

    time.sleep(5)

if not success:

    print(
        "NVD Feed Unavailable"
    )

    exit()

data = response.json()

conn = sqlite3.connect(
    "database/cybercrime.db"
)

cursor = conn.cursor()

added = 0

for item in data.get(
    "vulnerabilities",
    []
):

    try:

        cve = item["cve"]

        cve_id = cve["id"]

        description = (
            cve["descriptions"][0]["value"]
        )

        link = (
            "https://nvd.nist.gov/vuln/detail/"
            + cve_id
        )

        cursor.execute(
            """
            INSERT INTO intelligence_data(
            source,
            title,
            link,
            threat_score,
            sentiment
            )
            VALUES(?,?,?,?,?)
            """,
            (
                "NVD-CVE",
                f"{cve_id} - {description}",
                link,
                90,
                "Negative"
            )
        )

        added += 1

    except:
        pass

conn.commit()
conn.close()

print(
    f"NVD CVEs Added: {added}"
)