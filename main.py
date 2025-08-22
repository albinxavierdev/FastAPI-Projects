from fastapi import FastAPI
import pickle
import numpy as np
from pydantic import BaseModel

# Load the model
with open(r"C:\Users\Himani Singh\Downloads\xgboost_model.pkl", "rb") as f:
    model = pickle.load(f)

# Initialize FastAPI
app = FastAPI()

# Define input schema
class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Prediction endpoint
@app.post("/predict")
def predict(features: IrisFeatures):
    data = np.array([[features.sepal_length, features.sepal_width, features.petal_length, features.petal_width]])
    prediction = model.predict(data)
    return {"predicted_class": int(prediction[0])}
