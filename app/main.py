import os
import json
from flask import Flask, render_template, request
from app.recommender import recommend_venues

# Define the template directory before using it
template_dir = os.path.join(os.path.dirname(__file__), '..', 'templates')
app = Flask(__name__, template_folder=template_dir)

# Load venue data from JSON
def load_venue_data():
    try:
        json_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'venues.json')
        with open(json_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        print("❌ Failed to load venues.json:", e)
        return []

@app.route("/", methods=["GET", "POST"])
def index():
    recommendations = []

    if request.method == "POST":
        user_desc = request.form.get("user_input", "")
        location = request.form.get("location", "")
        budget = request.form.get("budget", "")

        user_input = f"I need a wedding banquet venue in {location or 'Singapore'} for 20 tables (200 guests) on a weekday, with a budget of ${budget or 'any'} per table. {user_desc}"

        venue_data = load_venue_data()
        recommendations = recommend_venues(user_input, venue_data)

    return render_template("index.html", recommendations=recommendations, results=bool(recommendations))

if __name__ == "__main__":
    app.run(debug=True)
