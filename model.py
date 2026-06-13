from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Sample dataset
texts = [
    "I love this product",
    "This is amazing",
    "Very good experience",
    "I hate this",
    "This is bad",
    "Very disappointing",
    "It is okay",
    "Not bad",
    "Average experience"
]

labels = [
    "Positive",
    "Positive",
    "Positive",
    "Negative",
    "Negative",
    "Negative",
    "Neutral",
    "Neutral",
    "Neutral"
]

# Convert text to numbers
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# Train model
model = MultinomialNB()
model.fit(X, labels)

# Prediction function
def predict_sentiment(text):
    text_vec = vectorizer.transform([text])
    return model.predict(text_vec)[0]