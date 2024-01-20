lint:
	poetry run isort . 
	poetry run black .

test:
	poetry run pytest

run-docker:
	docker run --rm -p 80:80 app:latest

build-docker:
	docker build -t app .

run-server-without-docker:
	poetry run uvicorn app.main:app --reload

test-request-prediction-docker:
	curl -X 'POST' http://0.0.0.0:80/predict -H 'Content-Type: application/json' -d '{"batches": [[1.5, 1.5]]}'

test-request-prediction:
	curl -X 'POST' http://0.0.0.0:8000/predict -H 'Content-Type: application/json' -d '{"batches": [[1.5, 1.5]]}'
