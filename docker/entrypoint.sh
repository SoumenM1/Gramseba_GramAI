#!/bin/sh

echo "Starting GramAI..."

exec uvicorn app.main:app \
    --host 0.0.0.0 \
    --port 8000