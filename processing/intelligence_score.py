def calculate_intelligence_score(
    risk_score,
    linked_cases
):

    score = risk_score

    score += (
        linked_cases * 10
    )

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