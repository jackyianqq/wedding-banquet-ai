import os
import json
import subprocess
from flask import Flask, request, render_template, redirect, url_for, flash
from app.recommender import recommend_venues

# Set the correct template folder location
base_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.abspath(os.path.join(base_dir, '..'))
template_dir = os.path.join(parent_dir, 'templates')
data_dir = os.path.join(parent_dir, 'data')

app = Flask(__name__, template_folder=template_dir)
app.secret_key = 'wedding-secret-key'

# Load venues data initially
with open(os.path.join(data_dir, 'venues.json'), 'r', encoding='utf-8') as f:
    venue_data = json.load(f)

@app.route('/', methods=['GET', 'POST'])
def index():
    recommendations = []
    if request.method == 'POST':
        user_input = request.form['user_input']
        location = request.form.get('location', '')
        budget = request.form.get('budget', '')

        filtered_data = venue_data
        if location:
            filtered_data = [v for v in filtered_data if location.lower() in v['location'].lower()]
        if budget:
            try:
                budget_value = int(budget)
                filtered_data = [v for v in filtered_data if v['price_per_table'] <= budget_value]
            except ValueError:
                pass

        recommendations = recommend_venues(user_input, filtered_data)

    return render_template("index.html", recommendations=recommendations, results=bool(recommendations))

@app.route('/update_venues', methods=['POST'])
def update_venues():
    try:
        subprocess.run(['python3', os.path.join(parent_dir, 'scripts', 'update_venues.py')], check=True)
        flash('✅ Venues successfully updated!')
    except subprocess.CalledProcessError:
        flash('❌ Failed to update venues.')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
