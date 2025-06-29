# This is the full, correct Dockerfile for your current structure.
FROM python:3.13-slim

WORKDIR /app

# The build context is the '05-user-post-api' folder, so the path is simple.
COPY 05-user-post-api/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy everything from the build context (the '05-user-post-api' folder)
# into the container's /app directory.
COPY 05-user-post-api/ /app

# Execute permissions to the entrypoint script.
RUN chmod +x /app/entrypoint.sh

# The entrypoint script path is now relative to the WORKDIR /app
ENTRYPOINT ["/app/entrypoint.sh"]

# The command to run the application.
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]