from unittest.mock import patch

from dateutil.parser import isoparse
from fastapi.testclient import TestClient

from app.main import app, load_model


class TestMainRoutes:
    def setup_class(cls):
        cls.client = TestClient(app)
        load_model()

    def test_predict_success(cls):
        inference_data = {"feature_1": 0.1, "feature_2": 2.5}

        response = cls.client.post("/predict", json=inference_data)
        json_response = response.json()

        assert response.status_code == 200
        assert isoparse(json_response["data"])
        assert isinstance(json_response["predicao"], float)
        assert "id" in json_response

    @patch("app.inference.predict.Predict.prediction")
    def test_predict_failure(cls, prediction):
        error_message = "Test error"
        prediction.side_effect = ValueError(error_message)
        inference_data = {"feature_1": 0.1, "feature_2": 2.5}

        response = cls.client.post("/predict", json=inference_data)
        json_response = response.json()

        assert json_response["error_msg"] == error_message
        assert response.status_code == 500

    def test_ping(cls):
        response = cls.client.get("/ping")
        json_response = response.json()

        expected_message = "The server is running"

        assert json_response["message"] == expected_message
