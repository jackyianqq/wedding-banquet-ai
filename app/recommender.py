import os
import openai
import json

# Initialize OpenAI client
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def recommend_venues(user_input, venue_data):
    # Format prompt to enforce JSON structure
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

        # Extract text and print for debugging
        response_text = response.choices[0].message.content.strip()
        print("=== GPT RAW RESPONSE ===")
        print(response_text)
        print("========================")

        # Try to parse response into Python list
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
