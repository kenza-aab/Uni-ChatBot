import nltk
import json
from nltk.stem import WordNetLemmatizer
import numpy as np

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('stopwords')
lemmatizer = WordNetLemmatizer()
with open('chatbot.json', 'r', encoding='utf-8') as file:
    intents = json.load(file)
words = []
classes = []
documents = []
ignore_letters = ['?', '!', '.', ',']
for intent in intents['intents']:
  for pattern in intent['patterns']:
    word_list = nltk.word_tokenize(pattern)
    words.extend(word_list)
    documents.append((word_list, intent['tag']))
    if intent['tag'] not in classes:
            classes.append(intent['tag'])
  words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_letters]
