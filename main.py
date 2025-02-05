from fastapi import FastAPI
import joblib
import pandas as pd
from pydantic import BaseModel
from pydantic import BaseModel

# Load the trained model
model = joblib.load("linear_regression_model.pkl")

# Initialize FastAPI
app = FastAPI(title="Olympic Medals Prediction API",
              description="Predict the number of medals a team will win based on key features.",
              version="1.0")

# Define input data schema
class MedalsInput(BaseModel):
    team: str
    country: str
    year: int
model = joblib.load("linear_regression_model.pkl")

# Initialize FastAPI
app = FastAPI(title="Olympic Medals Prediction API",
              description="Predict the number of medals a team will win based on key features.",
              version="1.0")

# Define input data schema
class MedalsInput(BaseModel):
    team: str
    country: str
    year: int
    athletes: int
    age: float
    prev_medals: float

# Welcome message endpoint
@app.get("/")
def welcome():
    return {"message": "Welcome to the Olympic Medals Prediction API! Use /predict/ to get medal predictions."}

# Define prediction endpoint
    age: float
    prev_medals: float

# Welcome message endpoint
@app.get("/")
def welcome():
    return {"message": "Welcome to the Olympic Medals Prediction API! Use /predict/ to get medal predictions."}

# Define prediction endpoint
@app.post("/predict/")
def predict_medals(data: MedalsInput):
    try:
        # Convert input data to DataFrame
        input_data = pd.DataFrame([data.dict()])

        # Select the features used for prediction
        predictors = ["athletes", "prev_medals"]
        prediction = model.predict(input_data[predictors])[0]
        prediction = max(0, round(prediction))  # Ensure non-negative integer output

        return {
            "message": "Prediction successful!",
            "team": data.team,
            "country": data.country,
            "year": data.year,
            "predicted_medals": prediction
        }
    except Exception as e:
        return {"error": "Prediction failed. Please check your input data.", "details": str(e)}