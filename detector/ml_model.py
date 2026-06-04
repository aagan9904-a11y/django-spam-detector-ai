import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load dataset
df = pd.read_csv("spam.csv", encoding='latin-1')

df = df[['v1', 'v2']]
df.columns = ['label', 'message']

df['label'] = df['label'].map({
    'ham': 0,
    'spam': 1
})

X = df['message']
y = df['label']

# Vectorization
vectorizer = CountVectorizer()

X_vectorized = vectorizer.fit_transform(X)

# Train model
model = MultinomialNB()

model.fit(X_vectorized, y)

# Prediction function
def predict_spam(message):

    vector = vectorizer.transform([message])

    prediction = model.predict(vector)

    return prediction[0]