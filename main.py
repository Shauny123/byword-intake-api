from fastapi import FastAPI, Request
import openai
import os

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Byword Legal Intake API is live."}

@app.post("/chatgpt")
async def chat_with_gpt(request: Request):
    data = await request.json()
    prompt = data.get("prompt")

    openai.api_key = os.getenv("OPENAI_API_KEY")

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return {"reply": response['choices'][0]['message']['content']}

