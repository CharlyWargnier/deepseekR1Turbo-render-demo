from fastapi import FastAPI, Request
from openai import OpenAI

app = FastAPI()

import os
from dotenv import load_dotenv

load_dotenv()
DEEPINFRA_TOKEN = os.getenv("DEEPINFRA_TOKEN")

# Set up OpenAI-compatible client (DeepInfra)
client = OpenAI(
    api_key=DEEPINFRA_TOKEN,
    base_url="https://api.deepinfra.com/v1/openai"
)

@app.get("/")
def home():
    return {"message": "✅ FastAPI + DeepSeek is running!"}

@app.post("/chat")
async def chat(request: Request):
    body = await request.json()
    user_input = body.get("message", "")

    chat_completion = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-R1-0528-Turbo",
        messages=[{"role": "user", "content": user_input}]
    )

    return {"response": chat_completion.choices[0].message.content} 