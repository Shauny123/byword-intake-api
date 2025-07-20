# Use a slim Python base image
FROM python:3.11-slim

# Prevents Python from buffering logs
ENV PYTHONUNBUFFERED=1

# Set working directory inside container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Optional: copy .env file if you're using it locally (NOT recommended for prod unless secrets are injected securely)
# COPY .env .env

# Expose the port expected by Google Cloud Run
EXPOSE 8080

# Run the FastAPI app using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]



