import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def process_text(text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": """
You are an AI text processing assistant.

Analyze the provided text and perform three tasks:

1. Summarize the text in a few sentences.
2. Classify the main topic of the text.
3. Extract the important concepts, technologies, or entities.

Return only valid JSON with exactly these fields:
summary
classification
extracted_information
"""
            },
            {
                "role": "user",
                "content": text
            }
        ],
        response_format={"type": "json_object"}
    )

    return json.loads(response.choices[0].message.content)


if __name__ == "__main__":

    with open("sample.txt", "r", encoding="utf-8") as file:
        text = file.read()

    result = process_text(text)

    print("\n===== AI TEXT PROCESSING LAB =====\n")

    print("SUMMARY:")
    print(result["summary"])

    print("\nCLASSIFICATION:")
    print(result["classification"])

    print("\nEXTRACTED INFORMATION:")
    for item in result["extracted_information"]:
        print("-", item)