# Use slim Python base image
FROM python:3.11-slim

# Prevents Python from buffering logs (immediate log output)
ENV PYTHONUNBUFFERED=1

# Set working directory inside container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Optionally copy .env if you use environment configs
# Remove this line if you inject secrets from Google Cloud directly
# COPY .env .env

# Expose the port expected by Google Cloud Run
EXPOSE 8080

# Run the FastAPI app with uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]




