import os
import json
import requests
from bs4 import BeautifulSoup

def scrape_and_save():
    url = "https://www.blissfulbrides.sg/wedding-banquet-price-list"
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    venues = []

    table = soup.select_one("table.banquet-list")
    if not table:
        print("❌ Could not find the banquet list table.")
        return []

    rows = table.select("tbody tr")

    for row in rows:
        try:
            cols = row.find_all("td")
            if len(cols) < 5:
                continue

            venue_name = cols[0].get_text(strip=True)
            hotel = cols[1].get_text(strip=True)
            price_str = cols[2].get_text(strip=True)
            capacity_str = cols[3].get_text(strip=True)

            price = int(''.join(filter(str.isdigit, price_str.split('–')[0])) or 0)

            if "-" in capacity_str:
                max_capacity = int(capacity_str.split("-")[-1].replace("tables", "").strip())
            else:
                max_capacity = int(''.join(filter(str.isdigit, capacity_str)) or 0)

            venues.append({
                "venue": venue_name,
                "location": hotel,
                "price_per_table": price,
                "capacity": max_capacity
            })

        except Exception as e:
            print(f"⚠️ Skipped a row due to error: {e}")
            continue

    os.makedirs("data", exist_ok=True)
    with open("data/venues.json", "w") as f:
        json.dump(venues, f, indent=2)

    print(f"✅ Scraped {len(venues)} venues.")
    return venues

def load_data():
    if not os.path.exists("data/venues.json"):
        return scrape_and_save()
    
    with open("data/venues.json", "r") as f:
        try:
            data = json.load(f)
            if not data:
                return scrape_and_save()
            return data
        except json.JSONDecodeError:
            return scrape_and_save()
