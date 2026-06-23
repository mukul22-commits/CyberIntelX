import requests

url = (
    "https://services.nvd.nist.gov/rest/json/cves/2.0"
    "?resultsPerPage=5"
)

r = requests.get(
    url,
    timeout=60,
    headers={
        "User-Agent":"Mozilla/5.0"
    }
)

print("Status:", r.status_code)

if r.status_code == 200:

    data = r.json()

    print(
        "CVEs Found:",
        len(data["vulnerabilities"])
    )

    for item in data["vulnerabilities"]:

        print(
            item["cve"]["id"]
        )