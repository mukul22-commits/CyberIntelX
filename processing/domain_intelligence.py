import pandas as pd


def analyze_domain(domain):

    domains = {

        "paytm-security.xyz": {

            "domain": domain,
            "registrar": "NameCheap",
            "age_days": 2,
            "risk": "Critical",
            "confidence": 98
        },

        "google.com": {

            "domain": domain,
            "registrar": "Google Registry",
            "age_days": 9500,
            "risk": "Low",
            "confidence": 100
        }

    }

    if domain in domains:

        return pd.DataFrame(
            [domains[domain]]
        )

    return pd.DataFrame(
        [{
            "domain": domain,
            "registrar": "Unknown",
            "age_days": 0,
            "risk": "Unknown",
            "confidence": 0
        }]
    )