import pandas as pd


def evaluate_ioc(ioc_value):

    value = str(ioc_value).lower()

    score = 0
    reasons = []

    suspicious_keywords = [
        "verify",
        "login",
        "secure",
        "update",
        "bank",
        "kyc",
        "wallet",
        "upi"
    ]

    for keyword in suspicious_keywords:

        if keyword in value:

            score += 15
            reasons.append(
                f"Suspicious keyword: {keyword}"
            )

    if ".xyz" in value:

        score += 25

        reasons.append(
            "High-risk TLD (.xyz)"
        )

    if ".top" in value:

        score += 25

        reasons.append(
            "High-risk TLD (.top)"
        )

    if ".click" in value:

        score += 25

        reasons.append(
            "High-risk TLD (.click)"
        )

    if score >= 70:

        risk = "Critical"

    elif score >= 40:

        risk = "High"

    elif score >= 20:

        risk = "Medium"

    else:

        risk = "Low"

    return {

        "ioc": ioc_value,
        "risk": risk,
        "score": score,
        "reasons": ", ".join(reasons)

    }


def evaluate_bulk_iocs(ioc_list):

    results = []

    for ioc in ioc_list:

        results.append(
            evaluate_ioc(ioc)
        )

    return pd.DataFrame(results)