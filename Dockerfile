FROM python:3.9.18

COPY poetry.lock .
COPY pyproject.toml . 

RUN pip install poetry
RUN poetry install

EXPOSE 80

COPY ./app /app

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]