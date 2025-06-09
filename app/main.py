
from flask import Flask, render_template, request
from app.recommender import recommend_venues
from app.scraper import load_data

app = Flask(__name__)
venue_data = load_data()

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        user_input = request.form["user_input"]
        result = recommend_venues(user_input, venue_data)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
