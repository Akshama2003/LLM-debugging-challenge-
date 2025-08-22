# Buggy Mini LLM (Next Word Predictor)
def train_model(corpus):
    freq = {}
    for sentence in corpus:
        words = sentence.split()
        for i in range(len(words)):
            key = words[i]
            next_word = words[i+1]
            if key not in freq:
                freq[key] = {}
            freq[key][next_word] = freq[key].get(next_word, 0) + 1
    return freq

def predict_next(freq, word):
    if word not in freq:
        return "UNKNOWN"
    return max(freq[word])

corpus = [
    "I love coding",
    "I love python",
    "python is powerful",
    "I love open source",
]

model = train_model(corpus)
print(predict_next(model, "I"))     # Expected: love
print(predict_next(model, "love"))  # Expected: coding OR python OR open
print(predict_next(model, "python"))# Expected: is
print(predict_next(model, "open"))  # Expected: source
