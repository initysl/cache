FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml .
RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-dev

COPY app ./app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
