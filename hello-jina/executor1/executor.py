import numpy as np
import torch
import transformers
from transformers import pipeline, AutoModelForTokenClassification, AutoTokenizer

from jina import Executor, requests, DocumentArray

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


biobert_ner = BioBERTNER()


class MyExecutor(Executor):
    @requests
    def foo(self, docs: DocumentArray, **kwargs):
        docs[0].text = 'hello, world!'
        docs[1].text = 'goodbye, world!'

    @requests(on='/crunch-numbers')
    def bar(self, docs: DocumentArray, **kwargs):
        for doc in docs:
            doc.tensor = torch.tensor(np.random.random([10, 2]))

    @requests(on='/NER')
    def ner(self, docs: Document, **kwargs):
        for doc in docs:
            entities = biobert_ner.extract_entities(doc.text)
            entities = biobert_ner.postprocess_entities(doc.text)
        return {"entities": entities}


