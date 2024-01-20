import uuid
from datetime import datetime

import joblib
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Parana Banco Inferencia")


class InferenceObject(BaseModel):
    feature_1: float
    feature_2: float


@app.on_event("startup")
def load_model():
    global model
    model = joblib.load("mlops/model/modelo.joblib")


@app.post("/predict")
def predict(inference_object: InferenceObject):
    data = np.array([[inference_object.feature_1, inference_object.feature_2]])

    prediction = model.predict(data)
    prediction = round(prediction[0], 5)

    date = datetime.now().date()
    date_iso = date.isoformat()

    id = uuid.uuid4()

    return {"data": date_iso, "predicao": prediction, "id": id}
