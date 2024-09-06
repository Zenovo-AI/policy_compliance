# Handles text extraction and preprocessing.
import nltk
import spacy
from typing import List

nltk.download('punkt')
nlp = spacy.load("en_core_web_sm")

def load_text(file_path: str) -> str:
    with open(file_path, 'r') as file:
        return file.read()

def preprocess_text(text: str) -> List[str]:
    doc = nlp(text)
    sentences = [sent.text.strip() for sent in doc.sents]
    return sentences