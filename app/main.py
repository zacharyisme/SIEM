from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai
from app.prompt import build_prompt
from app.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

app = FastAPI()

class TicketRequest(BaseModel):
    summary: str
    description: str

@app.post("/classify_ticket")
async def classify_ticket(ticket: TicketRequest):
    prompt = build_prompt(ticket.summary, ticket.description)

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
            max_tokens=10
        )
        category = response.choices[0].message.content.strip()
        return {"category": category}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
