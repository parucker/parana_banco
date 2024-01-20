import logging
import uuid
from datetime import datetime
from typing import List

import joblib
import numpy as np
from fastapi import FastAPI
from fastapi.responses import JSONResponse, Response
from pydantic import BaseModel, conlist

logging.basicConfig(
    filename="app.log",
    filemode="a",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)

app = FastAPI(title="Parana Banco Inferencia")


class InferenceObject(BaseModel):
    batches: List[conlist(item_type=float, min_length=2, max_length=2)]


@app.on_event("startup")
def load_model():
    logger.info("startup - loading model")
    global model
    model = joblib.load("app/model/modelo.joblib")
    logger.info("startup - model loaded")


@app.post("/predict")
def predict(inference_object: InferenceObject, response: Response) -> JSONResponse:
    try:
        batches = inference_object.batches
        data = np.array(batches)

        logger.info(f"predict - starting prediction with {data}")
        prediction = model.predict(data)
        prediction = round(prediction[0], 5)
        logger.info(f"predict - prediction has ended with value {prediction}")

        date = datetime.now().date()
        date_iso = date.isoformat()

        id = str(uuid.uuid4())

        return JSONResponse(
            content={"data": date_iso, "predicao": prediction, "id": id}
        )
    except Exception as e:
        response.status_code = 500
        logger.error(f"predict - error {str(e)}")
        return JSONResponse(content={"error_msg": str(e)})
