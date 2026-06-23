import pandas as pd


def map_to_mitre(text):

    text = text.lower()

    techniques = []

    keywords = {

        "phishing": (
            "T1566",
            "Phishing"
        ),

        "credential": (
            "T1110",
            "Brute Force / Credentials"
        ),

        "malware": (
            "T1204",
            "User Execution"
        ),

        "ransomware": (
            "T1486",
            "Data Encrypted For Impact"
        ),

        "powershell": (
            "T1059",
            "Command & Scripting"
        ),

        "remote access": (
            "T1219",
            "Remote Access Software"
        ),

        "upi": (
            "T1656",
            "Financial Theft"
        )
    }

    for word, value in keywords.items():

        if word in text:

            techniques.append(value)

    return techniques