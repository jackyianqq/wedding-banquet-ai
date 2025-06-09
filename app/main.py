import os
import json
from flask import Flask, render_template, request
from app.recommender import recommend_venues

# Set template folder correctly
template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'templates')
app = Flask(__name__, template_folder=template_dir)

# Load venues data
with open("data/venues.json", "r") as f:
    venue_data = json.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    recommendations = []

    if request.method == "POST":
        user_input = request.form.get("user_input", "")
        location = request.form.get("location", "")
        budget = request.form.get("budget", "")

        filters = []
        if location:
            filters.append(f"Preferred location: {location}")
        if budget:
            filters.append(f"Max budget per table: ${budget}")

        full_prompt = f"{user_input}\n" + "\n".join(filters)
        recommendations = recommend_venues(full_prompt, venue_data)

    return render_template("index.html", recommendations=recommendations, results=bool(recommendations))

if __name__ == "__main__":
    app.run(debug=True)
