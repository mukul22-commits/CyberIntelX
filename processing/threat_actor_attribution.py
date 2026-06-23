import pandas as pd


def attribute_actor(indicator):

    actors = {

        "paytm-security.xyz": {
            "actor": "APT29",
            "technique": "T1566 Phishing",
            "confidence": 75
        },

        "185.220.101.1": {
            "actor": "APT28",
            "technique": "T1090 Proxy",
            "confidence": 70
        },

        "44d88612fea8a8f36de82e1278abb02f": {
            "actor": "LockBit",
            "technique": "T1486 Data Encryption",
            "confidence": 90
        }

    }

    if indicator in actors:

        result = actors[indicator]

        return pd.DataFrame([{

            "indicator": indicator,
            "actor": result["actor"],
            "technique": result["technique"],
            "confidence": result["confidence"]

        }])

    return pd.DataFrame([{

        "indicator": indicator,
        "actor": "Unknown",
        "technique": "Unknown",
        "confidence": 0

    }])