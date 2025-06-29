FROM python:3.13-slim

WORKDIR /app

# Copy requirements first for build caching
COPY ./05-user-post-api/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY ./05-user-post-api/ .

# Grant execute permissions to our entrypoint script
RUN chmod +x /app/entrypoint.sh

# Set the entrypoint to our script
ENTRYPOINT ["/app/entrypoint.sh"]

# The default command that gets passed to the entrypoint
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]