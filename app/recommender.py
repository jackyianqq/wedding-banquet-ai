<<<<<<< HEAD

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
=======
import os
import openai
import json

# Initialize OpenAI client with API key from environment variable
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def recommend_venues(user_input, venue_data):
    prompt = f"""
You are a helpful wedding planner AI. Based on the user's request and the banquet venue data, recommend 3 suitable wedding banquet venues.

Respond ONLY in this valid JSON array format — no extra commentary, no Markdown, and no explanation outside the array:

[
  {{
    "venue": "string",        // name of venue
    "location": "string",     // venue location
    "price_per_table": number,
    "capacity": number,
    "reason": "string"        // reason this venue fits the request
  }},
  ...
]

User Request:
{user_input}

Available Venues:
{json.dumps(venue_data, indent=2)}

Only return the JSON array:
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a wedding planning assistant that always responds in valid JSON arrays."},
                {"role": "user", "content": prompt}
            ]
        )

        response_text = response.choices[0].message.content.strip()

        # Strip Markdown-style code block if GPT wraps response in ```json ... ```
        if response_text.startswith("```"):
            response_text = response_text.strip("`")
            lines = response_text.splitlines()
            response_text = "\n".join(line for line in lines if not line.strip().startswith("json"))

        print("=== GPT RAW RESPONSE ===")
        print(response_text)
        print("========================")

        return json.loads(response_text)

    except Exception as e:
        print("❌ Error parsing GPT response:", e)
        return [{
            "venue": "Error",
            "location": "-",
            "price_per_table": 0,
            "capacity": 0,
            "reason": f"Unable to parse GPT output: {str(e)}"
        }]
>>>>>>> 8540f75 (Update: working recommender system with JSON integration)
