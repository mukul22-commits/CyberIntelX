from entity_extractor import extract_entities

text = """
Google and INTERPOL detected a phishing campaign
targeting users in China.
"""

entities = extract_entities(text)

for e in entities:
    print(e)