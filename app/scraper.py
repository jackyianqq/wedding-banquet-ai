
import json

def load_data():
    with open("data/venues.json", "r") as f:
        return json.load(f)
