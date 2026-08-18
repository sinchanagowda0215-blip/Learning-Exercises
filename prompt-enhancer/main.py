import os
import json
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI

load_dotenv()

app = FastAPI(title="Prompt Enhancer API")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class PromptRequest(BaseModel):
    prompt: str


@app.get("/")
def home():
    return {"message": "Prompt Enhancer API is running"}


@app.post("/enhance")
def enhance_prompt(request: PromptRequest):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": """
You are a prompt enhancement assistant.

Analyze the user's prompt and return a JSON object with exactly these fields:

1. original_prompt
2. missing_information
3. enhanced_prompt

missing_information should contain the important details that are missing
from the user's original prompt.

enhanced_prompt should rewrite the original prompt to make it clearer,
more specific, and easier for an AI to understand.

Return only valid JSON.
"""
            },
            {
                "role": "user",
                "content": request.prompt
            }
        ],
        response_format={"type": "json_object"}
    )

    result = json.loads(response.choices[0].message.content)

    return result