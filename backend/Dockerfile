# Use official Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy backend code
COPY main.py .

# Install FastAPI + Uvicorn
RUN pip install fastapi uvicorn

# Run Uvicorn server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
