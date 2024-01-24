from locust import HttpUser, constant, task


class LoadTest(HttpUser):
    wait_time = constant(0)
    host = "http://localhost"

    @task
    def predict_without_batch(self):
        request_body = {"feature_1": 1.2, "feature_2": 2.3}
        self.client.post("http://batch-1:80/predict", json=request_body, name="batch-1")
