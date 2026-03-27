import pandas as pd
from src.preprocessing import clean_text, normalize_text, tokenize_text, lemmatize_tokens


def build_dataframe(pairs):
    all_rows = []



    for pair in pairs:
        text = pair["input"]
        text = clean_text(text)
        text = normalize_text(text)
        tokens = tokenize_text(text)
        processed = lemmatize_tokens(tokens)
        all_rows.extend(processed)

    df = pd.DataFrame(all_rows)



    return df