# Handles NLP models (if using Hugging Face Transformers for more advanced tasks).
from transformers import pipeline

def load_sentiment_model():
    return pipeline("sentiment-analysis")

def analyze_sentiment(text: str, model) -> str:
    result = model(text)
    return result[0]['label']