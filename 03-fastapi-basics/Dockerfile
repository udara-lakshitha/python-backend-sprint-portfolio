# Stage 1: Use an official Python runtime as a parent image
# We choose a slim version to keep our final image small.
FROM python:3.13-slim

# Set the working directory inside the container
# All subsequent commands will run from this directory.
WORKDIR /app

# Copy the file that lists our Python dependencies into the container
# We need to create this file next!
COPY requirements.txt .

# Install the dependencies listed in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy our application code (the current directory '.') into the container's /app directory
COPY . .

# Expose port 8000. This tells Docker that the container will listen on this port.
EXPOSE 8000

# Define the command to run when the container starts.
# This is the same command we used to run our app locally.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]