from fastapi import FastAPI
from transformers import pipeline

# Create a new FastAPI app instance
app = FastAPI()

# Load sentiment analysis pipeline
classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# Inference endpoint
@app.post("/predict")
async def predict(text: str):
    result = classifier(text)
    return result