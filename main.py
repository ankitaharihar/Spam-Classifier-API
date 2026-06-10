from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import uvicorn
import os

# Load model
with open("spam_model.pkl", "rb") as f:
    model = pickle.load(f)

# Load vectorizer
with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

app = FastAPI(title="Spam Classifier API")

# Input schema
class Message(BaseModel):
    text: str

# Home route
@app.get("/")
def home():
    return {
        "message": "Spam Classifier API Running 🚀"
    }

# Prediction route
@app.post("/predict")
def predict(message: Message):

    text_vector = vectorizer.transform([message.text])

    prediction = model.predict(text_vector)[0]

    probability = model.predict_proba(text_vector)[0].max()

    result = "spam" if prediction == 1 else "not spam"

    return {
        "message": message.text,
        "prediction": result,
        "confidence": round(float(probability), 2)
    }

# Run app
if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8000))
    )