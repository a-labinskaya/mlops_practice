import os
import joblib
import numpy as np

from fastapi import FastAPI
from pydantic import BaseModel


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "app", "model", "model.pkl")

app = FastAPI(title="Iris ML API", version="1.0.0")

model = joblib.load(MODEL_PATH)


class IrisRequest(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


@app.get("/")
def root():
    return {
        "status": "ok",
        "service": "iris-ml-api"
    }


@app.post("/predict")
def predict(data: IrisRequest):
    features = np.array([[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]])

    prediction = int(model.predict(features)[0])

    return {
        "prediction": prediction
    }
