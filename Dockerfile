FROM python:3.8.18

COPY poetry.lock .
COPY pyproject.toml . 

RUN pip install scikit-learn==1.0.1 \
                fastapi \
                uvicorn \
                joblib \
                datetime \
                python-dateutil

EXPOSE 80

COPY ./app /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]