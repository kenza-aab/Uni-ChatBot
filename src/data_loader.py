import json

def load_dataset(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def extract_pairs(data):
    pairs = []

    for intent in data['intents']:
        patterns = intent['patterns']
        responses = intent['responses']

        for pattern in patterns:
            for response in responses:
                pairs.append({
                    "input": pattern,
                    "output": response
                })

    return pairs