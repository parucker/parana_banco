from locust import HttpUser, constant, task


class LoadTest(HttpUser):
    wait_time = constant(0)
    host = "http://localhost"

    @task
    def predict_batch_1(self):
        request_body = {"batches": [[1.5 for i in range(2)]]}
        self.client.post("http://batch-1:80/predict", json=request_body, name="batch-1")
