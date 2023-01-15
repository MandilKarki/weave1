import transformers
from transformers import pipeline, AutoModelForTokenClassification, AutoTokenizer

MODEL_NAME = "alvaroalon2/biobert_diseases_ner"

model = pipeline("ner", model=MODEL_NAME, tokenizer=AutoTokenizer.from_pretrained(MODEL_NAME))
text = "preventing alzheimers and lung cancer"
entities = model(text)
print(entities)

def postprocess_entities(entities):
    disease_words = []
    for entity in entities:
        if entity['entity'] == "B-DISEASE":
            disease_words.append(entity)
    return disease_words


new = postprocess_entities(entities)
# print(new)

filtered_entities = list(filter(lambda entity: entity["entity"] == 'B-DISEASE' or entity["entity"] == 'I-DISEASE', entities))
print(filtered_entities)
filtered_entities = [entity for entity in entities if entity["entity"] == 'B-DISEASE' or entity["entity"] == 'I-DISEASE']
disease_words = " ".join([entity["word"] for entity in filtered_entities])
print(disease_words)
