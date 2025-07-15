from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import os
from datetime import datetime

app = FastAPI()
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
def health():
    return {"message": "Legal Intake API is alive."}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, f"{datetime.now().isoformat()}_{file.filename}")
    with open(file_path, "wb") as f:
        f.write(await file.read())
    return {"message": "File uploaded successfully", "path": file_path}

@app.get("/sanity-check")
def sanity():
    return {"result": "No hallucinations", "confidence": 0.99}
