import os
from dotenv import load_dotenv
load_dotenv()  # 🔁 charge la clé depuis le fichier .env

from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_music_prompt(idea: str) -> str:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a music composer who transforms ideas into descriptive prompts for generating music."
            },
            {
                "role": "user",
                "content": f"Transform this musical idea into a descriptive prompt: {idea}"
            }
        ]
    )
    return response.choices[0].message.content

