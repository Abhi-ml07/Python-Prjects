import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

data = {
    "text": [
        "Congratulations! You won a free lottery ticket",
        "Call me when you reach home",
        "Win money now!!! Click here",
        "Are we meeting tomorrow?",
        "Limited offer! Claim your prize now",
        "Let's complete the project today"
    ],
    "label": [1, 0, 1, 0, 1, 0]  # 1 = Spam, 0 = Ham
}

df = pd.DataFrame(data)

X_train, X_test, y_train, y_test = train_test_split(
    df["text"], df["label"], test_size=0.3, random_state=42
)

vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

model = MultinomialNB()
model.fit(X_train_vec, y_train)

y_pred = model.predict(X_test_vec)

print("Model Accuracy:", accuracy_score(y_test, y_pred))

while True:
    message = input("\nEnter a message to check (or type exit): ")
    if message.lower() == "exit":
        break

    message_vec = vectorizer.transform([message])
    prediction = model.predict(message_vec)

    if prediction[0] == 1:
        print("❌ Spam Email")
    else:
        print("✅ Not Spam (Ham)")