import os
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Get project root directory
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

csv_path = os.path.join(BASE_DIR, "spam.csv")

# Load dataset
df = pd.read_csv(csv_path, encoding="latin-1")

df = df[['v1', 'v2']]
df.columns = ['label', 'message']

df['label'] = df['label'].map({
    'ham': 0,
    'spam': 1
})

X = df['message']
y = df['label']

vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

model = MultinomialNB()
model.fit(X_vectorized, y)

def predict_spam(message):
    vector = vectorizer.transform([message])
    prediction = model.predict(vector)
    return prediction[0]