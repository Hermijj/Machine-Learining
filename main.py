from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Load the trained model
model = joblib.load('linear_regression_model.pkl')

app = FastAPI()

class PredictionRequest(BaseModel):
    athletes: int
    prev_medals: int

@app.post("/predict/")
def predict(request: PredictionRequest):
    data = pd.DataFrame([request.dict()])
    prediction = model.predict(data)
    return {"prediction": max(0, round(prediction[0]))}

@app.get("/")
def read_root():
    return {"message": "Welcome to the Olympic Medals Prediction API"}