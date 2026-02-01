import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

# Initialize client outside of function if possible, or inside. 
# The user example had it outside, but standard practice might be lazy loading. 
# Following user example exactly.

api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key) if api_key else None

def call_groq(prompt):
    if not client:
        raise ValueError("GROQ_API_KEY environment variable not set.")
        
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",

        messages=[
            {"role": "system", "content": "You are an expert AI script analyst for film directors."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.4
    )
    return response.choices[0].message.content
