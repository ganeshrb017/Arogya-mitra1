from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from app.chatbot import chatbot_pipeline

app = FastAPI()

# CORS FIX (for frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "Arogya Mitra API running"}

@app.post("/chat")
def chat(query: Query):
    return chatbot_pipeline(query.text)