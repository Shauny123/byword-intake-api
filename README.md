# Byword Legal Intake API

![Python](https://img.shields.io/badge/python-3.11-blue)
![License](https://img.shields.io/github/license/Shauny123/byword-intake-api)
![Last Commit](https://img.shields.io/github/last-commit/Shauny123/byword-intake-api)
![Deployment](https://img.shields.io/badge/Cloud%20Run-deployed-brightgreen)

This repository powers the **Byword Legal Intake System**, a FastAPI-based backend deployed to Google Cloud Run.

## 📌 Features

- 🌐 Domain mapping: `bywordofmouthlegal.{ai, com, help}`
- 🚀 FastAPI + Uvicorn backend
- 🔐 OpenAI GPT integration
- 📡 DNS monitoring tools
- 🐍 Python 3.11, clean Docker build

## 🛠️ DNS Tools

Check DNS resolution:

```bash
python dns_tools/check_dns.py


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

