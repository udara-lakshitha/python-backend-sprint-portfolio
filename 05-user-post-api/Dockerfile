# --- Stage 1: Use an official, slim Python image ---
# Using a specific version is good practice for reproducibility.
FROM python:3.13-slim

# --- Set environment variables ---
# Prevents Python from writing .pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# Ensures Python output is sent straight to the terminal without buffering
ENV PYTHONUNBUFFERED 1

# --- Set the working directory inside the container ---
# All subsequent commands will run from this path.
WORKDIR /app

# --- Install dependencies ---
# First, copy only the requirements file. This takes advantage of Docker's layer caching.
# If requirements.txt doesn't change, Docker won't re-run this layer, making builds faster.
COPY 05-user-post-api/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# --- Copy the application code ---
# Copy the rest of your application code from its subfolder into the container.
COPY 05-user-post-api/ .

# --- Expose the port the app runs on ---
# This is metadata. It tells Docker the container is intended to listen on this port.
# Railway will automatically detect this.
EXPOSE 8000

# --- The Command to run the application ---
# This is the command that starts your server when the container is run.
# It's crucial for cloud deployment. We use the $PORT variable that Railway provides.
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]