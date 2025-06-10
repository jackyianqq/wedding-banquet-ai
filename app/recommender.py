import os
import openai
import json


# Initialize OpenAI client with API key from environment variable
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def recommend_venues(user_input, venue_data):
    """
    Generates venue recommendations using OpenAI's GPT model based on user input and venue dataset.
    Returns a list of recommended venues as JSON.
    """

    # Construct a structured and secure prompt
    prompt = {
        "system": (
            "You are a helpful wedding planner AI. Based on the user's request and the banquet venue data, "
            "recommend exactly 3 suitable wedding banquet venues.\n\n"
            "Return ONLY a valid JSON array. Do NOT include any extra text or formatting such as Markdown.\n\n"
            "Each object in the array should have:\n"
            "- venue (string)\n"
            "- location (string)\n"
            "- price_per_table (number)\n"
            "- capacity (number)\n"
            "- reason (string explaining why it matches)\n\n"
            "Strictly output only the JSON array."
        ),
        "user": (
            f"User Request:\n{user_input}\n\n"
            f"Available Venues:\n{json.dumps(venue_data, indent=2)}"
        )
    }

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": prompt["system"]},
                {"role": "user", "content": prompt["user"]}
            ],
            temperature=0.7,
            max_tokens=1000
        )

        # Extract the content of the AI's message
        content = response.choices[0].message.content.strip()

        # Safely parse and return JSON data
        return json.loads(content)

    except json.JSONDecodeError:
        print("Error: Response is not valid JSON.")
        print("Raw response:", content)
        return []

    except Exception as e:
        print("Error communicating with OpenAI:", str(e))
        return []
