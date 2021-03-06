from fastapi import FastAPI
import uvicorn
import spacy

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to the named entity recognizer"}


@app.get("/add/{num1}/{num2}")  # route, where parameters get passed in
async def add(num1: int, num2: int):  # function
    """Add two numbers together"""

    total = num1 + num2
    return {"total": total}

@app.get("/ner/{input_sentence}") # route, where parameters get passed in
async def ner(input_sentence):
    model = spacy.load("en_core_web_sm")
    output = {}
    doc = model(input_sentence)
    for entity in doc.ents:
        if entity.label_ == "GPE":
            label = "COUNTRY"
        elif entity.label_ == "LOC":
            label = "LOCATION"
        elif entity.label_ == "ORG":
            label = "ORGANIZATION"
        else:
            label = entity.label_
        output[entity.text] = label

    return output

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
