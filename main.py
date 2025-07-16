from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
import openai
import os
from typing import Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Byword Legal Intake API",
    description="API for legal intake processing with AI assistance",
    version="1.0.0"
)

# Initialize OpenAI client (updated syntax)
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Request/Response models
class ChatRequest(BaseModel):
    prompt: str
    max_tokens: Optional[int] = 1000
    temperature: Optional[float] = 0.7

class ChatResponse(BaseModel):
    reply: str
    usage: Optional[dict] = None

@app.get("/")
def root():
    return {"message": "Byword Legal Intake API is live.", "version": "1.0.0"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "legal-intake-api"}

@app.post("/chatgpt", response_model=ChatResponse)
async def chat_with_gpt(request: ChatRequest):
    try:
        # Validate API key exists
        if not os.getenv("OPENAI_API_KEY"):
            raise HTTPException(status_code=500, detail="OpenAI API key not configured")
        
        # Log the request (be careful with sensitive legal data in production)
        logger.info(f"Processing chat request with prompt length: {len(request.prompt)}")
        
        # Make request to OpenAI with updated client syntax
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system", 
                    "content": "You are a helpful assistant for legal intake processing. Provide accurate, professional responses while noting that this is not legal advice."
                },
                {
                    "role": "user", 
                    "content": request.prompt
                }
            ],
            max_tokens=request.max_tokens,
            temperature=request.temperature
        )
        
        return ChatResponse(
            reply=response.choices[0].message.content,
            usage=response.usage.model_dump() if response.usage else None
        )
        
    except openai.OpenAIError as e:
        logger.error(f"OpenAI API error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"OpenAI API error: {str(e)}")
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.post("/legal-intake")
async def legal_intake_analysis(request: ChatRequest):
    """
    Specialized endpoint for legal intake analysis
    """
    try:
        if not os.getenv("OPENAI_API_KEY"):
            raise HTTPException(status_code=500, detail="OpenAI API key not configured")
        
        # Enhanced system prompt for legal intake
        system_prompt = """
        You are an AI assistant specialized in legal intake processing. Your role is to:
        1. Analyze client information and legal issues
        2. Identify potential legal areas and concerns
        3. Suggest relevant questions for further intake
        4. Provide professional, structured responses
        
        Important: Always remind users that this is not legal advice and they should consult with a qualified attorney.
        """
        
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": request.prompt}
            ],
            max_tokens=request.max_tokens,
            temperature=request.temperature
        )
        
        return ChatResponse(
            reply=response.choices[0].message.content,
            usage=response.usage.model_dump() if response.usage else None
        )
        
    except openai.OpenAIError as e:
        logger.error(f"OpenAI API error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"OpenAI API error: {str(e)}")
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

# Add middleware for CORS if needed
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
