from threat_score import calculate_score

text = "Phishing attack caused a bank fraud"

score = calculate_score(text)

print("Threat Score:", score)