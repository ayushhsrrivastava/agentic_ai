from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from agent import agent_response
from crm import get_leads

# ✅ FIRST create app
app = FastAPI()

# ✅ THEN add middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model
class ChatRequest(BaseModel):
    session_id: str
    message: str

# Chat API
@app.post("/chat")
def chat(req: ChatRequest):
    reply = agent_response(req.session_id, req.message)
    return {"response": reply}

# CRM API
@app.get("/leads")
def leads():
    return get_leads()