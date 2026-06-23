def identify_threat_actor(text):

    text = text.lower()

    actors = []

    mappings = {

        "phishing": (
            "Phishing Kit Operators",
            "Credential Theft"
        ),

        "upi": (
            "Financial Fraud Group",
            "Banking Fraud"
        ),

        "ransomware": (
            "Ransomware Affiliate",
            "Data Extortion"
        ),

        "telegram": (
            "Social Engineering Group",
            "Fraud Campaign"
        ),

        "crypto": (
            "Crypto Scam Network",
            "Investment Fraud"
        ),

        "investment": (
            "Investment Scam Ring",
            "Ponzi Activity"
        ),

        "job": (
            "Recruitment Fraud Group",
            "Employment Scam"
        )
    }

    for keyword, actor in mappings.items():

        if keyword in text:

            actors.append(actor)

    return actors