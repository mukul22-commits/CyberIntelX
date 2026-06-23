import pandas as pd


def reputation_lookup(ioc):

    malicious = [

        "185.220.101.1",
        "paytm-security.xyz",
        "fakebank.com"

    ]

    if ioc in malicious:

        return pd.DataFrame([{

            "ioc": ioc,
            "reputation": "Malicious",
            "score": 95

        }])

    return pd.DataFrame([{

        "ioc": ioc,
        "reputation": "Unknown",
        "score": 20

    }])