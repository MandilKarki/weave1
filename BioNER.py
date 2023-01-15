import transformers
from transformers import pipeline, AutoModelForTokenClassification, AutoTokenizer

MODEL_NAME = "alvaroalon2/biobert_diseases_ner"
#BIO_NER_ALL = 'MODEL_NAME = "d4data/biomedical-ner-all"


class BioBERTNER:
    def __init__(self):
        self.model = pipeline("ner", model=MODEL_NAME, tokenizer=AutoTokenizer.from_pretrained(MODEL_NAME), aggregation_strategy="simple")

    def extract_entities(self, text):
        try:
            entities = self.model(text)
            return entities
        except Exception as e:
            raise ValueError("An error occured while trying to extract entities")

    def postprocess_entities(self, entities):
        disease_words = []
        for entity in entities:
            if entity['entity_group'] == "DISEASE":
                disease_words.append(entity.get('word'))
        return disease_words


# bioBERTNER = BioBERTNER()
# test = bioBERTNER.extract_entities("preventing alzheimers and lung cancer")
# print(test)
# test2 = bioBERTNER.postprocess_entities(test)
# print(test2)
