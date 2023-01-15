import json
from docarray import Document


# Create an empty list to store the Jina Documents
documents = []
data = test


def dict_to_docs(d):
    documents = {}
    keys_to_extract = ['Protein', 'Complex', 'Reaction', 'Pathway']
    for key in keys_to_extract:
        if key not in d:
            continue
        documents[key] = []
        value = d[key]
        doc = Document()
        doc.text = value
        documents[key].append(doc)
    return documents


docs = dict_to_docs(test)
print(docs)
print(type(docs))