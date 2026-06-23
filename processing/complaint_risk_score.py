def calculate_risk(text):

    keywords = {
        "phishing":30,
        "otp":25,
        "bank":15,
        "investment":35,
        "scam":30,
        "fraud":30,
        "upi":20,
        "crypto":25,
        "whatsapp":10
    }

    score = 0

    text = str(text).lower()

    for word, value in keywords.items():

        if word in text:
            score += value

    return min(score,100)