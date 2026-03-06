import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import joblib

data = pd.read_csv("ai_engine/dataset/scam_calls.csv")

X = data["text"]
y = data["label"]

vectorizer = TfidfVectorizer()

X_vector = vectorizer.fit_transform(X)

model = RandomForestClassifier(n_estimators=100)

model.fit(X_vector,y)

joblib.dump(model,"ai_engine/models/scam_model.pkl")
joblib.dump(vectorizer,"ai_engine/models/vectorizer.pkl")

print("Model trained successfully")