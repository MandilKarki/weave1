from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from BioNER import BioBERTNER
import json

app = FastAPI()


class TextInput(BaseModel):
    text: str


biobert_ner = BioBERTNER()


@app.post("/ner")
async def ner_text(text: TextInput):
    try:
        entities = biobert_ner.extract_entities(text.text)
        entities = biobert_ner.postprocess_entities(entities)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    # encoded_entities = json.dumps(entities, default=str)
    return {"entities": entities}



