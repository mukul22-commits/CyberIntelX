import requests
import time

url = "https://services.nvd.nist.gov/rest/json/cves/2.0?resultsPerPage=5"

for i in range(3):

    try:

        r = requests.get(
            url,
            timeout=60,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        print(
            f"Attempt {i+1}:",
            r.status_code
        )

    except Exception as e:

        print(e)

    time.sleep(5)