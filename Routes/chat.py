from fastapi import APIRouter
from llm.llm import generate_response, evaluate_response
from pydantic import BaseModel
import json


router = APIRouter()

class ChatRequest(BaseModel):
    query: str

@router.post('/chat')
def chat(request: ChatRequest):
    response = generate_response(request.query)
    return response

class EvaluateRequest(BaseModel):
    query: str
    response: str
    score: int
    feedback: str

@router.post('/evaluate')
def evaluate(request: ChatRequest) -> EvaluateRequest:
    response = generate_response(request.query)
    eval_raw = evaluate_response(request.query, response)
    eval_data = json.loads(eval_raw)

    return EvaluateRequest(
        query=request.query,
        response=response,
        score=eval_data['score'],
        feedback=eval_data['feedback']
    )
