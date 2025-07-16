# Byword Legal Intake API

A FastAPI-based multilingual legal intake assistant designed to capture and analyze legal leads, grounded with GPT-4 and sentence-transformer embeddings.

## 🔧 Features

- RESTful API using FastAPI
- `/` route returns status message
- `/chatgpt` route connects to OpenAI for GPT-4 response
- Support for multilingual input
- Embedding and vector search support (via `sentence-transformers` and `faiss-cpu`)
- Dockerized for easy deployment on Google Cloud Run

## 🚀 Deployment

This API is designed to deploy directly to **Google Cloud Run** using:
- `Dockerfile`
- `requirements.txt`
- `main.py`

### Endpoint example:
```bash
POST /chatgpt
Content-Type: application/json
{
  "prompt": "How can I file an ADA complaint?"
}

