
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def recommend_venues(user_input, venue_data):
    prompt = f"""You are a helpful wedding planner AI. Based on the user's request below and the list of venues provided, recommend 3 suitable options with reasons.

User request: {user_input}

Venues data:
{venue_data}

Your reply:"""

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]
