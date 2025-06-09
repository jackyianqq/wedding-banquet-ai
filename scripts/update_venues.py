import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import os

# Step 1: Scrape
url = "https://www.blissfulbrides.sg/wedding-banquet-price-list"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

tables = soup.find_all("table")
all_data = []

for table in tables:
    headers = [th.text.strip() for th in table.find_all("th")]
    for row in table.find_all("tr")[1:]:
        cols = [td.text.strip() for td in row.find_all("td")]
        if len(cols) == len(headers):
            all_data.append(dict(zip(headers, cols)))

# Step 2: Save to Excel
df = pd.DataFrame(all_data)
df.to_excel("venues.xlsx", index=False)

# Step 3: Convert to JSON
data_path = os.path.join(os.path.dirname(__file__), "../data/venues.json")
with open(data_path, "w", encoding="utf-8") as f:
    json.dump(all_data, f, ensure_ascii=False, indent=2)

print("✅ Data updated: venues.xlsx + venues.json")
