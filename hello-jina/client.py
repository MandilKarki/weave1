from jina import Client, DocumentArray
from docarray import Document

d1 = Document(text='hello, world.')
d2 = Document(text='goodbye, world.')

da = DocumentArray(
    [
        Document(text='hello world'),
        Document(text='goodbye world'),
        Document(text='hello goodbye'),
    ]
)
if __name__ == '__main__':
    c = Client(host='grpc://127.0.0.1:54321')
    da = c.post('/crunch-numbers', DocumentArray.empty(2))
    print(da.tensors)
    ner = c.post('/NER', da)
    print(ner)

