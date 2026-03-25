from src.data_loader import load_dataset, extract_pairs

def main():
    path = "data/raw/chatbot.json"

    data = load_dataset(path)
    pairs = extract_pairs(data)

    print("Nombre de paires :", len(pairs))

    for i in range(5):
        print(pairs[i])

if __name__ == "__main__":
    main()