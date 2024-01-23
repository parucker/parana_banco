from pydantic import BaseModel


class InferenceFeatures(BaseModel):
    feature_1: float
    feature_2: float
