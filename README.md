Debre Birhan University
College of computing Department of Software Engineering
Fundamental of machine learning

NAME: Hermela Gashaw
ID:1401389

Submitted to: Derebew
Submission Date 02/02/2025
Open your browser and navigate to http://127.0.0.1:8000/docs for the welcome message.
Render link  on  https://machine-learining-nl9l.onrender.com

# Olympic Medals Prediction Project

# Project Overview

 This project will cover the full process of building a beginner machine learning project. This includes creating a hypothesis, setting up the model.
To make this interesting, we'll use a fun dataset. We'll use data from historical Olympic games. We'll try to  predict the number of medals an Olympic team will win based on historical data using a linear regression model. The model is deployed as a FastAPI application.

# Machine learning project steps

Most machine learning projects follow a similar outline, which we'll also follow here.  This outline will help you tackle any machine learning problem.

**Project Steps**

1. Form a hypothesis.
2. Find and explore the data.
3. (If necessary) Reshape the data to predict your target.
4. Clean the data for ML.
5. Pick an error metric.
6. Split your data.
7. Train a model.
8. Deployment


File overview:

* `olyompic_medal.ipynb` - the main project code

# Local Setup

## Installation

To follow this project, please install the following locally:

* Python 3.8+
* Python packages
    * pandas
    * numpy
    * scikit-learn
    * seaborn


## Data

We'll be using data from the Olympics, which was originally on [Kaggle](https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results).

You can download the files we'll use in this project here:

* [teams.csv](https://drive.google.com/uc?export=download&id=1L3YAlts8tijccIndVPB-mOsRpEpVawk7) - the team-level data that we use in this project.

## How to Run

1. **Install Dependencies:**
   ```bash
   pip install pandas numpy seaborn scikit-learn joblib fastapi uvicorn
Open your browser and navigate to http://127.0.0.1:8000 for the welcome message.
On render deployed link  https://machine-learining-nl9l.onrender.com
Fix: Check Your Request JSON
Correct Example (for Postman or /docs):
json
{
  "team": "USA",
  "country": "United States",
  "year": 2012,
  "athletes": 689,
  "age": 26.7,
  "prev_medals": 317.0,
}
