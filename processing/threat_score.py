def calculate_score(text):

    text = str(text).lower()

    score = 0

    keywords = {
    "phishing": 30,
    "ransomware": 35,
    "malware": 25,
    "breach": 25,
    "data breach": 35,
    "exploit": 25,
    "zero-day": 40,
    "cve": 30,
    "botnet": 30,
    "apt": 35,
    "ddos": 25,
    "credential": 20,
    "vulnerability": 20,
    "attack": 15,
    "hacker": 15,
    "hackers": 15,
    "crypto": 15,
    "laundering": 20,
    "fraud": 20,
    "scam": 20
    }

    for keyword, value in keywords.items():
        if keyword in text:
            score += value

    return min(score, 100)