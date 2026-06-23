def calculate_confidence(
    linked_cases,
    virustotal_hits,
    abuse_score,
    campaign_hits
):

    score = 0

    score += linked_cases * 15

    score += virustotal_hits * 10

    score += abuse_score

    score += campaign_hits * 10

    if score > 100:
        score = 100

    if score >= 80:
        level = "Critical"

    elif score >= 60:
        level = "High"

    elif score >= 30:
        level = "Medium"

    else:
        level = "Low"

    return score, level