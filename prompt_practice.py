from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

question = "What do data analysts earn?"

prompts = [
    "You are a strict hiring manager. Be direct and concise.",
    "You are a friendly career coach. Be encouraging and detailed.",
    "You are a technical expert. Focus only on facts and numbers.",
    "You are a beginner teacher. Explain simply.",
    "You are a sarcastic analyst. Be slightly witty but informative.",
    "You are a senior data analyst. Provide salary ranges, key influencing factors, and format the answer in concise bullet points. Avoid unnecessary explanation."
]

for i, system_prompt in enumerate(prompts):
    print(f"\n--- Prompt {i+1} ---")
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ]
    )
    
    print(response.choices[0].message.content)