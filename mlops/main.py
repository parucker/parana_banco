import uuid
from datetime import datetime

import joblib
import numpy as np
from fastapi import FastAPI
from fastapi.responses import JSONResponse, Response
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
def predict(inference_object: InferenceObject, response: Response) -> JSONResponse:
    try:
        data = np.array([[inference_object.feature_1, inference_object.feature_2]])

        prediction = model.predict(data)
        prediction = round(prediction[0], 5)

        date = datetime.now().date()
        date_iso = date.isoformat()

        id = str(uuid.uuid4())

        return JSONResponse(
            content={"data": date_iso, "predicao": prediction, "id": id}
        )
    except Exception as e:
        response.status_code = 500
        return JSONResponse(content={"error_msg": str(e)})
