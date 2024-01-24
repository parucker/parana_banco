# This is an API builded with fastAPI to run inferences

## Setup
Make sure you have pyenv installed and then run the following commands:
```
pyenv install 3.9.18
pyenv virtualenv 3.9.18 name_for_your_env
pyenv activate name_for_your_env
```
With the enviroment, now you can install poetry to manage the dependencies
```
pip install poetry
poetry install
```
Now your enviroment is finished and you can run the api

Note:
If you have a error trying to install scikit-learn==1.0.1, try this command before running poetry install again:
```
poetry run pip wheel --no-cache-dir --use-pep517 "scikit-learn (==1.0.1)"
```

## How to run it

### Locally
To run the server you can run
```
make run-server-without-docker
```

Then you can send a test request with
```
test-request-prediction
```

### With Docker
Make sure you have builded the image with
```
make build-docker
```

Then you can start the server with
```
make run-docker
```

And you can send a test-resquest with:
```
make test-request-prediction-docker
```

## Extras
### Lint
You can run the lint with 
```
make lint
```
it will run black and isort
### Pytest
You can simple run your tests with 
```
make test
``` 
### Locust
You can test run a performance test with Locust, just type:
```
docker-compose up
```
And then go to `http://localhost:8089/`
