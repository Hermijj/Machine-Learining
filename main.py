from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
import socket

# Load the trained model
model = joblib.load('linear_regression_model.pkl')

app = FastAPI()

class PredictionRequest(BaseModel):
    athletes: int
    prev_medals: int

@app.post("/predict/")
def predict(request: PredictionRequest):
    try:
        data = pd.DataFrame([request.dict()])
        prediction = model.predict(data)
        return {"prediction": max(0, round(prediction[0]))}
    except socket.timeout:
        raise HTTPException(status_code=408, detail="Port scan timeout reached, no open ports detected on 0.0.0.0. Detected open ports on localhost -- did you mean to bind one of these to 0.0.0.0?")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def read_root():
    return {"message": "Welcome to the Olympic Medals Prediction API"}

@app.get("/")
def read_root():
    return {"message": "Welcome to the Olympic Medals Prediction API"}