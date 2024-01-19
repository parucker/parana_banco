FROM python:3.8.18

COPY poetry.lock .
COPY pyproject.toml . 

RUN pip install poetry
RUN poetry install 

EXPOSE 80

COPY ./mlops /mlops

CMD ["poetry run uvicorn", "mlops.main:app", "--host", "0.0.0.0", "--port", "80"]