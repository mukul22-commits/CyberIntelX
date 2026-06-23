import spacy

nlp = spacy.load("en_core_web_sm")

def extract_entities(text):

    doc = nlp(str(text))

    entities = []

    for ent in doc.ents:
        entities.append(
            (
                ent.text,
                ent.label_
            )
        )

    return entities



from entity_extractor import extract_entities

text = "Google and INTERPOL detected a phishing campaign in China"

print(extract_entities(text))





import spacy

nlp = spacy.load("en_core_web_sm")

def extract_entities(text):

    doc = nlp(str(text))

    entities = []

    for ent in doc.ents:

        entities.append(
            {
                "text": ent.text,
                "label": ent.label_
            }
        )

    return entities