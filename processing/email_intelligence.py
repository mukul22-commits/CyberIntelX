import pandas as pd


def analyze_email(email):

    try:
        domain = email.split("@")[1]
    except:
        domain = "Invalid"

    suspicious_domains = [
        "fakebank.com",
        "paytm-security.xyz",
        "upi-verification.xyz"
    ]

    if domain in suspicious_domains:

        return pd.DataFrame([{
            "email": email,
            "domain": domain,
            "category": "Suspicious Domain",
            "risk": "High",
            "confidence": 90
        }])

    return pd.DataFrame([{
        "email": email,
        "domain": domain,
        "category": "No Known Threat",
        "risk": "Low",
        "confidence": 60
    }])