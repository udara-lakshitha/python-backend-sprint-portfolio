FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# The CMD will be defined by docker-compose for development, 
# but we can add a production CMD here later.