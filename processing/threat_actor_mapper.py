import pandas as pd


def get_actor(actor):

    actors = {

        "APT28": {
            "country": "Russia",
            "motivation": "Espionage",
            "severity": "Critical"
        },

        "APT29": {
            "country": "Russia",
            "motivation": "Espionage",
            "severity": "Critical"
        },

        "Lazarus": {
            "country": "North Korea",
            "motivation": "Financial Theft",
            "severity": "Critical"
        },

        "FIN7": {
            "country": "Unknown",
            "motivation": "Cyber Crime",
            "severity": "High"
        },

        "LockBit": {
            "country": "Unknown",
            "motivation": "Ransomware",
            "severity": "Critical"
        }
    }

    if actor in actors:

        data = actors[actor]

        data["actor"] = actor

        return pd.DataFrame([data])

    return pd.DataFrame([{

        "actor": actor,
        "country": "Unknown",
        "motivation": "Unknown",
        "severity": "Unknown"

    }])