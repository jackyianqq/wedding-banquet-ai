import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.blissfulbrides.sg/wedding-banquet-price-list"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Collect all table rows from the price list
tables = soup.find_all("table")

all_data = []

for table in tables:
    headers = [th.text.strip() for th in table.find_all("th")]
    for row in table.find_all("tr")[1:]:
        cols = [td.text.strip() for td in row.find_all("td")]
        if len(cols) == len(headers):
            all_data.append(dict(zip(headers, cols)))

# Convert to DataFrame and save to Excel
df = pd.DataFrame(all_data)
df.to_excel("venues.xlsx", index=False)
print("✅ venues.xlsx saved successfully!")

