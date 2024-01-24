import logging
import uuid
from datetime import datetime

import joblib
import numpy as np
from fastapi import FastAPI
from fastapi.responses import JSONResponse, Response

from app.inference.inference_features import InferenceFeatures
from app.inference.predict import Predict

logging.basicConfig(
    filename="app.log",
    filemode="a",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)

app = FastAPI(title="Parana Banco Inferencia")


@app.on_event("startup")
def load_model():
    logger.info("startup - loading model")
    global model
    model = joblib.load("app/artifacts/modelo.joblib")
    logger.info("startup - model loaded")


@app.post("/predict")
def predict(inference_object: InferenceFeatures, response: Response) -> JSONResponse:
    try:
        id = str(uuid.uuid4())
        data = np.array([[inference_object.feature_1, inference_object.feature_2]])

        logger.info(f"predict - starting prediction with {data}")
        predict = Predict(model=model)
        prediction = predict.prediction(data)
        logger.info(f"predict - prediction id:{id} has ended with value {prediction}")

        date = datetime.now().date()
        date_iso = date.isoformat()

        return JSONResponse(
            content={"data": date_iso, "predicao": prediction, "id": id}
        )
    except Exception as e:
        logger.error(f"predict - error {str(e)}")
        return JSONResponse(content={"error_msg": str(e)}, status_code=500)


@app.get("/ping")
def ping() -> JSONResponse:
    message = "The server is running"
    return JSONResponse(content={"message": message})
