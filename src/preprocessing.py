import re


import download_nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer

def clean_text(text):
    # Suppression HTML
    text = re.sub(r"<.*?>", "", text)

    # Suppression emails
    text = re.sub(r'\S+@\S+', '', text)
    # Suppression URL
    text = re.sub(r'http\S+|www\S+', '', text)

    # Suppression chiffres
    text = re.sub(r'\d+', '', text)



    return text


def normalize_text(text):
    return text.lower()


def tokenize_text(text):
    sentences = sent_tokenize(text)
    tokenized_sentences = [word_tokenize(sent) for sent in sentences]
    return tokenized_sentences


def lemmatize_tokens(tokenized_sentences):
    lemmatizer = WordNetLemmatizer()
    processed_data = []

    for sentence in tokenized_sentences:
        pos_tags = download_nltk.pos_tag(sentence)

        for token, pos in pos_tags:
            if token.isalnum():
                lemma = lemmatizer.lemmatize(token)
                processed_data.append({
                    "token": token,
                    "lemma": lemma,
                    "pos": pos
                })

        # séparation entre phrases
        processed_data.append({"token": "", "lemma": "", "pos": ""})




    return processed_data