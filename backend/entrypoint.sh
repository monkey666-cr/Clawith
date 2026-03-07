#!/bin/bash
# Docker entrypoint: run DB migrations, then start the app.
# Use bash (not sh/dash) to avoid CRLF/set-option compatibility issues.
set -e

echo "[entrypoint] Running database migrations..."
alembic upgrade head
echo "[entrypoint] Migrations done - starting uvicorn..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000
