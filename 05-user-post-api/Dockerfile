FROM python:3.13-slim

WORKDIR /app

# Copy requirements first for build caching
COPY ./05-user-post-api/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY ./05-user-post-api/ .

# This is the new, single startup command.
# It runs the waiter script, and IF it succeeds (exits 0),
# THEN it runs the uvicorn server.
# This is the most reliable way to chain commands.
CMD python wait_for_db.py && uvicorn app:app --host 0.0.0.0 --port 8000