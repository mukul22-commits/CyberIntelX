import pandas as pd


def analyze_hash(file_hash):

    malware_db = {

        "44d88612fea8a8f36de82e1278abb02f": {

            "hash": file_hash,
            "family": "WannaCry",
            "type": "Ransomware",
            "risk": "Critical",
            "confidence": 99
        },

        "5d41402abc4b2a76b9719d911017c592": {

            "hash": file_hash,
            "family": "Generic Malware",
            "type": "Trojan",
            "risk": "High",
            "confidence": 85
        }
    }

    if file_hash in malware_db:

        return pd.DataFrame(
            [malware_db[file_hash]]
        )

    return pd.DataFrame([
        {
            "hash": file_hash,
            "family": "Unknown",
            "type": "Unknown",
            "risk": "Unknown",
            "confidence": 0
        }
    ])