from complaint_risk_score import calculate_risk

text = """
WhatsApp investment scam.
Lost money through UPI fraud.
"""

print(
    calculate_risk(text)
)