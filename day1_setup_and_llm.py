# ============================================================
# DAY 1 — Setup + Call Your First LLM
# ============================================================
# GOAL: Set up your environment and make your first API call
# TIME: 2:00 PM – 4:00 PM
# ============================================================

# STEP 1: Make sure you have installed all packages
# Run this in your terminal BEFORE running this file:
# pip install openai langchain langchain-openai chromadb streamlit pandas python-dotenv

# STEP 2: Create a file called .env in your project folder
# Inside .env write exactly this (no quotes):
# OPENAI_API_KEY=your_actual_key_here
# Get your key from: platform.openai.com

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load your API key from the .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Check that the key loaded correctly
if not api_key:
    print("ERROR: API key not found. Check your .env file.")
    exit()
else:
    print("API key loaded successfully!")

# Create the OpenAI client
client = OpenAI(api_key=api_key)

# ============================================================
# STEP 3: Make your first LLM call
# ============================================================

def ask_llm(system_prompt, user_question):
    """
    Sends a question to the LLM and returns the answer.
    system_prompt = the rules and role for the AI
    user_question = what the user is asking
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",       # cheap and fast model, good for testing
        temperature=0.0,           # 0 = focused/factual, 1 = creative/random
        max_tokens=500,            # max length of response
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_question}
        ]
    )
    # Extract just the text from the response
    return response.choices[0].message.content

# ============================================================
# STEP 4: Test 5 different system prompts
# Notice how the SAME question gets different answers
# based on the system prompt
# ============================================================

question = "What skills do data analysts need in 2026?"

prompts = [
    "You are a helpful assistant. Answer clearly and concisely.",
    "You are a strict hiring manager. Be direct and critical.",
    "You are a friendly career coach. Be encouraging and motivating.",
    "You are a technical expert. Focus only on technical skills.",
    "You are a data analyst with 10 years experience. Speak from personal experience.",
]

print("\n" + "="*60)
print("TESTING 5 DIFFERENT SYSTEM PROMPTS — SAME QUESTION")
print("="*60)

for i, prompt in enumerate(prompts, 1):
    print(f"\n--- System Prompt {i} ---")
    print(f"Role: {prompt[:50]}...")
    answer = ask_llm(prompt, question)
    print(f"Answer: {answer[:200]}...")  # print first 200 chars
    print()

# ============================================================
# STEP 5: YOUR TASK
# Change the question below to something about salaries
# and write your own system prompt
# ============================================================

print("\n" + "="*60)
print("YOUR TURN — Write your own system prompt below")
print("="*60)

my_system_prompt = "You are a data analyst assistant who answers questions about salaries and compensation in the tech industry."
my_question = "What is the average salary for a data analyst with Python skills?"

my_answer = ask_llm(my_system_prompt, my_question)
print(f"Question: {my_question}")
print(f"Answer: {my_answer}")

print("\n DAY 1 COMPLETE!")
print("Next step: Push this file to GitHub")
print("Commit message: 'Day 1 - First LLM API call and prompt testing'")
