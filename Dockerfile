# Use a lightweight Python image
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
COPY app.py .

# dependencies installing 
RUN pip install --no-cache-dir -r requirements.txt


CMD ["python", "app.py"]
