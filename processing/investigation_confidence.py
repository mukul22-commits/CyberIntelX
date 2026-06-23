import pandas as pd


def calculate_confidence(

        risk_score,
        fraud_ring,
        campaign,
        verification_matches

):

    score = 0

    score += min(risk_score, 100) * 0.40

    if fraud_ring:
        score += 20

    if campaign:
        score += 20

    score += verification_matches * 10

    score = min(score, 100)

    if score >= 85:

        level = "Critical"

    elif score >= 70:

        level = "High"

    elif score >= 40:

        level = "Medium"

    else:

        level = "Low"

    return pd.DataFrame([{

        "confidence_score": round(score, 2),
        "confidence_level": level

    }])