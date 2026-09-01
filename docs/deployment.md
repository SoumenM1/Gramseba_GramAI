# Deployment

## Local

Install dependencies:

pip install -r requirements.txt

Run API:

uvicorn app.main:app --reload

## Docker

docker compose up --build